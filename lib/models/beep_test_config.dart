/// Configuration for the Beep Test session
class BeepTestConfig {
  /// Distance between shuttles in meters (default 20m, but fully customizable, e.g. 10m for kids)
  final double distanceMeters;

  /// Starting speed at Level 1 in km/h (standard Luc Léger is 8.5 km/h, kids can start at 7.0 or 8.0)
  final double startSpeedKmh;

  /// Speed increase per level in km/h (standard 0.5 km/h)
  final double speedIncrementKmh;

  /// Sound beeps enabled
  final bool soundEnabled;

  /// Voice announcements (TTS) enabled
  final bool ttsEnabled;

  /// Vibration on beep enabled
  final bool vibrationEnabled;

  /// Prep countdown duration in seconds before starting (e.g. 5s)
  final int countdownSeconds;

  /// Target duration per level in seconds (approx 60s standard)
  final int targetLevelDurationSeconds;

  const BeepTestConfig({
    this.distanceMeters = 10.0, // Default 10m for playground running with kids!
    this.startSpeedKmh = 8.0,
    this.speedIncrementKmh = 0.5,
    this.soundEnabled = true,
    this.ttsEnabled = true,
    this.vibrationEnabled = true,
    this.countdownSeconds = 5,
    this.targetLevelDurationSeconds = 60,
  });

  BeepTestConfig copyWith({
    double? distanceMeters,
    double? startSpeedKmh,
    double? speedIncrementKmh,
    bool? soundEnabled,
    bool? ttsEnabled,
    bool? vibrationEnabled,
    int? countdownSeconds,
    int? targetLevelDurationSeconds,
  }) {
    return BeepTestConfig(
      distanceMeters: distanceMeters ?? this.distanceMeters,
      startSpeedKmh: startSpeedKmh ?? this.startSpeedKmh,
      speedIncrementKmh: speedIncrementKmh ?? this.speedIncrementKmh,
      soundEnabled: soundEnabled ?? this.soundEnabled,
      ttsEnabled: ttsEnabled ?? this.ttsEnabled,
      vibrationEnabled: vibrationEnabled ?? this.vibrationEnabled,
      countdownSeconds: countdownSeconds ?? this.countdownSeconds,
      targetLevelDurationSeconds:
          targetLevelDurationSeconds ?? this.targetLevelDurationSeconds,
    );
  }
}
