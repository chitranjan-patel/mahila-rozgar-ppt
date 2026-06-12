html_content = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI & Digital Marketing</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Noto+Sans+Devanagari:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #004b93;
            --secondary: #007bff;
            --light: #f4f8fb;
            --dark: #2c3e50;
            --white: #ffffff;
            --accent: #e1effe;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', 'Noto Sans Devanagari', sans-serif; }

        body {
            background-color: var(--light);
            color: var(--dark);
            overflow: hidden;
            display: flex; justify-content: center; align-items: center;
            height: 100vh;
        }

        .slider-container {
            width: 100%; height: 100vh; position: relative; overflow: hidden; background: var(--white);
        }

        .slide {
            position: absolute; top: 0; left: 100%; width: 100%; height: 100%; display: flex;
            transition: left 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .slide.active { left: 0; }
        .slide.prev { left: -100%; }

        .slide-content-wrapper {
            width: 100%; height: 100%; display: flex; flex-direction: row;
        }

        .text-section {
            flex: 1; padding: 3rem 4rem; display: flex; flex-direction: column; justify-content: center; z-index: 2;
            background: var(--light); /* Give it a light background to separate it softly */
            box-shadow: -5px 0 15px rgba(0,0,0,0.05); /* Slight shadow to separate from image */
        }

        .image-section {
            flex: 1.2;
            background-size: contain; /* This prevents the image from being cut! */
            background-repeat: no-repeat;
            background-position: center;
            background-color: var(--white); /* White background so it blends well */
        }

        h1 { color: var(--primary); font-size: 3.5rem; margin-bottom: 1.5rem; line-height: 1.3; font-weight: 700; }
        h2 { color: var(--primary); font-size: 2.5rem; margin-bottom: 1.5rem; font-weight: 700; }
        h3 { color: var(--secondary); font-size: 1.5rem; margin-bottom: 1rem; font-weight: 600; }
        h4 { color: var(--primary); font-size: 1.2rem; margin-bottom: 0.5rem; }
        p { font-size: 1rem; color: var(--dark); margin-bottom: 0.5rem; }
        ul { list-style-type: none; margin-bottom: 1.5rem; }
        ul li { position: relative; padding-left: 1.5rem; margin-bottom: 0.8rem; font-size: 1rem; color: var(--dark); }
        ul li::before { content: '✔'; color: var(--secondary); position: absolute; left: 0; font-weight: bold; }

        .tagline {
            display: inline-block; background: var(--primary); color: var(--white);
            padding: 1rem 2rem; border-radius: 50px; font-size: 1.2rem; font-weight: 600;
        }

        .demo-box {
            background: var(--white); border-left: 6px solid var(--secondary);
            padding: 1rem 1.5rem; border-radius: 0 12px 12px 0; font-size: 1rem; color: var(--primary); font-weight: 600;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .controls { position: absolute; bottom: 2rem; right: 3rem; display: flex; gap: 1rem; z-index: 100; }
        button {
            background: var(--white); color: var(--primary); border: 2px solid var(--primary);
            width: 50px; height: 50px; border-radius: 50%; font-size: 1.5rem; cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1); transition: all 0.3s;
        }
        button:hover { background: var(--primary); color: var(--white); transform: translateY(-3px); }
        .slide-counter {
            position: absolute; bottom: 2rem; left: 3rem; font-size: 1.2rem; color: var(--dark); font-weight: 600;
            background: var(--white); padding: 0.5rem 1.5rem; border-radius: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
    </style>
</head>
<body>
    <div class="slider-container" id="slider">

        <!-- Slide 1 -->
        <div class="slide active">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide1.png');"></div>
                <div class="text-section">
                    <h1>AI और Digital Marketing से महिलाओं के लिए रोजगार के नए अवसर</h1>
                    <h3>सीखें • सिखाएँ • कमाएँ • आत्मनिर्भर बनें</h3>
                    <div class="tagline">तकनीक से सशक्त महिला, आत्मनिर्भर परिवार और विकसित समाज</div>
                </div>
            </div>
        </div>

        <!-- Slide 2 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide2.png');"></div>
                <div class="text-section">
                    <h2>आज की डिजिटल दुनिया</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">डिजिटल तकनीक ने सीखने, कमाने और व्यवसाय करने के तरीके बदल दिए हैं।</h3>
                    <h4>🌐 इंटरनेट और स्मार्टफोन का बढ़ता उपयोग</h4>
                    <p>• आज अधिकांश लोग मोबाइल और इंटरनेट का उपयोग कर रहे हैं।</p>
                    <p>• जानकारी, शिक्षा और व्यापार तेजी से ऑनलाइन हो रहे हैं。</p>
                    <h4 style="margin-top:1rem;">📱 सोशल मीडिया का प्रभाव</h4>
                    <p>• Facebook, Instagram और WhatsApp लाखों लोगों तक पहुँचने का आसान माध्यम हैं।</p>
                    <p>• छोटे व्यवसाय भी सोशल मीडिया से अपने ग्राहकों तक पहुँच रहे हैं।</p>
                    <div class="demo-box" style="margin-top: 1.5rem;">💡 "डिजिटल ज्ञान आज के समय की सबसे बड़ी शक्ति है।"</div>
                </div>
            </div>
        </div>

        <!-- Slide 3 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide3.png');"></div>
                <div class="text-section">
                    <h2>AI क्या है? (Artificial Intelligence)</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">AI एक स्मार्ट तकनीक है जो इंसानों की तरह सोचने और काम करने में सहायता करती है।</h3>
                    <h4>⚡ AI के कार्य</h4>
                    <ul>
                        <li>प्रश्नों के उत्तर देना और कंटेंट लिखना</li>
                        <li>पोस्ट और डिजाइन बनाना</li>
                        <li>भाषा अनुवाद करना</li>
                    </ul>
                    <h4>🌟 महिलाओं के लिए फायदे</h4>
                    <ul>
                        <li style="color: green;">समय और पैसों की बचत</li>
                        <li style="color: green;">नए रोजगार और सीखने के अवसर</li>
                    </ul>
                    <div style="display: flex; gap: 10px; margin-top: 1rem;">
                        <span class="tagline" style="font-size: 1rem; padding: 0.5rem 1rem;">ChatGPT</span>
                        <span class="tagline" style="font-size: 1rem; padding: 0.5rem 1rem;">Google Gemini</span>
                        <span class="tagline" style="font-size: 1rem; padding: 0.5rem 1rem;">Canva AI</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 4 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide4.png');"></div>
                <div class="text-section">
                    <h2>AI महिलाओं के लिए क्यों महत्वपूर्ण है?</h2>
                    <h3 style="color: var(--dark); font-weight: normal;">सीखने, काम करने और आत्मनिर्भर बनने के नए अवसर</h3>
                    <h4>🏠 घर बैठे काम करने की सुविधा</h4>
                    <p>AI की मदद से घर से ही कई डिजिटल कार्य संभव हैं। समय और संसाधनों की बचत होती है।</p>
                    <h4 style="margin-top:1rem;">💰 कम लागत में व्यवसाय</h4>
                    <p>केवल मोबाइल और इंटरनेट से शुरुआत की जा सकती है। बड़े निवेश की आवश्यकता नहीं।</p>
                    <h4 style="margin-top:1rem;">🌟 AI से महिलाएं क्या कर सकती हैं?</h4>
                    <ul>
                        <li>सोशल मीडिया पोस्ट और व्यवसाय का प्रचार</li>
                        <li>पोस्टर और लोगो डिज़ाइन</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Slide 5 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide5.png');"></div>
                <div class="text-section">
                    <h2>ChatGPT: आपका डिजिटल सहायक</h2>
                    <h4>यह कैसे काम करता है:</h4>
                    <ul>
                        <li>📝 लंबी पोस्ट और कंटेंट को सेकंडों में लिखता है।</li>
                        <li>❓ सवालों के आसान और सटीक जवाब देता है।</li>
                        <li>💡 व्यवसाय को बढ़ाने के लिए नए विचार (Ideas) देता है।</li>
                        <li>📧 ग्राहकों के लिए प्रोफेशनल मैसेज तैयार करता है।</li>
                    </ul>
                    <div class="demo-box" style="margin-top: 1.5rem;">
                        <strong>💻 Demo:</strong><br>
                        "मेरे अचार व्यवसाय के लिए Facebook Post लिखो"
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 6 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide6.png');"></div>
                <div class="text-section">
                    <h2>Canva AI से डिजाइन बनाना</h2>
                    <h4>📌 आप क्या-क्या बना सकते हैं:</h4>
                    <ul>
                        <li>आकर्षक Poster Design और Logo Design</li>
                        <li>व्यवसाय के लिए Banner Design और Social Media Post</li>
                        <li>त्योहारों के लिए Festival Poster</li>
                    </ul>
                    <h4>🌟 इसके मुख्य फायदे:</h4>
                    <ul>
                        <li>इस्तेमाल में बहुत आसान (कोई डिजाइनिंग कोर्स जरूरी नहीं)</li>
                        <li>मिनटों में तैयार और Professional लुक</li>
                    </ul>
                    <div class="tagline" style="margin-top: 1rem; background: green;">💰 Income: ₹100–500 प्रति डिजाइन</div>
                </div>
            </div>
        </div>

        <!-- Slide 7 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide7.png');"></div>
                <div class="text-section">
                    <h2>Facebook Business Page</h2>
                    <h4>📌 आप क्या-क्या कर सकते हैं:</h4>
                    <ul>
                        <li>व्यवसाय की प्रोफेशनल ऑनलाइन पहचान बनाना (Virtual Shop)</li>
                        <li>अपने उत्पादों और सेवाओं का मुफ्त में प्रचार करना</li>
                        <li>ग्राहकों के सीधे सवालों का जवाब देना</li>
                        <li>नए Offers और Updates को तुरंत ग्राहकों तक पहुँचाना</li>
                    </ul>
                    <div style="display: flex; gap: 10px; margin-top: 1rem;">
                        <span class="tagline" style="font-size: 1rem; padding: 0.5rem 1rem;">Local Reach</span>
                        <span class="tagline" style="font-size: 1rem; padding: 0.5rem 1rem;">Brand Awareness</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 8 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide8.png');"></div>
                <div class="text-section">
                    <h2>Instagram Business Account</h2>
                    <h4>📌 मुख्य विशेषताएं:</h4>
                    <ul>
                        <li>🎥 आकर्षक Reels बनाकर लाखों नए लोगों तक पहुँचना</li>
                        <li>📸 बेहतरीन फोटो के जरिए उत्पादों (Products) का Showcase करना</li>
                        <li>📱 Stories के माध्यम से दैनिक अपडेट्स और ऑफर्स दिखाना</li>
                        <li>❤️ ग्राहकों के साथ Engagement बढ़ाना</li>
                    </ul>
                    <div class="tagline" style="margin-top: 1rem; background: #e1306c;">Free Marketing & Online Sales</div>
                </div>
            </div>
        </div>

        <!-- Slide 9 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide9.png');"></div>
                <div class="text-section">
                    <h2>WhatsApp Business</h2>
                    <h4>📌 इसके पावरफुल टूल्स:</h4>
                    <ul>
                        <li>🛒 <b>Product Catalog:</b> अपने उत्पादों की लिस्ट दिखाना</li>
                        <li>🤖 <b>Auto Reply:</b> ग्राहकों का तुरंत स्वचालित जवाब देना</li>
                        <li>⚡ <b>Quick Replies:</b> बार-बार पूछे जाने वाले सवालों के शार्टकट</li>
                        <li>📢 <b>Broadcast:</b> एक क्लिक में 250+ ग्राहकों तक नया ऑफर भेजना</li>
                    </ul>
                    <div class="tagline" style="margin-top: 1rem; background: #25d366;">Direct Contact & Easy Orders</div>
                </div>
            </div>
        </div>

        <!-- Slide 10 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide10.png');"></div>
                <div class="text-section">
                    <h2>Digital Marketing</h2>
                    <h4>📌 डिजिटल मार्केटिंग क्यों जरूरी है?</h4>
                    <ul>
                        <li>इंटरनेट के माध्यम से अपने व्यवसाय का स्मार्ट प्रचार करना</li>
                        <li>केवल उन ग्राहकों तक पहुँचना जो खरीदने में रुचि रखते हों</li>
                        <li>कम बजट में व्यवसाय और बिक्री को तेजी से बढ़ाना</li>
                        <li>अपनी स्थानीय दुकान को ऑनलाइन ब्रांड में बदलना</li>
                    </ul>
                    <div class="demo-box" style="margin-top: 1.5rem;">
                        💡 <b>Example:</b> Facebook Ads, Instagram Ads, Google Business
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 11 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide11.png');"></div>
                <div class="text-section">
                    <h2>5 KM Radius Ads (स्थानीय विज्ञापन)</h2>
                    <h4>📌 यह कैसे काम करता है?</h4>
                    <ul>
                        <li>📍 व्यवसाय के 5 किलोमीटर के दायरे में विज्ञापन दिखाना</li>
                        <li>💰 बहुत कम बजट (₹100-200 प्रति दिन) में हजारों लोगों तक पहुँचना</li>
                        <li>🏪 बुटीक, ब्यूटी पार्लर और छोटे व्यवसायों के लिए असरदार</li>
                        <li>👥 आस-पास के लोग विज्ञापन देखकर आसानी से आ सकते हैं</li>
                    </ul>
                    <div class="tagline" style="margin-top: 1rem;">Local Customers, Better Reach</div>
                </div>
            </div>
        </div>

        <!-- Slide 12 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide12.png');"></div>
                <div class="text-section">
                    <h2>रोजगार के नए अवसर</h2>
                    <h4>📌 डिजिटल युग में घर बैठे काम:</h4>
                    <ul>
                        <li>🎨 <b>Poster Designer:</b> Canva से पोस्टर और लोगो बनाना</li>
                        <li>📱 <b>Social Media Manager:</b> दूसरों के पेज सँभालना</li>
                        <li>✍️ <b>Content Creator:</b> सोशल मीडिया के लिए पोस्ट लिखना</li>
                        <li>📈 <b>Digital Marketing:</b> ऑनलाइन विज्ञापन चलाना</li>
                        <li>💻 <b>Freelance:</b> अपने समय के अनुसार काम करना</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Slide 13 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide13.png');"></div>
                <div class="text-section">
                    <h2>कमाई के संभावित स्रोत</h2>
                    <ul>
                        <li>💰 <b>Poster Design:</b> ₹100–₹500 प्रति पोस्टर</li>
                        <li>💰 <b>Social Media Management:</b> ₹2000–₹5000 प्रति महीना/क्लाइंट</li>
                        <li>💰 <b>Ad Management:</b> ₹1000–₹3000 प्रति कैंपेन</li>
                    </ul>
                    <p>यदि एक महिला 3-4 छोटे व्यवसायों का डिजिटल मार्केटिंग सँभालती है, तो वह आसानी से घर बैठे <b>₹10,000 से ₹15,000</b> प्रति माह कमा सकती है।</p>
                </div>
            </div>
        </div>

        <!-- Slide 14 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide14.png');"></div>
                <div class="text-section">
                    <h2>AWO का समर्थन (Support)</h2>
                    <h4>📌 AWO महिलाओं की कैसे मदद करेगा?</h4>
                    <ul>
                        <li>🎓 <b>Digital Skills Training:</b> AI और सोशल मीडिया का प्रशिक्षण</li>
                        <li>🤝 <b>Mentorship:</b> विशेषज्ञों द्वारा मार्गदर्शन</li>
                        <li>💼 <b>Business Setup:</b> अपना काम शुरू करने में सहायता</li>
                        <li>🏆 <b>Certification:</b> कोर्स पूरा होने पर प्रमाणपत्र</li>
                    </ul>
                    <div class="tagline" style="margin-top: 1rem; background: var(--secondary);">कदम-दर-कदम सहायता</div>
                </div>
            </div>
        </div>

        <!-- Slide 15 -->
        <div class="slide">
            <div class="slide-content-wrapper">
                <div class="image-section" style="background-image: url('images/slide15.png');"></div>
                <div class="text-section">
                    <h2>निष्कर्ष एवं धन्यवाद</h2>
                    <ul>
                        <li>✔ <b>AI सीखें:</b> नई तकनीक से डरें नहीं, इसे अपनी ताकत बनाएँ।</li>
                        <li>✔ <b>Digital Marketing अपनाएँ:</b> अपने कौशल को लोगों तक पहुँचाएँ।</li>
                        <li>✔ <b>सोशल मीडिया का उपयोग करें:</b> इसका इस्तेमाल व्यवसाय के लिए करें।</li>
                        <li>✔ <b>आत्मनिर्भर बनें:</b> घर बैठे अपनी पहचान बनाएँ।</li>
                    </ul>
                    <div class="demo-box" style="margin-top: 1.5rem; text-align: center;">
                        AWO महिला सशक्तिकरण एवं डिजिटल कौशल प्रशिक्षण कार्यक्रम
                    </div>
                </div>
            </div>
        </div>

    </div>

    <div class="slide-counter"><span id="current">1</span> / 15</div>
    <div class="controls">
        <button onclick="prevSlide()">❮</button>
        <button onclick="nextSlide()">❯</button>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const counter = document.getElementById('current');

        function showSlide(index) {
            slides.forEach((slide, i) => {
                slide.classList.remove('active', 'prev');
                if (i === index) slide.classList.add('active');
                else if (i < index) slide.classList.add('prev');
            });
            counter.innerText = index + 1;
        }
        function nextSlide() { if (currentSlide < slides.length - 1) { currentSlide++; showSlide(currentSlide); } }
        function prevSlide() { if (currentSlide > 0) { currentSlide--; showSlide(currentSlide); } }
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
        });
    </script>
</body>
</html>"""

import os
html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Restored HTML to split layout with background-size: contain')
