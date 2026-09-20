import subprocess
import os

media_dir = "/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа"
os.makedirs(media_dir, exist_ok=True)

# ----------------- DIAGRAM 1 FIX -----------------
svg1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <style>
      .bg { fill: #131722; }
      .card { fill: #1e2433; stroke: #334155; stroke-width: 1.5; rx: 8; }
      .title { font-family: 'DejaVu Sans', sans-serif; font-size: 19px; font-weight: bold; fill: #f8fafc; }
      .subtitle { font-family: 'DejaVu Sans', sans-serif; font-size: 13px; fill: #94a3b8; }
      .card-title { font-family: 'DejaVu Sans', sans-serif; font-size: 15px; font-weight: bold; }
      .label { font-family: 'DejaVu Sans', sans-serif; font-size: 12.5px; fill: #e2e8f0; }
      .label-sm { font-family: 'DejaVu Sans', sans-serif; font-size: 11.5px; fill: #94a3b8; }
      .math { font-family: 'DejaVu Serif', serif; font-style: italic; font-size: 14.5px; fill: #ffffff; }
      .math-sm { font-family: 'DejaVu Serif', serif; font-style: italic; font-size: 12px; fill: #cbd5e1; }
      .math-bold { font-family: 'DejaVu Serif', serif; font-weight: bold; font-size: 15px; fill: #ffffff; }
      .axis { stroke: #64748b; stroke-width: 2; }
      .tick { stroke: #64748b; stroke-width: 1.5; }
      .v-point { fill: #ec4899; stroke: #f472b6; stroke-width: 1.5; }
      .shift-1 { fill: #38bdf8; stroke: #0284c7; stroke-width: 1.5; }
      .shift-2 { fill: #34d399; stroke: #059669; stroke-width: 1.5; }
      .shift-3 { fill: #fbbf24; stroke: #d97706; stroke-width: 1.5; }
      .badge-pink { fill: #831843; stroke: #db2777; stroke-width: 1; rx: 6; }
      .badge-blue { fill: #0c4a6e; stroke: #0284c7; stroke-width: 1; rx: 6; }
      .badge-green { fill: #064e3b; stroke: #059669; stroke-width: 1; rx: 6; }
      .badge-amber { fill: #78350f; stroke: #d97706; stroke-width: 1; rx: 6; }
    </style>
    <marker id="axis-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b"/>
    </marker>
  </defs>

  <rect width="1000" height="600" class="bg" rx="12"/>

  <!-- Top Title -->
  <text x="35" y="36" class="title">Конструкция множества Витали и его рациональных сдвигов</text>
  <text x="35" y="58" class="subtitle">Пример множества, неизмеримого относительно счётно-аддитивной сдвиг-инвариантной меры Лебега</text>

  <!-- Left Card: Equivalence Classes & Choice -->
  <rect x="30" y="78" width="460" height="275" class="card"/>
  <text x="45" y="105" class="card-title" style="fill: #ec4899;">1. Факторизация отрезка [0; 1] по ℝ/ℚ</text>
  <text x="45" y="128" class="label">Отношение эквивалентности на [0; 1]:</text>
  <text x="120" y="152" class="math-bold" style="font-size: 16px; fill: #f472b6;">x ~ y  ⇔  x - y ∈ ℚ</text>

  <text x="45" y="180" class="label">Отрезок распадается на несчётное число дизъюнктных классов:</text>
  <text x="55" y="202" class="math" style="fill: #e2e8f0; font-size: 14px;">[0; 1] = ⨆_α C_α,   каждый класс C_α счётный и плотный</text>

  <!-- Choice Axiom Box -->
  <rect x="45" y="220" width="430" height="115" class="badge-pink"/>
  <text x="58" y="242" class="math-bold" style="fill: #fbcfe8;">Аксиома выбора (ZFC):</text>
  <text x="58" y="263" class="label" style="fill: #fdf2f8; font-size: 12px;">Из каждого класса C_α выбираем ровно по одной точке v_α ∈ [0; 1]:</text>
  <text x="120" y="295" class="math-bold" style="font-size: 16px; fill: #ffffff;">V = { v_α }_α ⊂ [0; 1]   (Множество Витали)</text>
  <text x="58" y="322" class="label-sm" style="fill: #fbcfe8;">В каждом C_α ровно один представитель, разности v_i - v_j ∉ ℚ</text>

  <!-- Right Card: Disjoint Shifts & Double Inclusion -->
  <rect x="510" y="78" width="460" height="275" class="card"/>
  <text x="525" y="105" class="card-title" style="fill: #38bdf8;">2. Счётное семейство сдвигов  Q = [-1; 1] ∩ ℚ</text>
  
  <!-- Property 1 -->
  <rect x="525" y="122" width="430" height="60" class="badge-blue"/>
  <text x="535" y="141" class="label" style="font-weight: bold; fill: #bae6fd;">(i) Попарная дизъюнктность при q₁ ≠ q₂:</text>
  <text x="535" y="160" class="math-sm" style="fill: #e0f2fe;">(V + q₁) ∩ (V + q₂) = ∅</text>
  <text x="535" y="174" class="label-sm" style="fill: #7dd3fc;">(иначе v₁ + q₁ = v₂ + q₂ ⇒ v₁ - v₂ = q₂ - q₁ ∈ ℚ ⇒ v₁ = v₂)</text>

  <!-- Property 2 -->
  <rect x="525" y="190" width="430" height="52" class="badge-green"/>
  <text x="535" y="209" class="label" style="font-weight: bold; fill: #a7f3d0;">(ii) Двойное включение на числовой оси:</text>
  <text x="535" y="230" class="math-sm" style="fill: #ecfdf5; font-size: 13px;">[0; 1] ⊂ ⨆_{q ∈ Q} (V + q) ⊂ [-1; 2]</text>

  <!-- Contradiction note -->
  <rect x="525" y="250" width="430" height="85" class="badge-amber"/>
  <text x="535" y="269" class="label" style="font-weight: bold; fill: #fde68a;">(iii) Неизмеримость по Лебегу (противоречие):</text>
  <text x="535" y="290" class="math-sm" style="fill: #fffbeb;">1 = μ([0; 1]) ≤ ∑_{q ∈ Q} μ(V + q) = ∑_{q ∈ Q} μ(V) ≤ 3</text>
  <text x="535" y="310" class="label-sm" style="fill: #fed7aa;">• Если μ(V) = 0 ⇒ сумма равна 0  (противоречие 1 ≤ 0)</text>
  <text x="535" y="325" class="label-sm" style="fill: #fed7aa;">• Если μ(V) &gt; 0 ⇒ сумма равна +∞ (противоречие +∞ ≤ 3)</text>

  <!-- Bottom Panel: Visual Real Line Diagram -->
  <rect x="30" y="368" width="940" height="210" class="card"/>
  <text x="45" y="394" class="card-title" style="fill: #f8fafc;">3. Геометрическая схема покрытия на числовой прямой ℝ</text>

  <!-- Number axis -->
  <!-- Coordinates: -1 at x=130, 0 at x=360, 1 at x=590, 2 at x=820 -->
  <line x1="70" y1="475" x2="900" y2="475" class="axis" marker-end="url(#axis-arrow)"/>
  <text x="910" y="480" class="math-bold" style="font-size: 16px;">ℝ</text>

  <!-- Segment [-1; 2] container bracket -->
  <rect x="130" y="445" width="690" height="48" style="fill: rgba(148, 163, 184, 0.08); stroke: #475569; stroke-width: 1; rx: 4;"/>
  <text x="420" y="437" class="label-sm" style="fill: #94a3b8;">Объемлющий отрезок [-1; 2],   длина = 3</text>

  <!-- Segment [0; 1] highlighted -->
  <rect x="360" y="454" width="230" height="32" style="fill: rgba(59, 130, 246, 0.25); stroke: #3b82f6; stroke-width: 2; rx: 3;"/>
  <text x="430" y="505" class="math-bold" style="fill: #60a5fa;">[0; 1],  длина = 1</text>

  <!-- Ticks -->
  <!-- -1 -->
  <line x1="130" y1="468" x2="130" y2="482" class="tick" style="stroke-width: 2; stroke: #f8fafc;"/>
  <text x="122" y="502" class="math-bold">-1</text>

  <!-- 0 -->
  <line x1="360" y1="465" x2="360" y2="485" class="tick" style="stroke-width: 2.5; stroke: #60a5fa;"/>
  <text x="355" y="502" class="math-bold" style="fill: #60a5fa;">0</text>

  <!-- 1 -->
  <line x1="590" y1="465" x2="590" y2="485" class="tick" style="stroke-width: 2.5; stroke: #60a5fa;"/>
  <text x="585" y="502" class="math-bold" style="fill: #60a5fa;">1</text>

  <!-- 2 -->
  <line x1="820" y1="468" x2="820" y2="482" class="tick" style="stroke-width: 2; stroke: #f8fafc;"/>
  <text x="815" y="502" class="math-bold">2</text>

  <!-- Points of V (pink dots inside [0; 1]) -->
  <g>
    <circle cx="380" cy="470" r="4.5" class="v-point"/>
    <circle cx="415" cy="470" r="4.5" class="v-point"/>
    <circle cx="450" cy="470" r="4.5" class="v-point"/>
    <circle cx="495" cy="470" r="4.5" class="v-point"/>
    <circle cx="535" cy="470" r="4.5" class="v-point"/>
    <circle cx="570" cy="470" r="4.5" class="v-point"/>
    <text x="460" y="450" class="math-bold" style="fill: #f472b6;">V</text>
  </g>

  <!-- Shift V + q1 (blue, e.g. q1 = 0.45) -->
  <g>
    <circle cx="485" cy="470" r="3.5" class="shift-1"/>
    <circle cx="520" cy="470" r="3.5" class="shift-1"/>
    <circle cx="555" cy="470" r="3.5" class="shift-1"/>
    <circle cx="600" cy="470" r="3.5" class="shift-1"/>
    <circle cx="640" cy="470" r="3.5" class="shift-1"/>
    <circle cx="675" cy="470" r="3.5" class="shift-1"/>
    <text x="620" y="450" class="math-sm" style="fill: #38bdf8;">V + q₁</text>
  </g>

  <!-- Shift V + q2 (green, e.g. q2 = -0.55) -->
  <g>
    <circle cx="225" cy="470" r="3.5" class="shift-2"/>
    <circle cx="260" cy="470" r="3.5" class="shift-2"/>
    <circle cx="295" cy="470" r="3.5" class="shift-2"/>
    <circle cx="340" cy="470" r="3.5" class="shift-2"/>
    <circle cx="380" cy="470" r="3.5" class="shift-2"/>
    <circle cx="415" cy="470" r="3.5" class="shift-2"/>
    <text x="245" y="450" class="math-sm" style="fill: #34d399;">V + q₂</text>
  </g>

  <!-- Shift V + q3 (amber, e.g. q3 = 0.85) -->
  <g>
    <circle cx="585" cy="470" r="3.5" class="shift-3"/>
    <circle cx="620" cy="470" r="3.5" class="shift-3"/>
    <circle cx="655" cy="470" r="3.5" class="shift-3"/>
    <circle cx="700" cy="470" r="3.5" class="shift-3"/>
    <circle cx="740" cy="470" r="3.5" class="shift-3"/>
    <circle cx="775" cy="470" r="3.5" class="shift-3"/>
    <text x="735" y="450" class="math-sm" style="fill: #fbbf24;">V + q₃</text>
  </g>

  <!-- Legend -->
  <g transform="translate(50, 545)">
    <circle cx="15" cy="15" r="4.5" class="v-point"/>
    <text x="26" y="19" class="label-sm" style="fill: #f472b6;">Точки V</text>

    <circle cx="110" cy="15" r="3.5" class="shift-2"/>
    <text x="121" y="19" class="label-sm" style="fill: #34d399;">V + q₂ (q₂ &lt; 0)</text>

    <circle cx="240" cy="15" r="3.5" class="shift-1"/>
    <text x="251" y="19" class="label-sm" style="fill: #38bdf8;">V + q₁ (q₁ &gt; 0)</text>

    <circle cx="370" cy="15" r="3.5" class="shift-3"/>
    <text x="381" y="19" class="label-sm" style="fill: #fbbf24;">V + q₃ (q₃ → 1)</text>

    <text x="510" y="19" class="label-sm" style="font-weight: bold; fill: #f87171;">Все сдвиги попарно дизъюнктны и вместе покрывают [0; 1]</text>
  </g>
</svg>"""

with open(f"{media_dir}/Лекция 3 рис 1.svg", "w", encoding="utf-8") as f:
    f.write(svg1)
subprocess.run(["rsvg-convert", f"{media_dir}/Лекция 3 рис 1.svg", "-o", f"{media_dir}/Лекция 3 рис 1.png"], check=True)

# ----------------- DIAGRAM 2 FIX -----------------
svg2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 580" width="1000" height="580">
  <defs>
    <style>
      .bg { fill: #131722; }
      .card { fill: #1e2433; stroke: #334155; stroke-width: 1.5; rx: 8; }
      .title { font-family: 'DejaVu Sans', sans-serif; font-size: 19px; font-weight: bold; fill: #f8fafc; }
      .subtitle { font-family: 'DejaVu Sans', sans-serif; font-size: 13px; fill: #94a3b8; }
      .card-title { font-family: 'DejaVu Sans', sans-serif; font-size: 14.5px; font-weight: bold; }
      .label { font-family: 'DejaVu Sans', sans-serif; font-size: 12.5px; fill: #e2e8f0; }
      .label-sm { font-family: 'DejaVu Sans', sans-serif; font-size: 11.5px; fill: #94a3b8; }
      .math { font-family: 'DejaVu Serif', serif; font-style: italic; font-size: 14.5px; fill: #ffffff; }
      .math-sm { font-family: 'DejaVu Serif', serif; font-style: italic; font-size: 12.5px; fill: #cbd5e1; }
      .math-bold { font-family: 'DejaVu Serif', serif; font-weight: bold; font-size: 14.5px; fill: #ffffff; }
      .axis { stroke: #64748b; stroke-width: 2; marker-end: url(#arrow-head); }
      .proj-line { stroke: #818cf8; stroke-width: 1.2; stroke-dasharray: 4,4; }
      .preimage-rect { fill: rgba(16, 185, 129, 0.3); stroke: #10b981; stroke-width: 2; rx: 3; }
      .y-band { fill: rgba(59, 130, 246, 0.15); stroke: #3b82f6; stroke-width: 1; stroke-dasharray: 5,4; }
      .badge-indigo { fill: #1e1b4b; stroke: #6366f1; stroke-width: 1; rx: 4; }
    </style>
    <marker id="arrow-head" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b"/>
    </marker>
  </defs>

  <rect width="1000" height="580" class="bg" rx="12"/>

  <!-- Header -->
  <text x="35" y="36" class="title">Геометрический смысл измеримой функции и эквивалентные прообразы</text>
  <text x="35" y="58" class="subtitle">Функция f : A → ℝ измерима ⇔ прообраз любого промежутка или луча является измеримым множеством</text>

  <!-- Left Panel: Graph & Preimage -->
  <rect x="30" y="78" width="510" height="475" class="card"/>
  <text x="45" y="105" class="card-title" style="fill: #60a5fa;">Прообраз полосы f⁻¹((a; b)) = { x ∈ A : a &lt; f(x) &lt; b }</text>

  <!-- Coordinate system -->
  <line x1="60" y1="465" x2="510" y2="465" class="axis"/>
  <text x="500" y="490" class="math-bold">x</text>

  <line x1="90" y1="485" x2="90" y2="125" class="axis"/>
  <text x="70" y="135" class="math-bold">y</text>

  <!-- Band on Y: (a, b) -->
  <rect x="90" y="200" width="410" height="120" class="y-band"/>
  <line x1="85" y1="200" x2="95" y2="200" stroke="#3b82f6" stroke-width="2"/>
  <text x="70" y="205" class="math-bold" style="fill: #60a5fa;">b</text>

  <line x1="85" y1="320" x2="95" y2="320" stroke="#3b82f6" stroke-width="2"/>
  <text x="70" y="325" class="math-bold" style="fill: #60a5fa;">a</text>

  <text x="425" y="265" class="label-sm" style="fill: #93c5fd;">Полоса (a; b)</text>

  <!-- Curve y = f(x) -->
  <path d="M 100 420 C 140 380, 160 160, 220 170 C 270 180, 290 390, 360 380 C 420 370, 440 160, 485 150" 
        fill="none" stroke="#f59e0b" stroke-width="3"/>
  <text x="455" y="140" class="math-bold" style="fill: #f59e0b;">y = f(x)</text>

  <!-- Projections down to X axis -->
  <line x1="140" y1="320" x2="140" y2="465" class="proj-line"/>
  <line x1="175" y1="200" x2="175" y2="465" class="proj-line"/>
  <line x1="260" y1="200" x2="260" y2="465" class="proj-line"/>
  <line x1="310" y1="320" x2="310" y2="465" class="proj-line"/>
  <line x1="385" y1="320" x2="385" y2="465" class="proj-line"/>
  <line x1="440" y1="200" x2="440" y2="465" class="proj-line"/>

  <!-- Preimage blocks on X axis -->
  <rect x="140" y="457" width="35" height="16" class="preimage-rect"/>
  <rect x="260" y="457" width="50" height="16" class="preimage-rect"/>
  <rect x="385" y="457" width="55" height="16" class="preimage-rect"/>

  <!-- Points on curve -->
  <circle cx="140" cy="320" r="3.5" fill="#3b82f6"/>
  <circle cx="175" cy="200" r="3.5" fill="#3b82f6"/>
  <circle cx="260" cy="200" r="3.5" fill="#3b82f6"/>
  <circle cx="310" cy="320" r="3.5" fill="#3b82f6"/>
  <circle cx="385" cy="320" r="3.5" fill="#3b82f6"/>
  <circle cx="440" cy="200" r="3.5" fill="#3b82f6"/>

  <text x="180" y="508" class="math-bold" style="fill: #34d399; font-size: 15px;">f⁻¹((a; b)) = E₁ ∪ E₂ ∪ E₃ ∈ M</text>
  <text x="150" y="530" class="label-sm">Прообраз полосы — измеримое подмножество области определения A</text>

  <!-- Right Panel: Equivalences Chain -->
  <rect x="560" y="78" width="410" height="475" class="card"/>
  <text x="575" y="105" class="card-title" style="fill: #a78bfa;">Цепочка эквивалентных условий (1 ⇔ ... ⇔ 8)</text>

  <g transform="translate(575, 120)">
    <!-- Item 1 -> 2 -->
    <rect x="0" y="0" width="380" height="45" class="badge-indigo"/>
    <text x="10" y="18" class="label" style="font-weight: bold; fill: #c7d2fe;">(1 ⇒ 2)  Полуинтервал (a; b]:</text>
    <text x="10" y="35" class="math-sm">(a; b] = ⋂_{n=1}^∞ (a; b + 1/n)  ⇒  пересечение</text>

    <!-- Item 2 -> 3 -->
    <rect x="0" y="52" width="380" height="45" class="badge-indigo"/>
    <text x="10" y="70" class="label" style="font-weight: bold; fill: #c7d2fe;">(2 ⇒ 3)  Отрезок [a; b]:</text>
    <text x="10" y="87" class="math-sm">[a; b] = ⋂_{n=1}^∞ (a - 1/n; b]  ⇒  пересечение</text>

    <!-- Item 3 -> 4 -->
    <rect x="0" y="104" width="380" height="45" class="badge-indigo"/>
    <text x="10" y="122" class="label" style="font-weight: bold; fill: #c7d2fe;">(3 ⇒ 4)  Полуинтервал [a; b):</text>
    <text x="10" y="139" class="math-sm">[a; b) = [a; c] ∖ [b; c]  (c &gt; b)  ⇒  разность</text>

    <!-- Item 4 -> 5 -->
    <rect x="0" y="156" width="380" height="45" class="badge-indigo"/>
    <text x="10" y="174" class="label" style="font-weight: bold; fill: #c7d2fe;">(4 ⇒ 5)  Луч [c; +∞):</text>
    <text x="10" y="191" class="math-sm">[c; +∞) = ⋃_{n=1}^∞ [c; c + n)  ⇒  объединение</text>

    <!-- Item 5 -> 6 -->
    <rect x="0" y="208" width="380" height="45" class="badge-indigo"/>
    <text x="10" y="226" class="label" style="font-weight: bold; fill: #c7d2fe;">(5 ⇒ 6)  Открытый луч (c; +∞):</text>
    <text x="10" y="243" class="math-sm">(c; +∞) = ⋃_{n=1}^∞ [c + 1/n; +∞)  ⇒  объединение</text>

    <!-- Item 6 -> 7 -->
    <rect x="0" y="260" width="380" height="45" class="badge-indigo"/>
    <text x="10" y="278" class="label" style="font-weight: bold; fill: #c7d2fe;">(6 ⇒ 7)  Луч (-∞; c]:</text>
    <text x="10" y="295" class="math-sm">(-∞; c] = ℝ ∖ (c; +∞)  ⇒  дополнение (A ∖ f⁻¹)</text>

    <!-- Item 7 -> 8 -->
    <rect x="0" y="312" width="380" height="45" class="badge-indigo"/>
    <text x="10" y="330" class="label" style="font-weight: bold; fill: #c7d2fe;">(7 ⇒ 8)  Открытый луч (-∞; c):</text>
    <text x="10" y="347" class="math-sm">(-∞; c) = ⋃_{n=1}^∞ (-∞; c - 1/n]  ⇒  объединение</text>

    <!-- Item 8 -> 1 -->
    <rect x="0" y="364" width="380" height="45" class="badge-indigo"/>
    <text x="10" y="382" class="label" style="font-weight: bold; fill: #c7d2fe;">(8 ⇒ 1)  Возврат к интервалу (a; b):</text>
    <text x="10" y="399" class="math-sm">(a; b) = (-∞; b) ∖ ⋂_{n=1}^∞ (-∞; a + 1/n) ∈ M</text>
  </g>
</svg>"""

with open(f"{media_dir}/Лекция 3 рис 2.svg", "w", encoding="utf-8") as f:
    f.write(svg2)
subprocess.run(["rsvg-convert", f"{media_dir}/Лекция 3 рис 2.svg", "-o", f"{media_dir}/Лекция 3 рис 2.png"], check=True)

# ----------------- DIAGRAM 3 FIX -----------------
svg3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="1000" height="600">
  <defs>
    <style>
      .bg { fill: #131722; }
      .card { fill: #1e2433; stroke: #334155; stroke-width: 1.5; rx: 8; }
      .title { font-family: 'DejaVu Sans', sans-serif; font-size: 19px; font-weight: bold; fill: #f8fafc; }
      .subtitle { font-family: 'DejaVu Sans', sans-serif; font-size: 13px; fill: #94a3b8; }
      .card-title { font-family: 'DejaVu Sans', sans-serif; font-size: 14.5px; font-weight: bold; }
      .label { font-family: 'DejaVu Sans', sans-serif; font-size: 12.5px; fill: #e2e8f0; }
      .label-sm { font-family: 'DejaVu Sans', sans-serif; font-size: 11.5px; fill: #94a3b8; }
      .math { font-family: 'DejaVu Serif', serif; font-style: italic; font-size: 14.5px; fill: #ffffff; }
      .math-sm { font-family: 'DejaVu Serif', serif; font-style: italic; font-size: 12.5px; fill: #cbd5e1; }
      .math-bold { font-family: 'DejaVu Serif', serif; font-weight: bold; font-size: 14.5px; fill: #ffffff; }
      .axis { stroke: #64748b; stroke-width: 2; marker-end: url(#arrow-head); }
      .region-gamma { fill: rgba(99, 102, 241, 0.12); stroke: #818cf8; stroke-width: 2.5; }
      .rect-cell { fill: rgba(56, 189, 248, 0.22); stroke: #38bdf8; stroke-width: 1.3; stroke-dasharray: 4,3; }
      .pt-target { fill: #ec4899; stroke: #f472b6; stroke-width: 2; }
    </style>
    <marker id="arrow-head" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b"/>
    </marker>
  </defs>

  <rect width="1000" height="600" class="bg" rx="12"/>

  <!-- Top Title -->
  <text x="35" y="36" class="title">Измеримость суперпозиции F(f(x), g(x)) с непрерывной функцией F : Γ → ℝ</text>
  <text x="35" y="58" class="subtitle">Открытый прообраз Γ_c на плоскости представляется в виде счётного объединения открытых брусов</text>

  <!-- Left: Plane (u, v) in R2 -->
  <rect x="30" y="78" width="520" height="495" class="card"/>
  <text x="45" y="105" class="card-title" style="fill: #818cf8;">1. Открытое множество Γ_c = { (u, v) ∈ Γ : F(u, v) &gt; c } ⊂ ℝ²</text>

  <!-- Axes in (u, v) -->
  <line x1="55" y1="465" x2="505" y2="465" class="axis"/>
  <text x="498" y="490" class="math-bold">u</text>

  <line x1="80" y1="495" x2="80" y2="125" class="axis"/>
  <text x="60" y="135" class="math-bold">v</text>

  <!-- Region Gamma_c: smooth contour -->
  <path d="M 150 365 C 110 270, 150 160, 260 150 C 360 140, 460 190, 470 300 C 480 390, 400 440, 300 430 C 210 420, 180 420, 150 365 Z"
        class="region-gamma"/>
  <text x="350" y="185" class="math-bold" style="fill: #818cf8; font-size: 16px;">Γ_c (открыто)</text>

  <!-- Countable rectangle decomposition: rectangles inside Gamma_c -->
  <rect x="180" y="200" width="80" height="75" class="rect-cell"/>
  <rect x="260" y="200" width="95" height="75" class="rect-cell"/>
  <rect x="180" y="275" width="80" height="85" class="rect-cell"/>
  
  <!-- Highlighted j-th rectangle: (a_j; b_j) x (c_j; d_j) -->
  <rect x="260" y="275" width="105" height="85" style="fill: rgba(236, 72, 153, 0.25); stroke: #ec4899; stroke-width: 2.2; rx: 2;"/>
  <rect x="155" y="305" width="25" height="50" class="rect-cell"/>
  <rect x="365" y="260" width="60" height="85" class="rect-cell"/>

  <!-- Target Point (f(x), g(x)) inside j-th rectangle -->
  <circle cx="305" cy="320" r="4.5" class="pt-target"/>
  <text x="315" y="325" class="math-bold" style="fill: #f472b6; font-size: 13.5px;">(f(x), g(x))</text>

  <!-- Bounds for highlighted rectangle -->
  <line x1="260" y1="360" x2="260" y2="465" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <line x1="365" y1="360" x2="365" y2="465" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="252" y="482" class="math-sm">a_j</text>
  <text x="357" y="482" class="math-sm">b_j</text>

  <line x1="80" y1="360" x2="260" y2="360" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <line x1="80" y1="275" x2="260" y2="275" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="58" y="365" class="math-sm">c_j</text>
  <text x="58" y="280" class="math-sm">d_j</text>

  <text x="55" y="525" class="math" style="fill: #38bdf8; font-size: 13.5px;">Γ_c = ⋃_{j=1}^∞ (a_j; b_j) × (c_j; d_j)  (счётное объединение брусов)</text>
  <text x="55" y="550" class="label-sm">Так как F непрерывна, а (c; +∞) открыт, прообраз Γ_c открыт в ℝ²</text>

  <!-- Right: Preimage in A & Algebraic Consequences -->
  <rect x="570" y="78" width="400" height="495" class="card"/>
  <text x="585" y="105" class="card-title" style="fill: #38bdf8;">2. Прообраз h⁻¹((c; +∞)) в множестве A</text>

  <!-- Mapping formula box -->
  <g transform="translate(585, 120)">
    <rect x="0" y="0" width="370" height="110" style="fill: #0c4a6e; stroke: #0284c7; stroke-width: 1; rx: 6;"/>
    <text x="12" y="23" class="label" style="font-weight: bold; fill: #bae6fd;">Точка (f(x), g(x)) ∈ Γ_c равносильна:</text>
    <text x="20" y="50" class="math-bold" style="font-size: 13.5px; fill: #ffffff;">∃ j :  f(x) ∈ (a_j; b_j)  и  g(x) ∈ (c_j; d_j)</text>
    <text x="12" y="76" class="label-sm" style="fill: #e0f2fe;">Поэтому прообраз раскладывается в счётное объединение:</text>
    <text x="12" y="96" class="math-sm" style="fill: #38bdf8; font-size: 12px;">h⁻¹((c; +∞)) = ⋃_j ( f⁻¹((a_j; b_j)) ∩ g⁻¹((c_j; d_j)) ) ∈ M</text>
  </g>

  <!-- Bottom: Algebraic Operations table -->
  <text x="585" y="260" class="card-title" style="fill: #f59e0b;">3. Следствия: алгебраические операции</text>

  <g transform="translate(585, 275)">
    <!-- Row 1: Sum -->
    <rect x="0" y="0" width="370" height="54" style="fill: #1e2433; stroke: #334155; rx: 4;"/>
    <text x="12" y="22" class="math-bold" style="fill: #34d399;">f + g :</text>
    <text x="68" y="22" class="label-sm">F(u, v) = u + v  непрерывна на ℝ²</text>
    <text x="68" y="42" class="label-sm" style="fill: #94a3b8;">⇒ сумма измеримых функций измерима</text>

    <!-- Row 2: Product -->
    <rect x="0" y="62" width="370" height="54" style="fill: #1e2433; stroke: #334155; rx: 4;"/>
    <text x="12" y="84" class="math-bold" style="fill: #60a5fa;">f · g :</text>
    <text x="68" y="84" class="label-sm">F(u, v) = u · v  непрерывна на ℝ²</text>
    <text x="68" y="104" class="label-sm" style="fill: #94a3b8;">⇒ произведение измеримых функций измеримо</text>

    <!-- Row 3: Quotient -->
    <rect x="0" y="124" width="370" height="54" style="fill: #1e2433; stroke: #334155; rx: 4;"/>
    <text x="12" y="146" class="math-bold" style="fill: #f472b6;">f / g :</text>
    <text x="68" y="146" class="label-sm">F(u, v) = u / v  непр. на Γ = {v ≠ 0}</text>
    <text x="68" y="166" class="label-sm" style="fill: #94a3b8;">⇒ частное при g(x) ≠ 0 измеримо</text>

    <!-- Row 4: Continuous comp -->
    <rect x="0" y="186" width="370" height="54" style="fill: #1e2433; stroke: #334155; rx: 4;"/>
    <text x="12" y="208" class="math-bold" style="fill: #fbbf24;">f ∘ g :</text>
    <text x="68" y="208" class="label-sm">F(u, v) = f(v)  непрерывна при непр. f</text>
    <text x="68" y="228" class="label-sm" style="fill: #94a3b8;">⇒ непрерывная от измеримой измерима</text>
  </g>
</svg>"""

with open(f"{media_dir}/Лекция 3 рис 3.svg", "w", encoding="utf-8") as f:
    f.write(svg3)
subprocess.run(["rsvg-convert", f"{media_dir}/Лекция 3 рис 3.svg", "-o", f"{media_dir}/Лекция 3 рис 3.png"], check=True)

print("Updated all 3 diagrams successfully!")
