import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:vibration/vibration.dart';

class AudioService {
  final AudioPlayer _beepPlayer = AudioPlayer();
  final AudioPlayer _chimePlayer = AudioPlayer();
  final FlutterTts _tts = FlutterTts();

  bool _ttsInitialized = false;
  bool _hasVibrator = false;

  AudioService() {
    _init();
  }

  Future<void> _init() async {
    try {
      // Configure audio players for low latency response
      await _beepPlayer.setPlayerMode(PlayerMode.lowLatency);
      await _chimePlayer.setPlayerMode(PlayerMode.lowLatency);
      await _beepPlayer.setReleaseMode(ReleaseMode.stop);
      await _chimePlayer.setReleaseMode(ReleaseMode.stop);

      // Check vibration capability
      if (!kIsWeb) {
        _hasVibrator = await Vibration.hasVibrator();
      }

      // Configure Text to Speech
      await _initTts();
    } catch (e) {
      debugPrint('AudioService init error: $e');
    }
  }

  Future<void> _initTts() async {
    try {
      await _tts.setSpeechRate(0.5);
      await _tts.setVolume(1.0);
      await _tts.setPitch(1.0);

      // Try Slovak language first
      final languages = await _tts.getLanguages;
      if (languages is List) {
        final hasSlovak = languages.any((lang) =>
            lang.toString().toLowerCase().contains('sk') ||
            lang.toString().toLowerCase().contains('slo'));
        if (hasSlovak) {
          await _tts.setLanguage('sk-SK');
        } else {
          // Fallback to default device language
          await _tts.setLanguage('en-US');
        }
      }
      _ttsInitialized = true;
    } catch (e) {
      debugPrint('TTS init error: $e');
    }
  }

  /// Play standard shuttle turnaround beep
  Future<void> playBeep({bool vibration = true}) async {
    try {
      await _beepPlayer.stop();
      await _beepPlayer.play(AssetSource('audio/beep.wav'));
      if (vibration && _hasVibrator) {
        Vibration.vibrate(duration: 80);
      }
    } catch (e) {
      debugPrint('playBeep error: $e');
    }
  }

  /// Play special level change sound
  Future<void> playLevelUp({bool vibration = true}) async {
    try {
      await _chimePlayer.stop();
      await _chimePlayer.play(AssetSource('audio/level_up.wav'));
      if (vibration && _hasVibrator) {
        Vibration.vibrate(pattern: [0, 100, 50, 150]);
      }
    } catch (e) {
      debugPrint('playLevelUp error: $e');
    }
  }

  /// Play countdown tick (3, 2, 1)
  Future<void> playTick({bool vibration = true}) async {
    try {
      await _beepPlayer.stop();
      await _beepPlayer.play(AssetSource('audio/tick.wav'));
      if (vibration && _hasVibrator) {
        Vibration.vibrate(duration: 40);
      }
    } catch (e) {
      debugPrint('playTick error: $e');
    }
  }

  /// Play start sound
  Future<void> playStart({bool vibration = true}) async {
    try {
      await _chimePlayer.stop();
      await _chimePlayer.play(AssetSource('audio/start.wav'));
      if (vibration && _hasVibrator) {
        Vibration.vibrate(duration: 250);
      }
    } catch (e) {
      debugPrint('playStart error: $e');
    }
  }

  /// Play finish fanfare
  Future<void> playFinish({bool vibration = true}) async {
    try {
      await _chimePlayer.stop();
      await _chimePlayer.play(AssetSource('audio/finish.wav'));
      if (vibration && _hasVibrator) {
        Vibration.vibrate(pattern: [0, 150, 80, 150, 80, 300]);
      }
    } catch (e) {
      debugPrint('playFinish error: $e');
    }
  }

  /// Immediately stop any ongoing vibration
  Future<void> cancelVibration() async {
    try {
      if (!kIsWeb && _hasVibrator) {
        await Vibration.cancel();
      }
    } catch (e) {
      debugPrint('cancelVibration error: $e');
    }
  }

  /// Speak announcement via TTS
  Future<void> speak(String text) async {
    try {
      if (!_ttsInitialized) {
        await _initTts();
      }
      await _tts.stop();
      await _tts.speak(text);
    } catch (e) {
      debugPrint('TTS speak error: $e');
    }
  }

  /// Announce next level before it starts
  /// Requirement: "A vzdy nech mi povie dalsi level je 10 napriklad"
  Future<void> announceNextLevel(int nextLevel) async {
    await speak('Pozor, ďalší level je $nextLevel!');
  }

  /// Announce level starting
  Future<void> announceLevelStart(int level) async {
    await speak('Level $level.');
  }

  Future<void> dispose() async {
    try {
      await _beepPlayer.dispose();
      await _chimePlayer.dispose();
      await _tts.stop();
    } catch (e) {
      debugPrint('AudioService dispose error: $e');
    }
  }
}
