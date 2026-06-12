import re
html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the subtitle with colorful words
colorful_subtitle = '''<h3 class="colorful-subtitle" style="font-size: 1.6rem; margin-bottom: 1.5rem; font-weight: 700;">
    <span style="color: #e91e63;">सीखें</span>
    <span style="color: #bdc3c7; margin: 0 8px;">•</span>
    <span style="color: #ff9800;">सिखाएँ</span>
    <span style="color: #bdc3c7; margin: 0 8px;">•</span>
    <span style="color: #4caf50;">कमाएँ</span>
    <span style="color: #bdc3c7; margin: 0 8px;">•</span>
    <span style="color: #9c27b0;">आत्मनिर्भर बनें</span>
</h3>'''
content = content.replace('<h3>सीखें • सिखाएँ • कमाएँ • आत्मनिर्भर बनें</h3>', colorful_subtitle)

# 2. Add premium CSS to make it less messy
css_updates = '''
        h1, h2 { 
            background: linear-gradient(135deg, var(--primary) 0%, #00a8ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.4;
            padding-bottom: 5px; /* prevents clipping of gradient text */
            font-size: 3.2rem;
            margin-bottom: 1.5rem;
            font-weight: 700;
        }
        
        h2 { font-size: 2.5rem; }
        
        h3 { color: var(--secondary); font-size: 1.5rem; margin-bottom: 1rem; font-weight: 600; }
        
        h4 {
            color: var(--primary);
            font-size: 1.3rem;
            margin-bottom: 0.8rem;
            margin-top: 1.5rem;
            border-bottom: 2px dashed #eee;
            padding-bottom: 5px;
            display: inline-block;
        }

        p {
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 1rem;
            color: #444;
        }

        ul { list-style-type: none; margin-bottom: 1.5rem; }
        ul li { 
            position: relative; 
            padding: 0.8rem 1rem 0.8rem 2.5rem; 
            margin-bottom: 0.8rem; 
            font-size: 1.05rem; 
            color: var(--dark); 
            background: #f8faff; 
            border-radius: 8px;
            border-left: 3px solid var(--secondary);
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            transition: transform 0.2s;
        }
        ul li:hover {
            transform: translateX(5px);
        }
        ul li::before { 
            content: '✔'; 
            color: var(--secondary); 
            position: absolute; 
            left: 0.8rem; 
            font-weight: bold; 
        }
'''
# Re-replace the existing CSS block for content
content = re.sub(r'h1\s*\{.*?(?=\.tagline)', css_updates, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated content layout for premium look')
