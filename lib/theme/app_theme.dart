import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AppTheme {
  // Dark Theme Colors
  static const Color bgDark = Color(0xFF090D16);
  static const Color cardDark = Color(0xFF131A29);
  static const Color cardDarkHover = Color(0xFF1C263B);
  static const Color borderSubtle = Color(0xFF24324D);

  // Light Theme Colors (High-contrast outdoor daylight)
  static const Color bgLight = Color(0xFFF4F6FB);
  static const Color cardLight = Color(0xFFFFFFFF);
  static const Color borderLight = Color(0xFFE2E8F0);
  static const Color textDark = Color(0xFF0F172A);
  static const Color textMutedLight = Color(0xFF64748B);

  // Accents
  static const Color neonVolt = Color(0xFF10E76F); // Active running green
  static const Color electricCyan = Color(0xFF00B4D8); // Cyan
  static const Color vibrantCyan = Color(0xFF00F2FE); // High energy cyan
  static const Color pulseAmber = Color(0xFFFF9F1C); // Warning / countdown
  static const Color dangerRose = Color(0xFFFF3366); // Stop / High intensity
  static const Color purpleEnergy = Color(0xFF7928CA);

  // Gradients
  static const LinearGradient primaryGradient = LinearGradient(
    colors: [Color(0xFF00F2FE), Color(0xFF4FACFE)],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static const LinearGradient neonGradient = LinearGradient(
    colors: [Color(0xFF10E76F), Color(0xFF00F2FE)],
    begin: Alignment.centerLeft,
    end: Alignment.centerRight,
  );

  static const LinearGradient flameGradient = LinearGradient(
    colors: [Color(0xFFFF9F1C), Color(0xFFFF3366)],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static const LinearGradient cardGradientDark = LinearGradient(
    colors: [Color(0xFF161F33), Color(0xFF101726)],
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
  );

  static const LinearGradient cardGradientLight = LinearGradient(
    colors: [Color(0xFFFFFFFF), Color(0xFFF8FAFC)],
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
  );

  static ThemeData get darkTheme {
    final textTheme = GoogleFonts.outfitTextTheme(ThemeData.dark().textTheme);

    return ThemeData(
      brightness: Brightness.dark,
      scaffoldBackgroundColor: bgDark,
      primaryColor: vibrantCyan,
      colorScheme: const ColorScheme.dark(
        primary: vibrantCyan,
        secondary: neonVolt,
        surface: cardDark,
        error: dangerRose,
      ),
      textTheme: textTheme.copyWith(
        displayLarge: GoogleFonts.outfit(
          fontSize: 64,
          fontWeight: FontWeight.w800,
          color: Colors.white,
          letterSpacing: -1.5,
        ),
        displayMedium: GoogleFonts.outfit(
          fontSize: 48,
          fontWeight: FontWeight.w800,
          color: Colors.white,
          letterSpacing: -1.0,
        ),
        headlineMedium: GoogleFonts.outfit(
          fontSize: 28,
          fontWeight: FontWeight.w700,
          color: Colors.white,
        ),
        titleLarge: GoogleFonts.outfit(
          fontSize: 20,
          fontWeight: FontWeight.w600,
          color: Colors.white,
        ),
        bodyLarge: GoogleFonts.outfit(
          fontSize: 16,
          fontWeight: FontWeight.w500,
          color: const Color(0xFFCBD5E1),
        ),
        bodyMedium: GoogleFonts.outfit(
          fontSize: 14,
          fontWeight: FontWeight.w400,
          color: const Color(0xFF94A3B8),
        ),
      ),
      cardTheme: CardThemeData(
        color: cardDark,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: const BorderSide(color: borderSubtle, width: 1),
        ),
      ),
    );
  }

  static ThemeData get lightTheme {
    final textTheme = GoogleFonts.outfitTextTheme(ThemeData.light().textTheme);

    return ThemeData(
      brightness: Brightness.light,
      scaffoldBackgroundColor: bgLight,
      primaryColor: const Color(0xFF0284C7),
      colorScheme: const ColorScheme.light(
        primary: Color(0xFF0284C7),
        secondary: Color(0xFF059669),
        surface: cardLight,
        error: dangerRose,
      ),
      textTheme: textTheme.copyWith(
        displayLarge: GoogleFonts.outfit(
          fontSize: 64,
          fontWeight: FontWeight.w800,
          color: textDark,
          letterSpacing: -1.5,
        ),
        displayMedium: GoogleFonts.outfit(
          fontSize: 48,
          fontWeight: FontWeight.w800,
          color: textDark,
          letterSpacing: -1.0,
        ),
        headlineMedium: GoogleFonts.outfit(
          fontSize: 28,
          fontWeight: FontWeight.w700,
          color: textDark,
        ),
        titleLarge: GoogleFonts.outfit(
          fontSize: 20,
          fontWeight: FontWeight.w600,
          color: textDark,
        ),
        bodyLarge: GoogleFonts.outfit(
          fontSize: 16,
          fontWeight: FontWeight.w500,
          color: const Color(0xFF334155),
        ),
        bodyMedium: GoogleFonts.outfit(
          fontSize: 14,
          fontWeight: FontWeight.w400,
          color: textMutedLight,
        ),
      ),
      cardTheme: CardThemeData(
        color: cardLight,
        elevation: 2,
        shadowColor: Colors.black.withValues(alpha: 0.05),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: const BorderSide(color: borderLight, width: 1),
        ),
      ),
    );
  }
}
