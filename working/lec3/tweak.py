with open("/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа/Лекция 3 рис 1.svg", "r") as f:
    s1 = f.read()

s1 = s1.replace(
    '<text x="120" y="295" class="math-bold" style="font-size: 16px; fill: #ffffff;">V = { v_α }_α ⊂ [0; 1]   (Множество Витали)</text>\n  <text x="58" y="322" class="label-sm" style="fill: #fbcfe8;">В каждом C_α ровно один представитель, разности v_i - v_j ∉ ℚ</text>',
    '<text x="80" y="290" class="math-bold" style="font-size: 15px; fill: #ffffff;">V = { v_α }_α ⊂ [0; 1]</text><text x="255" y="290" class="card-title" style="fill: #f472b6; font-size: 13px;">— Множество Витали</text>\n  <text x="58" y="318" class="label-sm" style="fill: #fbcfe8;">В каждом C_α ровно один представитель, разности v_i - v_j ∉ ℚ</text>'
)

with open("/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа/Лекция 3 рис 1.svg", "w") as f:
    f.write(s1)

with open("/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа/Лекция 3 рис 3.svg", "r") as f:
    s3 = f.read()

s3 = s3.replace(
    '<circle cx="305" cy="320" r="4.5" class="pt-target"/>\n  <text x="315" y="325" class="math-bold" style="fill: #f472b6; font-size: 13.5px;">(f(x), g(x))</text>',
    '<circle cx="280" cy="320" r="4.5" class="pt-target"/>\n  <text x="290" y="325" class="math-bold" style="fill: #f472b6; font-size: 12.5px;">(f(x), g(x))</text>'
)

with open("/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа/Лекция 3 рис 3.svg", "w") as f:
    f.write(s3)

import subprocess
subprocess.run(["rsvg-convert", "/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа/Лекция 3 рис 1.svg", "-o", "/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа/Лекция 3 рис 1.png"], check=True)
subprocess.run(["rsvg-convert", "/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа/Лекция 3 рис 3.svg", "-o", "/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/медиа/Лекция 3 рис 3.png"], check=True)
print("Tweaks applied!")
