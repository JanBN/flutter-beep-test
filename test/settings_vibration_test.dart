import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:beep_test/models/beep_test_config.dart';
import 'package:beep_test/screens/beep_test_screen.dart';
import 'package:beep_test/screens/splash_screen.dart';
import 'package:beep_test/services/audio_service.dart';
import 'package:beep_test/services/beep_test_controller.dart';
import 'package:beep_test/services/preferences_service.dart';

class FakeAudioService implements AudioService {
  bool cancelVibrationCalled = false;
  List<bool> playedBeeps = [];

  @override
  Future<void> playBeep({bool vibration = true}) async {
    playedBeeps.add(vibration);
  }

  @override
  Future<void> playLevelUp({bool vibration = true}) async {}

  @override
  Future<void> playTick({bool vibration = true}) async {}

  @override
  Future<void> playStart({bool vibration = true}) async {}

  @override
  Future<void> playFinish({bool vibration = true}) async {}

  @override
  Future<void> cancelVibration() async {
    cancelVibrationCalled = true;
  }

  @override
  Future<void> speak(String text) async {}

  @override
  Future<void> announceNextLevel(int nextLevel) async {}

  @override
  Future<void> announceLevelStart(int level) async {}

  @override
  Future<void> dispose() async {}
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('PreferencesService & Vibration Persistence', () {
    setUp(() {
      SharedPreferences.setMockInitialValues({});
    });

    test('Loads default config with vibration enabled when empty', () async {
      final prefs = await PreferencesService.init();
      final config = prefs.loadConfig();
      expect(config.vibrationEnabled, isTrue);
    });

    test('Saves and restores vibrationEnabled: false', () async {
      final prefs = await PreferencesService.init();
      const newConfig = BeepTestConfig(vibrationEnabled: false);
      await prefs.saveConfig(newConfig);

      final reloaded = prefs.loadConfig();
      expect(reloaded.vibrationEnabled, isFalse);
    });
  });

  group('BeepTestController Configuration Updates', () {
    late FakeAudioService fakeAudio;

    setUp(() {
      SharedPreferences.setMockInitialValues({});
      fakeAudio = FakeAudioService();
    });

    test('updateConfig works while test is running and cancels vibration', () async {
      final controller = BeepTestController(
        audioService: fakeAudio,
        initialConfig: const BeepTestConfig(vibrationEnabled: true),
      );

      // Start running
      await controller.start();
      expect(controller.config.vibrationEnabled, isTrue);

      // User disables vibration during test
      controller.updateConfig(controller.config.copyWith(vibrationEnabled: false));

      expect(controller.config.vibrationEnabled, isFalse);
      expect(fakeAudio.cancelVibrationCalled, isTrue);
    });

    test('updateConfig persists setting to PreferencesService', () async {
      final prefs = await PreferencesService.init();
      final controller = BeepTestController(
        audioService: fakeAudio,
        initialConfig: const BeepTestConfig(vibrationEnabled: true),
        preferencesService: prefs,
      );

      controller.updateConfig(controller.config.copyWith(vibrationEnabled: false));
      expect(controller.config.vibrationEnabled, isFalse);

      final reloaded = prefs.loadConfig();
      expect(reloaded.vibrationEnabled, isFalse);
    });

    testWidgets('SplashScreen displays branding and navigates', (tester) async {
      final fakeAudio = FakeAudioService();
      final controller = BeepTestController(audioService: fakeAudio);

      await tester.pumpWidget(
        MaterialApp(
          home: SplashScreen(controller: controller),
        ),
      );

      expect(find.text('BEEP TEST PRO'), findsOneWidget);
      expect(find.text('Ihriskový & Detský vytrvalostný test'), findsOneWidget);

      // Fast-forward past 1800ms timer and transitions
      await tester.pump(const Duration(milliseconds: 2000));
      await tester.pumpAndSettle();

      expect(find.byType(BeepTestScreen), findsOneWidget);
    });
  });
}
