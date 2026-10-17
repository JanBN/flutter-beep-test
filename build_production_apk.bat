@echo off
echo ========================================
echo Stavanie Production (Release) APK...
echo ========================================
flutter build apk --release
echo.
echo Cesta k APK: build\app\outputs\flutter-apk\app-release.apk
echo.
pause
