import 'package:flutter_test/flutter_test.dart';
import 'package:beep_test/models/beep_level.dart';
import 'package:beep_test/models/beep_test_config.dart';

void main() {
  group('Beep Test Math & Level Calculations', () {
    test('Standard 20m distance calculation at Level 1', () {
      const config = BeepTestConfig(
        distanceMeters: 20.0,
        startSpeedKmh: 8.0,
        targetLevelDurationSeconds: 60,
      );

      final level1 = BeepLevel.calculate(levelNumber: 1, config: config);
      expect(level1.levelNumber, 1);
      expect(level1.speedKmh, 8.0);
      // t = (20 * 3.6) / 8.0 = 9.0s
      expect(level1.shuttleDurationSeconds, closeTo(9.0, 0.01));
      // 60 / 9 = ~7 shuttles
      expect(level1.shuttlesCount, 7);
    });

    test('Custom 10m playground distance calculation at Level 1', () {
      const config = BeepTestConfig(
        distanceMeters: 10.0,
        startSpeedKmh: 8.0,
        targetLevelDurationSeconds: 60,
      );

      final level1 = BeepLevel.calculate(levelNumber: 1, config: config);
      expect(level1.levelNumber, 1);
      expect(level1.speedKmh, 8.0);
      // t = (10 * 3.6) / 8.0 = 4.5s
      expect(level1.shuttleDurationSeconds, closeTo(4.5, 0.01));
      // 60 / 4.5 = ~13 shuttles
      expect(level1.shuttlesCount, 13);
    });

    test('Level 10 speed increases correctly', () {
      const config = BeepTestConfig(
        distanceMeters: 10.0,
        startSpeedKmh: 8.0,
        speedIncrementKmh: 0.5,
      );

      final level10 = BeepLevel.calculate(levelNumber: 10, config: config);
      // Speed at Level 10 = 8.0 + (10 - 1) * 0.5 = 12.5 km/h
      expect(level10.speedKmh, 12.5);
      // t = (10 * 3.6) / 12.5 = 2.88s
      expect(level10.shuttleDurationSeconds, closeTo(2.88, 0.01));
    });
  });
}
