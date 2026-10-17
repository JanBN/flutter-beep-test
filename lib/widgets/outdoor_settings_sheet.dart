import 'package:flutter/material.dart';
import '../models/beep_test_config.dart';
import '../theme/app_theme.dart';

class OutdoorSettingsSheet extends StatefulWidget {
  final BeepTestConfig config;
  final ThemeMode currentThemeMode;
  final Function(ThemeMode mode) onSaveTheme;
  final Function(BeepTestConfig newConfig) onSave;

  const OutdoorSettingsSheet({
    super.key,
    required this.config,
    required this.currentThemeMode,
    required this.onSaveTheme,
    required this.onSave,
  });

  static Future<void> show(
    BuildContext context, {
    required BeepTestConfig config,
    required ThemeMode currentThemeMode,
    required Function(ThemeMode mode) onSaveTheme,
    required Function(BeepTestConfig newConfig) onSave,
  }) {
    return showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => OutdoorSettingsSheet(
        config: config,
        currentThemeMode: currentThemeMode,
        onSaveTheme: onSaveTheme,
        onSave: onSave,
      ),
    );
  }

  @override
  State<OutdoorSettingsSheet> createState() => _OutdoorSettingsSheetState();
}

class _OutdoorSettingsSheetState extends State<OutdoorSettingsSheet> {
  late double _distance;
  late double _startSpeed;
  late bool _soundEnabled;
  late bool _ttsEnabled;
  late bool _vibrationEnabled;
  late int _countdownSeconds;
  late ThemeMode _themeMode;

  @override
  void initState() {
    super.initState();
    _distance = widget.config.distanceMeters;
    _startSpeed = widget.config.startSpeedKmh;
    _soundEnabled = widget.config.soundEnabled;
    _ttsEnabled = widget.config.ttsEnabled;
    _vibrationEnabled = widget.config.vibrationEnabled;
    _countdownSeconds = widget.config.countdownSeconds;
    _themeMode = widget.currentThemeMode;
  }

  void _syncChanges() {
    widget.onSaveTheme(_themeMode);
    final updated = widget.config.copyWith(
      distanceMeters: _distance,
      startSpeedKmh: _startSpeed,
      soundEnabled: _soundEnabled,
      ttsEnabled: _ttsEnabled,
      vibrationEnabled: _vibrationEnabled,
      countdownSeconds: _countdownSeconds,
    );
    widget.onSave(updated);
  }

  void _save() {
    _syncChanges();
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final shuttleTime = (_distance * 3.6) / _startSpeed;

    final sheetBg = isDark ? const Color(0xFF0F1523) : Colors.white;
    final cardBg = isDark ? const Color(0xFF161F33) : const Color(0xFFF8FAFC);
    final borderColor = isDark ? AppTheme.borderSubtle : AppTheme.borderLight;
    final textColor = isDark ? Colors.white : AppTheme.textDark;
    final textMuted = isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B);

    return PopScope(
      canPop: true,
      onPopInvokedWithResult: (didPop, _) {
        if (didPop) {
          _syncChanges();
        }
      },
      child: Container(
        height: MediaQuery.of(context).size.height * 0.88,
        decoration: BoxDecoration(
          color: sheetBg,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(28)),
          border: Border(
            top: BorderSide(color: borderColor, width: 1.5),
          ),
        ),
      child: SafeArea(
        top: false,
        child: Column(
          children: [
            // Drag handle
          Container(
            margin: const EdgeInsets.only(top: 12, bottom: 8),
            width: 44,
            height: 5,
            decoration: BoxDecoration(
              color: (isDark ? Colors.white : Colors.black).withValues(alpha: 0.2),
              borderRadius: BorderRadius.circular(10),
            ),
          ),

          // Header
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'NASTAVENIA BEHU',
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.w800,
                    color: textColor,
                  ),
                ),
                TextButton(
                  onPressed: _save,
                  child: const Text(
                    'ULOŽIŤ',
                    style: TextStyle(
                      color: AppTheme.electricCyan,
                      fontWeight: FontWeight.w800,
                      fontSize: 16,
                    ),
                  ),
                ),
              ],
            ),
          ),

          Divider(color: borderColor, height: 1),

          Expanded(
            child: ListView(
              padding: const EdgeInsets.all(20),
              children: [
                // 1. Theme mode selection (Dark / Light / System)
                _buildSectionTitle(
                  title: 'VZHĽAD A TÉMA (DEŇ / NOC)',
                  subtitle: 'Svetlý režim je ideálny na priame vonkajšie slnko',
                  icon: Icons.palette_outlined,
                  textColor: textColor,
                  mutedColor: textMuted,
                ),
                const SizedBox(height: 12),
                Row(
                  children: [
                    _buildThemeChip(ThemeMode.dark, 'Tmavý', Icons.dark_mode_rounded, isDark),
                    const SizedBox(width: 8),
                    _buildThemeChip(ThemeMode.light, 'Svetlý', Icons.light_mode_rounded, isDark),
                    const SizedBox(width: 8),
                    _buildThemeChip(ThemeMode.system, 'Systém', Icons.brightness_auto_rounded, isDark),
                  ],
                ),

                const SizedBox(height: 24),

                // 2. Distance Section
                _buildSectionTitle(
                  title: 'DĹŽKA ROVINKY (VZDIAĽENOSŤ)',
                  subtitle: 'Zadaj vzdialenosť podľa ihriska alebo záhrady',
                  icon: Icons.straighten_rounded,
                  textColor: textColor,
                  mutedColor: textMuted,
                ),
                const SizedBox(height: 12),

                // Distance value display
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: cardBg,
                    borderRadius: BorderRadius.circular(18),
                    border: Border.all(color: borderColor),
                  ),
                  child: Column(
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            'Nastavená dĺžka:',
                            style: TextStyle(
                              fontSize: 14,
                              color: textMuted,
                            ),
                          ),
                          Row(
                            crossAxisAlignment: CrossAxisAlignment.baseline,
                            textBaseline: TextBaseline.alphabetic,
                            children: [
                              Text(
                                _distance.toStringAsFixed(0),
                                style: const TextStyle(
                                  fontSize: 32,
                                  fontWeight: FontWeight.w900,
                                  color: AppTheme.electricCyan,
                                ),
                              ),
                              const SizedBox(width: 4),
                              const Text(
                                'metrov',
                                style: TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w700,
                                  color: AppTheme.electricCyan,
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),
                      SliderTheme(
                        data: SliderTheme.of(context).copyWith(
                          activeTrackColor: AppTheme.electricCyan,
                          inactiveTrackColor: isDark ? const Color(0xFF24324D) : const Color(0xFFCBD5E1),
                          thumbColor: AppTheme.neonVolt,
                          overlayColor: AppTheme.neonVolt.withValues(alpha: 0.2),
                          trackHeight: 6,
                        ),
                        child: Slider(
                          value: _distance,
                          min: 5.0,
                          max: 30.0,
                          divisions: 25,
                          onChanged: (val) => setState(() => _distance = val),
                          onChangeEnd: (val) => _syncChanges(),
                        ),
                      ),
                      // Preset buttons
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          _buildDistancePreset(10.0, '10m (Deti)', isDark),
                          _buildDistancePreset(12.0, '12m', isDark),
                          _buildDistancePreset(15.0, '15m', isDark),
                          _buildDistancePreset(20.0, '20m (Ofic.)', isDark),
                        ],
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 10),
                // Computed pace preview
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: AppTheme.neonVolt.withValues(alpha: 0.1),
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(
                      color: AppTheme.neonVolt.withValues(alpha: 0.3),
                    ),
                  ),
                  child: Row(
                    children: [
                      const Icon(Icons.info_outline_rounded,
                          color: AppTheme.neonVolt, size: 20),
                      const SizedBox(width: 10),
                      Expanded(
                        child: Text(
                          'Pri dĺžke ${_distance.toStringAsFixed(0)} m bude rovinka v Leveli 1 trvať presne ${shuttleTime.toStringAsFixed(2)}s.',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                            color: textColor,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 24),

                // 3. Starting Speed Section
                _buildSectionTitle(
                  title: 'POČIATOČNÁ RÝCHLOSŤ (LEVEL 1)',
                  subtitle: 'Nastav podľa veku a kondície detí',
                  icon: Icons.speed_rounded,
                  textColor: textColor,
                  mutedColor: textMuted,
                ),
                const SizedBox(height: 12),
                Row(
                  children: [
                    _buildSpeedChip(7.0, '7.0 km/h', 'Malé deti', isDark),
                    const SizedBox(width: 8),
                    _buildSpeedChip(8.0, '8.0 km/h', 'Odporúčané', isDark),
                    const SizedBox(width: 8),
                    _buildSpeedChip(8.5, '8.5 km/h', 'Štandard', isDark),
                  ],
                ),

                const SizedBox(height: 24),

                // 4. Audio & Voice Section
                _buildSectionTitle(
                  title: 'ZVUK A HLASOVÝ TRÉNER',
                  subtitle: 'Hlásenie ďalšieho levelu a pípnutia',
                  icon: Icons.volume_up_rounded,
                  textColor: textColor,
                  mutedColor: textMuted,
                ),
                const SizedBox(height: 12),

                _buildSwitchTile(
                  title: 'Hlasové hlásenie (TTS)',
                  subtitle: 'Vždy povie: „Pozor, ďalší level je 10!“',
                  value: _ttsEnabled,
                  onChanged: (val) {
                    setState(() => _ttsEnabled = val);
                    _syncChanges();
                  },
                  icon: Icons.record_voice_over_rounded,
                  isDark: isDark,
                ),

                _buildSwitchTile(
                  title: 'Zvukové pípnutia (Beep)',
                  subtitle: 'Akustický tón pri každej obrátke',
                  value: _soundEnabled,
                  onChanged: (val) {
                    setState(() => _soundEnabled = val);
                    _syncChanges();
                  },
                  icon: Icons.notifications_active_rounded,
                  isDark: isDark,
                ),

                _buildSwitchTile(
                  title: 'Vibrácia vo vrecku',
                  subtitle: 'Hmatová odozva pri obrátke a leveli',
                  value: _vibrationEnabled,
                  onChanged: (val) {
                    setState(() => _vibrationEnabled = val);
                    _syncChanges();
                  },
                  icon: Icons.vibration_rounded,
                  isDark: isDark,
                ),

                const SizedBox(height: 16),

                // 5. Countdown seconds
                _buildSectionTitle(
                  title: 'ODPOČÍTAVANIE PRED ŠTARTOM',
                  subtitle: 'Čas na postavenie sa na štartovú čiaru',
                  icon: Icons.timer_rounded,
                  textColor: textColor,
                  mutedColor: textMuted,
                ),
                const SizedBox(height: 12),
                Row(
                  children: [
                    _buildCountdownChip(3, '3 sekundy', isDark),
                    const SizedBox(width: 8),
                    _buildCountdownChip(5, '5 sekúnd', isDark),
                    const SizedBox(width: 8),
                    _buildCountdownChip(10, '10 sekúnd', isDark),
                  ],
                ),
                const SizedBox(height: 24),
              ],
            ),
          ),
        ],
      ),
    ),
  ),
);
}

  Widget _buildSectionTitle({
    required String title,
    required String subtitle,
    required IconData icon,
    required Color textColor,
    required Color mutedColor,
  }) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Icon(icon, size: 20, color: AppTheme.electricCyan),
        const SizedBox(width: 8),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                title,
                style: TextStyle(
                  fontSize: 13,
                  fontWeight: FontWeight.w800,
                  color: textColor,
                  letterSpacing: 0.5,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                subtitle,
                style: TextStyle(
                  fontSize: 11,
                  color: mutedColor,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildThemeChip(ThemeMode mode, String label, IconData icon, bool isDark) {
    final isSelected = _themeMode == mode;
    return Expanded(
      child: InkWell(
        onTap: () {
          setState(() => _themeMode = mode);
          _syncChanges();
        },
        borderRadius: BorderRadius.circular(14),
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 8),
          decoration: BoxDecoration(
            color: isSelected
                ? AppTheme.electricCyan.withValues(alpha: 0.2)
                : (isDark ? const Color(0xFF161F33) : const Color(0xFFF1F5F9)),
            borderRadius: BorderRadius.circular(14),
            border: Border.all(
              color: isSelected
                  ? AppTheme.electricCyan
                  : (isDark ? AppTheme.borderSubtle : AppTheme.borderLight),
              width: isSelected ? 2 : 1,
            ),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                icon,
                size: 16,
                color: isSelected
                    ? AppTheme.electricCyan
                    : (isDark ? Colors.white70 : const Color(0xFF475569)),
              ),
              const SizedBox(width: 6),
              Text(
                label,
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: isSelected ? FontWeight.w800 : FontWeight.w600,
                  color: isSelected
                      ? AppTheme.electricCyan
                      : (isDark ? Colors.white : AppTheme.textDark),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildDistancePreset(double distance, String label, bool isDark) {
    final isSelected = (_distance - distance).abs() < 0.1;
    return InkWell(
      onTap: () {
        setState(() => _distance = distance);
        _syncChanges();
      },
      borderRadius: BorderRadius.circular(10),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
        decoration: BoxDecoration(
          color: isSelected
              ? AppTheme.electricCyan.withValues(alpha: 0.2)
              : (isDark ? const Color(0xFF0F1523) : const Color(0xFFE2E8F0)),
          borderRadius: BorderRadius.circular(10),
          border: Border.all(
            color: isSelected ? AppTheme.electricCyan : (isDark ? const Color(0xFF24324D) : const Color(0xFFCBD5E1)),
          ),
        ),
        child: Text(
          label,
          style: TextStyle(
            fontSize: 11,
            fontWeight: isSelected ? FontWeight.w800 : FontWeight.w600,
            color: isSelected ? AppTheme.electricCyan : (isDark ? Colors.white70 : AppTheme.textDark),
          ),
        ),
      ),
    );
  }

  Widget _buildSpeedChip(double speed, String label, String desc, bool isDark) {
    final isSelected = (_startSpeed - speed).abs() < 0.1;
    return Expanded(
      child: InkWell(
        onTap: () {
          setState(() => _startSpeed = speed);
          _syncChanges();
        },
        borderRadius: BorderRadius.circular(12),
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 8),
          decoration: BoxDecoration(
            color: isSelected
                ? AppTheme.neonVolt.withValues(alpha: 0.18)
                : (isDark ? const Color(0xFF161F33) : const Color(0xFFF1F5F9)),
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: isSelected ? AppTheme.neonVolt : (isDark ? AppTheme.borderSubtle : AppTheme.borderLight),
              width: isSelected ? 1.5 : 1,
            ),
          ),
          child: Column(
            children: [
              Text(
                label,
                style: TextStyle(
                  fontSize: 13,
                  fontWeight: FontWeight.w800,
                  color: isSelected ? AppTheme.neonVolt : (isDark ? Colors.white : AppTheme.textDark),
                ),
              ),
              const SizedBox(height: 2),
              Text(
                desc,
                style: TextStyle(
                  fontSize: 10,
                  color: isSelected
                      ? AppTheme.neonVolt.withValues(alpha: 0.8)
                      : (isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B)),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildCountdownChip(int seconds, String label, bool isDark) {
    final isSelected = _countdownSeconds == seconds;
    return Expanded(
      child: InkWell(
        onTap: () {
          setState(() => _countdownSeconds = seconds);
          _syncChanges();
        },
        borderRadius: BorderRadius.circular(12),
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 10),
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: isSelected
                ? AppTheme.pulseAmber.withValues(alpha: 0.2)
                : (isDark ? const Color(0xFF161F33) : const Color(0xFFF1F5F9)),
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: isSelected ? AppTheme.pulseAmber : (isDark ? AppTheme.borderSubtle : AppTheme.borderLight),
            ),
          ),
          child: Text(
            label,
            style: TextStyle(
              fontSize: 12,
              fontWeight: isSelected ? FontWeight.w800 : FontWeight.w600,
              color: isSelected ? AppTheme.pulseAmber : (isDark ? Colors.white70 : AppTheme.textDark),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildSwitchTile({
    required String title,
    required String subtitle,
    required bool value,
    required Function(bool) onChanged,
    required IconData icon,
    required bool isDark,
  }) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF161F33) : const Color(0xFFF8FAFC),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: isDark ? AppTheme.borderSubtle : AppTheme.borderLight),
      ),
      child: Row(
        children: [
          Icon(icon, size: 22, color: AppTheme.electricCyan),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: TextStyle(
                    fontSize: 13,
                    fontWeight: FontWeight.w700,
                    color: isDark ? Colors.white : AppTheme.textDark,
                  ),
                ),
                Text(
                  subtitle,
                  style: TextStyle(
                    fontSize: 11,
                    color: isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B),
                  ),
                ),
              ],
            ),
          ),
          Switch(
            value: value,
            activeThumbColor: AppTheme.electricCyan,
            onChanged: onChanged,
          ),
        ],
      ),
    );
  }
}
