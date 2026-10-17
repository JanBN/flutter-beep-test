import 'package:flutter/material.dart';
import '../models/beep_level.dart';
import '../models/beep_test_config.dart';
import '../theme/app_theme.dart';

class LevelJumpSheet extends StatelessWidget {
  final int currentLevel;
  final BeepTestConfig config;
  final Function(int level) onSelectLevel;

  const LevelJumpSheet({
    super.key,
    required this.currentLevel,
    required this.config,
    required this.onSelectLevel,
  });

  static Future<void> show(
    BuildContext context, {
    required int currentLevel,
    required BeepTestConfig config,
    required Function(int level) onSelectLevel,
  }) {
    return showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => LevelJumpSheet(
        currentLevel: currentLevel,
        config: config,
        onSelectLevel: onSelectLevel,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final sheetBg = isDark ? const Color(0xFF0F1523) : Colors.white;
    final cardBg = isDark ? const Color(0xFF151D2F) : const Color(0xFFF8FAFC);
    final borderColor = isDark ? AppTheme.borderSubtle : AppTheme.borderLight;
    final textColor = isDark ? Colors.white : AppTheme.textDark;
    final textMuted = isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B);

    return Container(
      height: MediaQuery.of(context).size.height * 0.75,
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
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'SKOK NA LEVEL',
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w800,
                        color: textColor,
                        letterSpacing: 0.5,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      'Prepočítané pre vzdialenosť ${config.distanceMeters.toStringAsFixed(0)} m',
                      style: TextStyle(
                        fontSize: 12,
                        color: textMuted,
                      ),
                    ),
                  ],
                ),
                IconButton(
                  onPressed: () => Navigator.pop(context),
                  icon: Icon(
                    Icons.close_rounded,
                    color: isDark ? Colors.white70 : const Color(0xFF475569),
                  ),
                ),
              ],
            ),
          ),

          Divider(color: borderColor, height: 1),

          // Quick jump action chips
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                children: [
                  _buildQuickChip(context, 'Level 1 (Štart)', 1, isDark),
                  _buildQuickChip(context, 'Level 5 (Zahriatie)', 5, isDark),
                  _buildQuickChip(context, 'Level 10 (Výzva)', 10, isDark),
                  _buildQuickChip(context, 'Level 15 (Športovci)', 15, isDark),
                ],
              ),
            ),
          ),

          // Level Grid
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.fromLTRB(16, 8, 16, 24),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                childAspectRatio: 1.7,
                crossAxisSpacing: 12,
                mainAxisSpacing: 12,
              ),
              itemCount: 25, // Levels 1 to 25
              itemBuilder: (context, index) {
                final levelNum = index + 1;
                final isCurrent = levelNum == currentLevel;
                final levelInfo = BeepLevel.calculate(
                  levelNumber: levelNum,
                  config: config,
                );

                return InkWell(
                  onTap: () {
                    onSelectLevel(levelNum);
                    Navigator.pop(context);
                  },
                  borderRadius: BorderRadius.circular(16),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 200),
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: isCurrent
                          ? AppTheme.electricCyan.withValues(alpha: 0.15)
                          : cardBg,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(
                        color: isCurrent
                            ? AppTheme.electricCyan
                            : borderColor,
                        width: isCurrent ? 2 : 1,
                      ),
                      boxShadow: isCurrent
                          ? [
                              BoxShadow(
                                color: AppTheme.electricCyan.withValues(alpha: 0.3),
                                blurRadius: 10,
                                spreadRadius: 1,
                              ),
                            ]
                          : null,
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text(
                              'LEVEL $levelNum',
                              style: TextStyle(
                                fontSize: 16,
                                fontWeight: FontWeight.w800,
                                color: isCurrent
                                    ? AppTheme.electricCyan
                                    : textColor,
                              ),
                            ),
                            if (isCurrent)
                              Container(
                                padding: const EdgeInsets.symmetric(
                                    horizontal: 6, vertical: 2),
                                decoration: BoxDecoration(
                                  color: AppTheme.electricCyan,
                                  borderRadius: BorderRadius.circular(6),
                                ),
                                child: const Text(
                                  'AKTÍVNY',
                                  style: TextStyle(
                                    fontSize: 9,
                                    fontWeight: FontWeight.w900,
                                    color: Colors.black,
                                  ),
                                ),
                              ),
                          ],
                        ),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Row(
                              children: [
                                const Icon(Icons.speed_rounded,
                                    size: 14, color: AppTheme.neonVolt),
                                const SizedBox(width: 4),
                                Text(
                                  levelInfo.formattedSpeed,
                                  style: TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.w700,
                                    color: textColor,
                                  ),
                                ),
                              ],
                            ),
                            Row(
                              children: [
                                Icon(Icons.timer_outlined,
                                    size: 14, color: textMuted),
                                const SizedBox(width: 4),
                                Text(
                                  levelInfo.formattedShuttleTime,
                                  style: TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.w600,
                                    color: textMuted,
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                        Text(
                          '${levelInfo.shuttlesCount} roviniek (~60s)',
                          style: TextStyle(
                            fontSize: 11,
                            color: textMuted.withValues(alpha: 0.8),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    ),
  );
}

  Widget _buildQuickChip(BuildContext context, String title, int level, bool isDark) {
    return Padding(
      padding: const EdgeInsets.only(right: 8),
      child: ActionChip(
        label: Text(
          title,
          style: TextStyle(
            fontSize: 12,
            fontWeight: FontWeight.w700,
            color: isDark ? Colors.white : AppTheme.textDark,
          ),
        ),
        backgroundColor: isDark ? const Color(0xFF1C263B) : const Color(0xFFF1F5F9),
        side: BorderSide(color: isDark ? AppTheme.borderSubtle : AppTheme.borderLight),
        onPressed: () {
          onSelectLevel(level);
          Navigator.pop(context);
        },
      ),
    );
  }
}
