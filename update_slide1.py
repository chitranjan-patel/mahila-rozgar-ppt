import re

html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_slide1 = '''        <!-- Slide 1 -->
        <div class="slide active">
            <div class="slide-content-wrapper" style="flex-direction: row;">
                <div class="image-section" style="flex: 1.2; background-image: url('images/slide1.png');">
                </div>
                <div class="text-section" style="flex: 1; padding: 3rem; overflow-y: auto; background: var(--white);">
                    <h1 style="font-size: 3.5rem; color: var(--primary); margin-bottom: 1rem;">AI और Digital Marketing से महिलाओं के लिए रोजगार के नए अवसर</h1>
                    <h3 style="font-size: 1.8rem; color: var(--secondary); margin-bottom: 2rem;">सीखें • सिखाएँ • कमाएँ • आत्मनिर्भर बनें</h3>
                    <div class="tagline" style="background: var(--primary); color: var(--white); padding: 1rem 2rem; border-radius: 50px; display: inline-block; font-size: 1.2rem;">तकनीक से सशक्त महिला, आत्मनिर्भर परिवार और विकसित समाज</div>
                </div>
            </div>
        </div>'''

content = re.sub(r'<!-- Slide 1 -->.*?<!-- Slide 2 -->', new_slide1 + '\n\n        <!-- Slide 2 -->', content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Slide 1 to split layout')
