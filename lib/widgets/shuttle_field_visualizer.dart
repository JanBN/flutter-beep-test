import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class ShuttleFieldVisualizer extends StatelessWidget {
  final double progress; // 0.0 to 1.0
  final bool directionToB; // true: A -> B, false: B -> A
  final double distanceMeters;
  final bool isRunning;
  final double remainingSeconds;

  const ShuttleFieldVisualizer({
    super.key,
    required this.progress,
    required this.directionToB,
    required this.distanceMeters,
    required this.isRunning,
    required this.remainingSeconds,
  });

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    // Current normalized position of runner on track (0.0 = Line A, 1.0 = Line B)
    final double runnerPos = directionToB ? progress : (1.0 - progress);

    final cardBg = isDark ? const Color(0xFF131A29) : Colors.white;
    final courtBg = isDark ? const Color(0xFF0F1728) : const Color(0xFFEEF2F6);
    final borderColor = isDark ? AppTheme.borderSubtle : AppTheme.borderLight;
    final textColor = isDark ? Colors.white : AppTheme.textDark;
    final textMuted = isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B);

    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: cardBg,
        gradient: isDark ? AppTheme.cardGradientDark : AppTheme.cardGradientLight,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: borderColor, width: 1.5),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: isDark ? 0.4 : 0.06),
            blurRadius: 16,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Column(
        children: [
          // Header with distance & direction
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  Container(
                    width: 8,
                    height: 8,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: isRunning ? AppTheme.neonVolt : Colors.grey,
                      boxShadow: isRunning
                          ? [
                              BoxShadow(
                                color: AppTheme.neonVolt.withValues(alpha: 0.8),
                                blurRadius: 8,
                                spreadRadius: 2,
                              )
                            ]
                          : null,
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text(
                    isRunning
                        ? (directionToB ? 'SMER: ČIARA A ➔ B' : 'SMER: ČIARA B ➔ A')
                        : 'ROVINKA PRIPRAVENÁ',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.w700,
                      color: isRunning ? (isDark ? AppTheme.neonVolt : const Color(0xFF059669)) : textMuted,
                      letterSpacing: 1.0,
                    ),
                  ),
                ],
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: AppTheme.electricCyan.withValues(alpha: 0.12),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(
                    color: AppTheme.electricCyan.withValues(alpha: 0.3),
                    width: 1,
                  ),
                ),
                child: Text(
                  '${distanceMeters.toStringAsFixed(0)} METROV',
                  style: const TextStyle(
                    fontSize: 11,
                    fontWeight: FontWeight.w800,
                    color: AppTheme.electricCyan,
                    letterSpacing: 0.5,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 18),

          // Track Area
          LayoutBuilder(
            builder: (context, constraints) {
              final trackWidth = constraints.maxWidth;
              const runnerRadius = 20.0;
              final maxLeft = trackWidth - (runnerRadius * 2);
              final currentLeft = (runnerPos * maxLeft).clamp(0.0, maxLeft);

              return SizedBox(
                height: 72,
                child: Stack(
                  alignment: Alignment.centerLeft,
                  children: [
                    // Field background court
                    Container(
                      height: 52,
                      decoration: BoxDecoration(
                        color: courtBg,
                        borderRadius: BorderRadius.circular(14),
                        border: Border.all(
                          color: isDark ? const Color(0xFF1E293B) : const Color(0xFFCBD5E1),
                          width: 1,
                        ),
                      ),
                    ),

                    // Center dashed line
                    Positioned.fill(
                      child: Center(
                        child: CustomPaint(
                          painter: _DashedLinePainter(
                            color: isDark ? const Color(0xFF334155) : const Color(0xFFCBD5E1),
                          ),
                          size: Size(trackWidth - 32, 2),
                        ),
                      ),
                    ),

                    // Left Boundary Line (Line A)
                    Positioned(
                      left: 12,
                      top: 10,
                      bottom: 10,
                      child: Container(
                        width: 4,
                        decoration: BoxDecoration(
                          color: AppTheme.electricCyan,
                          borderRadius: BorderRadius.circular(2),
                          boxShadow: [
                            BoxShadow(
                              color: AppTheme.electricCyan.withValues(alpha: 0.6),
                              blurRadius: 6,
                            ),
                          ],
                        ),
                      ),
                    ),

                    // Right Boundary Line (Line B)
                    Positioned(
                      right: 12,
                      top: 10,
                      bottom: 10,
                      child: Container(
                        width: 4,
                        decoration: BoxDecoration(
                          color: AppTheme.neonVolt,
                          borderRadius: BorderRadius.circular(2),
                          boxShadow: [
                            BoxShadow(
                              color: AppTheme.neonVolt.withValues(alpha: 0.6),
                              blurRadius: 6,
                            ),
                          ],
                        ),
                      ),
                    ),

                    // Directional chevron arrows behind runner
                    Positioned.fill(
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: List.generate(
                          5,
                          (i) => Icon(
                            directionToB
                                ? Icons.arrow_forward_ios_rounded
                                : Icons.arrow_back_ios_new_rounded,
                            size: 14,
                            color: (isDark ? Colors.white : Colors.black)
                                .withValues(alpha: isRunning ? 0.25 : 0.08),
                          ),
                        ),
                      ),
                    ),

                    // Running Dot / Runner Avatar (Flipped horizontally when running backwards!)
                    Positioned(
                      left: currentLeft,
                      child: Container(
                        width: runnerRadius * 2,
                        height: runnerRadius * 2,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          gradient: const LinearGradient(
                            colors: [Color(0xFF00F2FE), Color(0xFF10E76F)],
                            begin: Alignment.topLeft,
                            end: Alignment.bottomRight,
                          ),
                          boxShadow: [
                            BoxShadow(
                              color: AppTheme.neonVolt.withValues(alpha: isRunning ? 0.7 : 0.2),
                              blurRadius: isRunning ? 16 : 6,
                              spreadRadius: isRunning ? 3 : 0,
                            ),
                          ],
                        ),
                        child: Center(
                          // User requirement: "ked panacik bezi napoak, tak ho otoc naopak v gui"
                          child: Transform.flip(
                            flipX: !directionToB,
                            child: Icon(
                              Icons.directions_run_rounded,
                              size: 24,
                              color: Colors.black.withValues(alpha: 0.9),
                            ),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              );
            },
          ),

          const SizedBox(height: 8),

          // Ground Labels (0m and target distance)
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                'ČIARA A (0 m)',
                style: TextStyle(
                  fontSize: 11,
                  fontWeight: FontWeight.w700,
                  color: AppTheme.electricCyan,
                ),
              ),
              if (isRunning)
                Text(
                  'Obrátka o ${remainingSeconds.toStringAsFixed(1)}s',
                  style: TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.w700,
                    color: textColor,
                  ),
                ),
              const Text(
                'ČIARA B',
                style: TextStyle(
                  fontSize: 11,
                  fontWeight: FontWeight.w700,
                  color: AppTheme.neonVolt,
                ),
              ),
            ],
          ),

          const SizedBox(height: 12),

          // Linear shuttle pace progress indicator
          ClipRRect(
            borderRadius: BorderRadius.circular(6),
            child: LinearProgressIndicator(
              value: progress,
              backgroundColor: isDark ? const Color(0xFF1E293B) : const Color(0xFFE2E8F0),
              valueColor: AlwaysStoppedAnimation<Color>(
                directionToB ? AppTheme.electricCyan : AppTheme.neonVolt,
              ),
              minHeight: 5,
            ),
          ),
        ],
      ),
    );
  }
}

class _DashedLinePainter extends CustomPainter {
  final Color color;

  _DashedLinePainter({required this.color});

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = color
      ..strokeWidth = 1.5;

    const dashWidth = 6.0;
    const dashSpace = 4.0;
    double startX = 0.0;

    while (startX < size.width) {
      canvas.drawLine(
        Offset(startX, size.height / 2),
        Offset(startX + dashWidth, size.height / 2),
        paint,
      );
      startX += dashWidth + dashSpace;
    }
  }

  @override
  bool shouldRepaint(covariant _DashedLinePainter oldDelegate) =>
      oldDelegate.color != color;
}
