"""Compose the REAL den scene (locked cast + desks) for the portfolio:
den_bg() + tejas at his desk + zcode hovering at his desk + the speech bubble.
Crop to the desk band, save wide PNG.
"""
import sys
from pathlib import Path

FACTORY_ASSETS = "/home/linux/youtube-automation/factory/skit_assets"
CHARS = "/home/linux/youtube-automation/docs/skit/characters"
OUT = Path.home() / "tejas/portfolio/cast"
OUT.mkdir(exist_ok=True)

sys.path.insert(0, FACTORY_ASSETS)
sys.path.insert(0, CHARS)

import stage
import sprites
import scenes
from PIL import Image, ImageDraw

img = scenes.den_bg()  # 1080x1920 locked room

# cast at their desks (matches the App-Settings skit frame)
sprites.paste(img, sprites.tejas("happy", "stand", 8), 300, 1568)
sprites.paste(img, sprites.zcode("happy", "hover", 8), 790, 1400)

# the speech bubble — skit style, real font so the words read
from PIL import ImageFont
FB = "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"
try:
    f_tag = ImageFont.truetype(FB, 30)
    f_line = ImageFont.truetype(FB, 34)
except Exception:
    f_tag = f_line = ImageFont.load_default()
d = ImageDraw.Draw(img)
bx0, by0, bx1, by1 = 30, 900, 760, 1070
d.rectangle([bx0, by0, bx1, by1], fill=stage.C("FFFFFF"), outline=stage.C("1A1626"), width=6)
d.polygon([(300, by1), (350, by1), (300, by1 + 30)], fill=stage.C("FFFFFF"))
d.line([(300, by1), (300, by1 + 30), (350, by1)], fill=stage.C("1A1626"), width=6)
d.rectangle([bx0 + 20, by0 + 20, bx0 + 200, by0 + 76], fill=stage.C("F2B33D"), outline=stage.C("1A1626"), width=4)
d.text((bx0 + 42, by0 + 28), "TEJAS", font=f_tag, fill=stage.C("1A1626"))
d.text((bx0 + 32, by0 + 96), "COME ON. IT'S ONE TOGGLE.", font=f_line, fill=stage.C("1A1626"))

# crop: keep the heads + desks, lose the ceiling
scene = img.crop((0, 700, 1080, 1640))
scene = scene.resize((540, 470), Image.NEAREST)
scene.save(OUT / "den-scene.png")
print("den scene:", scene.size, "->", OUT / "den-scene.png")
