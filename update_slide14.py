import re
html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

slide14_new = '''
                    <h2>सफलता की प्रेरणादायक कहानी</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">📌 एक ग्रामीण महिला की सफलता:</h3>
                    <ul>
                        <li>👩🏻 एक महिला ने सिलाई/अचार का छोटा सा व्यवसाय शुरू किया।</li>
                        <li>📱 AI और Digital Marketing सीखकर अपना Facebook Page बनाया।</li>
                        <li>🤖 ChatGPT से बढ़िया पोस्ट लिखवाई और Canva से सुंदर पोस्टर बनाए।</li>
                        <li>📍 5 KM Radius में Ads चलाए जिससे आस-पास के लोग ग्राहक बन गए।</li>
                        <li>📈 आज उनकी आय कई गुना बढ़ चुकी है और वे आत्मनिर्भर हैं!</li>
                    </ul>
                    <div class="demo-box" style="margin-top: 1.5rem; text-align: center;">
                        📢 <b>"सीखने की शुरुआत ही सफलता की पहली सीढ़ी है।"</b>
                    </div>
'''

def replace_slide_content(slide_num, new_content):
    global content
    pattern = re.compile(rf'(<!-- Slide {slide_num} -->.*?</div\s*>\s*<div class="text-section">)(.*?)(</div\s*>\s*</div\s*>\s*</div\s*>)', re.DOTALL)
    match = pattern.search(content)
    if match:
        content = content[:match.start(2)] + '\n' + new_content + '\n                ' + content[match.start(3):]
    else:
        print(f"Could not find slide {slide_num}")

replace_slide_content(14, slide14_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated slide 14 with success story')
