import 'package:flutter/material.dart';
import '../services/beep_test_controller.dart';
import '../theme/app_theme.dart';

class ResultsDialog extends StatelessWidget {
  final BeepTestController controller;
  final VoidCallback onRestart;

  const ResultsDialog({
    super.key,
    required this.controller,
    required this.onRestart,
  });

  static Future<void> show(
    BuildContext context, {
    required BeepTestController controller,
    required VoidCallback onRestart,
  }) {
    return showDialog(
      context: context,
      barrierDismissible: false,
      builder: (context) => ResultsDialog(
        controller: controller,
        onRestart: onRestart,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final badge = controller.getKidsBadgeTitle();
    final vo2 = controller.calculateVo2Max();
    final distance = controller.totalDistanceMeters;
    final minutes = controller.totalElapsedTime.inMinutes;
    final seconds = controller.totalElapsedTime.inSeconds % 60;
    final formattedTime =
        '${minutes.toString().padLeft(2, '0')}:${seconds.toString().padLeft(2, '0')}';

    final dialogBg = isDark ? const Color(0xFF131A29) : Colors.white;
    final cardBg = isDark ? const Color(0xFF161F33) : const Color(0xFFF8FAFC);
    final borderColor = isDark ? AppTheme.borderSubtle : AppTheme.borderLight;
    final textColor = isDark ? Colors.white : AppTheme.textDark;
    final textMuted = isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B);

    return Dialog(
      backgroundColor: Colors.transparent,
      insetPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
      child: Container(
        padding: const EdgeInsets.all(24),
        decoration: BoxDecoration(
          color: dialogBg,
          gradient: isDark
              ? const LinearGradient(
                  colors: [Color(0xFF131A29), Color(0xFF0A0E17)],
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                )
              : null,
          borderRadius: BorderRadius.circular(30),
          border: Border.all(
            color: isDark ? AppTheme.electricCyan.withValues(alpha: 0.4) : AppTheme.borderLight,
            width: 1.5,
          ),
          boxShadow: [
            BoxShadow(
              color: AppTheme.electricCyan.withValues(alpha: isDark ? 0.15 : 0.08),
              blurRadius: 30,
              spreadRadius: 2,
            ),
          ],
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            // App Icon 1 Branding
            Container(
              width: 64,
              height: 64,
              margin: const EdgeInsets.only(bottom: 14),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16),
                boxShadow: [
                  BoxShadow(
                    color: AppTheme.neonVolt.withValues(alpha: 0.4),
                    blurRadius: 18,
                    spreadRadius: 1,
                  ),
                ],
              ),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(16),
                child: Image.asset(
                  'assets/images/app_icon.png',
                  fit: BoxFit.cover,
                ),
              ),
            ),

            // Motivational Badge
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              decoration: BoxDecoration(
                gradient: AppTheme.neonGradient,
                borderRadius: BorderRadius.circular(20),
                boxShadow: [
                  BoxShadow(
                    color: AppTheme.neonVolt.withValues(alpha: 0.4),
                    blurRadius: 12,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: Text(
                badge,
                style: const TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w900,
                  color: Colors.black,
                  letterSpacing: 0.5,
                ),
              ),
            ),
            const SizedBox(height: 20),

            Text(
              'SKVELÝ BEH!',
              style: TextStyle(
                fontSize: 26,
                fontWeight: FontWeight.w900,
                color: textColor,
                letterSpacing: 1.0,
              ),
            ),
            const SizedBox(height: 4),
            Text(
              'Test ukončený pri dĺžke ${controller.config.distanceMeters.toStringAsFixed(0)} m',
              style: TextStyle(
                fontSize: 13,
                color: textMuted,
              ),
            ),
            const SizedBox(height: 24),

            // Score Highlight
            Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(vertical: 16),
              decoration: BoxDecoration(
                color: cardBg,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: borderColor),
              ),
              child: Column(
                children: [
                  Text(
                    'DOSIAHNUTÁ ÚROVEŇ',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w800,
                      color: textMuted,
                      letterSpacing: 1.0,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.baseline,
                    textBaseline: TextBaseline.alphabetic,
                    children: [
                      Text(
                        'LEVEL ${controller.currentLevelNumber}',
                        style: const TextStyle(
                          fontSize: 34,
                          fontWeight: FontWeight.w900,
                          color: AppTheme.electricCyan,
                        ),
                      ),
                      const SizedBox(width: 8),
                      Text(
                        '(${controller.currentShuttle}. rovinka)',
                        style: TextStyle(
                          fontSize: 15,
                          fontWeight: FontWeight.w700,
                          color: isDark ? AppTheme.neonVolt : const Color(0xFF059669),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),

            const SizedBox(height: 16),

            // Detailed Stats Grid
            Row(
              children: [
                Expanded(
                  child: _buildMetricTile(
                    'Celková vzdialenosť',
                    '${distance.toStringAsFixed(0)} m',
                    Icons.straighten_rounded,
                    AppTheme.neonVolt,
                    isDark,
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildMetricTile(
                    'Čas behu',
                    formattedTime,
                    Icons.timer_rounded,
                    AppTheme.electricCyan,
                    isDark,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                Expanded(
                  child: _buildMetricTile(
                    'Max rýchlosť',
                    controller.currentLevel.formattedSpeed,
                    Icons.speed_rounded,
                    AppTheme.pulseAmber,
                    isDark,
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildMetricTile(
                    'Odhad VO2 Max',
                    vo2.toStringAsFixed(1),
                    Icons.favorite_rounded,
                    AppTheme.dangerRose,
                    isDark,
                  ),
                ),
              ],
            ),

            const SizedBox(height: 28),

            // Action Buttons
            Row(
              children: [
                Expanded(
                  child: OutlinedButton(
                    onPressed: () => Navigator.pop(context),
                    style: OutlinedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      side: BorderSide(color: borderColor),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                    child: Text(
                      'ZAVRIEŤ',
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w700,
                        color: isDark ? Colors.white70 : const Color(0xFF475569),
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: ElevatedButton(
                    onPressed: () {
                      Navigator.pop(context);
                      onRestart();
                    },
                    style: ElevatedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      backgroundColor: AppTheme.electricCyan,
                      foregroundColor: Colors.black,
                      elevation: 0,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                    child: const Text(
                      'BEHAŤ ZNOVA',
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w900,
                        letterSpacing: 0.5,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildMetricTile(
    String label,
    String value,
    IconData icon,
    Color color,
    bool isDark,
  ) {
    final tileBg = isDark ? const Color(0xFF141D2E) : const Color(0xFFF8FAFC);
    final borderColor = isDark ? const Color(0xFF1E2B42) : AppTheme.borderLight;
    final textColor = isDark ? Colors.white : AppTheme.textDark;
    final textMuted = isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B);

    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: tileBg,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: borderColor),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(icon, size: 16, color: color),
              const SizedBox(width: 6),
              Expanded(
                child: Text(
                  label,
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: 11,
                    color: textMuted,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),
          Text(
            value,
            style: TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.w800,
              color: textColor,
            ),
          ),
        ],
      ),
    );
  }
}
