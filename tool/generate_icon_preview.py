import os
import json
import re

# Generator for 40 Beep Test SVG App Icons and Interactive HTML Preview

icons = []

def add_icon(id_num, title_sk, title_en, category, tags, svg_inner):
    svg_id = f"icon_{id_num:02d}"
    # Standard 512x512 app icon with rounded squircle clipping or rect
    svg_code = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%" class="app-icon-svg" data-id="{id_num}">
  <defs>
    <clipPath id="clip_{svg_id}">
      <rect width="512" height="512" rx="115" ry="115"/>
    </clipPath>
  </defs>
  <g clip-path="url(#clip_{svg_id})">
{svg_inner}
  </g>
</svg>'''
    icons.append({
        "id": id_num,
        "svg_id": svg_id,
        "title_sk": title_sk,
        "title_en": title_en,
        "category": category,
        "tags": tags,
        "svg": svg_code.strip()
    })

# ==========================================
# CATEGORY 1: Bežci & Pohyb (Runners & Motion)
# ==========================================

# 01: Neon Sprinter & Sonic Rings
add_icon(
    1, "Neónový šprintér & Zvukové vlny", "Neon Sprinter & Sonic Boom", "runners",
    ["šprintér", "zvukové vlny", "neón", "dynamika"],
    '''    <defs>
      <linearGradient id="g1_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#080F1E"/>
        <stop offset="100%" stop-color="#03060B"/>
      </linearGradient>
      <linearGradient id="g1_runner" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="50%" stop-color="#00C9FF"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <linearGradient id="g1_ring" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.9"/>
        <stop offset="100%" stop-color="#10E76F" stop-opacity="0.2"/>
      </linearGradient>
      <filter id="f1_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g1_bg)"/>
    <!-- Speed floor grid -->
    <path d="M 40 430 L 472 430 M 70 450 L 442 450 M 110 470 L 402 470" stroke="#10E76F" stroke-opacity="0.2" stroke-width="2" stroke-dasharray="8 8"/>
    <!-- Sonic concentric rings radiating forward -->
    <path d="M 320 160 A 120 120 0 0 1 320 360" fill="none" stroke="url(#g1_ring)" stroke-width="12" stroke-linecap="round" filter="url(#f1_glow)"/>
    <path d="M 360 120 A 170 170 0 0 1 360 400" fill="none" stroke="url(#g1_ring)" stroke-width="8" stroke-linecap="round" opacity="0.6"/>
    <path d="M 400 80 A 220 220 0 0 1 400 440" fill="none" stroke="url(#g1_ring)" stroke-width="5" stroke-linecap="round" opacity="0.3"/>
    <!-- Trailing speed streaks -->
    <path d="M 60 210 L 160 210 M 40 260 L 180 260 M 70 310 L 150 310" stroke="#00F2FE" stroke-opacity="0.35" stroke-width="4" stroke-linecap="round"/>
    <!-- Dynamic Runner Silhouette (Sprinting forward) -->
    <g fill="url(#g1_runner)" filter="url(#f1_glow)">
      <!-- Head -->
      <circle cx="270" cy="145" r="28"/>
      <!-- Torso & Arms -->
      <path d="M 245 180 L 290 240 L 235 285 L 210 230 Z"/>
      <!-- Forward arm -->
      <path d="M 280 205 L 340 235 L 355 220" fill="none" stroke="url(#g1_runner)" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Rear arm -->
      <path d="M 240 210 L 180 235 L 165 260" fill="none" stroke="url(#g1_runner)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Lead leg (forward knee bent high) -->
      <path d="M 245 280 L 305 320 L 325 390" fill="none" stroke="url(#g1_runner)" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Trail leg (extended back push-off) -->
      <path d="M 225 280 L 170 325 L 125 355" fill="none" stroke="url(#g1_runner)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''
)

# 02: Pacer Shuttle & Turnaround Cones
add_icon(
    2, "Člnkový beh & Obratové kužele", "Pacer Shuttle & Turnaround Cones", "cones",
    ["člnkový beh", "kužele", "obrat", "20m", "dráha"],
    '''    <defs>
      <linearGradient id="g2_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0B132B"/>
        <stop offset="100%" stop-color="#040814"/>
      </linearGradient>
      <linearGradient id="g2_cone_l" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#FF5A36"/>
      </linearGradient>
      <linearGradient id="g2_cone_r" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#00F2FE"/>
      </linearGradient>
      <linearGradient id="g2_arrow" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FF9F1C"/>
        <stop offset="50%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f2_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g2_bg)"/>
    <!-- Center Beep Ping Ripple -->
    <circle cx="256" cy="240" r="160" fill="none" stroke="#00F2FE" stroke-opacity="0.1" stroke-width="2"/>
    <circle cx="256" cy="240" r="100" fill="none" stroke="#00F2FE" stroke-opacity="0.2" stroke-width="2" stroke-dasharray="6 6"/>
    <circle cx="256" cy="240" r="40" fill="none" stroke="#00F2FE" stroke-opacity="0.35" stroke-width="3"/>
    <!-- Left Cone (Orange/Amber) -->
    <g transform="translate(60, 220)">
      <ellipse cx="40" cy="140" rx="42" ry="14" fill="#FF9F1C" fill-opacity="0.2"/>
      <path d="M 40 20 L 15 135 A 40 12 0 0 0 65 135 Z" fill="url(#g2_cone_l)" filter="url(#f2_glow)"/>
      <path d="M 28 80 L 52 80 L 56 100 L 24 100 Z" fill="#FFFFFF" fill-opacity="0.9"/>
      <circle cx="40" cy="20" r="7" fill="#FFF"/>
    </g>
    <!-- Right Cone (Volt/Cyan) -->
    <g transform="translate(352, 220)">
      <ellipse cx="40" cy="140" rx="42" ry="14" fill="#10E76F" fill-opacity="0.2"/>
      <path d="M 40 20 L 15 135 A 40 12 0 0 0 65 135 Z" fill="url(#g2_cone_r)" filter="url(#f2_glow)"/>
      <path d="M 28 80 L 52 80 L 56 100 L 24 100 Z" fill="#FFFFFF" fill-opacity="0.9"/>
      <circle cx="40" cy="20" r="7" fill="#FFF"/>
    </g>
    <!-- Dynamic Infinity / Shuttle Arrow Arc -->
    <path d="M 120 280 C 180 140, 332 140, 392 280" fill="none" stroke="url(#g2_arrow)" stroke-width="12" stroke-linecap="round" filter="url(#f2_glow)"/>
    <path d="M 392 310 C 332 430, 180 430, 120 310" fill="none" stroke="url(#g2_arrow)" stroke-width="12" stroke-linecap="round" stroke-dasharray="16 10"/>
    <!-- Arrow heads -->
    <polygon points="385,270 415,285 390,305" fill="#10E76F"/>
    <polygon points="127,320 97,305 122,285" fill="#FF9F1C"/>
    <!-- 20m Badge -->
    <rect x="206" y="90" width="100" height="34" rx="17" fill="#0E1E38" stroke="#00F2FE" stroke-width="2"/>
    <text x="256" y="113" fill="#00F2FE" font-family="Arial, sans-serif" font-weight="900" font-size="16" text-anchor="middle" letter-spacing="2">20 METERS</text>
'''
)

# 03: Sonic Dash Equalizer Runner
add_icon(
    3, "Frekvenčný šprintér (Equalizer)", "Sonic Equalizer Sprinter", "runners",
    ["audio", "ekvalizér", "frekvencia", "silueta", "šprint"],
    '''    <defs>
      <linearGradient id="g3_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0E0720"/>
        <stop offset="100%" stop-color="#040209"/>
      </linearGradient>
      <linearGradient id="g3_bar" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#7928CA"/>
        <stop offset="50%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f3_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g3_bg)"/>
    <!-- Background pulse grid -->
    <circle cx="256" cy="256" r="190" fill="none" stroke="#7928CA" stroke-opacity="0.15" stroke-width="2"/>
    <!-- Equalizer bars shaped into high-speed runner slope -->
    <g fill="url(#g3_bar)" filter="url(#f3_glow)" transform="skewX(-14) translate(60, 0)">
      <rect x="70" y="330" width="18" height="90" rx="9"/>
      <rect x="100" y="290" width="18" height="130" rx="9"/>
      <rect x="130" y="240" width="18" height="180" rx="9"/>
      <rect x="160" y="200" width="18" height="220" rx="9"/>
      <rect x="190" y="160" width="18" height="260" rx="9"/>
      <rect x="220" y="130" width="18" height="290" rx="9"/>
      <rect x="250" y="110" width="18" height="310" rx="9"/>
      <rect x="280" y="150" width="18" height="270" rx="9"/>
      <rect x="310" y="190" width="18" height="230" rx="9"/>
      <rect x="340" y="250" width="18" height="170" rx="9"/>
      <rect x="370" y="320" width="18" height="100" rx="9"/>
      <!-- Head dot -->
      <circle cx="259" cy="70" r="22" fill="#10E76F"/>
    </g>
    <!-- Sine pulse baseline -->
    <path d="M 60 420 Q 150 400, 256 420 T 452 420" fill="none" stroke="#00F2FE" stroke-width="4" stroke-linecap="round" opacity="0.7"/>
'''
)

# 04: Orbital Velocity Ring
add_icon(
    4, "Orbitálny rýchlostný prstenec", "Orbital Velocity Ring", "runners",
    ["športovec", "prstenec", "kruh", "rýchlosť", "neon"],
    '''    <defs>
      <linearGradient id="g4_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#07131E"/>
        <stop offset="100%" stop-color="#02070D"/>
      </linearGradient>
      <linearGradient id="g4_ring" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="60%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#FF9F1C"/>
      </linearGradient>
      <filter id="f4_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g4_bg)"/>
    <!-- Outer dash ticks -->
    <circle cx="256" cy="256" r="215" fill="none" stroke="#00F2FE" stroke-opacity="0.25" stroke-width="4" stroke-dasharray="6 14"/>
    <!-- Thick energetic orbital ring with break -->
    <path d="M 256 56 A 200 200 0 1 1 80 340" fill="none" stroke="url(#g4_ring)" stroke-width="20" stroke-linecap="round" filter="url(#f4_glow)"/>
    <!-- Break comet trail -->
    <circle cx="256" cy="56" r="14" fill="#00F2FE" filter="url(#f4_glow)"/>
    <circle cx="256" cy="56" r="6" fill="#FFF"/>
    <!-- Center Runner Figure bursting through -->
    <g fill="#FFFFFF" filter="url(#f4_glow)">
      <circle cx="280" cy="170" r="24" fill="#00F2FE"/>
      <!-- Body -->
      <path d="M 260 205 L 300 260 L 255 295 L 230 240 Z" fill="#00F2FE"/>
      <!-- Arms -->
      <path d="M 285 225 L 345 235" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round"/>
      <path d="M 250 230 L 195 245" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round"/>
      <!-- Legs -->
      <path d="M 260 290 L 315 345 L 340 410" fill="none" stroke="#10E76F" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 240 290 L 190 325 L 140 340" fill="none" stroke="#10E76F" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <!-- Speed blurs -->
    <line x1="100" y1="256" x2="160" y2="256" stroke="#00F2FE" stroke-width="4" stroke-linecap="round" opacity="0.4"/>
    <line x1="80" y1="280" x2="150" y2="280" stroke="#00F2FE" stroke-width="4" stroke-linecap="round" opacity="0.3"/>
'''
)

# 05: Beep Frequency Track
add_icon(
    5, "Zvuková sínusoida & Dráha", "Beep Frequency Track", "runners",
    ["dráha", "sínusoida", "zvuk", "štadión", "tempo", "bežec"],
    '''    <defs>
      <linearGradient id="g5_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#091428"/>
        <stop offset="100%" stop-color="#02060E"/>
      </linearGradient>
      <linearGradient id="g5_lane" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#10E76F"/>
        <stop offset="60%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#7928CA"/>
      </linearGradient>
      <filter id="f5_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g5_bg)"/>
    <!-- Perspective Running Track Lanes -->
    <path d="M 90 460 L 210 180" stroke="#00F2FE" stroke-width="6" stroke-opacity="0.4"/>
    <path d="M 200 460 L 240 180" stroke="#00F2FE" stroke-width="4" stroke-dasharray="14 14" stroke-opacity="0.6"/>
    <path d="M 312 460 L 272 180" stroke="#00F2FE" stroke-width="4" stroke-dasharray="14 14" stroke-opacity="0.6"/>
    <path d="M 422 460 L 302 180" stroke="#00F2FE" stroke-width="6" stroke-opacity="0.4"/>
    <!-- Horizontal distance meter rungs -->
    <path d="M 170 380 L 342 380 M 190 320 L 322 320 M 205 260 L 307 260 M 215 210 L 297 210" stroke="#10E76F" stroke-opacity="0.3" stroke-width="3"/>
    <!-- Audio Waveform Portal at Horizon -->
    <path d="M 60 160 Q 120 80, 180 160 T 300 160 T 420 160 T 480 160" fill="none" stroke="url(#g5_lane)" stroke-width="12" stroke-linecap="round" filter="url(#f5_glow)"/>
    <!-- Center Beep Signal Beacon -->
    <circle cx="256" cy="160" r="16" fill="#10E76F" filter="url(#f5_glow)"/>
    <circle cx="256" cy="160" r="6" fill="#FFF"/>
    <!-- Radiating sonic beacons from top -->
    <circle cx="256" cy="160" r="45" fill="none" stroke="#10E76F" stroke-opacity="0.4" stroke-width="2"/>
    <circle cx="256" cy="160" r="85" fill="none" stroke="#00F2FE" stroke-opacity="0.2" stroke-width="2"/>
'''
)

# 06: Infinity Shuttle Loop
add_icon(
    6, "Nekonečný Shuttle Loop (∞)", "Infinity Shuttle Loop", "cones",
    ["nekonečno", "člnkový beh", "loop", "vytrvalosť", "gradient"],
    '''    <defs>
      <linearGradient id="g6_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0A0B1A"/>
        <stop offset="100%" stop-color="#020308"/>
      </linearGradient>
      <linearGradient id="g6_inf" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FF3366"/>
        <stop offset="50%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f6_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g6_bg)"/>
    <!-- Ambient glow behind infinity curve -->
    <circle cx="150" cy="256" r="90" fill="#FF3366" fill-opacity="0.08" filter="url(#f6_glow)"/>
    <circle cx="362" cy="256" r="90" fill="#10E76F" fill-opacity="0.08" filter="url(#f6_glow)"/>
    <!-- Infinity Track (3D perspective / twisted ribbon) -->
    <path d="M 256 256 C 200 150, 80 150, 80 256 C 80 362, 200 362, 256 256 C 312 150, 432 150, 432 256 C 432 362, 312 362, 256 256 Z" 
          fill="none" stroke="url(#g6_inf)" stroke-width="24" stroke-linecap="round" stroke-linejoin="round" filter="url(#f6_glow)"/>
    <!-- Inner dashed race line -->
    <path d="M 256 256 C 200 150, 80 150, 80 256 C 80 362, 200 362, 256 256 C 312 150, 432 150, 432 256 C 432 362, 312 362, 256 256 Z" 
          fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="10 12" opacity="0.6"/>
    <!-- Apex Cones at both turnaround nodes -->
    <circle cx="120" cy="256" r="18" fill="#FF3366" filter="url(#f6_glow)"/>
    <circle cx="120" cy="256" r="6" fill="#FFF"/>
    <circle cx="392" cy="256" r="18" fill="#10E76F" filter="url(#f6_glow)"/>
    <circle cx="392" cy="256" r="6" fill="#FFF"/>
    <!-- "BEEP" label badge -->
    <rect x="216" y="70" width="80" height="28" rx="14" fill="#131A29" stroke="#FF9F1C" stroke-width="2"/>
    <text x="256" y="89" fill="#FF9F1C" font-family="Arial, sans-serif" font-weight="900" font-size="13" text-anchor="middle" letter-spacing="2">PACER</text>
'''
)

# ==========================================
# CATEGORY 2: Kužele & Trasa (Cones & Shuttle)
# ==========================================

# 07: Dual Cones & 20m Laser Line
add_icon(
    7, "Dva kužele & 20m Laser", "Dual Cones & 20m Laser", "cones",
    ["kužeľ", "laser", "20m", "meranie", "člnkový beh"],
    '''    <defs>
      <linearGradient id="g7_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#081426"/>
        <stop offset="100%" stop-color="#02060C"/>
      </linearGradient>
      <linearGradient id="g7_c1" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#FF3366"/>
      </linearGradient>
      <linearGradient id="g7_c2" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f7_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g7_bg)"/>
    <!-- Laser Beam between Cones -->
    <line x1="110" y1="320" x2="402" y2="320" stroke="#00F2FE" stroke-width="8" filter="url(#f7_glow)"/>
    <line x1="110" y1="320" x2="402" y2="320" stroke="#FFFFFF" stroke-width="2"/>
    <!-- Distance Text -->
    <rect x="206" y="296" width="100" height="48" rx="24" fill="#091322" stroke="#10E76F" stroke-width="3" filter="url(#f7_glow)"/>
    <text x="256" y="328" fill="#FFFFFF" font-family="Arial, sans-serif" font-weight="900" font-size="22" text-anchor="middle">20m</text>
    <!-- Left Cone -->
    <g transform="translate(45, 170)">
      <path d="M 65 30 L 15 170 A 50 14 0 0 0 115 170 Z" fill="url(#g7_c1)" filter="url(#f7_glow)"/>
      <path d="M 37 105 L 93 105 L 98 128 L 32 128 Z" fill="#FFFFFF" opacity="0.9"/>
      <!-- Radiating sonic pulses from cone tip -->
      <path d="M 65 10 A 30 30 0 0 1 85 30" fill="none" stroke="#FF9F1C" stroke-width="4" stroke-linecap="round"/>
      <path d="M 65 -10 A 50 50 0 0 1 105 30" fill="none" stroke="#FF9F1C" stroke-width="3" stroke-linecap="round" opacity="0.6"/>
    </g>
    <!-- Right Cone -->
    <g transform="translate(337, 170)">
      <path d="M 65 30 L 15 170 A 50 14 0 0 0 115 170 Z" fill="url(#g7_c2)" filter="url(#f7_glow)"/>
      <path d="M 37 105 L 93 105 L 98 128 L 32 128 Z" fill="#FFFFFF" opacity="0.9"/>
      <!-- Radiating sonic pulses from cone tip -->
      <path d="M 65 10 A 30 30 0 0 0 45 30" fill="none" stroke="#10E76F" stroke-width="4" stroke-linecap="round"/>
      <path d="M 65 -10 A 50 50 0 0 0 25 30" fill="none" stroke="#10E76F" stroke-width="3" stroke-linecap="round" opacity="0.6"/>
    </g>
    <!-- Top Sound Wave -->
    <path d="M 120 100 Q 256 60, 392 100" fill="none" stroke="#00F2FE" stroke-width="3" stroke-dasharray="8 8" opacity="0.4"/>
'''
)

# 08: 180° Turnaround Arrow
add_icon(
    8, "180° Obratová šípka (U-Turn)", "180° Turnaround Arrow", "cones",
    ["obrat", "otočka", "šípka", "tempo", "člnok"],
    '''    <defs>
      <linearGradient id="g8_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#140C24"/>
        <stop offset="100%" stop-color="#07030D"/>
      </linearGradient>
      <linearGradient id="g8_arrow" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="50%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#FF9F1C"/>
      </linearGradient>
      <filter id="f8_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="9" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g8_bg)"/>
    <!-- Center Pivot Cone -->
    <circle cx="210" cy="256" r="34" fill="#131A29" stroke="#FF9F1C" stroke-width="6" filter="url(#f8_glow)"/>
    <circle cx="210" cy="256" r="14" fill="#FF9F1C"/>
    <!-- Shockwaves radiating from the pivot -->
    <circle cx="210" cy="256" r="70" fill="none" stroke="#FF9F1C" stroke-opacity="0.3" stroke-width="3" stroke-dasharray="6 8"/>
    <circle cx="210" cy="256" r="110" fill="none" stroke="#FF9F1C" stroke-opacity="0.15" stroke-width="2"/>
    <!-- Giant U-Turn Hairpin Arrow -->
    <path d="M 390 150 L 230 150 C 130 150, 130 362, 230 362 L 350 362" 
          fill="none" stroke="url(#g8_arrow)" stroke-width="38" stroke-linecap="round" filter="url(#f8_glow)"/>
    <!-- Arrow Head pointing back -->
    <polygon points="330,320 420,362 330,404" fill="#FF9F1C" filter="url(#f8_glow)"/>
    <!-- Speed notch accents -->
    <path d="M 370 150 L 250 150" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity="0.8"/>
    <text x="310" y="270" fill="#00F2FE" font-family="Arial, sans-serif" font-weight="900" font-size="28" letter-spacing="3">TURN</text>
'''
)

# 09: Perspective Pacer Runway
add_icon(
    9, "Perspektívna dráha 20m", "Perspective Pacer Runway", "cones",
    ["dráha", "perspektíva", "20m", "bežec", "brána"],
    '''    <defs>
      <linearGradient id="g9_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#040D1A"/>
        <stop offset="100%" stop-color="#010307"/>
      </linearGradient>
      <linearGradient id="g9_portal" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f9_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g9_bg)"/>
    <!-- Runway Perspective converging to horizon -->
    <polygon points="40,470 472,470 300,160 212,160" fill="#0B1B36" fill-opacity="0.5"/>
    <line x1="40" y1="470" x2="212" y2="160" stroke="#10E76F" stroke-width="8" filter="url(#f9_glow)"/>
    <line x1="472" y1="470" x2="300" y2="160" stroke="#10E76F" stroke-width="8" filter="url(#f9_glow)"/>
    <!-- Center dashed speed strip -->
    <line x1="256" y1="470" x2="256" y2="160" stroke="#00F2FE" stroke-width="6" stroke-dasharray="24 16"/>
    <!-- Distance cross bars -->
    <line x1="86" y1="400" x2="426" y2="400" stroke="#00F2FE" stroke-width="4" stroke-opacity="0.4"/>
    <line x1="135" y1="320" x2="377" y2="320" stroke="#00F2FE" stroke-width="4" stroke-opacity="0.6"/>
    <line x1="180" y1="240" x2="332" y2="240" stroke="#00F2FE" stroke-width="3" stroke-opacity="0.8"/>
    <!-- 20m Neon Finish Arch / Portal -->
    <path d="M 195 160 L 195 90 A 61 61 0 0 1 317 90 L 317 160" fill="none" stroke="url(#g9_portal)" stroke-width="12" stroke-linecap="round" filter="url(#f9_glow)"/>
    <!-- Giant Pulsing Beep Orb at Horizon -->
    <circle cx="256" cy="90" r="18" fill="#FFFFFF" filter="url(#f9_glow)"/>
    <circle cx="256" cy="90" r="45" fill="none" stroke="#10E76F" stroke-width="3" stroke-opacity="0.6"/>
    <circle cx="256" cy="90" r="75" fill="none" stroke="#00F2FE" stroke-width="2" stroke-opacity="0.3"/>
    <text x="256" y="445" fill="#10E76F" font-family="Arial, sans-serif" font-weight="900" font-size="24" text-anchor="middle" letter-spacing="4">START / 20M</text>
'''
)

# 10: Shuttle Court Tactical Radar
add_icon(
    10, "Taktický radar člnkového behu", "Tactical Shuttle Radar", "audio",
    ["radar", "taktika", "sken", "zameriavač", "audio"],
    '''    <defs>
      <linearGradient id="g10_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#04121A"/>
        <stop offset="100%" stop-color="#010609"/>
      </linearGradient>
      <linearGradient id="g10_sweep" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#10E76F" stop-opacity="0.5"/>
        <stop offset="100%" stop-color="#10E76F" stop-opacity="0.0"/>
      </linearGradient>
      <filter id="f10_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g10_bg)"/>
    <!-- Tactical Range Rings -->
    <circle cx="256" cy="256" r="210" fill="none" stroke="#10E76F" stroke-width="3" stroke-opacity="0.4"/>
    <circle cx="256" cy="256" r="150" fill="none" stroke="#10E76F" stroke-width="2" stroke-opacity="0.3"/>
    <circle cx="256" cy="256" r="90" fill="none" stroke="#10E76F" stroke-width="2" stroke-opacity="0.3"/>
    <!-- Crosshairs -->
    <line x1="256" y1="36" x2="256" y2="476" stroke="#10E76F" stroke-width="2" stroke-opacity="0.3" stroke-dasharray="6 6"/>
    <line x1="36" y1="256" x2="476" y2="256" stroke="#10E76F" stroke-width="2" stroke-opacity="0.3" stroke-dasharray="6 6"/>
    <!-- Radar Sweep Wedge -->
    <path d="M 256 256 L 400 112 A 210 210 0 0 1 466 256 Z" fill="url(#g10_sweep)"/>
    <line x1="256" y1="256" x2="400" y2="112" stroke="#10E76F" stroke-width="4" filter="url(#f10_glow)"/>
    <!-- Shuttle Targets (Left cone & Right cone blips) -->
    <circle cx="120" cy="256" r="14" fill="#FF9F1C" filter="url(#f10_glow)"/>
    <circle cx="120" cy="256" r="28" fill="none" stroke="#FF9F1C" stroke-width="3" stroke-opacity="0.6"/>
    <circle cx="392" cy="256" r="14" fill="#00F2FE" filter="url(#f10_glow)"/>
    <circle cx="392" cy="256" r="28" fill="none" stroke="#00F2FE" stroke-width="3" stroke-opacity="0.6"/>
    <!-- Active Runner Blip in motion -->
    <circle cx="310" cy="220" r="10" fill="#FFFFFF" filter="url(#f10_glow)"/>
    <!-- Pulse trails -->
    <line x1="120" y1="256" x2="392" y2="256" stroke="#00F2FE" stroke-width="4" stroke-linecap="round" stroke-dasharray="8 8"/>
'''
)

# 11: Isometric Beep Grid
add_icon(
    11, "Izometrická člnková plocha", "Isometric Beep Grid", "cones",
    ["izometria", "plocha", "3D", "vektor", "šport"],
    '''    <defs>
      <linearGradient id="g11_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0E1026"/>
        <stop offset="100%" stop-color="#03040A"/>
      </linearGradient>
      <linearGradient id="g11_line" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="50%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#FF3366"/>
      </linearGradient>
      <filter id="f11_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g11_bg)"/>
    <!-- Isometric Floor Grid -->
    <g stroke="#1F2A4A" stroke-width="2" opacity="0.6">
      <line x1="256" y1="120" x2="60" y2="230"/>
      <line x1="256" y1="160" x2="60" y2="270"/>
      <line x1="256" y1="200" x2="60" y2="310"/>
      <line x1="256" y1="120" x2="452" y2="230"/>
      <line x1="256" y1="160" x2="452" y2="270"/>
      <line x1="256" y1="200" x2="452" y2="310"/>
    </g>
    <!-- Isometric Shuttle Track Zig-Zag Path -->
    <polyline points="100,280 256,190 412,280 256,370 100,280" fill="none" stroke="url(#g11_line)" stroke-width="12" stroke-linejoin="round" filter="url(#f11_glow)"/>
    <!-- Sound ripple ellipses at turnaround vertices -->
    <ellipse cx="100" cy="280" rx="35" ry="18" fill="none" stroke="#00F2FE" stroke-width="4"/>
    <circle cx="100" cy="280" r="10" fill="#00F2FE"/>
    <ellipse cx="412" cy="280" rx="35" ry="18" fill="none" stroke="#FF3366" stroke-width="4"/>
    <circle cx="412" cy="280" r="10" fill="#FF3366"/>
    <!-- Top Beacon Cone -->
    <ellipse cx="256" cy="190" rx="20" ry="10" fill="#10E76F"/>
    <polygon points="256,130 240,190 272,190" fill="#10E76F" filter="url(#f11_glow)"/>
'''
)

# 12: Apex Cone Shockwave
add_icon(
    12, "Šoková vlna z kužeľa", "Apex Cone Shockwave", "cones",
    ["kužeľ", "šoková vlna", "pípnutie", "výboj", "energia"],
    '''    <defs>
      <linearGradient id="g12_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#140E0A"/>
        <stop offset="100%" stop-color="#050302"/>
      </linearGradient>
      <linearGradient id="g12_cone" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FF5E00"/>
        <stop offset="50%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#FFAE33"/>
      </linearGradient>
      <filter id="f12_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g12_bg)"/>
    <!-- Huge Shockwave Rings bursting from Cone Tip -->
    <circle cx="256" cy="190" r="80" fill="none" stroke="#FF9F1C" stroke-width="6" stroke-dasharray="14 10" filter="url(#f12_glow)"/>
    <circle cx="256" cy="190" r="140" fill="none" stroke="#00F2FE" stroke-width="8" stroke-opacity="0.8" filter="url(#f12_glow)"/>
    <circle cx="256" cy="190" r="200" fill="none" stroke="#10E76F" stroke-width="4" stroke-opacity="0.4"/>
    <!-- Foreground Training Cone -->
    <ellipse cx="256" cy="420" rx="140" ry="32" fill="#000000" fill-opacity="0.5"/>
    <path d="M 256 190 L 140 420 A 140 30 0 0 0 372 420 Z" fill="url(#g12_cone)" filter="url(#f12_glow)"/>
    <!-- White Reflective Stripes on Cone -->
    <path d="M 198 305 L 314 305 L 328 340 L 184 340 Z" fill="#FFFFFF"/>
    <path d="M 224 240 L 288 240 L 296 265 L 216 265 Z" fill="#FFFFFF"/>
    <!-- Blinding Beacon Tip -->
    <circle cx="256" cy="190" r="16" fill="#FFFFFF" filter="url(#f12_glow)"/>
'''
)

# ==========================================
# CATEGORY 3: Zvuk & Radar (Audio & Waves)
# ==========================================

# 13: Sonic Pulse Core
add_icon(
    13, "Akustické jadro & Pulz", "Sonic Pulse Core", "audio",
    ["zvuk", "pulz", "vlny", "akustika", "čistý"],
    '''    <defs>
      <linearGradient id="g13_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#040B18"/>
        <stop offset="100%" stop-color="#010308"/>
      </linearGradient>
      <linearGradient id="g13_pulse" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f13_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="9" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g13_bg)"/>
    <!-- Concentric High-Energy Sonic Waves -->
    <g stroke="url(#g13_pulse)" fill="none" filter="url(#f13_glow)">
      <!-- Wave 1 -->
      <path d="M 256 186 A 70 70 0 1 1 255 186" stroke-width="14"/>
      <!-- Wave 2 with sports speed gaps -->
      <path d="M 256 126 A 130 130 0 1 1 255 126" stroke-width="16" stroke-dasharray="140 50 140 50"/>
      <!-- Wave 3 -->
      <path d="M 256 66 A 190 190 0 1 1 255 66" stroke-width="18" stroke-dasharray="210 60 210 60"/>
    </g>
    <!-- Center Audio Emitter Core -->
    <circle cx="256" cy="256" r="32" fill="url(#g13_pulse)" filter="url(#f13_glow)"/>
    <circle cx="256" cy="256" r="14" fill="#FFFFFF"/>
'''
)

# 14: Athletic Megaphone & Beep Burst
add_icon(
    14, "Trénerský megafón & BEEP!", "Coach Megaphone & Beep Burst", "audio",
    ["megafón", "tréner", "zvuk", "výkrik", "štart"],
    '''    <defs>
      <linearGradient id="g14_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#1A0D10"/>
        <stop offset="100%" stop-color="#070203"/>
      </linearGradient>
      <linearGradient id="g14_mega" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FF3366"/>
        <stop offset="100%" stop-color="#FF9F1C"/>
      </linearGradient>
      <filter id="f14_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g14_bg)"/>
    <!-- Megaphone Body -->
    <g transform="rotate(-20 200 280)">
      <!-- Handle -->
      <path d="M 170 290 L 150 380 L 185 380 L 195 290 Z" fill="#FF3366"/>
      <!-- Horn Cone -->
      <path d="M 130 230 L 270 170 L 270 350 L 130 290 Z" fill="url(#g14_mega)" filter="url(#f14_glow)"/>
      <!-- Back cylinder -->
      <rect x="90" y="235" width="45" height="50" rx="8" fill="#FFFFFF"/>
      <!-- Front Rim -->
      <ellipse cx="270" cy="260" rx="18" ry="90" fill="#FF9F1C" stroke="#FFFFFF" stroke-width="4"/>
    </g>
    <!-- Giant Blasting Audio Waves -->
    <path d="M 340 180 A 100 100 0 0 1 380 320" fill="none" stroke="#FF9F1C" stroke-width="14" stroke-linecap="round" filter="url(#f14_glow)"/>
    <path d="M 390 130 A 160 160 0 0 1 450 370" fill="none" stroke="#10E76F" stroke-width="12" stroke-linecap="round" filter="url(#f14_glow)"/>
    <path d="M 440 90 A 220 220 0 0 1 490 410" fill="none" stroke="#00F2FE" stroke-width="8" stroke-linecap="round" opacity="0.6"/>
    <!-- Sound lightning flash -->
    <polygon points="340,240 370,225 360,248 390,235 340,270" fill="#FFFFFF"/>
'''
)

# 15: Cardio EKG Beep Wave
add_icon(
    15, "Kardio EKG & Zvukový impulz", "Cardio EKG & Beep Spike", "cardio",
    ["kardio", "ekg", "pulz", "srdce", "vytrvalosť"],
    '''    <defs>
      <linearGradient id="g15_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#1A0713"/>
        <stop offset="100%" stop-color="#070105"/>
      </linearGradient>
      <linearGradient id="g15_line" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="45%" stop-color="#10E76F"/>
        <stop offset="70%" stop-color="#FF3366"/>
        <stop offset="100%" stop-color="#FF9F1C"/>
      </linearGradient>
      <filter id="f15_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g15_bg)"/>
    <!-- Heart background watermark -->
    <path d="M 256 120 C 230 60, 140 60, 110 130 C 80 200, 180 300, 256 380 C 332 300, 432 200, 402 130 C 372 60, 282 60, 256 120 Z" 
          fill="none" stroke="#FF3366" stroke-opacity="0.12" stroke-width="8"/>
    <!-- Audio Wave morphing into intense EKG Heart Spike -->
    <path d="M 40 270 Q 70 240, 100 270 T 160 270 L 190 270 L 210 320 L 250 80 L 290 420 L 320 230 L 340 290 L 370 270 Q 400 250, 430 270 T 472 270" 
          fill="none" stroke="url(#g15_line)" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" filter="url(#f15_glow)"/>
    <!-- Peak Beep Dot -->
    <circle cx="250" cy="80" r="14" fill="#FFFFFF" filter="url(#f15_glow)"/>
    <!-- Radiating pulse ring from peak -->
    <circle cx="250" cy="80" r="38" fill="none" stroke="#FF3366" stroke-width="4" stroke-opacity="0.7"/>
    <text x="256" y="465" fill="#FF3366" font-family="Arial, sans-serif" font-weight="900" font-size="20" text-anchor="middle" letter-spacing="4">MAX VO2 PULSE</text>
'''
)

# 16: Sonar Beep Target
add_icon(
    16, "Sonarový radar & Zameranie", "Sonar Beep Target", "audio",
    ["sonar", "radar", "zameriavač", "terč", "signál"],
    '''    <defs>
      <linearGradient id="g16_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#021A1A"/>
        <stop offset="100%" stop-color="#010606"/>
      </linearGradient>
      <filter id="f16_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g16_bg)"/>
    <!-- Concentric Target Circles -->
    <circle cx="256" cy="256" r="200" fill="none" stroke="#00F2FE" stroke-width="4" stroke-opacity="0.3"/>
    <circle cx="256" cy="256" r="140" fill="none" stroke="#10E76F" stroke-width="4" stroke-opacity="0.5"/>
    <circle cx="256" cy="256" r="80" fill="none" stroke="#00F2FE" stroke-width="6" stroke-dasharray="16 12" filter="url(#f16_glow)"/>
    <!-- 4 Radar cross ticks -->
    <line x1="256" y1="40" x2="256" y2="90" stroke="#10E76F" stroke-width="6" stroke-linecap="round"/>
    <line x1="256" y1="422" x2="256" y2="472" stroke="#10E76F" stroke-width="6" stroke-linecap="round"/>
    <line x1="40" y1="256" x2="90" y2="256" stroke="#10E76F" stroke-width="6" stroke-linecap="round"/>
    <line x1="422" y1="256" x2="472" y2="256" stroke="#10E76F" stroke-width="6" stroke-linecap="round"/>
    <!-- Center Target Crosshair & Blip -->
    <circle cx="256" cy="256" r="22" fill="#10E76F" filter="url(#f16_glow)"/>
    <circle cx="256" cy="256" r="8" fill="#FFF"/>
    <!-- Sweep Ray -->
    <line x1="256" y1="256" x2="420" y2="140" stroke="#00F2FE" stroke-width="6" stroke-linecap="round" filter="url(#f16_glow)"/>
'''
)

# 17: Triple Beep Countdown (3... 2... 1... GO!)
add_icon(
    17, "Trojité odpočítavanie (3.. 2.. 1..)", "Triple Beep Countdown", "audio",
    ["odpočítavanie", "pípnutie", "štart", "zvuk", "semafór"],
    '''    <defs>
      <linearGradient id="g17_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0A1118"/>
        <stop offset="100%" stop-color="#020406"/>
      </linearGradient>
      <filter id="f17_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g17_bg)"/>
    <!-- 3 Progressive Beep Discs -->
    <!-- Beep 1 (Amber) -->
    <g transform="translate(100, 256)">
      <circle cx="0" cy="0" r="32" fill="#FF9F1C" fill-opacity="0.25"/>
      <circle cx="0" cy="0" r="18" fill="#FF9F1C"/>
    </g>
    <!-- Beep 2 (Cyan) -->
    <g transform="translate(210, 256)">
      <circle cx="0" cy="0" r="48" fill="#00F2FE" fill-opacity="0.25"/>
      <circle cx="0" cy="0" r="26" fill="#00F2FE" filter="url(#f17_glow)"/>
    </g>
    <!-- Beep 3 / GO! (Huge Neon Volt with Shockwaves) -->
    <g transform="translate(360, 256)">
      <circle cx="0" cy="0" r="100" fill="none" stroke="#10E76F" stroke-width="3" stroke-opacity="0.2"/>
      <circle cx="0" cy="0" r="75" fill="none" stroke="#10E76F" stroke-width="5" stroke-opacity="0.5" filter="url(#f17_glow)"/>
      <circle cx="0" cy="0" r="48" fill="#10E76F" filter="url(#f17_glow)"/>
      <circle cx="0" cy="0" r="20" fill="#FFFFFF"/>
    </g>
    <!-- Sound wave connectors -->
    <path d="M 125 256 L 175 256 M 245 256 L 305 256" stroke="#FFFFFF" stroke-width="4" stroke-dasharray="6 6" opacity="0.6"/>
    <text x="360" y="395" fill="#10E76F" font-family="Arial, sans-serif" font-weight="900" font-size="28" text-anchor="middle" letter-spacing="4">GO!</text>
'''
)

# 18: Soundwave Negative Runner
add_icon(
    18, "Negatívny šprintér v audio spektre", "Negative Space Audio Sprinter", "runners",
    ["ekvalizér", "negatívny priestor", "šprintér", "grafika", "minimalizmus"],
    '''    <defs>
      <linearGradient id="g18_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#08101E"/>
        <stop offset="100%" stop-color="#020408"/>
      </linearGradient>
      <linearGradient id="g18_bars" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f18_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g18_bg)"/>
    <!-- Audio Frequency Spectrogram Lines -->
    <g fill="url(#g18_bars)" filter="url(#f18_glow)">
      <rect x="60" y="210" width="16" height="92" rx="8"/>
      <rect x="90" y="160" width="16" height="192" rx="8"/>
      <rect x="120" y="110" width="16" height="292" rx="8"/>
      <rect x="150" y="70" width="16" height="372" rx="8"/>
      <rect x="180" y="120" width="16" height="272" rx="8"/>
      <rect x="210" y="80" width="16" height="352" rx="8"/>
      <rect x="240" y="50" width="16" height="412" rx="8"/>
      <rect x="270" y="90" width="16" height="332" rx="8"/>
      <rect x="300" y="60" width="16" height="392" rx="8"/>
      <rect x="330" y="120" width="16" height="272" rx="8"/>
      <rect x="360" y="80" width="16" height="352" rx="8"/>
      <rect x="390" y="140" width="16" height="232" rx="8"/>
      <rect x="420" y="190" width="16" height="132" rx="8"/>
    </g>
    <!-- Crisp Runner Silhouette in Negative/High-Contrast Cutout -->
    <circle cx="270" cy="170" r="30" fill="#08101E" stroke="#FFFFFF" stroke-width="4"/>
    <path d="M 240 210 L 290 270 L 230 310 L 200 250 Z" fill="#08101E" stroke="#FFFFFF" stroke-width="4"/>
    <path d="M 290 230 L 350 250" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/>
    <path d="M 240 300 L 300 370 L 330 420" fill="none" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
'''
)

# ==========================================
# CATEGORY 4: Stopky & Meradlá (Stopwatches & VO2)
# ==========================================

# 19: Cyber Chrono Stopwatch
add_icon(
    19, "Kybernetické športové stopky", "Cyber Chrono Stopwatch", "stopwatch",
    ["stopky", "časovač", "displej", "tlačidlá", "šport"],
    '''    <defs>
      <linearGradient id="g19_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0D1424"/>
        <stop offset="100%" stop-color="#03060B"/>
      </linearGradient>
      <linearGradient id="g19_case" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#1E293B"/>
        <stop offset="100%" stop-color="#0F172A"/>
      </linearGradient>
      <linearGradient id="g19_rim" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f19_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g19_bg)"/>
    <!-- Top Stopwatch Buttons -->
    <rect x="236" y="40" width="40" height="30" rx="6" fill="#64748B"/>
    <rect x="220" y="65" width="72" height="18" rx="4" fill="#334155"/>
    <rect x="360" y="90" width="28" height="40" rx="6" fill="#10E76F" transform="rotate(40 374 110)"/>
    <rect x="124" y="90" width="28" height="40" rx="6" fill="#FF9F1C" transform="rotate(-40 138 110)"/>
    <!-- Main Stopwatch Body -->
    <circle cx="256" cy="280" r="180" fill="url(#g19_case)" stroke="url(#g19_rim)" stroke-width="8" filter="url(#f19_glow)"/>
    <!-- Inner dial ticks -->
    <circle cx="256" cy="280" r="150" fill="#0A0F1D" stroke="#00F2FE" stroke-width="3" stroke-dasharray="4 16"/>
    <!-- Center Waveform display -->
    <path d="M 140 280 Q 180 230, 210 280 T 270 280 T 330 280 T 372 280" fill="none" stroke="#10E76F" stroke-width="6" stroke-linecap="round"/>
    <!-- Chrono Hand pointing to top split -->
    <line x1="256" y1="280" x2="256" y2="160" stroke="#00F2FE" stroke-width="6" stroke-linecap="round" filter="url(#f19_glow)"/>
    <circle cx="256" cy="280" r="12" fill="#FFFFFF"/>
    <!-- Digital Time text -->
    <text x="256" y="340" fill="#00F2FE" font-family="'Courier New', monospace" font-weight="900" font-size="28" text-anchor="middle">08.5s</text>
'''
)

# 20: VO2 Max Performance Gauge
add_icon(
    20, "VO2 Max Tachometer (Výkon)", "VO2 Max Tachometer", "cardio",
    ["vo2 max", "budík", "tachometer", "intenzita", "červená zóna"],
    '''    <defs>
      <linearGradient id="g20_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#140812"/>
        <stop offset="100%" stop-color="#040103"/>
      </linearGradient>
      <linearGradient id="g20_arc" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="40%" stop-color="#10E76F"/>
        <stop offset="75%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#FF3366"/>
      </linearGradient>
      <filter id="f20_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g20_bg)"/>
    <!-- Tachometer Dial Arc -->
    <path d="M 96 350 A 180 180 0 1 1 416 350" fill="none" stroke="#1F2438" stroke-width="36" stroke-linecap="round"/>
    <!-- Colored Active Arc -->
    <path d="M 96 350 A 180 180 0 1 1 390 280" fill="none" stroke="url(#g20_arc)" stroke-width="36" stroke-linecap="round" filter="url(#f20_glow)"/>
    <!-- Ticks -->
    <circle cx="256" cy="270" r="130" fill="none" stroke="#FFFFFF" stroke-opacity="0.3" stroke-width="3" stroke-dasharray="4 22"/>
    <!-- Needle pinned into High Performance / Red Zone -->
    <g transform="rotate(75 256 270)">
      <polygon points="252,270 256,120 260,270" fill="#FF3366" filter="url(#f20_glow)"/>
      <circle cx="256" cy="270" r="22" fill="#FFFFFF"/>
      <circle cx="256" cy="270" r="8" fill="#FF3366"/>
    </g>
    <!-- Label -->
    <text x="256" y="380" fill="#FFFFFF" font-family="Arial, sans-serif" font-weight="900" font-size="28" text-anchor="middle" letter-spacing="3">VO2 MAX</text>
    <text x="256" y="415" fill="#FF3366" font-family="Arial, sans-serif" font-weight="700" font-size="18" text-anchor="middle">PEAK ZONE</text>
'''
)

# 21: Shuttle Chrono Dual Dial
add_icon(
    21, "Stopky s člnkovým ciferníkom", "Shuttle Chrono Dual Dial", "stopwatch",
    ["stopky", "kužele", "člnok", "časomer", "ciferník"],
    '''    <defs>
      <linearGradient id="g21_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#061220"/>
        <stop offset="100%" stop-color="#010408"/>
      </linearGradient>
      <linearGradient id="g21_hand" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f21_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g21_bg)"/>
    <!-- Outer Bezel -->
    <circle cx="256" cy="256" r="195" fill="#0C192E" stroke="#00F2FE" stroke-width="6" filter="url(#f21_glow)"/>
    <circle cx="256" cy="256" r="170" fill="#060E1A" stroke="#10E76F" stroke-width="2" stroke-dasharray="8 12"/>
    <!-- Two Mini Cone Sub-dials -->
    <!-- Left cone icon -->
    <g transform="translate(140, 240)">
      <polygon points="30,10 10,60 50,60" fill="#FF9F1C"/>
      <ellipse cx="30" cy="60" rx="20" ry="6" fill="#FF9F1C"/>
    </g>
    <!-- Right cone icon -->
    <g transform="translate(312, 240)">
      <polygon points="30,10 10,60 50,60" fill="#10E76F"/>
      <ellipse cx="30" cy="60" rx="20" ry="6" fill="#10E76F"/>
    </g>
    <!-- Shuttle Arrow between cones in center -->
    <path d="M 185 270 L 325 270" stroke="#FFFFFF" stroke-width="4" stroke-dasharray="6 6"/>
    <!-- Sweeping Chrono Hand -->
    <line x1="256" y1="256" x2="330" y2="130" stroke="url(#g21_hand)" stroke-width="8" stroke-linecap="round" filter="url(#f21_glow)"/>
    <circle cx="256" cy="256" r="16" fill="#FFFFFF"/>
'''
)

# 22: 21-Level Ring Timer
add_icon(
    22, "21-Úrovňový prstenec (Levels)", "21-Level Ring Timer", "stopwatch",
    ["21 levelov", "úrovne", "prstenec", "segmenty", "progres"],
    '''    <defs>
      <linearGradient id="g22_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#080A18"/>
        <stop offset="100%" stop-color="#020308"/>
      </linearGradient>
      <linearGradient id="g22_seg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#10E76F"/>
        <stop offset="50%" stop-color="#00F2FE"/>
        <stop offset="85%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#FF3366"/>
      </linearGradient>
      <filter id="f22_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g22_bg)"/>
    <!-- 21 segmented ticks forming complete training dial -->
    <circle cx="256" cy="256" r="180" fill="none" stroke="url(#g22_seg)" stroke-width="26" stroke-dasharray="21 6" stroke-linecap="round" filter="url(#f22_glow)"/>
    <!-- Inner dial ring -->
    <circle cx="256" cy="256" r="140" fill="#0E1324" stroke="#232C4A" stroke-width="3"/>
    <!-- Big Level Display in center -->
    <text x="256" y="235" fill="#64748B" font-family="Arial, sans-serif" font-weight="700" font-size="20" text-anchor="middle" letter-spacing="3">STAGE</text>
    <text x="256" y="295" fill="#FFFFFF" font-family="Arial, sans-serif" font-weight="900" font-size="64" text-anchor="middle">21</text>
    <text x="256" y="330" fill="#10E76F" font-family="Arial, sans-serif" font-weight="800" font-size="16" text-anchor="middle" letter-spacing="2">SHUTTLE 16</text>
'''
)

# 23: Lightning Bolt Chrono
add_icon(
    23, "Bleskové stopky (Rýchlosť)", "Lightning Bolt Chrono", "stopwatch",
    ["blesk", "stopky", "energie", "rýchlosť", "výboj"],
    '''    <defs>
      <linearGradient id="g23_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#141005"/>
        <stop offset="100%" stop-color="#050401"/>
      </linearGradient>
      <linearGradient id="g23_bolt" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FFE600"/>
        <stop offset="50%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#FF3366"/>
      </linearGradient>
      <filter id="f23_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g23_bg)"/>
    <!-- Circular Stopwatch Shell -->
    <circle cx="256" cy="270" r="170" fill="#14131A" stroke="#FF9F1C" stroke-width="6" stroke-dasharray="16 8"/>
    <!-- Powerful Diagonal Lightning Bolt splitting the face -->
    <polygon points="280,60 170,260 250,260 210,450 340,220 260,220" fill="url(#g23_bolt)" filter="url(#f23_glow)"/>
    <!-- Speed arcs -->
    <path d="M 120 200 A 150 150 0 0 1 200 130" fill="none" stroke="#FFE600" stroke-width="8" stroke-linecap="round" filter="url(#f23_glow)"/>
    <path d="M 390 320 A 150 150 0 0 1 310 400" fill="none" stroke="#FF3366" stroke-width="8" stroke-linecap="round" filter="url(#f23_glow)"/>
'''
)

# 24: Precision HUD Crosshair Timer
add_icon(
    24, "Precízny HUD časomerač", "Precision HUD Crosshair Timer", "stopwatch",
    ["hud", "technológia", "zameriavač", "meranie", "presnosť"],
    '''    <defs>
      <linearGradient id="g24_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#031622"/>
        <stop offset="100%" stop-color="#01070B"/>
      </linearGradient>
      <filter id="f24_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g24_bg)"/>
    <!-- HUD Box corners -->
    <path d="M 90 140 L 90 90 L 140 90 M 372 90 L 422 90 L 422 140 M 422 372 L 422 422 L 372 422 M 140 422 L 90 422 L 90 372" 
          fill="none" stroke="#00F2FE" stroke-width="6" stroke-linecap="round"/>
    <!-- Central HUD Circle -->
    <circle cx="256" cy="256" r="130" fill="none" stroke="#00F2FE" stroke-width="3" stroke-opacity="0.4"/>
    <circle cx="256" cy="256" r="100" fill="none" stroke="#10E76F" stroke-width="5" stroke-dasharray="12 8" filter="url(#f24_glow)"/>
    <!-- Crosshairs -->
    <line x1="256" y1="126" x2="256" y2="176" stroke="#00F2FE" stroke-width="4"/>
    <line x1="256" y1="336" x2="256" y2="386" stroke="#00F2FE" stroke-width="4"/>
    <line x1="126" y1="256" x2="176" y2="256" stroke="#00F2FE" stroke-width="4"/>
    <line x1="336" y1="256" x2="386" y2="256" stroke="#00F2FE" stroke-width="4"/>
    <!-- Center Beep Metric -->
    <text x="256" y="245" fill="#FFFFFF" font-family="'Courier New', monospace" font-weight="900" font-size="34" text-anchor="middle">08.52</text>
    <text x="256" y="280" fill="#10E76F" font-family="Arial, sans-serif" font-weight="700" font-size="14" text-anchor="middle" letter-spacing="2">PACER INTERVAL</text>
'''
)

# ==========================================
# CATEGORY 5: Monogramy & Logá (Monograms & Badges)
# ==========================================

# 25: Letter 'B' Sonic Wave
add_icon(
    25, "Monogram 'B' & Audio vlny", "Letter 'B' Sonic Wave", "badges",
    ["písmeno b", "monogram", "logo", "audio vlny", "značka"],
    '''    <defs>
      <linearGradient id="g25_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#081024"/>
        <stop offset="100%" stop-color="#02040A"/>
      </linearGradient>
      <linearGradient id="g25_b" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="50%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#00C9FF"/>
      </linearGradient>
      <filter id="f25_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="9" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g25_bg)"/>
    <!-- Left Stem composed of 4 Audio Equalizer capsules -->
    <g fill="url(#g25_b)" filter="url(#f25_glow)">
      <rect x="110" y="110" width="36" height="60" rx="18"/>
      <rect x="110" y="185" width="36" height="142" rx="18"/>
      <rect x="110" y="342" width="36" height="60" rx="18"/>
    </g>
    <!-- Right Upper & Lower Lobes made of dynamic sonic arcs -->
    <g fill="none" stroke="url(#g25_b)" stroke-linecap="round" filter="url(#f25_glow)">
      <!-- Top Lobe -->
      <path d="M 155 125 L 250 125 C 330 125, 330 235, 250 235 L 155 235" stroke-width="34"/>
      <!-- Bottom Lobe -->
      <path d="M 155 275 L 270 275 C 365 275, 365 385, 270 385 L 155 385" stroke-width="34"/>
    </g>
    <!-- Speed notch accents cutting through lobes -->
    <line x1="280" y1="180" x2="330" y2="180" stroke="#081024" stroke-width="10"/>
    <line x1="300" y1="330" x2="360" y2="330" stroke="#081024" stroke-width="10"/>
'''
)

# 26: Interlocking 'BT' Speedmark
add_icon(
    26, "Športový monogram 'BT' (Beep Test)", "Interlocking 'BT' Speedmark", "badges",
    ["bt", "beep test", "monogram", "šport", "typografia"],
    '''    <defs>
      <linearGradient id="g26_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#120A24"/>
        <stop offset="100%" stop-color="#04020A"/>
      </linearGradient>
      <linearGradient id="g26_bt" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FF3366"/>
        <stop offset="50%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#00F2FE"/>
      </linearGradient>
      <filter id="f26_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g26_bg)"/>
    <!-- Italic / Slanted athletic monogram -->
    <g transform="skewX(-16) translate(60, 0)" filter="url(#f26_glow)">
      <!-- Letter B -->
      <path d="M 110 110 L 220 110 C 280 110, 280 230, 220 230 C 290 230, 290 400, 210 400 L 110 400 Z" 
            fill="none" stroke="url(#g26_bt)" stroke-width="36" stroke-linejoin="round"/>
      <line x1="110" y1="230" x2="220" y2="230" stroke="url(#g26_bt)" stroke-width="32"/>
      <!-- Interlocking Letter T passing through B -->
      <path d="M 270 110 L 390 110 M 330 110 L 330 400" stroke="#00F2FE" stroke-width="36" stroke-linecap="round"/>
    </g>
'''
)

# 27: Tactical Beep Hexagon
add_icon(
    27, "Taktický šesťuholníkový odznak", "Tactical Beep Hexagon", "badges",
    ["šesťuholník", "odznak", "crest", "taktika", "armáda"],
    '''    <defs>
      <linearGradient id="g27_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0B1626"/>
        <stop offset="100%" stop-color="#02060C"/>
      </linearGradient>
      <linearGradient id="g27_hex" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#00F2FE"/>
      </linearGradient>
      <filter id="f27_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g27_bg)"/>
    <!-- Outer Hexagon Crest -->
    <polygon points="256,50 420,145 420,367 256,462 92,367 92,145" fill="#0F1F38" stroke="url(#g27_hex)" stroke-width="12" filter="url(#f27_glow)"/>
    <polygon points="256,80 395,160 395,352 256,432 117,352 117,160" fill="none" stroke="#00F2FE" stroke-width="2" stroke-dasharray="8 8" opacity="0.6"/>
    <!-- Center Sprinter Silhouette in Hexagon -->
    <g fill="#FFFFFF" filter="url(#f27_glow)" transform="translate(10, -10)">
      <circle cx="240" cy="190" r="22" fill="#10E76F"/>
      <path d="M 225 220 L 260 270 L 220 300 L 200 250 Z" fill="#10E76F"/>
      <!-- Legs -->
      <path d="M 225 300 L 275 350 L 305 400" fill="none" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round"/>
      <path d="M 210 300 L 170 330 L 130 350" fill="none" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round"/>
    </g>
    <!-- Radio Soundwave wings -->
    <path d="M 140 220 A 40 40 0 0 1 140 300" fill="none" stroke="#10E76F" stroke-width="6" stroke-linecap="round"/>
    <path d="M 360 220 A 40 40 0 0 0 360 300" fill="none" stroke="#10E76F" stroke-width="6" stroke-linecap="round"/>
'''
)

# 28: Aero Sole & Speaker Wave
add_icon(
    28, "Bežecká podrážka & Zvuk", "Aero Sole & Sound Wave", "badges",
    ["podrážka", "tretra", "obuv", "zvuk", "šport"],
    '''    <defs>
      <linearGradient id="g28_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#140A18"/>
        <stop offset="100%" stop-color="#040106"/>
      </linearGradient>
      <linearGradient id="g28_sole" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FF3366"/>
        <stop offset="50%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f28_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g28_bg)"/>
    <!-- Stylized Running Shoe Profile in mid-air acceleration -->
    <g transform="rotate(-25 256 256)">
      <!-- Dynamic Sole with audio grip lugs -->
      <path d="M 110 300 Q 230 330, 370 270 Q 420 250, 440 220 L 410 200 Q 360 230, 230 250 Q 130 250, 110 270 Z" 
            fill="url(#g28_sole)" filter="url(#f28_glow)"/>
      <!-- Upper Shoe Silhouette -->
      <path d="M 120 270 C 130 180, 250 160, 310 210 L 400 210" fill="none" stroke="#00F2FE" stroke-width="12" stroke-linecap="round"/>
      <!-- Heel Strike Sound Shockwaves -->
      <path d="M 80 270 A 50 50 0 0 1 80 370" fill="none" stroke="#FF3366" stroke-width="8" stroke-linecap="round" filter="url(#f28_glow)"/>
      <path d="M 50 250 A 80 80 0 0 1 50 400" fill="none" stroke="#FF9F1C" stroke-width="6" stroke-linecap="round"/>
    </g>
'''
)

# 29: Endurance Shield Crest
add_icon(
    29, "Štít vytrvalosti (Shield)", "Endurance Shield Crest", "badges",
    ["štít", "erb", "crest", "vytrvalosť", "elitný"],
    '''    <defs>
      <linearGradient id="g29_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#080F1E"/>
        <stop offset="100%" stop-color="#020408"/>
      </linearGradient>
      <linearGradient id="g29_shield" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f29_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g29_bg)"/>
    <!-- Athletic Shield Silhouette -->
    <path d="M 256 60 L 412 110 C 412 280, 256 420, 256 450 C 256 420, 100 280, 100 110 Z" 
          fill="#0F1B33" stroke="url(#g29_shield)" stroke-width="14" filter="url(#f29_glow)"/>
    <!-- Inner dividing wave line -->
    <path d="M 120 220 Q 200 160, 256 220 T 392 220" fill="none" stroke="#10E76F" stroke-width="8" stroke-linecap="round"/>
    <!-- Upper section: Twin Shuttle Cones -->
    <polygon points="180,140 165,190 195,190" fill="#FF9F1C"/>
    <polygon points="332,140 317,190 347,190" fill="#FF9F1C"/>
    <line x1="180" y1="190" x2="332" y2="190" stroke="#00F2FE" stroke-width="3" stroke-dasharray="4 4"/>
    <!-- Lower section: Audio Ping Core -->
    <circle cx="256" cy="310" r="30" fill="none" stroke="#00F2FE" stroke-width="6"/>
    <circle cx="256" cy="310" r="14" fill="#10E76F" filter="url(#f29_glow)"/>
'''
)

# 30: Tri-Arc Minimal B
add_icon(
    30, "Tri-Arc minimalistické 'B'", "Tri-Arc Minimal 'B'", "badges",
    ["minimalizmus", "oblúky", "čistý", "moderný", "b"],
    '''    <defs>
      <linearGradient id="g30_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0A0E18"/>
        <stop offset="100%" stop-color="#020306"/>
      </linearGradient>
      <linearGradient id="g30_arc" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f30_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="9" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g30_bg)"/>
    <!-- Three concentric expanding arcs curving into stylized 'B' -->
    <path d="M 160 110 L 240 110 A 75 75 0 0 1 240 260 L 160 260 L 260 260 A 75 75 0 0 1 260 410 L 160 410" 
          fill="none" stroke="url(#g30_arc)" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" filter="url(#f30_glow)"/>
    <!-- Inner pulse dot -->
    <circle cx="240" cy="185" r="14" fill="#00F2FE"/>
    <circle cx="260" cy="335" r="14" fill="#10E76F"/>
'''
)

# ==========================================
# CATEGORY 6: Kardio & Výdrž (Cardio & Energy)
# ==========================================

# 31: Endurance Pulse Heart
add_icon(
    31, "Atletické vytrvalostné srdce", "Athletic Endurance Heart", "cardio",
    ["srdce", "kardio", "pulz", "vytrvalosť", "život"],
    '''    <defs>
      <linearGradient id="g31_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#1A0610"/>
        <stop offset="100%" stop-color="#050103"/>
      </linearGradient>
      <linearGradient id="g31_heart" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FF3366"/>
        <stop offset="60%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#FFE600"/>
      </linearGradient>
      <filter id="f31_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="9" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g31_bg)"/>
    <!-- Glowing Heart Shape -->
    <path d="M 256 140 C 230 70, 120 70, 90 160 C 60 250, 180 340, 256 420 C 332 340, 452 250, 422 160 C 392 70, 282 70, 256 140 Z" 
          fill="none" stroke="url(#g31_heart)" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" filter="url(#f31_glow)"/>
    <!-- Inner audio frequency wave passing across heart -->
    <path d="M 120 260 L 190 260 L 220 180 L 260 330 L 290 220 L 320 260 L 392 260" 
          fill="none" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" filter="url(#f31_glow)"/>
'''
)

# 32: VO2 Fire Runner
add_icon(
    32, "Ohnivý plameň VO2 (Fire)", "VO2 Fire Runner", "cardio",
    ["oheň", "plameň", "energia", "intenzita", "bežec"],
    '''    <defs>
      <linearGradient id="g32_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#180800"/>
        <stop offset="100%" stop-color="#050200"/>
      </linearGradient>
      <linearGradient id="g32_fire" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#FF3366"/>
        <stop offset="50%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#FFEA00"/>
      </linearGradient>
      <filter id="f32_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="9" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g32_bg)"/>
    <!-- Outer Energetic Flame -->
    <path d="M 256 50 C 320 140, 410 200, 410 320 C 410 405, 340 450, 256 450 C 172 450, 102 405, 102 320 C 102 210, 200 150, 256 50 Z" 
          fill="url(#g32_fire)" filter="url(#f32_glow)"/>
    <!-- Inner negative space Runner -->
    <circle cx="256" cy="210" r="22" fill="#180800"/>
    <path d="M 240 240 L 280 290 L 235 320 L 210 270 Z" fill="#180800"/>
    <path d="M 240 320 L 290 380 L 320 420" fill="none" stroke="#180800" stroke-width="14" stroke-linecap="round"/>
    <path d="M 220 320 L 180 360 L 140 370" fill="none" stroke="#180800" stroke-width="14" stroke-linecap="round"/>
'''
)

# 33: Level 21 Escalation Stairs
add_icon(
    33, "Stupne úrovní (Level 1 až 21)", "Level 21 Escalation Stairs", "cardio",
    ["úrovne", "schody", "stúpanie", "progres", "vrchol"],
    '''    <defs>
      <linearGradient id="g33_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#070E1A"/>
        <stop offset="100%" stop-color="#010307"/>
      </linearGradient>
      <linearGradient id="g33_bar" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="50%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#FF3366"/>
      </linearGradient>
      <filter id="f33_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g33_bg)"/>
    <!-- 7 Escalating stadium blocks -->
    <rect x="70" y="380" width="40" height="70" rx="8" fill="#00F2FE" opacity="0.6"/>
    <rect x="120" y="330" width="40" height="120" rx="8" fill="#00F2FE" opacity="0.8"/>
    <rect x="170" y="280" width="40" height="170" rx="8" fill="#10E76F" opacity="0.8"/>
    <rect x="220" y="230" width="40" height="220" rx="8" fill="#10E76F"/>
    <rect x="270" y="180" width="40" height="270" rx="8" fill="#FF9F1C" filter="url(#f33_glow)"/>
    <rect x="320" y="130" width="40" height="320" rx="8" fill="#FF5E00" filter="url(#f33_glow)"/>
    <rect x="370" y="80" width="40" height="370" rx="8" fill="#FF3366" filter="url(#f33_glow)"/>
    <!-- Star on the peak -->
    <polygon points="390,30 396,48 415,48 400,60 405,78 390,66 375,78 380,60 365,48 384,48" fill="#FFE600" filter="url(#f33_glow)"/>
    <!-- Acceleration curve line across peaks -->
    <path d="M 90 370 C 190 320, 270 200, 390 70" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
'''
)

# 34: Hyper Pulse Core
add_icon(
    34, "Hyperaktívny akustický reaktor", "Hyper Pulse Reactor Core", "futuristic",
    ["reaktor", "jadro", "energia", "vlny", "akustika"],
    '''    <defs>
      <linearGradient id="g34_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#05141E"/>
        <stop offset="100%" stop-color="#01050A"/>
      </linearGradient>
      <linearGradient id="g34_orb" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f34_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="9" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g34_bg)"/>
    <!-- Radiating sonic pulses -->
    <circle cx="256" cy="256" r="190" fill="none" stroke="#00F2FE" stroke-opacity="0.2" stroke-width="4"/>
    <circle cx="256" cy="256" r="140" fill="none" stroke="#10E76F" stroke-opacity="0.4" stroke-width="6" stroke-dasharray="24 16"/>
    <!-- 4 directional sports power fins -->
    <path d="M 256 50 L 270 120 L 242 120 Z" fill="#00F2FE"/>
    <path d="M 256 462 L 270 392 L 242 392 Z" fill="#00F2FE"/>
    <path d="M 50 256 L 120 270 L 120 242 Z" fill="#10E76F"/>
    <path d="M 462 256 L 392 270 L 392 242 Z" fill="#10E76F"/>
    <!-- Glowing Reactor Orb -->
    <circle cx="256" cy="256" r="75" fill="url(#g34_orb)" filter="url(#f34_glow)"/>
    <circle cx="256" cy="256" r="40" fill="#FFFFFF" filter="url(#f34_glow)"/>
'''
)

# 35: Stamina Turbo Battery
add_icon(
    35, "Turbo batéria vytrvalosti", "Turbo Stamina Battery", "futuristic",
    ["batéria", "vytrvalosť", "energie", "kondícia", "nabíjanie"],
    '''    <defs>
      <linearGradient id="g35_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#08140E"/>
        <stop offset="100%" stop-color="#010503"/>
      </linearGradient>
      <linearGradient id="g35_charge" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="60%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#FFE600"/>
      </linearGradient>
      <filter id="f35_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g35_bg)"/>
    <!-- Battery Outer Shell -->
    <rect x="136" y="100" width="240" height="340" rx="36" fill="none" stroke="#1F3D2C" stroke-width="12"/>
    <!-- Top terminal nipple -->
    <rect x="206" y="60" width="100" height="36" rx="12" fill="#10E76F" filter="url(#f35_glow)"/>
    <!-- Internal Charged Energy Bars -->
    <rect x="160" y="350" width="192" height="60" rx="16" fill="#00F2FE" filter="url(#f35_glow)"/>
    <rect x="160" y="275" width="192" height="60" rx="16" fill="#10E76F" filter="url(#f35_glow)"/>
    <rect x="160" y="200" width="192" height="60" rx="16" fill="#10E76F" filter="url(#f35_glow)"/>
    <rect x="160" y="125" width="192" height="60" rx="16" fill="#FFE600" filter="url(#f35_glow)"/>
    <!-- Fast Lightning Overlay -->
    <polygon points="270,140 210,270 270,270 230,390 320,240 260,240" fill="#FFFFFF"/>
'''
)

# ==========================================
# CATEGORY 7: Futuristické & High-Tech
# ==========================================

# 36: Prism Shuttle Beam
add_icon(
    36, "Hranol & Refrakčný lúč", "Prism Shuttle Beam", "futuristic",
    ["hranol", "laser", "svetlo", "futuristické", "moderné"],
    '''    <defs>
      <linearGradient id="g36_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#070918"/>
        <stop offset="100%" stop-color="#020308"/>
      </linearGradient>
      <linearGradient id="g36_beam" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="50%" stop-color="#10E76F"/>
        <stop offset="100%" stop-color="#FF3366"/>
      </linearGradient>
      <filter id="f36_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g36_bg)"/>
    <!-- Glassmorphic Triangle Prism -->
    <polygon points="256,100 400,380 112,380" fill="#111B38" stroke="#00F2FE" stroke-width="8" stroke-linejoin="round" filter="url(#f36_glow)"/>
    <!-- Incoming Beep Ray -->
    <line x1="40" y1="260" x2="184" y2="260" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" filter="url(#f36_glow)"/>
    <!-- Refracted Multi-colored Shuttle Beams -->
    <line x1="280" y1="240" x2="472" y2="160" stroke="#FF3366" stroke-width="8" stroke-linecap="round" filter="url(#f36_glow)"/>
    <line x1="290" y1="260" x2="472" y2="260" stroke="#FF9F1C" stroke-width="8" stroke-linecap="round" filter="url(#f36_glow)"/>
    <line x1="280" y1="280" x2="472" y2="360" stroke="#10E76F" stroke-width="8" stroke-linecap="round" filter="url(#f36_glow)"/>
'''
)

# 37: Neon Track Circuit
add_icon(
    37, "Kybernetická čipová dráha", "Cyber Circuit Track", "futuristic",
    ["čip", "plošný spoj", "kybernetika", "dráha", "hi-tech"],
    '''    <defs>
      <linearGradient id="g37_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#041214"/>
        <stop offset="100%" stop-color="#010607"/>
      </linearGradient>
      <filter id="f37_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g37_bg)"/>
    <!-- Stadium Circuit Oval -->
    <rect x="106" y="90" width="300" height="332" rx="150" fill="none" stroke="#0B3036" stroke-width="28"/>
    <rect x="106" y="90" width="300" height="332" rx="150" fill="none" stroke="#10E76F" stroke-width="6" stroke-dasharray="40 18" filter="url(#f37_glow)"/>
    <!-- Circuit PCB Traces branching out -->
    <g stroke="#00F2FE" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M 256 90 L 256 40 M 256 40 L 320 40"/>
      <path d="M 256 422 L 256 472 M 256 472 L 190 472"/>
      <path d="M 106 256 L 50 256 M 50 256 L 50 310"/>
      <path d="M 406 256 L 462 256 M 462 256 L 462 200"/>
    </g>
    <!-- Circuit Nodes -->
    <circle cx="320" cy="40" r="10" fill="#00F2FE" filter="url(#f37_glow)"/>
    <circle cx="190" cy="472" r="10" fill="#00F2FE" filter="url(#f37_glow)"/>
    <!-- Central Processing Core: BEEP CHIP -->
    <rect x="206" y="206" width="100" height="100" rx="18" fill="#0E242B" stroke="#10E76F" stroke-width="4" filter="url(#f37_glow)"/>
    <text x="256" y="266" fill="#10E76F" font-family="'Courier New', monospace" font-weight="900" font-size="22" text-anchor="middle">BEEP</text>
'''
)

# 38: Acoustic Coach Whistle
add_icon(
    38, "Akustická píšťalka & Šoková vlna", "Acoustic Whistle & Shockwave", "audio",
    ["píšťalka", "rozhodca", "tréner", "zvuk", "signál"],
    '''    <defs>
      <linearGradient id="g38_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0F172A"/>
        <stop offset="100%" stop-color="#020617"/>
      </linearGradient>
      <linearGradient id="g38_metal" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#E2E8F0"/>
        <stop offset="50%" stop-color="#94A3B8"/>
        <stop offset="100%" stop-color="#475569"/>
      </linearGradient>
      <filter id="f38_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g38_bg)"/>
    <!-- Whistle Icon Body -->
    <g transform="rotate(-15 220 280)">
      <!-- Lanyard ring -->
      <circle cx="110" cy="270" r="28" fill="none" stroke="#94A3B8" stroke-width="12"/>
      <!-- Main Barrel -->
      <circle cx="190" cy="270" r="75" fill="url(#g38_metal)"/>
      <!-- Mouthpiece Stem -->
      <path d="M 190 200 L 330 200 L 330 260 L 255 260 Z" fill="url(#g38_metal)"/>
      <!-- Sound slot opening -->
      <rect x="235" y="190" width="22" height="40" rx="4" fill="#0F172A"/>
    </g>
    <!-- Supersonic Whistle Beep Blastwaves -->
    <path d="M 360 160 A 80 80 0 0 1 420 300" fill="none" stroke="#00F2FE" stroke-width="14" stroke-linecap="round" filter="url(#f38_glow)"/>
    <path d="M 400 110 A 140 140 0 0 1 475 350" fill="none" stroke="#10E76F" stroke-width="10" stroke-linecap="round" filter="url(#f38_glow)"/>
'''
)

# 39: Quantum Polygon Runner
add_icon(
    39, "Kvantový polygonový bežec", "Quantum Polygon Runner", "runners",
    ["polygón", "geometria", "častice", "dynamika", "abstrakt"],
    '''    <defs>
      <linearGradient id="g39_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#080718"/>
        <stop offset="100%" stop-color="#010106"/>
      </linearGradient>
      <filter id="f39_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g39_bg)"/>
    <!-- Faceted low-poly runner composed of glowing triangles -->
    <g filter="url(#f39_glow)">
      <!-- Head -->
      <polygon points="280,120 310,140 270,160" fill="#00F2FE"/>
      <!-- Chest / Torso Facets -->
      <polygon points="270,160 310,140 330,220 260,210" fill="#00C9FF"/>
      <polygon points="260,210 330,220 280,270 230,250" fill="#10E76F"/>
      <!-- Arms -->
      <polygon points="310,140 380,180 340,210" fill="#00F2FE"/>
      <polygon points="260,180 200,210 220,240" fill="#7928CA"/>
      <!-- Forward Leg -->
      <polygon points="280,270 330,330 300,340" fill="#10E76F"/>
      <polygon points="330,330 350,420 320,400" fill="#00F2FE"/>
      <!-- Rear Leg -->
      <polygon points="230,250 170,300 200,320" fill="#7928CA"/>
      <polygon points="170,300 110,340 140,350" fill="#FF3366"/>
    </g>
    <!-- Exploding sonic particles -->
    <circle cx="370" cy="120" r="8" fill="#00F2FE"/>
    <circle cx="410" cy="180" r="6" fill="#10E76F"/>
    <circle cx="390" cy="270" r="10" fill="#FFE600"/>
    <circle cx="100" cy="230" r="6" fill="#FF3366"/>
    <circle cx="70" cy="280" r="8" fill="#7928CA"/>
'''
)

# 40: Obsidian Gold Master Badge
add_icon(
    40, "Zlatý odznak šampióna (Obsidian Gold)", "Obsidian Gold Master Badge", "badges",
    ["zlato", "luxus", "šampión", "odznak", "master"],
    '''    <defs>
      <linearGradient id="g40_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#141418"/>
        <stop offset="100%" stop-color="#050508"/>
      </linearGradient>
      <linearGradient id="g40_gold" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FFE885"/>
        <stop offset="35%" stop-color="#D4AF37"/>
        <stop offset="70%" stop-color="#AA7C11"/>
        <stop offset="100%" stop-color="#FED000"/>
      </linearGradient>
      <filter id="f40_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g40_bg)"/>
    <!-- Outer Bevelled Gold Shield -->
    <polygon points="256,50 426,110 426,300 256,462 86,300 86,110" 
             fill="#0E0E12" stroke="url(#g40_gold)" stroke-width="14" filter="url(#f40_glow)"/>
    <!-- Inner gold filigree ring -->
    <circle cx="256" cy="240" r="120" fill="none" stroke="url(#g40_gold)" stroke-width="3" stroke-dasharray="10 8"/>
    <!-- Laurel Wreath Leaves / Wings of Speed -->
    <path d="M 160 270 C 140 200, 190 140, 230 140" fill="none" stroke="url(#g40_gold)" stroke-width="8" stroke-linecap="round"/>
    <path d="M 352 270 C 372 200, 322 140, 282 140" fill="none" stroke="url(#g40_gold)" stroke-width="8" stroke-linecap="round"/>
    <!-- Center Beep Runner & Crown Glyph -->
    <g fill="url(#g40_gold)" filter="url(#f40_glow)">
      <!-- Crown -->
      <polygon points="220,180 232,205 256,185 280,205 292,180 290,215 222,215"/>
      <!-- Golden 'B' Monogram -->
      <text x="256" y="300" font-family="'Times New Roman', serif" font-weight="900" font-size="82" text-anchor="middle">B</text>
    </g>
    <!-- Bottom Ribbon text -->
    <rect x="176" y="340" width="160" height="34" rx="17" fill="#1C1C24" stroke="url(#g40_gold)" stroke-width="2"/>
    <text x="256" y="363" fill="#FFE885" font-family="Arial, sans-serif" font-weight="900" font-size="14" text-anchor="middle" letter-spacing="3">LEVEL 21</text>
'''
)

# ==========================================
# NOVÉ VARIANTY IKONY 1 (#41 - #45)
# ==========================================

# 41: Ikona 1A — Supersonický zvukový tresk (Mach 1 Shockwave)
add_icon(
    41, "Ikona 1A — Supersonický tresk (Mach 1)", "Variant 1A: Supersonic Shockwave", "icon1_variants",
    ["variant ikony 1", "šprintér", "zvukový tresk", "mach 1", "tlaková vlna"],
    '''    <defs>
      <linearGradient id="g41_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#050C1B"/>
        <stop offset="100%" stop-color="#020409"/>
      </linearGradient>
      <linearGradient id="g41_runner" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FFFFFF"/>
        <stop offset="30%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <linearGradient id="g41_mach" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.9"/>
        <stop offset="40%" stop-color="#00F2FE" stop-opacity="0.8"/>
        <stop offset="100%" stop-color="#10E76F" stop-opacity="0.0"/>
      </linearGradient>
      <filter id="f41_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g41_bg)"/>
    <!-- Speed ground perspective rays -->
    <line x1="40" y1="460" x2="472" y2="460" stroke="#10E76F" stroke-width="4" stroke-opacity="0.3"/>
    <line x1="80" y1="440" x2="440" y2="440" stroke="#00F2FE" stroke-width="2" stroke-opacity="0.2" stroke-dasharray="8 12"/>
    <line x1="120" y1="420" x2="400" y2="420" stroke="#00F2FE" stroke-width="2" stroke-opacity="0.15" stroke-dasharray="6 8"/>
    <!-- Mach Cone Shockwave V-angle -->
    <path d="M 330 200 L 70 80 M 330 200 L 70 380" stroke="url(#g41_mach)" stroke-width="8" stroke-linecap="round" filter="url(#f41_glow)"/>
    <!-- Compressed Doppler sound wavefronts ahead of runner -->
    <path d="M 345 160 A 60 60 0 0 1 345 280" fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" filter="url(#f41_glow)"/>
    <path d="M 375 130 A 100 100 0 0 1 375 310" fill="none" stroke="#00F2FE" stroke-width="8" stroke-linecap="round" filter="url(#f41_glow)"/>
    <path d="M 405 100 A 140 140 0 0 1 405 340" fill="none" stroke="#10E76F" stroke-width="6" stroke-linecap="round" opacity="0.7"/>
    <path d="M 435 70 A 180 180 0 0 1 435 370" fill="none" stroke="#10E76F" stroke-width="4" stroke-linecap="round" opacity="0.35"/>
    <!-- Trailing sonic boom streaks -->
    <line x1="60" y1="190" x2="200" y2="190" stroke="#00F2FE" stroke-width="4" stroke-linecap="round" opacity="0.4"/>
    <line x1="40" y1="240" x2="180" y2="240" stroke="#00F2FE" stroke-width="6" stroke-linecap="round" opacity="0.5"/>
    <line x1="80" y1="280" x2="210" y2="280" stroke="#10E76F" stroke-width="4" stroke-linecap="round" opacity="0.4"/>
    <!-- Sprinter Figure in extreme forward acceleration drive -->
    <g fill="url(#g41_runner)" filter="url(#f41_glow)">
      <!-- Head -->
      <circle cx="285" cy="140" r="28" fill="#FFFFFF"/>
      <!-- Torso -->
      <path d="M 260 170 L 310 230 L 250 280 L 220 220 Z"/>
      <!-- Forward Arm reaching through sound barrier -->
      <path d="M 295 195 L 360 215 L 375 195" fill="none" stroke="#FFFFFF" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Rear Arm pumping backward -->
      <path d="M 250 200 L 185 215 L 165 240" fill="none" stroke="url(#g41_runner)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Forward Leg driving knee high -->
      <path d="M 260 270 L 320 310 L 340 380" fill="none" stroke="url(#g41_runner)" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Back Leg fully extended drive -->
      <path d="M 240 270 L 175 320 L 120 345" fill="none" stroke="url(#g41_runner)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <!-- Explosive impact flare at point of sound barrier break -->
    <circle cx="330" cy="205" r="14" fill="#FFFFFF" filter="url(#f41_glow)"/>
    <circle cx="330" cy="205" r="5" fill="#00F2FE"/>
'''
)

# 42: Ikona 1B — Čistý minimalistický obrys (Pure Neon Radian)
add_icon(
    42, "Ikona 1B — Čistý minimalizmus & Zvuk", "Variant 1B: Pure Minimal Neon Radian", "icon1_variants",
    ["variant ikony 1", "minimalizmus", "čistý", "vektor", "apple štýl"],
    '''    <defs>
      <linearGradient id="g42_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#080C14"/>
        <stop offset="100%" stop-color="#020306"/>
      </linearGradient>
      <linearGradient id="g42_arcs" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f42_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g42_bg)"/>
    <!-- Ambient subtle center energy bloom -->
    <circle cx="280" cy="256" r="140" fill="#00F2FE" fill-opacity="0.06"/>
    <!-- Minimalist ground baseline with 20m pace dot -->
    <line x1="80" y1="410" x2="432" y2="410" stroke="#24324D" stroke-width="3" stroke-linecap="round"/>
    <line x1="160" y1="410" x2="380" y2="410" stroke="#10E76F" stroke-width="3" stroke-linecap="round" filter="url(#f42_glow)"/>
    <circle cx="380" cy="410" r="6" fill="#10E76F" filter="url(#f42_glow)"/>
    <!-- 4 Pure, razor-sharp geometric concentric sound arcs -->
    <g fill="none" stroke="url(#g42_arcs)" stroke-linecap="round" filter="url(#f42_glow)">
      <path d="M 330 190 A 70 70 0 0 1 330 310" stroke-width="12"/>
      <path d="M 365 155 A 115 115 0 0 1 365 345" stroke-width="9" stroke-opacity="0.85"/>
      <path d="M 400 120 A 160 160 0 0 1 400 380" stroke-width="6" stroke-opacity="0.55"/>
      <path d="M 435 85 A 205 205 0 0 1 435 415" stroke-width="4" stroke-opacity="0.3"/>
    </g>
    <!-- Crisp, High-Contrast Solid White Runner Silhouette -->
    <g fill="#FFFFFF" filter="url(#f42_glow)">
      <circle cx="250" cy="145" r="26"/>
      <path d="M 230 178 L 272 235 L 222 280 L 195 225 Z"/>
      <path d="M 260 205 L 320 230 L 332 215" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 225 210 L 165 230 L 150 255" fill="none" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 230 275 L 290 315 L 310 385" fill="none" stroke="#FFFFFF" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 210 275 L 155 315 L 105 345" fill="none" stroke="#FFFFFF" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <!-- Cyan athletic rim-light stroke on runner -->
    <path d="M 260 205 L 320 230" stroke="#00F2FE" stroke-width="6" stroke-linecap="round"/>
    <path d="M 230 275 L 290 315 L 310 385" stroke="#00F2FE" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
'''
)

# 43: Ikona 1C — Pohybová stopa / After-image (Velocity Ghost Trail)
add_icon(
    43, "Ikona 1C — Pohybová stopa (Ghost Trail)", "Variant 1C: Velocity Ghost Trail", "icon1_variants",
    ["variant ikony 1", "pohybová stopa", "after-image", "zrýchlenie", "tempo"],
    '''    <defs>
      <linearGradient id="g43_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0E0B1F"/>
        <stop offset="100%" stop-color="#030208"/>
      </linearGradient>
      <linearGradient id="g43_lead" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <filter id="f43_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g43_bg)"/>
    <!-- Concentric sonic rings ahead -->
    <path d="M 350 150 A 100 100 0 0 1 350 350" fill="none" stroke="#10E76F" stroke-width="10" stroke-linecap="round" filter="url(#f43_glow)"/>
    <path d="M 390 110 A 150 150 0 0 1 390 390" fill="none" stroke="#00F2FE" stroke-width="7" stroke-linecap="round" opacity="0.6"/>
    <path d="M 430 70 A 200 200 0 0 1 430 430" fill="none" stroke="#7928CA" stroke-width="4" stroke-linecap="round" opacity="0.4"/>
    <!-- Ghost Runner 1 (Deep Purple, earliest stride) -->
    <g transform="translate(-100, 0)" opacity="0.25">
      <circle cx="270" cy="145" r="26" fill="#7928CA"/>
      <path d="M 245 180 L 290 240 L 235 285 L 210 230 Z" fill="#7928CA"/>
      <path d="M 280 205 L 340 235" stroke="#7928CA" stroke-width="18" stroke-linecap="round"/>
      <path d="M 245 280 L 305 320 L 325 390" stroke="#7928CA" stroke-width="22" stroke-linecap="round"/>
      <path d="M 225 280 L 170 325 L 125 355" stroke="#7928CA" stroke-width="20" stroke-linecap="round"/>
    </g>
    <!-- Ghost Runner 2 (Electric Cyan, mid stride) -->
    <g transform="translate(-50, 0)" opacity="0.55">
      <circle cx="270" cy="145" r="26" fill="#00F2FE"/>
      <path d="M 245 180 L 290 240 L 235 285 L 210 230 Z" fill="#00F2FE"/>
      <path d="M 280 205 L 340 235" stroke="#00F2FE" stroke-width="18" stroke-linecap="round"/>
      <path d="M 245 280 L 305 320 L 325 390" stroke="#00F2FE" stroke-width="22" stroke-linecap="round"/>
      <path d="M 225 280 L 170 325 L 125 355" stroke="#00F2FE" stroke-width="20" stroke-linecap="round"/>
    </g>
    <!-- Lead Runner (Neon Volt + White highlight, 100% full energy) -->
    <g fill="url(#g43_lead)" filter="url(#f43_glow)">
      <circle cx="270" cy="145" r="28"/>
      <path d="M 245 180 L 290 240 L 235 285 L 210 230 Z"/>
      <path d="M 280 205 L 340 235 L 355 220" fill="none" stroke="url(#g43_lead)" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 240 210 L 180 235 L 165 260" fill="none" stroke="url(#g43_lead)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 245 280 L 305 320 L 325 390" fill="none" stroke="url(#g43_lead)" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 225 280 L 170 325 L 125 355" fill="none" stroke="url(#g43_lead)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Inner crisp white core -->
      <circle cx="270" cy="145" r="14" fill="#FFFFFF"/>
    </g>
'''
)

# 44: Ikona 1D — Zvukové pásy & Frekvencie (Audio Ribbon Sprint)
add_icon(
    44, "Ikona 1D — Zvukové pásy & Frekvencie", "Variant 1D: Audio Ribbon Sprint", "icon1_variants",
    ["variant ikony 1", "zvukové pásy", "ekvalizér", "oranžová", "dynamika"],
    '''    <defs>
      <linearGradient id="g44_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#140A10"/>
        <stop offset="100%" stop-color="#040105"/>
      </linearGradient>
      <linearGradient id="g44_ribbon" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#FF3366"/>
        <stop offset="50%" stop-color="#FF9F1C"/>
        <stop offset="100%" stop-color="#10E76F"/>
      </linearGradient>
      <linearGradient id="g44_runner" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FFFFFF"/>
        <stop offset="100%" stop-color="#00F2FE"/>
      </linearGradient>
      <filter id="f44_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="7" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g44_bg)"/>
    <!-- Vibrating vertical audio bars curving like stadium tunnel -->
    <g fill="url(#g44_ribbon)" filter="url(#f44_glow)" opacity="0.85">
      <rect x="70" y="240" width="14" height="120" rx="7"/>
      <rect x="95" y="190" width="14" height="180" rx="7"/>
      <rect x="120" y="140" width="14" height="250" rx="7"/>
      <rect x="145" y="100" width="14" height="310" rx="7"/>
      <rect x="360" y="90" width="14" height="330" rx="7"/>
      <rect x="385" y="130" width="14" height="270" rx="7"/>
      <rect x="410" y="180" width="14" height="200" rx="7"/>
      <rect x="435" y="230" width="14" height="130" rx="7"/>
    </g>
    <!-- Horizontal audio sine wave baseline -->
    <path d="M 50 420 Q 150 380, 256 420 T 462 420" fill="none" stroke="#FF9F1C" stroke-width="4" stroke-linecap="round" opacity="0.6"/>
    <!-- Runner bursting through center gap -->
    <g fill="url(#g44_runner)" filter="url(#f44_glow)">
      <circle cx="265" cy="135" r="28"/>
      <path d="M 240 170 L 285 230 L 230 275 L 205 220 Z"/>
      <path d="M 275 195 L 335 225 L 350 210" fill="none" stroke="url(#g44_runner)" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 235 200 L 175 225 L 160 250" fill="none" stroke="url(#g44_runner)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 240 270 L 300 310 L 320 380" fill="none" stroke="url(#g44_runner)" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 220 270 L 165 315 L 120 345" fill="none" stroke="url(#g44_runner)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <!-- Acoustic pulse ripples bursting outward -->
    <circle cx="265" cy="240" r="130" fill="none" stroke="#00F2FE" stroke-width="3" stroke-dasharray="14 14" opacity="0.4"/>
'''
)

# 45: Ikona 1E — Štadiónový sonický tunel (3D Sonic Gate Tunnel)
add_icon(
    45, "Ikona 1E — Štadiónový sonický tunel", "Variant 1E: 3D Sonic Gate Tunnel", "icon1_variants",
    ["variant ikony 1", "tunel", "štadión", "brány", "perspektíva", "3d"],
    '''    <defs>
      <linearGradient id="g45_bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#05101E"/>
        <stop offset="100%" stop-color="#010307"/>
      </linearGradient>
      <linearGradient id="g45_gate" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#10E76F"/>
        <stop offset="60%" stop-color="#00F2FE"/>
        <stop offset="100%" stop-color="#FFFFFF"/>
      </linearGradient>
      <filter id="f45_glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="8" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
    </defs>
    <rect width="512" height="512" fill="url(#g45_bg)"/>
    <!-- Concentric 3D Stadium Sonic Gates in perspective depth -->
    <!-- Gate 1 (deep horizon) -->
    <ellipse cx="256" cy="210" rx="60" ry="100" fill="none" stroke="#00F2FE" stroke-width="4" stroke-opacity="0.3"/>
    <!-- Gate 2 (mid) -->
    <ellipse cx="256" cy="225" rx="110" ry="145" fill="none" stroke="#00F2FE" stroke-width="6" stroke-opacity="0.5"/>
    <!-- Gate 3 (foreground) -->
    <ellipse cx="256" cy="240" rx="170" ry="195" fill="none" stroke="url(#g45_gate)" stroke-width="12" stroke-linecap="round" filter="url(#f45_glow)"/>
    <!-- Running track perspective floor -->
    <polygon points="60,460 452,460 310,240 202,240" fill="#0C1B33" fill-opacity="0.6"/>
    <line x1="256" y1="460" x2="256" y2="240" stroke="#10E76F" stroke-width="6" stroke-dasharray="16 12" filter="url(#f45_glow)"/>
    <!-- Runner bursting straight out through the main gate -->
    <g fill="#FFFFFF" filter="url(#f45_glow)">
      <!-- Head -->
      <circle cx="256" cy="155" r="26" fill="#10E76F"/>
      <!-- Torso -->
      <path d="M 235 185 L 277 185 L 265 260 L 247 260 Z" fill="#FFFFFF"/>
      <!-- Pumping Arms in frontal stride -->
      <path d="M 235 195 L 180 230 L 170 260" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 277 195 L 330 220 L 340 190" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Legs bursting forward -->
      <path d="M 247 260 L 220 330 L 205 400" fill="none" stroke="#10E76F" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 265 260 L 300 310 L 325 365" fill="none" stroke="#00F2FE" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <!-- Ground impact sound wave -->
    <ellipse cx="256" cy="420" rx="150" ry="24" fill="none" stroke="#10E76F" stroke-width="5" stroke-opacity="0.7" filter="url(#f45_glow)"/>
'''
)

# Build HTML template
icons_json = json.dumps(icons, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Beep Test App — 40 Návrhov SVG Ikon</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-dark: #090D16;
      --card-dark: #131A29;
      --card-hover: #1A2438;
      --border-subtle: #24324D;
      --neon-volt: #10E76F;
      --electric-cyan: #00F2FE;
      --pulse-amber: #FF9F1C;
      --danger-rose: #FF3366;
      --text-white: #FFFFFF;
      --text-muted: #94A3B8;
      --font-main: 'Outfit', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: var(--bg-dark);
      color: var(--text-white);
      font-family: var(--font-main);
      min-height: 100vh;
      line-height: 1.5;
      padding-bottom: 80px;
    }}

    /* Header */
    header {{
      background: linear-gradient(180deg, #101726 0%, rgba(9, 13, 22, 0.95) 100%);
      border-bottom: 1px solid var(--border-subtle);
      padding: 32px 24px 24px;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(16px);
    }}

    .header-container {{
      max-width: 1440px;
      margin: 0 auto;
    }}

    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 24px;
    }}

    .app-title-group {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .badge-live {{
      background: rgba(16, 231, 111, 0.15);
      border: 1px solid var(--neon-volt);
      color: var(--neon-volt);
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
    }}

    h1 {{
      font-size: 28px;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(90deg, #FFFFFF, var(--electric-cyan));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: 14px;
      margin-top: 2px;
    }}

    .stats-bar {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}

    .stat-pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 6px 14px;
      font-size: 13px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .stat-pill strong {{
      color: var(--electric-cyan);
      font-size: 15px;
    }}

    /* Controls Bar */
    .controls-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      justify-content: space-between;
      align-items: center;
    }}

    .filter-chips {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .filter-btn {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
    }}

    .filter-btn:hover {{
      background: rgba(255, 255, 255, 0.1);
      color: var(--text-white);
      border-color: #3b4e75;
    }}

    .filter-btn.active {{
      background: var(--electric-cyan);
      color: #03060C;
      border-color: var(--electric-cyan);
      font-weight: 700;
      box-shadow: 0 0 16px rgba(0, 242, 254, 0.35);
    }}

    .view-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .search-input {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 8px 16px;
      color: var(--text-white);
      font-size: 13px;
      font-family: inherit;
      outline: none;
      width: 200px;
      transition: border-color 0.2s;
    }}

    .search-input:focus {{
      border-color: var(--electric-cyan);
    }}

    .mode-select {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-white);
      padding: 8px 14px;
      border-radius: 12px;
      font-size: 13px;
      font-family: inherit;
      cursor: pointer;
      outline: none;
    }}

    /* Main Container */
    main {{
      max-width: 1440px;
      margin: 32px auto 0;
      padding: 0 24px;
    }}

    /* Grid Layouts */
    .icon-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 24px;
    }}

    .icon-grid.compact {{
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 16px;
    }}

    /* Icon Card */
    .icon-card {{
      background: var(--card-dark);
      border: 1px solid var(--border-subtle);
      border-radius: 20px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      cursor: pointer;
    }}

    .icon-card:hover {{
      transform: translateY(-4px);
      border-color: #3a5078;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
      background: var(--card-hover);
    }}

    .icon-card.favorited {{
      border-color: var(--pulse-amber);
    }}

    .card-top-meta {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}

    .icon-num {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: var(--electric-cyan);
      background: rgba(0, 242, 254, 0.1);
      padding: 2px 8px;
      border-radius: 6px;
    }}

    .fav-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 18px;
      transition: transform 0.2s, color 0.2s;
    }}

    .fav-btn:hover {{
      transform: scale(1.2);
      color: var(--pulse-amber);
    }}

    .icon-card.favorited .fav-btn {{
      color: var(--pulse-amber);
    }}

    /* Preview Canvas Wrapper */
    .preview-canvas-wrapper {{
      width: 160px;
      height: 160px;
      margin: 8px 0 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      filter: drop-shadow(0 12px 24px rgba(0, 0, 0, 0.5));
      transition: transform 0.2s;
    }}

    .icon-grid.compact .preview-canvas-wrapper {{
      width: 100px;
      height: 100px;
      margin: 4px 0 12px;
    }}

    .icon-card:hover .preview-canvas-wrapper {{
      transform: scale(1.04);
    }}

    .icon-canvas {{
      width: 100%;
      height: 100%;
      border-radius: 22.5%;
      overflow: hidden;
      display: block;
      transition: border-radius 0.2s;
    }}

    /* Shape variations */
    .shape-circle .icon-canvas {{
      border-radius: 50% !important;
    }}
    .shape-squircle .icon-canvas {{
      border-radius: 22.5% !important;
    }}
    .shape-square .icon-canvas {{
      border-radius: 12% !important;
    }}

    /* Card Details */
    .card-info {{
      width: 100%;
      text-align: center;
      margin-top: 4px;
    }}

    .icon-title-sk {{
      font-size: 16px;
      font-weight: 700;
      color: var(--text-white);
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .icon-title-en {{
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 12px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .tag-pills {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 4px;
      margin-bottom: 16px;
    }}

    .tag-pill {{
      font-size: 10px;
      background: rgba(255, 255, 255, 0.05);
      color: #94A3B8;
      padding: 2px 8px;
      border-radius: 4px;
    }}

    /* Card Actions */
    .card-actions {{
      width: 100%;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-top: auto;
    }}

    .action-btn {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-white);
      padding: 8px 12px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
      font-family: inherit;
    }}

    .action-btn:hover {{
      background: var(--electric-cyan);
      color: #03060C;
      border-color: var(--electric-cyan);
    }}

    .btn-download:hover {{
      background: var(--neon-volt);
      border-color: var(--neon-volt);
      color: #03060C;
    }}

    /* Phone Mockup Screen */
    .phone-mockup-section {{
      display: none;
      justify-content: center;
      padding: 40px 0;
    }}

    .phone-frame {{
      width: 375px;
      height: 760px;
      background: #000;
      border-radius: 54px;
      border: 12px solid #1E293B;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 0 2px #334155;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .phone-wallpaper {{
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 20%, #1e3a8a 0%, #090d16 80%);
      z-index: 1;
    }}

    .phone-notch {{
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 150px;
      height: 28px;
      background: #1E293B;
      border-bottom-left-radius: 18px;
      border-bottom-right-radius: 18px;
      z-index: 10;
    }}

    .phone-screen-content {{
      position: relative;
      z-index: 2;
      padding: 48px 24px 24px;
      display: flex;
      flex-direction: column;
      height: 100%;
    }}

    .phone-clock {{
      text-align: center;
      font-size: 44px;
      font-weight: 300;
      margin: 16px 0 32px;
      letter-spacing: -1px;
    }}

    .phone-icons-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px 14px;
    }}

    .phone-app-item {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}

    .phone-app-icon-wrap {{
      width: 58px;
      height: 58px;
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
      transition: transform 0.2s;
    }}

    .phone-app-item:hover .phone-app-icon-wrap {{
      transform: scale(1.1);
    }}

    .phone-app-name {{
      font-size: 11px;
      color: rgba(255, 255, 255, 0.9);
      text-align: center;
      max-width: 64px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}

    .phone-dock {{
      margin-top: auto;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(20px);
      border-radius: 30px;
      padding: 14px;
      display: flex;
      justify-content: space-around;
    }}

    /* Modal / Inspector */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(4, 8, 16, 0.85);
      backdrop-filter: blur(12px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}

    .modal-overlay.open {{
      display: flex;
    }}

    .modal-card {{
      background: var(--card-dark);
      border: 1px solid var(--border-subtle);
      border-radius: 28px;
      max-width: 800px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 32px;
      position: relative;
      box-shadow: 0 24px 64px rgba(0, 0, 0, 0.8);
    }}

    .modal-close {{
      position: absolute;
      top: 24px;
      right: 24px;
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #FFF;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .modal-body {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 32px;
      margin-top: 12px;
    }}

    @media (max-width: 768px) {{
      .modal-body {{
        grid-template-columns: 1fr;
      }}
    }}

    .modal-preview-box {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
    }}

    .modal-canvas-wrap {{
      width: 256px;
      height: 256px;
      border-radius: 22.5%;
      overflow: hidden;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
    }}

    .code-box {{
      background: #080D1A;
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 16px;
      font-family: var(--font-mono);
      font-size: 11px;
      max-height: 240px;
      overflow: auto;
      color: #A5B4FC;
      white-space: pre-wrap;
      word-break: break-all;
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 32px;
      right: 32px;
      background: var(--neon-volt);
      color: #03060C;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(16, 231, 111, 0.4);
      z-index: 2000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-container">
      <div class="header-top">
        <div class="app-title-group">
          <div>
            <div style="display: flex; align-items: center; gap: 10px;">
              <h1>Beep Test — 45 Návrhov SVG Ikon</h1>
              <span class="badge-live">Katalóg</span>
            </div>
            <p class="subtitle">Vyberte si ideálnu ikonu aplikácie (+ pridaných 5 špeciálnych variantov Ikony 1). Kliknutím skopírujete SVG kód alebo stiahnete súbor.</p>
          </div>
        </div>

        <div class="stats-bar">
          <div class="stat-pill">Spolu: <strong id="totalCount">40</strong></div>
          <div class="stat-pill">Obľúbené: <strong id="favCount" style="color: var(--pulse-amber);">0</strong></div>
          <button id="exportFavsBtn" class="action-btn" style="background: rgba(255, 159, 28, 0.15); border-color: var(--pulse-amber); color: var(--pulse-amber);">
            ★ Vyexportovať obľúbené
          </button>
        </div>
      </div>

      <!-- Controls & Filter bar -->
      <div class="controls-bar">
        <div class="filter-chips">
          <button class="filter-btn active" data-filter="all">Všetky (45)</button>
          <button class="filter-btn" data-filter="icon1_variants" style="border-color: var(--neon-volt); color: var(--neon-volt); font-weight: 700;">⚡ Varianty Ikony 1 (6)</button>
          <button class="filter-btn" data-filter="runners">Bežci & Pohyb (6)</button>
          <button class="filter-btn" data-filter="cones">Kužele & Trasa (8)</button>
          <button class="filter-btn" data-filter="audio">Zvuk & Radar (7)</button>
          <button class="filter-btn" data-filter="stopwatch">Stopky & Časovače (5)</button>
          <button class="filter-btn" data-filter="badges">Monogramy & Logá (7)</button>
          <button class="filter-btn" data-filter="cardio">Kardio & VO2 (4)</button>
          <button class="filter-btn" data-filter="futuristic">High-Tech (3)</button>
          <button class="filter-btn" data-filter="favs">★ Obľúbené</button>
        </div>

        <div class="view-actions">
          <input type="text" id="searchInput" class="search-input" placeholder="Hľadať ikonu...">
          
          <select id="shapeSelect" class="mode-select">
            <option value="shape-squircle">Tvar: Squircle (iOS)</option>
            <option value="shape-circle">Tvar: Kruh (Android)</option>
            <option value="shape-square">Tvar: Zaoblený štvorec</option>
          </select>

          <select id="viewModeSelect" class="mode-select">
            <option value="grid">Zobrazenie: Mriežka</option>
            <option value="compact">Zobrazenie: Kompaktné</option>
            <option value="phone">Zobrazenie: Telefón mockup</option>
          </select>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main>
    <!-- Standard Grid View -->
    <div id="iconGrid" class="icon-grid shape-squircle">
      <!-- Icons rendered via JavaScript -->
    </div>

    <!-- Phone Mockup Screen View -->
    <div id="phoneMockupSection" class="phone-mockup-section">
      <div class="phone-frame">
        <div class="phone-wallpaper"></div>
        <div class="phone-notch"></div>
        <div class="phone-screen-content">
          <div class="phone-clock">09:41</div>
          <div id="phoneIconsGrid" class="phone-icons-grid">
            <!-- First 16 icons rendered here for home-screen context -->
          </div>
          <div class="phone-dock">
            <div style="width: 48px; height: 48px; border-radius: 12px; background: #22c55e; display: flex; align-items: center; justify-content: center; font-size: 20px;">📞</div>
            <div style="width: 48px; height: 48px; border-radius: 12px; background: #0ea5e9; display: flex; align-items: center; justify-content: center; font-size: 20px;">✉️</div>
            <div style="width: 48px; height: 48px; border-radius: 12px; background: #64748b; display: flex; align-items: center; justify-content: center; font-size: 20px;">⚙️</div>
            <div id="phoneDockApp" style="width: 48px; height: 48px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.5);">
              <!-- Selected Beep Test Icon in Dock -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

  <!-- Inspector / Details Modal -->
  <div id="modalOverlay" class="modal-overlay">
    <div class="modal-card">
      <button id="modalClose" class="modal-close">✕</button>
      <div class="modal-header">
        <span id="modalNum" class="icon-num">#01</span>
        <h2 id="modalTitleSk" style="font-size: 24px; font-weight: 800; margin-top: 6px;">Názov ikony</h2>
        <p id="modalTitleEn" style="color: var(--text-muted); font-size: 14px;">Title in English</p>
      </div>

      <div class="modal-body">
        <div class="modal-preview-box">
          <div id="modalCanvasWrap" class="modal-canvas-wrap shape-squircle">
            <!-- Full SVG -->
          </div>
          <div style="display: flex; gap: 8px; width: 100%;">
            <button id="modalCopyBtn" class="action-btn" style="flex: 1; background: var(--electric-cyan); color: #000; font-weight: 700;">
              📋 Kopírovať SVG
            </button>
            <button id="modalDownloadBtn" class="action-btn btn-download" style="flex: 1;">
              ⬇ Stiahnuť .SVG
            </button>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 16px;">
          <div>
            <h4 style="font-size: 13px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); margin-bottom: 6px;">Kľúčové prvky & Tagy</h4>
            <div id="modalTags" class="tag-pills" style="justify-content: flex-start;"></div>
          </div>
          <div>
            <h4 style="font-size: 13px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); margin-bottom: 6px;">SVG Zdrojový kód (veľkosť 512x512)</h4>
            <div id="modalCodeBox" class="code-box"></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div id="toast" class="toast">SVG skopírované do schránky!</div>

  <script>
    const iconsData = {icons_json};
    let favorites = JSON.parse(localStorage.getItem('beep_icon_favs') || '[]');
    let currentFilter = 'all';
    let searchQuery = '';
    let currentShape = 'shape-squircle';

    const iconGrid = document.getElementById('iconGrid');
    const phoneIconsGrid = document.getElementById('phoneIconsGrid');
    const phoneDockApp = document.getElementById('phoneDockApp');
    const phoneMockupSection = document.getElementById('phoneMockupSection');
    const totalCountEl = document.getElementById('totalCount');
    const favCountEl = document.getElementById('favCount');
    const toastEl = document.getElementById('toast');
    const searchInput = document.getElementById('searchInput');
    const shapeSelect = document.getElementById('shapeSelect');
    const viewModeSelect = document.getElementById('viewModeSelect');

    // Modal elements
    const modalOverlay = document.getElementById('modalOverlay');
    const modalClose = document.getElementById('modalClose');
    const modalNum = document.getElementById('modalNum');
    const modalTitleSk = document.getElementById('modalTitleSk');
    const modalTitleEn = document.getElementById('modalTitleEn');
    const modalCanvasWrap = document.getElementById('modalCanvasWrap');
    const modalTags = document.getElementById('modalTags');
    const modalCodeBox = document.getElementById('modalCodeBox');
    const modalCopyBtn = document.getElementById('modalCopyBtn');
    const modalDownloadBtn = document.getElementById('modalDownloadBtn');
    let activeModalIcon = null;

    function showToast(msg) {{
      toastEl.textContent = msg;
      toastEl.classList.add('show');
      setTimeout(() => toastEl.classList.remove('show'), 2400);
    }}

    function toggleFavorite(id, e) {{
      if (e) e.stopPropagation();
      if (favorites.includes(id)) {{
        favorites = favorites.filter(f => f !== id);
      }} else {{
        favorites.push(id);
      }}
      localStorage.setItem('beep_icon_favs', JSON.stringify(favorites));
      updateFavCount();
      updateFilterCounts();
      renderIcons();
    }}

    function updateFavCount() {{
      favCountEl.textContent = favorites.length;
    }}

    function copySvg(svgCode, e) {{
      if (e) e.stopPropagation();
      navigator.clipboard.writeText(svgCode).then(() => {{
        showToast('✓ SVG kód skopírovaný do schránky!');
      }}).catch(() => {{
        // Fallback
        const ta = document.createElement('textarea');
        ta.value = svgCode;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast('✓ SVG kód skopírovaný do schránky!');
      }});
    }}

    function downloadSvg(id, svgCode, e) {{
      if (e) e.stopPropagation();
      const blob = new Blob([svgCode], {{ type: 'image/svg+xml;charset=utf-8' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `beep_test_icon_${{String(id).padStart(2, '0')}}.svg`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast(`✓ Stiahnutá ikona #${{String(id).padStart(2, '0')}}`);
    }}

    function openModal(item) {{
      activeModalIcon = item;
      modalNum.textContent = `#${{String(item.id).padStart(2, '0')}}`;
      modalTitleSk.textContent = item.title_sk;
      modalTitleEn.textContent = item.title_en;
      modalCanvasWrap.innerHTML = item.svg;
      modalCanvasWrap.className = `modal-canvas-wrap ${{currentShape}}`;
      modalCodeBox.textContent = item.svg;
      
      modalTags.innerHTML = item.tags.map(t => `<span class="tag-pill">#${{t}}</span>`).join('');
      modalOverlay.classList.add('open');
    }}

    modalClose.addEventListener('click', () => modalOverlay.classList.remove('open'));
    modalOverlay.addEventListener('click', (e) => {{
      if (e.target === modalOverlay) modalOverlay.classList.remove('open');
    }});

    modalCopyBtn.addEventListener('click', () => {{
      if (activeModalIcon) copySvg(activeModalIcon.svg);
    }});

    modalDownloadBtn.addEventListener('click', () => {{
      if (activeModalIcon) downloadSvg(activeModalIcon.id, activeModalIcon.svg);
    }});

    // Render Grid
    function renderIcons() {{
      const filtered = iconsData.filter(item => {{
        const matchesFilter = (currentFilter === 'all') 
          || (currentFilter === 'favs' && favorites.includes(item.id))
          || (currentFilter === 'icon1_variants' && (item.id === 1 || item.category === 'icon1_variants'))
          || (item.category === currentFilter);
        
        const q = searchQuery.toLowerCase().trim();
        const matchesSearch = !q 
          || item.title_sk.toLowerCase().includes(q)
          || item.title_en.toLowerCase().includes(q)
          || item.tags.some(t => t.toLowerCase().includes(q))
          || String(item.id).includes(q);

        return matchesFilter && matchesSearch;
      }});

      totalCountEl.textContent = filtered.length;

      iconGrid.innerHTML = filtered.map(item => {{
        const isFav = favorites.includes(item.id);
        return `
          <div class="icon-card ${{isFav ? 'favorited' : ''}}" onclick="openModal(iconsData[${{item.id - 1}}])">
            <div class="card-top-meta">
              <span class="icon-num">#${{String(item.id).padStart(2, '0')}}</span>
              <button class="fav-btn" onclick="toggleFavorite(${{item.id}}, event)" title="Pridať do obľúbených">
                ${{isFav ? '★' : '☆'}}
              </button>
            </div>
            
            <div class="preview-canvas-wrapper">
              <div class="icon-canvas">
                ${{item.svg}}
              </div>
            </div>

            <div class="card-info">
              <h3 class="icon-title-sk">${{item.title_sk}}</h3>
              <p class="icon-title-en">${{item.title_en}}</p>
              <div class="tag-pills">
                ${{item.tags.slice(0, 3).map(t => `<span class="tag-pill">#${{t}}</span>`).join('')}}
              </div>
            </div>

            <div class="card-actions">
              <button class="action-btn" onclick="copySvg(iconsData[${{item.id - 1}}].svg, event)">
                📋 Kopírovať
              </button>
              <button class="action-btn btn-download" onclick="downloadSvg(${{item.id}}, iconsData[${{item.id - 1}}].svg, event)">
                ⬇ Stiahnuť
              </button>
            </div>
          </div>
        `;
      }}).join('');

      renderPhoneMockup();
    }}

    function renderPhoneMockup() {{
      // Render first 12 icons in the mockup
      const displayIcons = iconsData.slice(0, 16);
      phoneIconsGrid.innerHTML = displayIcons.map(item => `
        <div class="phone-app-item" onclick="selectPhoneDockIcon(${{item.id}})" title="${{item.title_sk}}">
          <div class="phone-app-icon-wrap">
            ${{item.svg}}
          </div>
          <span class="phone-app-name">Beep #${{item.id}}</span>
        </div>
      `).join('');

      // Dock app defaults to icon #1 or active favorite
      const dockIcon = favorites.length > 0 ? iconsData[favorites[0] - 1] : iconsData[0];
      phoneDockApp.innerHTML = dockIcon.svg;
    }}

    function selectPhoneDockIcon(id) {{
      phoneDockApp.innerHTML = iconsData[id - 1].svg;
      showToast(`Ikona #${{String(id).padStart(2, '0')}} umiestnená do Docku`);
    }}

    // Filter Buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.dataset.filter;
        renderIcons();
      }});
    }});

    // Search Input
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value;
      renderIcons();
    }});

    // Shape Switcher
    shapeSelect.addEventListener('change', (e) => {{
      currentShape = e.target.value;
      iconGrid.classList.remove('shape-squircle', 'shape-circle', 'shape-square');
      iconGrid.classList.add(currentShape);
    }});

    // View Mode Switcher
    viewModeSelect.addEventListener('change', (e) => {{
      const val = e.target.value;
      if (val === 'compact') {{
        iconGrid.style.display = 'grid';
        iconGrid.classList.add('compact');
        phoneMockupSection.style.display = 'none';
      }} else if (val === 'phone') {{
        iconGrid.style.display = 'none';
        phoneMockupSection.style.display = 'flex';
      }} else {{
        iconGrid.style.display = 'grid';
        iconGrid.classList.remove('compact');
        phoneMockupSection.style.display = 'none';
      }}
    }});

    // Export favorites
    document.getElementById('exportFavsBtn').addEventListener('click', () => {{
      if (favorites.length === 0) {{
        alert('Nemáte vybrané žiadne obľúbené ikony. Kliknite na hviezdičku (☆) pri ikonách, ktoré sa vám páčia!');
        return;
      }}
      const favItems = iconsData.filter(i => favorites.includes(i.id));
      const summary = favItems.map(i => `#${{String(i.id).padStart(2, '0')}} - ${{i.title_sk}} (${{i.title_en}})`).join('\\n');
      navigator.clipboard.writeText(summary).then(() => {{
        showToast('✓ Zoznam vybraných ikon skopírovaný do schránky!');
        alert('Skopírované do schránky:\\n\\n' + summary);
      }});
    }});

    function updateFilterCounts() {{
      const counts = {{ all: iconsData.length }};
      iconsData.forEach(item => {{
        counts[item.category] = (counts[item.category] || 0) + 1;
      }});
      counts['icon1_variants'] = (counts['icon1_variants'] || 0) + 1; // Includes #01 original
      document.querySelectorAll('.filter-btn').forEach(btn => {{
        const f = btn.dataset.filter;
        const label = btn.dataset.label || btn.textContent.split(' (')[0];
        btn.dataset.label = label;
        if (f === 'all') {{
          btn.textContent = `${{label}} (${{iconsData.length}})`;
        }} else if (f === 'favs') {{
          btn.textContent = `${{label}} (${{favorites.length}})`;
        }} else {{
          btn.textContent = `${{label}} (${{counts[f] || 0}})`;
        }}
      }});
    }}

    // Init
    updateFavCount();
    updateFilterCounts();
    renderIcons();
  </script>
</body>
</html>
'''

output_path = r"c:\projects\AI2\flutter-beep-test\icon_preview.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Successfully generated {output_path} with {len(icons)} icons!")
