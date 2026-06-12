import re

html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove ALL image-overlay divs (including any remaining ones with class variations)
content = re.sub(r'\s*<div class="image-overlay"[^/]*/>', '', content)
content = re.sub(r'\s*<div class="image-overlay"[^>]*>.*?</div>', '', content, flags=re.DOTALL)

# Remove ALL linear-gradient from background-image properties 
# They look like: background-image: linear-gradient(...), url('...')
# We want: background-image: url('...')
content = re.sub(r'linear-gradient\(rgba\(\d+,\s*\d+,\s*\d+,\s*[\d.]+\),\s*rgba\(\d+,\s*\d+,\s*\d+,\s*[\d.]+\)\),\s*', '', content)
content = re.sub(r'linear-gradient\([^)]+\),\s*(?=url)', '', content)

# Also fix any remaining: background: linear-gradient(...) that was on .image-section
content = re.sub(r'background:\s*linear-gradient\([^;]+;', 'background-size: cover;', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
remaining_overlay = content.count('image-overlay')
remaining_gradient = content.count('linear-gradient')
print(f'Done! image-overlay remaining: {remaining_overlay}, linear-gradient remaining: {remaining_gradient}')
