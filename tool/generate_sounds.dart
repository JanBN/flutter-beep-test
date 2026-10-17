import 'dart:io';
import 'dart:math';
import 'dart:typed_data';

Uint8List createWav({
  required int sampleRate,
  required List<double> frequencies,
  required List<int> durationsMs,
  required List<double> volumes,
}) {
  // Calculate total samples
  int totalSamples = 0;
  for (int d in durationsMs) {
    totalSamples += (sampleRate * d / 1000).round();
  }

  final sampleData = Int16List(totalSamples);
  int sampleIdx = 0;

  for (int seg = 0; seg < frequencies.length; seg++) {
    final freq = frequencies[seg];
    final segDurMs = durationsMs[seg];
    final volume = volumes[seg];
    final segSamples = (sampleRate * segDurMs / 1000).round();

    // Envelope attack/decay (10ms fade in/out to eliminate clicking)
    final attackSamples = (sampleRate * 0.01).round();
    final decaySamples = (sampleRate * 0.015).round();

    for (int i = 0; i < segSamples; i++) {
      double env = 1.0;
      if (i < attackSamples) {
        env = i / attackSamples;
      } else if (i > segSamples - decaySamples) {
        env = (segSamples - i) / decaySamples;
      }

      if (freq <= 0) {
        sampleData[sampleIdx++] = 0;
      } else {
        final t = i / sampleRate;
        final val = sin(2 * pi * freq * t) * volume * env * 32767;
        sampleData[sampleIdx++] = val.clamp(-32768, 32767).toInt();
      }
    }
  }

  final byteData = ByteData(44 + sampleData.lengthInBytes);
  // RIFF header
  byteData.setUint8(0, 0x52); // R
  byteData.setUint8(1, 0x49); // I
  byteData.setUint8(2, 0x46); // F
  byteData.setUint8(3, 0x46); // F
  byteData.setUint32(4, 36 + sampleData.lengthInBytes, Endian.little);
  byteData.setUint8(8, 0x57);  // W
  byteData.setUint8(9, 0x41);  // A
  byteData.setUint8(10, 0x56); // V
  byteData.setUint8(11, 0x45); // E

  // fmt subchunk
  byteData.setUint8(12, 0x66); // f
  byteData.setUint8(13, 0x6D); // m
  byteData.setUint8(14, 0x74); // t
  byteData.setUint8(15, 0x20); // ' '
  byteData.setUint32(16, 16, Endian.little); // Subchunk1Size (16 for PCM)
  byteData.setUint16(20, 1, Endian.little);  // AudioFormat (1 = PCM)
  byteData.setUint16(22, 1, Endian.little);  // NumChannels (1 = Mono)
  byteData.setUint32(24, sampleRate, Endian.little); // SampleRate
  byteData.setUint32(28, sampleRate * 2, Endian.little); // ByteRate (SampleRate * NumChannels * BitsPerSample/8)
  byteData.setUint16(32, 2, Endian.little);  // BlockAlign (NumChannels * BitsPerSample/8)
  byteData.setUint16(34, 16, Endian.little); // BitsPerSample

  // data subchunk
  byteData.setUint8(36, 0x64); // d
  byteData.setUint8(37, 0x61); // a
  byteData.setUint8(38, 0x74); // t
  byteData.setUint8(39, 0x61); // a
  byteData.setUint32(40, sampleData.lengthInBytes, Endian.little);

  // Copy sample bytes
  final sampleBytes = Uint8List.view(sampleData.buffer);
  for (int i = 0; i < sampleBytes.length; i++) {
    byteData.setUint8(44 + i, sampleBytes[i]);
  }

  return byteData.buffer.asUint8List();
}

void main() {
  final outDir = Directory('assets/audio');
  if (!outDir.existsSync()) {
    outDir.createSync(recursive: true);
  }

  // 1. Shuttle Beep (1000 Hz, crisp 180ms)
  final beepWav = createWav(
    sampleRate: 44100,
    frequencies: [1000.0],
    durationsMs: [180],
    volumes: [0.9],
  );
  File('assets/audio/beep.wav').writeAsBytesSync(beepWav);
  print('Created assets/audio/beep.wav (${beepWav.length} bytes)');

  // 2. Level Up Beep (High dual chime: 1320 Hz for 120ms, 40ms pause, 1760 Hz for 240ms)
  final levelUpWav = createWav(
    sampleRate: 44100,
    frequencies: [1320.0, 0.0, 1760.0],
    durationsMs: [120, 40, 240],
    volumes: [0.9, 0.0, 0.95],
  );
  File('assets/audio/level_up.wav').writeAsBytesSync(levelUpWav);
  print('Created assets/audio/level_up.wav (${levelUpWav.length} bytes)');

  // 3. Countdown tick (660 Hz, short 80ms)
  final tickWav = createWav(
    sampleRate: 44100,
    frequencies: [660.0],
    durationsMs: [80],
    volumes: [0.8],
  );
  File('assets/audio/tick.wav').writeAsBytesSync(tickWav);
  print('Created assets/audio/tick.wav (${tickWav.length} bytes)');

  // 4. Start beep (Longer high tone 1200 Hz, 400ms)
  final startWav = createWav(
    sampleRate: 44100,
    frequencies: [1200.0],
    durationsMs: [400],
    volumes: [0.95],
  );
  File('assets/audio/start.wav').writeAsBytesSync(startWav);
  print('Created assets/audio/start.wav (${startWav.length} bytes)');

  // 5. Completion fanfare/whistle
  final doneWav = createWav(
    sampleRate: 44100,
    frequencies: [880.0, 0.0, 1100.0, 0.0, 1400.0],
    durationsMs: [150, 40, 150, 40, 450],
    volumes: [0.85, 0.0, 0.9, 0.0, 0.95],
  );
  File('assets/audio/finish.wav').writeAsBytesSync(doneWav);
  print('Created assets/audio/finish.wav (${doneWav.length} bytes)');
}
