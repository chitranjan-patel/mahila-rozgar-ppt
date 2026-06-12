import re

html_path = r'C:\Users\Chitranjan Kumar\Desktop\ppt\web\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace images for all 15 slides explicitly
new_content = content
for i in range(1, 16):
    img_url = f"images/slide{i}.png"
    # Search for <!-- Slide {i} --> block
    # We will replace the first background-image: url(...) we find after this comment before the next comment.
    pattern = r'(<!-- Slide ' + str(i) + r' -->.*?background-image:\s*url\()([^\)]*)(\))'
    # Use re.sub to replace only the first occurrence after the slide comment
    def replacer(m):
        return m.group(1) + f"'{img_url}'" + m.group(3)
    
    # We only want to replace it for this specific slide.
    # To do this safely, let's split the HTML by slides and replace in each chunk.
    pass

slides = re.split(r'(<!-- Slide \d+ -->)', content)
processed_slides = []
# slides[0] is everything before <!-- Slide 1 -->
processed_slides.append(slides[0])

for j in range(1, len(slides), 2):
    slide_comment = slides[j]
    slide_html = slides[j+1]
    slide_num = int(re.search(r'\d+', slide_comment).group())
    
    # Replace background-image: url(...)
    # Or if there's no background-image, maybe it's a title slide (Slide 1, Slide 15)
    # The title slides might have `background: linear-gradient(...), url(...)`
    # Let's just find any url(...) inside style="..."
    if 'url(' in slide_html:
        slide_html = re.sub(r'url\([^\)]+\)', f"url('images/slide{slide_num}.png')", slide_html, count=1)
    else:
        # If no url() is present, we might need to add an image-section or add background to slide.
        # For title slides, add background to the slide-content-wrapper
        slide_html = re.sub(r'(<div class="slide-content-wrapper.*?style=")(.*?)(">)',
                            r"\1\2; background-image: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.9)), url('images/slide" + str(slide_num) + r".png'); background-size: cover;\3", 
                            slide_html, count=1)

    processed_slides.append(slide_comment + slide_html)

new_content = "".join(processed_slides)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated HTML with all 15 images.")
