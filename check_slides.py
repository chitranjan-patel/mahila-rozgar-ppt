import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

for i in range(1, 16):
    marker = f'<!-- Slide {i} -->'
    pos = content.find(marker)
    if pos == -1:
        print(f'Slide {i}: NOT FOUND')
        continue
    ts_pos = content.find('<div class="text-section">', pos)
    if ts_pos == -1:
        print(f'Slide {i}: text-section NOT FOUND')
        continue
    ts_end = ts_pos + 26
    # Check if it has actual content (not empty)
    snippet = content[ts_end:ts_end+50].strip()
    has_content = len(snippet) > 5
    print(f'Slide {i}: {"HAS CONTENT" if has_content else "EMPTY"} => {snippet[:40]}')
