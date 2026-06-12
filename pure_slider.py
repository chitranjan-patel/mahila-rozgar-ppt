html_content = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI & Digital Marketing Presentation</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background-color: #000;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .slider-container {
            width: 100%;
            height: 100%;
            position: relative;
            overflow: hidden;
        }
        .slide {
            position: absolute;
            top: 0; left: 100%;
            width: 100%; height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: left 0.5s ease-in-out;
        }
        .slide.active { left: 0; }
        .slide.prev { left: -100%; }
        
        .slide-image {
            width: 100%;
            height: 100%;
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Controls */
        .controls {
            position: absolute;
            bottom: 3rem;
            right: 4rem;
            display: flex;
            gap: 1.5rem;
            z-index: 100;
        }
        button {
            background: rgba(255, 255, 255, 0.8);
            color: #000;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            font-size: 1.5rem;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            transition: all 0.3s;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        button:hover {
            background: #fff;
            transform: scale(1.1);
        }
        .slide-counter {
            position: absolute;
            bottom: 3rem;
            left: 4rem;
            font-size: 1.2rem;
            color: #fff;
            font-family: 'Poppins', sans-serif;
            z-index: 100;
            background: rgba(0,0,0,0.5);
            padding: 0.5rem 1.5rem;
            border-radius: 20px;
        }
    </style>
</head>
<body>

    <div class="slider-container" id="slider">
"""

for i in range(1, 16):
    active_class = " active" if i == 1 else ""
    html_content += f'''
        <!-- Slide {i} -->
        <div class="slide{active_class}">
            <div class="slide-image" style="background-image: url('images/slide{i}.png');"></div>
        </div>
'''

html_content += """
    </div>

    <div class="slide-counter">
        <span id="current">1</span> / 15
    </div>

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
                if (i === index) {
                    slide.classList.add('active');
                } else if (i < index) {
                    slide.classList.add('prev');
                }
            });
            counter.innerText = index + 1;
        }

        function nextSlide() {
            if (currentSlide < slides.length - 1) {
                currentSlide++;
                showSlide(currentSlide);
            }
        }

        function prevSlide() {
            if (currentSlide > 0) {
                currentSlide--;
                showSlide(currentSlide);
            }
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
        });
    </script>
</body>
</html>
"""

html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created pure image slider HTML")
