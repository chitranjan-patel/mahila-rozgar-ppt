import re

html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Refactor CSS
new_css = '''
        :root {
            --primary: #ffffff;
            --secondary: #ffcc00;
            --light: transparent;
            --dark: #f0f0f0;
            --white: transparent;
            --accent: rgba(255, 255, 255, 0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', 'Noto Sans Devanagari', sans-serif;
        }

        body {
            background-color: #000;
            color: #fff;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .slider-container {
            width: 100%;
            height: 100vh;
            position: relative;
            overflow: hidden;
            background: #000;
        }

        .slide {
            position: absolute;
            top: 0;
            left: 100%;
            width: 100%;
            height: 100%;
            display: flex;
            transition: left 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .slide.active { left: 0; }
        .slide.prev { left: -100%; }

        .slide-content-wrapper {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: row;
            background-size: cover;
            background-position: center;
        }
        .slide-overlay {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(to right, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 60%, rgba(0,0,0,0.95) 100%);
            z-index: 1;
        }
        .text-section {
            flex: 1;
            padding: 4rem 6rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            z-index: 2;
            position: relative;
            margin-left: 40%;
        }
        .image-section { display: none !important; }
'''
content = re.sub(r':root\s*\{.*?(?=\.title-slide)', new_css, content, flags=re.DOTALL)

def fix_slide(m):
    slide_num = m.group(1)
    slide_content = m.group(2)
    # find image url
    img_match = re.search(r'url\([^)]+\)', slide_content)
    img_url = img_match.group(0) if img_match else f"url('images/slide{slide_num}.png')"
    
    # recreate slide structure
    # remove old image-section
    slide_content = re.sub(r'<div class="image-section".*?</div>', '', slide_content, flags=re.DOTALL)
    
    # inject background and overlay
    slide_content = re.sub(r'<div class="slide-content-wrapper[^>]*>', 
                           f'<div class="slide-content-wrapper" style="background-image: {img_url};">\n<div class="slide-overlay"></div>', 
                           slide_content, count=1)
    return f'<!-- Slide {slide_num} -->\n{slide_content}'

content = re.sub(r'<!-- Slide (\d+) -->\s*(<div class=\"slide.*?(?=<!-- Slide |\Z))', fix_slide, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated layout to full screen with dark overlay')
