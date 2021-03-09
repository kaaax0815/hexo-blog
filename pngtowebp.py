from PIL import Image
import os, os.path
import re

imgs = []
img_path = r"D:\Bernd\BerndPC\Documents\Github\Javascript\hexo-blog\source\_posts\How-to-Host-a-Discord-Music-Bot-for-Free"
md_file  = r"D:\Bernd\BerndPC\Documents\Github\Javascript\hexo-blog\source\_posts\How-to-Host-a-Discord-Music-Bot-for-Free.md"
asset_regex = "^(\{% asset_img )(.*.png)( .* %\})$"
for f in os.listdir(img_path):
    ext = os.path.splitext(f)[1]
    if ext.lower() != ".png":
        continue
    imgs.append(os.path.join(img_path,f))



for img in imgs:
    im = Image.open(img).convert("RGB")
    im.save(img + ".webp", "webp")
    os.remove(img)


with open (md_file, 'r' ) as f:
    content = f.read()
    content_new = re.sub(asset_regex, r"\1\2.webp\3", content, flags = re.M)
    with open(md_file + ".bak", "w") as f:
        f.write(content)
    with open(md_file, "w") as f:
        f.write(content_new)