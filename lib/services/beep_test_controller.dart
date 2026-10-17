import 'dart:async';
import 'package:flutter/material.dart';
import 'package:wakelock_plus/wakelock_plus.dart';
import '../models/beep_level.dart';
import '../models/beep_test_config.dart';
import 'audio_service.dart';
import 'preferences_service.dart';

enum BeepTestState {
  idle,
  countdown,
  running,
  paused,
  finished,
}

class BeepTestController extends ChangeNotifier {
  final AudioService _audio;

  BeepTestConfig _config;
  BeepTestConfig get config => _config;

  BeepTestState _state = BeepTestState.idle;
  BeepTestState get state => _state;

  int _currentLevelNumber = 1;
  int get currentLevelNumber => _currentLevelNumber;

  late BeepLevel _currentLevel;
  BeepLevel get currentLevel => _currentLevel;

  int _currentShuttle = 1;
  int get currentShuttle => _currentShuttle;

  /// Direction of current shuttle: true = A -> B, false = B -> A
  bool _shuttleDirection = true;
  bool get shuttleDirection => _shuttleDirection;

  /// Shuttle progress from 0.0 to 1.0
  double _shuttleProgress = 0.0;
  double get shuttleProgress => _shuttleProgress;

  /// Shuttle remaining time in seconds
  double _shuttleRemainingSeconds = 0.0;
  double get shuttleRemainingSeconds => _shuttleRemainingSeconds;

  /// Total session elapsed time
  Duration _totalElapsedTime = Duration.zero;
  Duration get totalElapsedTime => _totalElapsedTime;

  /// Total shuttles completed in this session
  int _totalCompletedShuttles = 0;
  int get totalCompletedShuttles => _totalCompletedShuttles;

  /// Total distance run in meters
  double get totalDistanceMeters => _totalCompletedShuttles * _config.distanceMeters;

  /// Theme Mode (Dark, Light, System)
  ThemeMode _themeMode = ThemeMode.dark;
  ThemeMode get themeMode => _themeMode;

  final PreferencesService? _preferences;

  void setThemeMode(ThemeMode mode) {
    _themeMode = mode;
    _preferences?.saveThemeMode(mode);
    notifyListeners();
  }

  void toggleThemeMode() {
    switch (_themeMode) {
      case ThemeMode.dark:
        _themeMode = ThemeMode.light;
        break;
      case ThemeMode.light:
        _themeMode = ThemeMode.system;
        break;
      case ThemeMode.system:
        _themeMode = ThemeMode.dark;
        break;
    }
    _preferences?.saveThemeMode(_themeMode);
    notifyListeners();
  }

  /// Total remaining time in seconds until the next level starts
  double get levelRemainingSeconds {
    final remainingShuttlesAfterThis = _currentLevel.shuttlesCount - _currentShuttle;
    final totalSec = _shuttleRemainingSeconds +
        (remainingShuttlesAfterThis * _currentLevel.shuttleDurationSeconds);
    return totalSec.clamp(0.0, _currentLevel.totalDurationSeconds);
  }

  /// Progress through current level from 0.0 to 1.0
  double get levelProgress {
    final total = _currentLevel.totalDurationSeconds;
    if (total <= 0) return 0.0;
    final elapsedInLevel = total - levelRemainingSeconds;
    return (elapsedInLevel / total).clamp(0.0, 1.0);
  }

  /// True if currently running the very last shuttle of this level
  bool get isLastShuttleOfLevel => _currentShuttle >= _currentLevel.shuttlesCount;

  /// Remaining shuttles in current level including current one
  int get remainingShuttlesInLevel =>
      (_currentLevel.shuttlesCount - _currentShuttle + 1).clamp(1, _currentLevel.shuttlesCount);

  /// Countdown state
  int _countdownRemaining = 5;
  int get countdownRemaining => _countdownRemaining;

  Timer? _tickerTimer;
  Timer? _countdownTimer;
  final Stopwatch _shuttleStopwatch = Stopwatch();
  final Stopwatch _totalStopwatch = Stopwatch();

  BeepTestController({
    required AudioService audioService,
    BeepTestConfig? initialConfig,
    ThemeMode initialThemeMode = ThemeMode.dark,
    PreferencesService? preferencesService,
  })  : _audio = audioService,
        _config = initialConfig ?? const BeepTestConfig(),
        _themeMode = initialThemeMode,
        _preferences = preferencesService {
    _updateLevel();
  }

  void _updateLevel() {
    _currentLevel = BeepLevel.calculate(
      levelNumber: _currentLevelNumber,
      config: _config,
    );
    _shuttleRemainingSeconds = _currentLevel.shuttleDurationSeconds;
  }

  /// Update test configuration (distance, speed, audio toggles, vibration, etc.)
  void updateConfig(BeepTestConfig newConfig) {
    final oldDistance = _config.distanceMeters;
    final oldStartSpeed = _config.startSpeedKmh;

    _config = newConfig;

    // Stop ongoing vibration immediately if turned off
    if (!newConfig.vibrationEnabled) {
      _audio.cancelVibration();
    }

    // Only update level metrics if idle or paused
    if (_state == BeepTestState.idle || _state == BeepTestState.paused) {
      if (oldDistance != newConfig.distanceMeters || oldStartSpeed != newConfig.startSpeedKmh) {
        _updateLevel();
      }
    }

    // Save configuration persistently
    _preferences?.saveConfig(_config);
    notifyListeners();
  }

  /// Change running distance (e.g. 10m, 15m, 20m)
  void setDistance(double meters) {
    if (_state == BeepTestState.running) return;
    _config = _config.copyWith(distanceMeters: meters);
    _updateLevel();
    _preferences?.saveConfig(_config);
    notifyListeners();
  }

  /// Jump straight to any level (can be used idle, running, or paused!)
  /// Requirement: "A taktie chcem vediet preskocit na ktorykolvek level"
  Future<void> jumpToLevel(int targetLevel) async {
    if (targetLevel < 1) targetLevel = 1;
    if (targetLevel > 30) targetLevel = 30;

    _currentLevelNumber = targetLevel;
    _currentShuttle = 1;
    _shuttleProgress = 0.0;
    _updateLevel();

    // Voice announcement for the level jump
    if (_config.ttsEnabled) {
      await _audio.announceNextLevel(targetLevel);
    }

    if (_state == BeepTestState.running) {
      _shuttleStopwatch.reset();
      _shuttleStopwatch.start();
      _audio.playLevelUp(vibration: _config.vibrationEnabled);
    }

    notifyListeners();
  }

  /// Skip to next level immediately
  void nextLevel() {
    jumpToLevel(_currentLevelNumber + 1);
  }

  /// Skip to previous level
  void previousLevel() {
    if (_currentLevelNumber > 1) {
      jumpToLevel(_currentLevelNumber - 1);
    }
  }

  /// Start Beep Test with preparation countdown
  Future<void> start() async {
    if (_state == BeepTestState.running) return;

    // Enable wakelock so screen stays awake outdoors
    try {
      await WakelockPlus.enable();
    } catch (_) {}

    _state = BeepTestState.countdown;
    _countdownRemaining = _config.countdownSeconds;
    notifyListeners();

    if (_config.ttsEnabled) {
      _audio.speak('Pripravte sa. Level $_currentLevelNumber.');
    }

    _countdownTimer?.cancel();
    _countdownTimer = Timer.periodic(const Duration(seconds: 1), (timer) async {
      _countdownRemaining--;
      if (_countdownRemaining > 0) {
        if (_config.soundEnabled) {
          _audio.playTick(vibration: _config.vibrationEnabled);
        }
        notifyListeners();
      } else {
        timer.cancel();
        _countdownTimer = null;
        await _beginRunning();
      }
    });
  }

  Future<void> _beginRunning() async {
    _state = BeepTestState.running;
    _shuttleStopwatch.reset();
    _shuttleStopwatch.start();
    _totalStopwatch.start();

    if (_config.soundEnabled) {
      await _audio.playStart(vibration: _config.vibrationEnabled);
    }

    _startTicker();
    notifyListeners();
  }

  void _startTicker() {
    _tickerTimer?.cancel();
    _tickerTimer = Timer.periodic(const Duration(milliseconds: 30), (timer) {
      if (_state != BeepTestState.running) return;

      final elapsedSec = _shuttleStopwatch.elapsedMilliseconds / 1000.0;
      final shuttleDuration = _currentLevel.shuttleDurationSeconds;

      _shuttleProgress = (elapsedSec / shuttleDuration).clamp(0.0, 1.0);
      _shuttleRemainingSeconds = (shuttleDuration - elapsedSec).clamp(0.0, shuttleDuration);
      _totalElapsedTime = _totalStopwatch.elapsed;

      if (elapsedSec >= shuttleDuration) {
        _onShuttleCompleted();
      }

      notifyListeners();
    });
  }

  void _onShuttleCompleted() {
    _totalCompletedShuttles++;
    _shuttleDirection = !_shuttleDirection; // Switch run direction
    _shuttleStopwatch.reset();
    _shuttleStopwatch.start();

    // Check if level finished
    if (_currentShuttle >= _currentLevel.shuttlesCount) {
      // Advance to next level
      final nextLevelNum = _currentLevelNumber + 1;
      _currentLevelNumber = nextLevelNum;
      _currentShuttle = 1;
      _updateLevel();

      // Audio & Voice Cue: "A vzdy nech mi povie dalsi level je 10 napriklad"
      if (_config.soundEnabled) {
        _audio.playLevelUp(vibration: _config.vibrationEnabled);
      }
      if (_config.ttsEnabled) {
        _audio.announceNextLevel(nextLevelNum);
      }
    } else {
      // Next shuttle within same level
      _currentShuttle++;
      if (_config.soundEnabled) {
        _audio.playBeep(vibration: _config.vibrationEnabled);
      }
    }
  }

  /// Pause running session
  void pause() {
    if (_state != BeepTestState.running) return;
    _state = BeepTestState.paused;
    _shuttleStopwatch.stop();
    _totalStopwatch.stop();
    _tickerTimer?.cancel();
    notifyListeners();
  }

  /// Resume from paused state
  void resume() {
    if (_state != BeepTestState.paused) return;
    _state = BeepTestState.running;
    _shuttleStopwatch.start();
    _totalStopwatch.start();
    _startTicker();
    notifyListeners();
  }

  /// Stop and show results
  Future<void> stop() async {
    _state = BeepTestState.finished;
    _tickerTimer?.cancel();
    _countdownTimer?.cancel();
    _shuttleStopwatch.stop();
    _totalStopwatch.stop();

    if (_config.soundEnabled) {
      await _audio.playFinish(vibration: _config.vibrationEnabled);
    }
    if (_config.ttsEnabled) {
      _audio.speak('Výborne! Test ukončený.');
    }

    try {
      await WakelockPlus.disable();
    } catch (_) {}

    notifyListeners();
  }

  /// Reset to idle state
  Future<void> reset() async {
    _state = BeepTestState.idle;
    _tickerTimer?.cancel();
    _countdownTimer?.cancel();
    _shuttleStopwatch.reset();
    _totalStopwatch.reset();

    _currentLevelNumber = 1;
    _currentShuttle = 1;
    _shuttleProgress = 0.0;
    _shuttleDirection = true;
    _totalCompletedShuttles = 0;
    _totalElapsedTime = Duration.zero;

    _updateLevel();

    try {
      await WakelockPlus.disable();
    } catch (_) {}

    notifyListeners();
  }

  /// Estimate VO2 Max based on Léger formula adapted for speed reached
  double calculateVo2Max() {
    // Luc Léger: VO2 max (ml/kg/min) ~ 3.46 * maxSpeed - 12.2 (or ~31 + 3.2*(v-8))
    final speed = _currentLevel.speedKmh;
    final vo2 = 3.46 * speed - 12.2;
    return vo2 < 20.0 ? 20.0 : vo2;
  }

  /// Motivational title for kids
  String getKidsBadgeTitle() {
    if (_currentLevelNumber >= 12) return '🚀 Vesmírna Raketa!';
    if (_currentLevelNumber >= 9) return '⚡ Bleskový Šampión!';
    if (_currentLevelNumber >= 6) return '🐆 Rýchly Gepard!';
    if (_currentLevelNumber >= 4) return '🐺 Húževnatý Vlk!';
    if (_currentLevelNumber >= 2) return '🐰 Odvážny Zajačik!';
    return '🌟 Super Začiatok!';
  }

  @override
  void dispose() {
    _tickerTimer?.cancel();
    _countdownTimer?.cancel();
    try {
      WakelockPlus.disable();
    } catch (_) {}
    super.dispose();
  }
}
