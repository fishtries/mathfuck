import re

path = '/home/fish/Documents/mathfuck/syncing/Функциональный анализ/5 семестр/Лекция 3 16.09.26.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

cyrillic_pattern = re.compile(r'[\u0400-\u04FF]')

errors = []
for i, line in enumerate(lines):
    math_blocks = re.findall(r'\$\$([^\$]+)\$\$|\$([^\$]+)\$', line)
    for b1, b2 in math_blocks:
        b = b1 if b1 else b2
        # Remove \text{...}
        cleaned = re.sub(r'\\text\{[^}]*\}', '', b)
        match = cyrillic_pattern.search(cleaned)
        if match:
            errors.append((i+1, match.group(), line.strip()))

if errors:
    print(f"WARNING: {len(errors)} unescaped Cyrillic found in math mode:")
    for l_num, char, l_text in errors:
        print(f"Line {l_num} [char {char}]: {l_text}")
else:
    print("LaTeX verification: 100% CLEAN! No unescaped Cyrillic found in math mode.")
