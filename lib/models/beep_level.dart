import 'beep_test_config.dart';

/// Represents a single stage/level in the beep test
class BeepLevel {
  final int levelNumber;
  final double speedKmh;
  final double distanceMeters;
  final double shuttleDurationSeconds;
  final int shuttlesCount;

  BeepLevel({
    required this.levelNumber,
    required this.speedKmh,
    required this.distanceMeters,
    required this.shuttleDurationSeconds,
    required this.shuttlesCount,
  });

  /// Total duration of all shuttles in this level
  double get totalDurationSeconds => shuttlesCount * shuttleDurationSeconds;

  /// Total distance run in this level alone
  double get totalLevelDistanceMeters => shuttlesCount * distanceMeters;

  /// Factory to compute level properties based on configuration
  factory BeepLevel.calculate({
    required int levelNumber,
    required BeepTestConfig config,
  }) {
    // Speed increases by config.speedIncrementKmh each level
    final speed = config.startSpeedKmh + (levelNumber - 1) * config.speedIncrementKmh;

    // Time per shuttle: t = (d * 3.6) / v
    // e.g. 10m at 8.0 km/h: (10 * 3.6) / 8.0 = 4.50 seconds
    // e.g. 20m at 8.0 km/h: (20 * 3.6) / 8.0 = 9.00 seconds
    final shuttleDuration = (config.distanceMeters * 3.6) / speed;

    // Standard beep test levels are ~60 seconds long.
    // Calculate how many shuttles fit in ~60 seconds.
    final count = (config.targetLevelDurationSeconds / shuttleDuration).round();
    final shuttles = count < 1 ? 1 : count;

    return BeepLevel(
      levelNumber: levelNumber,
      speedKmh: speed,
      distanceMeters: config.distanceMeters,
      shuttleDurationSeconds: shuttleDuration,
      shuttlesCount: shuttles,
    );
  }

  /// Formatted duration string per shuttle (e.g. "4.5s")
  String get formattedShuttleTime => '${shuttleDurationSeconds.toStringAsFixed(2)}s';

  /// Formatted speed string (e.g. "8.5 km/h")
  String get formattedSpeed => '${speedKmh.toStringAsFixed(1)} km/h';
}
