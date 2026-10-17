import 'dart:async';
import 'package:flutter/material.dart';
import '../services/beep_test_controller.dart';
import '../theme/app_theme.dart';
import 'beep_test_screen.dart';

class SplashScreen extends StatefulWidget {
  final BeepTestController controller;

  const SplashScreen({super.key, required this.controller});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen>
    with SingleTickerProviderStateMixin {
  late final AnimationController _animController;
  late final Animation<double> _pulseAnimation;
  Timer? _timer;
  bool _navigated = false;

  @override
  void initState() {
    super.initState();

    _animController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1400),
    )..repeat(reverse: true);

    _pulseAnimation = Tween<double>(begin: 0.95, end: 1.08).animate(
      CurvedAnimation(
        parent: _animController,
        curve: Curves.easeInOut,
      ),
    );

    // Auto-advance after 1.8 seconds
    _timer = Timer(const Duration(milliseconds: 1800), _navigateToHome);
  }

  void _navigateToHome() {
    if (_navigated || !mounted) return;
    _navigated = true;
    Navigator.of(context).pushReplacement(
      PageRouteBuilder(
        transitionDuration: const Duration(milliseconds: 500),
        pageBuilder: (context, animation, secondaryAnimation) =>
            BeepTestScreen(controller: widget.controller),
        transitionsBuilder: (context, animation, secondaryAnimation, child) {
          return FadeTransition(opacity: animation, child: child);
        },
      ),
    );
  }

  @override
  void dispose() {
    _timer?.cancel();
    _animController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF090D16),
      body: GestureDetector(
        behavior: HitTestBehavior.opaque,
        onTap: _navigateToHome, // Tap to skip
        child: Container(
          width: double.infinity,
          height: double.infinity,
          decoration: const BoxDecoration(
            gradient: RadialGradient(
              center: Alignment(0, -0.15),
              radius: 0.9,
              colors: [
                Color(0xFF132238),
                Color(0xFF090D16),
              ],
            ),
          ),
          child: SafeArea(
            child: Stack(
              alignment: Alignment.center,
              children: [
                // Sonic Rings Effect behind icon
                AnimatedBuilder(
                  animation: _animController,
                  builder: (context, _) {
                    final progress = _animController.value;
                    return Stack(
                      alignment: Alignment.center,
                      children: [
                        Container(
                          width: 220 + (progress * 40),
                          height: 220 + (progress * 40),
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            border: Border.all(
                              color: AppTheme.electricCyan.withValues(
                                alpha: (1.0 - progress) * 0.35,
                              ),
                              width: 2,
                            ),
                          ),
                        ),
                        Container(
                          width: 270 + (progress * 50),
                          height: 270 + (progress * 50),
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            border: Border.all(
                              color: AppTheme.neonVolt.withValues(
                                alpha: (1.0 - progress) * 0.2,
                              ),
                              width: 1.5,
                            ),
                          ),
                        ),
                      ],
                    );
                  },
                ),

                // Center Branding
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    // Icon 1 with glowing shadow and squircle clipping
                    ScaleTransition(
                      scale: _pulseAnimation,
                      child: Container(
                        width: 140,
                        height: 140,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(32),
                          boxShadow: [
                            BoxShadow(
                              color: AppTheme.neonVolt.withValues(alpha: 0.4),
                              blurRadius: 36,
                              spreadRadius: 2,
                            ),
                            BoxShadow(
                              color: AppTheme.electricCyan.withValues(alpha: 0.3),
                              blurRadius: 20,
                              offset: const Offset(0, 10),
                            ),
                          ],
                        ),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(32),
                          child: Image.asset(
                            'assets/images/app_icon.png',
                            fit: BoxFit.cover,
                          ),
                        ),
                      ),
                    ),

                    const SizedBox(height: 36),

                    // App Title
                    ShaderMask(
                      shaderCallback: (bounds) => const LinearGradient(
                        colors: [Colors.white, AppTheme.electricCyan],
                        begin: Alignment.topLeft,
                        end: Alignment.bottomRight,
                      ).createShader(bounds),
                      child: const Text(
                        'BEEP TEST PRO',
                        style: TextStyle(
                          fontSize: 32,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 2.0,
                          color: Colors.white,
                        ),
                      ),
                    ),

                    const SizedBox(height: 8),

                    // Subtitle
                    Text(
                      'Ihriskový & Detský vytrvalostný test',
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w600,
                        letterSpacing: 0.5,
                        color: Colors.white.withValues(alpha: 0.7),
                      ),
                    ),

                    const SizedBox(height: 16),

                    // Distance badge
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 14,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: const Color(0xFF131A29),
                        borderRadius: BorderRadius.circular(20),
                        border: Border.all(
                          color: AppTheme.neonVolt.withValues(alpha: 0.4),
                        ),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Container(
                            width: 8,
                            height: 8,
                            decoration: const BoxDecoration(
                              color: AppTheme.neonVolt,
                              shape: BoxShape.circle,
                            ),
                          ),
                          const SizedBox(width: 8),
                          Text(
                            '${widget.controller.config.distanceMeters.toStringAsFixed(0)} METROV PACER',
                            style: const TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w800,
                              letterSpacing: 1.2,
                              color: AppTheme.neonVolt,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),

                // Bottom loading prompt
                Positioned(
                  bottom: 32,
                  child: Column(
                    children: [
                      SizedBox(
                        width: 24,
                        height: 24,
                        child: CircularProgressIndicator(
                          strokeWidth: 2.5,
                          valueColor: AlwaysStoppedAnimation<Color>(
                            AppTheme.electricCyan.withValues(alpha: 0.8),
                          ),
                        ),
                      ),
                      const SizedBox(height: 12),
                      Text(
                        'Pripravujem zvukový systém...',
                        style: TextStyle(
                          fontSize: 12,
                          color: Colors.white.withValues(alpha: 0.4),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
