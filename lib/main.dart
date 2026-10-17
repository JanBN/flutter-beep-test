import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'screens/splash_screen.dart';
import 'services/audio_service.dart';
import 'services/beep_test_controller.dart';
import 'services/preferences_service.dart';
import 'theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Allow portrait and portrait upside-down for outdoor phone usage
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);

  final prefsService = await PreferencesService.init();
  final initialConfig = prefsService.loadConfig();
  final initialThemeMode = prefsService.loadThemeMode();

  final audioService = AudioService();
  final controller = BeepTestController(
    audioService: audioService,
    initialConfig: initialConfig,
    initialThemeMode: initialThemeMode,
    preferencesService: prefsService,
  );

  runApp(BeepTestApp(controller: controller));
}

class BeepTestApp extends StatelessWidget {
  final BeepTestController controller;

  const BeepTestApp({super.key, required this.controller});

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: controller,
      builder: (context, _) {
        return MaterialApp(
          title: 'Beep Test Pro',
          debugShowCheckedModeBanner: false,
          theme: AppTheme.lightTheme,
          darkTheme: AppTheme.darkTheme,
          themeMode: controller.themeMode,
          home: SplashScreen(controller: controller),
        );
      },
    );
  }
}
