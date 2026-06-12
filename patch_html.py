import re
import os

html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
def replacer(match):
    global count
    count += 1
    # For slide 15, the background image is on body? No, it's slide 1 and 15 might be different.
    # Let's check how many matches we get.
    return match.group(1) + f"'images/slide{count}.png'" + match.group(3)

# The HTML uses: <div class="image-section" style="... background-image: url('...');">
# Actually, let's just find `background-image: url('https://images.unsplash.com/...');`
new_content = re.sub(r'(background-image:\s*url\()(\'https://images\.unsplash\.com/[^\']*\')(\))', replacer, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Replaced {count} image URLs in index.html")
