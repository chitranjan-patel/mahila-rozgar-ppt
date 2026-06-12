import re
html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

slide10_new = '''
                    <h2>डिजिटल मार्केटिंग क्या है?</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">सही ग्राहकों तक पहुँचने की सबसे आधुनिक और प्रभावी तकनीक</h3>
                    <h4>📌 यह क्यों जरूरी है?</h4>
                    <ul>
                        <li>पारंपरिक मार्केटिंग (अखबार, पर्चे) के मुकाबले यह बहुत सस्ती और सटीक है।</li>
                        <li>आप केवल उन लोगों तक पहुँच सकते हैं जो आपके उत्पाद (Product) में सच में रुचि रखते हैं।</li>
                        <li>कम बजट में व्यवसाय और बिक्री (Sales) को तेजी से बढ़ाना संभव है।</li>
                        <li>अपनी स्थानीय दुकान (Local Shop) को एक ऑनलाइन ब्रांड (Online Brand) में बदल सकते हैं।</li>
                    </ul>
                    <div class="demo-box" style="margin-top: 1.5rem;">
                        💡 <b>Example:</b> Facebook Ads, Instagram Ads, और Google My Business के ज़रिए ग्राहकों को सीधे आकर्षित करना।
                    </div>
'''

slide11_new = '''
                    <h2>5 KM Radius Ads (स्थानीय विज्ञापन)</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">अपने आस-पास के ग्राहकों को ऑनलाइन खोजें</h3>
                    <h4>📌 यह कैसे काम करता है?</h4>
                    <ul>
                        <li>📍 <b>Hyper-Local Targeting:</b> अपनी दुकान या व्यवसाय के 5 किलोमीटर के दायरे में ही विज्ञापन दिखाना।</li>
                        <li>💰 <b>बहुत कम बजट:</b> मात्र ₹100-200 प्रति दिन के बजट में रोज़ाना 1000 से 2000 लोगों तक पहुँचना।</li>
                        <li>🏪 <b>किनके लिए फायदेमंद:</b> बुटीक, ब्यूटी पार्लर, ट्यूशन सेंटर और बेकरी जैसे छोटे व्यवसायों के लिए अत्यंत असरदार।</li>
                        <li>👥 <b>सीधा संपर्क:</b> आस-पास के लोग विज्ञापन देखकर सीधे आपकी दुकान पर आ सकते हैं या WhatsApp पर आर्डर दे सकते हैं।</li>
                    </ul>
                    <div class="tagline" style="margin-top: 1rem;">Local Customers, Better Reach & Fast Sales</div>
'''

slide12_new = '''
                    <h2>रोजगार के नए और बेहतरीन अवसर</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">डिजिटल युग में घर बैठे काम करने के स्मार्ट तरीके</h3>
                    <ul>
                        <li>🎨 <b>Graphic Designer:</b> Canva का उपयोग करके छोटे दुकानदारों के लिए पोस्टर, लोगो और बैनर बनाना।</li>
                        <li>📱 <b>Social Media Manager:</b> अन्य व्यवसायों (Doctors, Boutiques) के Instagram और Facebook पेज सँभालना।</li>
                        <li>📈 <b>Local Ad Expert:</b> स्थानीय व्यवसायों के लिए Facebook/Instagram पर विज्ञापन (Ads) चलाना।</li>
                        <li>✍️ <b>Content Creator:</b> सोशल मीडिया के लिए आकर्षक पोस्ट लिखना और डिज़ाइन करना।</li>
                        <li>💬 <b>WhatsApp Marketer:</b> कैटलॉग बनाना और ग्राहकों को ऑफर्स के ब्रॉडकास्ट भेजना।</li>
                    </ul>
'''

slide13_new = '''
                    <h2>कमाई के संभावित स्रोत (Income)</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">यदि आप घर बैठे काम करती हैं, तो कितनी कमाई हो सकती है?</h3>
                    <ul>
                        <li>💰 <b>सोशल मीडिया मैनेजमेंट:</b> यदि आप 5 ग्राहकों का पेज संभालती हैं (₹2000 प्रति ग्राहक) = <b>₹10,000 / माह</b></li>
                        <li>💰 <b>डिजिटल एडवरटाइजिंग:</b> 3 ग्राहकों के लिए एड्स चलाना (₹3000 प्रति कैंपेन) = <b>₹9,000 / माह</b></li>
                        <li>💰 <b>पोस्टर डिज़ाइनिंग:</b> महीने में 20 पोस्टर बनाना (₹200 प्रति पोस्टर) = <b>₹4,000 / माह</b></li>
                    </ul>
                    <p style="font-size: 1.15rem; margin-top: 1.5rem; font-weight: 600; color: var(--primary);">
                        कुल मिलाकर एक महिला पार्ट-टाइम काम करके भी घर बैठे आसानी से <br><span style="font-size: 1.8rem; color: var(--secondary);">₹15,000 से ₹25,000</span> प्रति माह कमा सकती है।
                    </p>
'''

slide14_new = '''
                    <h2>AWO का समर्थन (We Stand With You)</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">AWO सिर्फ ट्रेनिंग नहीं देता, बल्कि आत्मनिर्भर बनने तक आपके साथ खड़ा रहता है</h3>
                    <ul>
                        <li>🎓 <b>प्रैक्टिकल ट्रेनिंग (Practical Training):</b> लाइव प्रोजेक्ट्स पर काम सिखाना ताकि आपको असली अनुभव मिले।</li>
                        <li>🤝 <b>मेंटरशिप (Mentorship):</b> बिज़नेस शुरू करने में विशेषज्ञों (Experts) द्वारा व्यक्तिगत मार्गदर्शन।</li>
                        <li>💼 <b>पहला ग्राहक (First Client):</b> आपको आपका पहला क्लाइंट या काम दिलाने में पूरी सहायता।</li>
                        <li>🌐 <b>कम्युनिटी सपोर्ट (Community):</b> सफल महिलाओं के एक बड़े नेटवर्क का हिस्सा बनने का मौका।</li>
                        <li>🏆 <b>प्रमाणपत्र (Certification):</b> कोर्स पूरा होने पर एक मान्यता प्राप्त प्रमाणपत्र।</li>
                    </ul>
                    <div class="tagline" style="margin-top: 1rem; background: var(--secondary);">हर कदम पर AWO का साथ</div>
'''

slide15_new = '''
                    <h2>निष्कर्ष (सफलता की ओर पहला कदम)</h2>
                    <ul>
                        <li>✔ <b>नई तकनीक अपनाएं:</b> आज की दुनिया में जिसके पास डिजिटल कौशल है, सफलता उसी के कदम चूमती है।</li>
                        <li>✔ <b>शुरुआत करें:</b> सीखने की कोई उम्र नहीं होती और आगे बढ़ने का कोई एक रास्ता नहीं होता।</li>
                        <li>✔ <b>झिझक छोड़ें:</b> अपनी झिझक को पीछे छोड़ें, मोबाइल का सही उपयोग करें और अपने सपनों को उड़ान दें।</li>
                        <li>✔ <b>आत्मनिर्भर बनें:</b> अपने और अपने परिवार के लिए एक मजबूत आर्थिक आधार (Financial Base) तैयार करें।</li>
                    </ul>
                    <div class="demo-box" style="margin-top: 2rem; text-align: center; font-size: 1.2rem;">
                        आइए, <b>AWO</b> के साथ मिलकर <span style="color: var(--secondary);">'आत्मनिर्भर भारत'</span> और <span style="color: var(--secondary);">'सशक्त महिला'</span> के सपने को साकार करें।<br>
                        <b>धन्यवाद!</b>
                    </div>
'''

# We need to replace the content of Slide 10 to 15 in the HTML
def replace_slide_content(slide_num, new_content):
    global content
    # Find the start of the slide text-section
    pattern = re.compile(rf'(<!-- Slide {slide_num} -->.*?</div\s*>\s*<div class="text-section">)(.*?)(</div\s*>\s*</div\s*>\s*</div\s*>)', re.DOTALL)
    match = pattern.search(content)
    if match:
        content = content[:match.start(2)] + '\n' + new_content + '\n                ' + content[match.start(3):]
    else:
        print(f"Could not find slide {slide_num}")

replace_slide_content(10, slide10_new)
replace_slide_content(11, slide11_new)
replace_slide_content(12, slide12_new)
replace_slide_content(13, slide13_new)
replace_slide_content(14, slide14_new)
replace_slide_content(15, slide15_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated slides 10-15 with rich content')
