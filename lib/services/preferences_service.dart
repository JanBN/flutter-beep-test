import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/beep_test_config.dart';

class PreferencesService {
  final SharedPreferences? _prefs;

  PreferencesService([this._prefs]);

  static const String _keyDistance = 'config_distance';
  static const String _keyStartSpeed = 'config_start_speed';
  static const String _keySpeedIncrement = 'config_speed_increment';
  static const String _keySound = 'config_sound';
  static const String _keyTts = 'config_tts';
  static const String _keyVibration = 'config_vibration';
  static const String _keyCountdown = 'config_countdown';
  static const String _keyThemeMode = 'app_theme_mode';

  static Future<PreferencesService> init() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      return PreferencesService(prefs);
    } catch (e) {
      debugPrint('PreferencesService init error: $e');
      return PreferencesService(null);
    }
  }

  BeepTestConfig loadConfig() {
    final prefs = _prefs;
    if (prefs == null) {
      return const BeepTestConfig();
    }

    return BeepTestConfig(
      distanceMeters: prefs.getDouble(_keyDistance) ?? 10.0,
      startSpeedKmh: prefs.getDouble(_keyStartSpeed) ?? 8.0,
      speedIncrementKmh: prefs.getDouble(_keySpeedIncrement) ?? 0.5,
      soundEnabled: prefs.getBool(_keySound) ?? true,
      ttsEnabled: prefs.getBool(_keyTts) ?? true,
      vibrationEnabled: prefs.getBool(_keyVibration) ?? true,
      countdownSeconds: prefs.getInt(_keyCountdown) ?? 5,
    );
  }

  Future<void> saveConfig(BeepTestConfig config) async {
    final prefs = _prefs;
    if (prefs == null) return;

    try {
      await Future.wait([
        prefs.setDouble(_keyDistance, config.distanceMeters),
        prefs.setDouble(_keyStartSpeed, config.startSpeedKmh),
        prefs.setDouble(_keySpeedIncrement, config.speedIncrementKmh),
        prefs.setBool(_keySound, config.soundEnabled),
        prefs.setBool(_keyTts, config.ttsEnabled),
        prefs.setBool(_keyVibration, config.vibrationEnabled),
        prefs.setInt(_keyCountdown, config.countdownSeconds),
      ]);
    } catch (e) {
      debugPrint('Error saving config to preferences: $e');
    }
  }

  ThemeMode loadThemeMode() {
    final prefs = _prefs;
    if (prefs == null) return ThemeMode.dark;

    final modeStr = prefs.getString(_keyThemeMode);
    switch (modeStr) {
      case 'light':
        return ThemeMode.light;
      case 'dark':
        return ThemeMode.dark;
      case 'system':
        return ThemeMode.system;
      default:
        return ThemeMode.dark;
    }
  }

  Future<void> saveThemeMode(ThemeMode mode) async {
    final prefs = _prefs;
    if (prefs == null) return;

    try {
      String modeStr;
      switch (mode) {
        case ThemeMode.light:
          modeStr = 'light';
          break;
        case ThemeMode.dark:
          modeStr = 'dark';
          break;
        case ThemeMode.system:
          modeStr = 'system';
          break;
      }
      await prefs.setString(_keyThemeMode, modeStr);
    } catch (e) {
      debugPrint('Error saving theme mode to preferences: $e');
    }
  }
}
