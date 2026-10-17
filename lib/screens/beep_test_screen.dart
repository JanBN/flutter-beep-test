import 'package:flutter/material.dart';
import '../services/beep_test_controller.dart';
import '../theme/app_theme.dart';
import '../widgets/level_jump_sheet.dart';
import '../widgets/outdoor_settings_sheet.dart';
import '../widgets/results_dialog.dart';
import '../widgets/shuttle_field_visualizer.dart';
import '../widgets/stat_badge.dart';

class BeepTestScreen extends StatelessWidget {
  final BeepTestController controller;

  const BeepTestScreen({super.key, required this.controller});

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: controller,
      builder: (context, _) {
        final isDark = Theme.of(context).brightness == Brightness.dark;
        final state = controller.state;
        final isRunning = state == BeepTestState.running;
        final isPaused = state == BeepTestState.paused;
        final isCountdown = state == BeepTestState.countdown;
        final isIdle = state == BeepTestState.idle;

        final bgGradient = isDark
            ? const LinearGradient(
                colors: [Color(0xFF090D16), Color(0xFF0E1624), Color(0xFF090D16)],
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
              )
            : const LinearGradient(
                colors: [Color(0xFFF8FAFC), Color(0xFFEDF2F7), Color(0xFFE2E8F0)],
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
              );

        return Scaffold(
          body: Container(
            decoration: BoxDecoration(gradient: bgGradient),
            child: SafeArea(
              child: Column(
                children: [
                  // Top App Bar
                  _buildHeader(context, isDark),

                  // Main Scrollable / Flexible Content
                  Expanded(
                    child: SingleChildScrollView(
                      physics: const BouncingScrollPhysics(),
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                      child: Column(
                        children: [
                          // Level & Shuttle Hero Card with Next Level Visual Countdown
                          _buildLevelHeroCard(context, isRunning, isCountdown, isDark),

                          const SizedBox(height: 16),

                          // Quick Level Control Bar (-1, Jump, +1)
                          _buildLevelSkipControls(context, isDark),

                          const SizedBox(height: 16),

                          // Running Track Visualizer (Line A <-> Line B) with Flipped Runner
                          ShuttleFieldVisualizer(
                            progress: controller.shuttleProgress,
                            directionToB: controller.shuttleDirection,
                            distanceMeters: controller.config.distanceMeters,
                            isRunning: isRunning,
                            remainingSeconds: controller.shuttleRemainingSeconds,
                          ),

                          const SizedBox(height: 16),

                          // Real-time Stats Grid
                          _buildStatsGrid(),
                        ],
                      ),
                    ),
                  ),

                  // Bottom Action Controls
                  _buildBottomControls(context, isIdle, isRunning, isPaused, isCountdown, isDark),
                ],
              ),
            ),
          ),
        );
      },
    );
  }

  /// Top navigation bar with logo, distance chip, theme toggle, and settings button
  Widget _buildHeader(BuildContext context, bool isDark) {
    IconData themeIcon = Icons.dark_mode_rounded;
    String themeTooltip = 'Tmavý režim';
    switch (controller.themeMode) {
      case ThemeMode.dark:
        themeIcon = Icons.dark_mode_rounded;
        themeTooltip = 'Tmavý režim';
        break;
      case ThemeMode.light:
        themeIcon = Icons.light_mode_rounded;
        themeTooltip = 'Svetlý režim';
        break;
      case ThemeMode.system:
        themeIcon = Icons.brightness_auto_rounded;
        themeTooltip = 'Podľa systému';
        break;
    }

    final cardBg = isDark ? const Color(0xFF161F33) : Colors.white;
    final borderColor = isDark ? AppTheme.borderSubtle : AppTheme.borderLight;
    final textColor = isDark ? Colors.white : AppTheme.textDark;

    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              Container(
                width: 38,
                height: 38,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(10),
                  boxShadow: [
                    BoxShadow(
                      color: AppTheme.neonVolt.withValues(alpha: 0.35),
                      blurRadius: 10,
                      spreadRadius: 1,
                    ),
                  ],
                ),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(10),
                  child: Image.asset(
                    'assets/images/app_icon.png',
                    fit: BoxFit.cover,
                  ),
                ),
              ),
              const SizedBox(width: 10),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'BEEP TEST PRO',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w900,
                      color: textColor,
                      letterSpacing: 0.5,
                    ),
                  ),
                  const Text(
                    'Ihriskový & Detský beh',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w700,
                      color: AppTheme.electricCyan,
                    ),
                  ),
                ],
              ),
            ],
          ),
          Row(
            children: [
              // Distance pill button
              InkWell(
                onTap: () => OutdoorSettingsSheet.show(
                  context,
                  config: controller.config,
                  currentThemeMode: controller.themeMode,
                  onSaveTheme: (mode) => controller.setThemeMode(mode),
                  onSave: (newConfig) => controller.updateConfig(newConfig),
                ),
                borderRadius: BorderRadius.circular(20),
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                  decoration: BoxDecoration(
                    color: cardBg,
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(color: AppTheme.electricCyan.withValues(alpha: 0.4)),
                  ),
                  child: Row(
                    children: [
                      const Icon(Icons.straighten_rounded,
                          size: 14, color: AppTheme.electricCyan),
                      const SizedBox(width: 4),
                      Text(
                        '${controller.config.distanceMeters.toStringAsFixed(0)}m',
                        style: TextStyle(
                          fontSize: 13,
                          fontWeight: FontWeight.w800,
                          color: textColor,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(width: 6),

              // Theme Mode Toggle (Dark / Light / System)
              IconButton(
                tooltip: themeTooltip,
                onPressed: () => controller.toggleThemeMode(),
                icon: Container(
                  padding: const EdgeInsets.all(6),
                  decoration: BoxDecoration(
                    color: cardBg,
                    shape: BoxShape.circle,
                    border: Border.all(color: borderColor),
                  ),
                  child: Icon(
                    themeIcon,
                    size: 18,
                    color: controller.themeMode == ThemeMode.light
                        ? Colors.amber.shade700
                        : (isDark ? AppTheme.electricCyan : Colors.blueGrey),
                  ),
                ),
              ),

              // Settings icon
              IconButton(
                onPressed: () => OutdoorSettingsSheet.show(
                  context,
                  config: controller.config,
                  currentThemeMode: controller.themeMode,
                  onSaveTheme: (mode) => controller.setThemeMode(mode),
                  onSave: (newConfig) => controller.updateConfig(newConfig),
                ),
                icon: Container(
                  padding: const EdgeInsets.all(6),
                  decoration: BoxDecoration(
                    color: cardBg,
                    shape: BoxShape.circle,
                    border: Border.all(color: borderColor),
                  ),
                  child: Icon(
                    Icons.tune_rounded,
                    size: 18,
                    color: isDark ? Colors.white70 : const Color(0xFF475569),
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  /// Big Level & Shuttle Hero Display with visual Next Level Countdown
  Widget _buildLevelHeroCard(
    BuildContext context,
    bool isRunning,
    bool isCountdown,
    bool isDark,
  ) {
    final cardBg = isDark ? const Color(0xFF131A29) : Colors.white;
    final borderColor = isDark ? AppTheme.borderSubtle : AppTheme.borderLight;
    final textColor = isDark ? Colors.white : AppTheme.textDark;
    final textMuted = isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B);

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(vertical: 18, horizontal: 16),
      decoration: BoxDecoration(
        color: cardBg,
        gradient: isDark ? AppTheme.cardGradientDark : AppTheme.cardGradientLight,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(
          color: isRunning
              ? (controller.isLastShuttleOfLevel
                  ? AppTheme.pulseAmber
                  : AppTheme.neonVolt.withValues(alpha: 0.5))
              : borderColor,
          width: isRunning ? 2 : 1.5,
        ),
        boxShadow: [
          BoxShadow(
            color: isRunning
                ? (controller.isLastShuttleOfLevel
                    ? AppTheme.pulseAmber.withValues(alpha: 0.2)
                    : AppTheme.neonVolt.withValues(alpha: isDark ? 0.08 : 0.05))
                : Colors.black.withValues(alpha: isDark ? 0.3 : 0.05),
            blurRadius: 20,
            spreadRadius: 2,
          ),
        ],
      ),
      child: Column(
        children: [
          // Countdown active mode before start
          if (isCountdown) ...[
            const Text(
              'PRIPRAVTE SA NA ŠTART',
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.w800,
                color: AppTheme.pulseAmber,
                letterSpacing: 1.2,
              ),
            ),
            const SizedBox(height: 10),
            Container(
              width: 90,
              height: 90,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: AppTheme.pulseAmber.withValues(alpha: 0.15),
                border: Border.all(color: AppTheme.pulseAmber, width: 3),
              ),
              child: Center(
                child: Text(
                  '${controller.countdownRemaining}',
                  style: TextStyle(
                    fontSize: 50,
                    fontWeight: FontWeight.w900,
                    color: textColor,
                  ),
                ),
              ),
            ),
            const SizedBox(height: 10),
            Text(
              'Štartujeme od Levelu ${controller.currentLevelNumber}',
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w600,
                color: textMuted,
              ),
            ),
          ] else ...[
            // Normal Running / Idle mode
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: BoxDecoration(
                    color: AppTheme.electricCyan.withValues(alpha: 0.12),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Text(
                    'AKTÍVNY LEVEL',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w800,
                      color: isRunning ? AppTheme.neonVolt : AppTheme.electricCyan,
                      letterSpacing: 1.0,
                    ),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 4),

            // Giant Level Number
            Text(
              'LEVEL ${controller.currentLevelNumber}',
              style: TextStyle(
                fontSize: 52,
                fontWeight: FontWeight.w900,
                color: textColor,
                letterSpacing: -1.0,
              ),
            ),

            // Shuttle stage info (e.g. Rovinka 2 z 14)
            Container(
              margin: const EdgeInsets.symmetric(vertical: 4),
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF1B253B) : const Color(0xFFF1F5F9),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(
                  color: isDark ? const Color(0xFF283654) : const Color(0xFFCBD5E1),
                ),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(Icons.sync_alt_rounded,
                      size: 16, color: AppTheme.neonVolt),
                  const SizedBox(width: 8),
                  Text(
                    'Rovinka ${controller.currentShuttle} z ${controller.currentLevel.shuttlesCount}',
                    style: TextStyle(
                      fontSize: 14,
                      fontWeight: FontWeight.w800,
                      color: textColor,
                    ),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 14),

            // VISUAL NEXT LEVEL COUNTDOWN SECTION (Requirement 2)
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
              decoration: BoxDecoration(
                color: controller.isLastShuttleOfLevel
                    ? AppTheme.pulseAmber.withValues(alpha: isDark ? 0.18 : 0.12)
                    : (isDark ? const Color(0xFF161F33) : const Color(0xFFF8FAFC)),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(
                  color: controller.isLastShuttleOfLevel
                      ? AppTheme.pulseAmber
                      : (isDark ? AppTheme.borderSubtle : AppTheme.borderLight),
                  width: controller.isLastShuttleOfLevel ? 2 : 1,
                ),
              ),
              child: Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Row(
                        children: [
                          Icon(
                            controller.isLastShuttleOfLevel
                                ? Icons.warning_amber_rounded
                                : Icons.alarm_rounded,
                            size: 18,
                            color: controller.isLastShuttleOfLevel
                                ? AppTheme.pulseAmber
                                : AppTheme.electricCyan,
                          ),
                          const SizedBox(width: 6),
                          Text(
                            controller.isLastShuttleOfLevel
                                ? '🚨 POSLEDNÁ ROVINKA!'
                                : 'ĎALŠÍ LEVEL ZAČÍNA ZA:',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w800,
                              color: controller.isLastShuttleOfLevel
                                  ? AppTheme.pulseAmber
                                  : textMuted,
                              letterSpacing: 0.5,
                            ),
                          ),
                        ],
                      ),
                      // Big remaining seconds readout
                      Text(
                        '${controller.levelRemainingSeconds.toStringAsFixed(1)}s',
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w900,
                          color: controller.isLastShuttleOfLevel
                              ? AppTheme.pulseAmber
                              : AppTheme.neonVolt,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),

                  // Visual Level Progress Bar
                  ClipRRect(
                    borderRadius: BorderRadius.circular(6),
                    child: LinearProgressIndicator(
                      value: controller.levelProgress,
                      backgroundColor: isDark
                          ? const Color(0xFF0F1728)
                          : const Color(0xFFE2E8F0),
                      valueColor: AlwaysStoppedAnimation<Color>(
                        controller.isLastShuttleOfLevel
                            ? AppTheme.pulseAmber
                            : AppTheme.neonVolt,
                      ),
                      minHeight: 8,
                    ),
                  ),

                  const SizedBox(height: 6),

                  // Helper caption
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'Postup v leveli: ${(controller.levelProgress * 100).toInt()}%',
                        style: TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.w600,
                          color: textMuted,
                        ),
                      ),
                      Text(
                        'Do Levelu ${controller.currentLevelNumber + 1}: ${controller.remainingShuttlesInLevel} ${controller.remainingShuttlesInLevel == 1 ? "rovinka" : "rovinky"}',
                        style: TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                          color: controller.isLastShuttleOfLevel
                              ? AppTheme.pulseAmber
                              : (isDark ? Colors.white70 : const Color(0xFF334155)),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),

            const SizedBox(height: 10),

            // Voice announcement reminder banner
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
              decoration: BoxDecoration(
                color: (isDark ? Colors.white : Colors.black).withValues(alpha: 0.04),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(Icons.record_voice_over_rounded,
                      size: 14, color: AppTheme.electricCyan),
                  const SizedBox(width: 6),
                  Text(
                    'Hlas povie: „Pozor, ďalší level je ${controller.currentLevelNumber + 1}!“',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                      color: textMuted,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ],
      ),
    );
  }

  /// Level Skip controls bar with -1 Level, Level Picker Sheet, +1 Level
  /// Requirement: "A taktie chcem vediet preskocit na ktorykolvek level"
  Widget _buildLevelSkipControls(BuildContext context, bool isDark) {
    final cardBg = isDark ? const Color(0xFF141C2D) : Colors.white;
    final borderColor = isDark ? AppTheme.borderSubtle : AppTheme.borderLight;
    final textColor = isDark ? Colors.white : AppTheme.textDark;

    return Row(
      children: [
        // Previous level button
        Expanded(
          flex: 2,
          child: InkWell(
            onTap: controller.currentLevelNumber > 1
                ? () => controller.previousLevel()
                : null,
            borderRadius: BorderRadius.circular(16),
            child: Container(
              padding: const EdgeInsets.symmetric(vertical: 12),
              decoration: BoxDecoration(
                color: cardBg,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: borderColor),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.remove_circle_outline_rounded,
                    size: 18,
                    color: controller.currentLevelNumber > 1
                        ? textColor
                        : (isDark ? Colors.white24 : Colors.black26),
                  ),
                  const SizedBox(width: 4),
                  Text(
                    '-1 Level',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w700,
                      color: controller.currentLevelNumber > 1
                          ? textColor
                          : (isDark ? Colors.white24 : Colors.black26),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),

        const SizedBox(width: 8),

        // Jump to any level (Opens full LevelJumpSheet)
        Expanded(
          flex: 4,
          child: ElevatedButton.icon(
            onPressed: () => LevelJumpSheet.show(
              context,
              currentLevel: controller.currentLevelNumber,
              config: controller.config,
              onSelectLevel: (lvl) => controller.jumpToLevel(lvl),
            ),
            icon: const Icon(Icons.bolt_rounded, size: 20, color: Colors.black),
            label: const Text(
              'SKOK NA LEVEL',
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w900,
                color: Colors.black,
                letterSpacing: 0.5,
              ),
            ),
            style: ElevatedButton.styleFrom(
              padding: const EdgeInsets.symmetric(vertical: 13),
              backgroundColor: AppTheme.electricCyan,
              elevation: 0,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(16),
              ),
            ),
          ),
        ),

        const SizedBox(width: 8),

        // Next level button
        Expanded(
          flex: 2,
          child: InkWell(
            onTap: () => controller.nextLevel(),
            borderRadius: BorderRadius.circular(16),
            child: Container(
              padding: const EdgeInsets.symmetric(vertical: 12),
              decoration: BoxDecoration(
                color: cardBg,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: borderColor),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    '+1 Level',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w700,
                      color: textColor,
                    ),
                  ),
                  const SizedBox(width: 4),
                  Icon(
                    Icons.add_circle_outline_rounded,
                    size: 18,
                    color: textColor,
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }

  /// Real-time athletic stats grid (Speed, Total Distance, Elapsed Time, Shuttle Pace)
  Widget _buildStatsGrid() {
    final minutes = controller.totalElapsedTime.inMinutes;
    final seconds = controller.totalElapsedTime.inSeconds % 60;
    final formattedTime =
        '${minutes.toString().padLeft(2, '0')}:${seconds.toString().padLeft(2, '0')}';

    return Column(
      children: [
        Row(
          children: [
            Expanded(
              child: StatBadge(
                label: 'Rýchlosť',
                value: controller.currentLevel.speedKmh.toStringAsFixed(1),
                unit: 'km/h',
                icon: Icons.speed_rounded,
                accentColor: AppTheme.neonVolt,
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: StatBadge(
                label: 'Vzdialenosť',
                value: controller.totalDistanceMeters.toStringAsFixed(0),
                unit: 'm',
                icon: Icons.straighten_rounded,
                accentColor: AppTheme.electricCyan,
              ),
            ),
          ],
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: StatBadge(
                label: 'Čas behu',
                value: formattedTime,
                icon: Icons.timer_rounded,
                accentColor: AppTheme.pulseAmber,
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: StatBadge(
                label: 'Čas rovinky',
                value: controller.currentLevel.shuttleDurationSeconds.toStringAsFixed(2),
                unit: 's',
                icon: Icons.hourglass_bottom_rounded,
                accentColor: AppTheme.purpleEnergy,
              ),
            ),
          ],
        ),
      ],
    );
  }

  /// Bottom action buttons (Start, Pause, Resume, Stop)
  Widget _buildBottomControls(
    BuildContext context,
    bool isIdle,
    bool isRunning,
    bool isPaused,
    bool isCountdown,
    bool isDark,
  ) {
    final barBg = isDark ? const Color(0xFF0F1523).withValues(alpha: 0.95) : Colors.white.withValues(alpha: 0.95);
    final borderColor = isDark ? AppTheme.borderSubtle : AppTheme.borderLight;

    return Container(
      padding: const EdgeInsets.fromLTRB(16, 12, 16, 16),
      decoration: BoxDecoration(
        color: barBg,
        border: Border(
          top: BorderSide(color: borderColor, width: 1),
        ),
      ),
      child: SafeArea(
        top: false,
        child: isIdle
            ? SizedBox(
                width: double.infinity,
                height: 56,
                child: ElevatedButton.icon(
                  onPressed: () => controller.start(),
                  icon: const Icon(Icons.play_arrow_rounded,
                      size: 28, color: Colors.black),
                  label: const Text(
                    'ŠTART BEEP TESTU',
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.w900,
                      color: Colors.black,
                      letterSpacing: 1.0,
                    ),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppTheme.neonVolt,
                    elevation: 8,
                    shadowColor: AppTheme.neonVolt.withValues(alpha: 0.5),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(18),
                    ),
                  ),
                ),
              )
            : isCountdown
                ? SizedBox(
                    width: double.infinity,
                    height: 56,
                    child: OutlinedButton(
                      onPressed: () => controller.reset(),
                      style: OutlinedButton.styleFrom(
                        side: const BorderSide(color: AppTheme.dangerRose),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(18),
                        ),
                      ),
                      child: const Text(
                        'ZRUŠIŤ ODPOČÍTAVANIE',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w800,
                          color: AppTheme.dangerRose,
                        ),
                      ),
                    ),
                  )
                : Row(
                    children: [
                      // Stop button (opens results dialog)
                      Expanded(
                        flex: 2,
                        child: OutlinedButton.icon(
                          onPressed: () async {
                            await controller.stop();
                            if (context.mounted) {
                              ResultsDialog.show(
                                context,
                                controller: controller,
                                onRestart: () => controller.start(),
                              );
                            }
                          },
                          icon: const Icon(Icons.stop_rounded,
                              color: AppTheme.dangerRose, size: 22),
                          label: const Text(
                            'UKONČIŤ',
                            style: TextStyle(
                              fontSize: 13,
                              fontWeight: FontWeight.w800,
                              color: AppTheme.dangerRose,
                            ),
                          ),
                          style: OutlinedButton.styleFrom(
                            padding: const EdgeInsets.symmetric(vertical: 16),
                            side: const BorderSide(color: AppTheme.dangerRose, width: 1.5),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(16),
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(width: 12),

                      // Pause or Resume button
                      Expanded(
                        flex: 3,
                        child: ElevatedButton.icon(
                          onPressed: () {
                            if (isRunning) {
                              controller.pause();
                            } else if (isPaused) {
                              controller.resume();
                            }
                          },
                          icon: Icon(
                            isRunning
                                ? Icons.pause_rounded
                                : Icons.play_arrow_rounded,
                            color: Colors.black,
                            size: 24,
                          ),
                          label: Text(
                            isRunning ? 'PAUZA' : 'POKRAČOVAŤ',
                            style: const TextStyle(
                              fontSize: 15,
                              fontWeight: FontWeight.w900,
                              color: Colors.black,
                              letterSpacing: 0.5,
                            ),
                          ),
                          style: ElevatedButton.styleFrom(
                            padding: const EdgeInsets.symmetric(vertical: 16),
                            backgroundColor: isRunning
                                ? AppTheme.pulseAmber
                                : AppTheme.neonVolt,
                            elevation: 6,
                            shadowColor: (isRunning
                                    ? AppTheme.pulseAmber
                                    : AppTheme.neonVolt)
                                .withValues(alpha: 0.4),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(16),
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
      ),
    );
  }
}
