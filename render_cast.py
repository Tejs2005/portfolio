"""Render the LOCKED cast sprites (tejas, zcode) + the new crew (opencode,
hermes, qwen) drawn in the same box style with the locked palette.
Output: ~/tejas/portfolio/cast/*.png (transparent, NEAREST-upscaled).
"""
import sys
from pathlib import Path

FACTORY_ASSETS = "/home/linux/youtube-automation/factory/skit_assets"
CHARS = "/home/linux/youtube-automation/docs/skit/characters"
OUT = Path.home() / "tejas/portfolio/cast"
OUT.mkdir(exist_ok=True)

sys.path.insert(0, FACTORY_ASSETS)
sys.path.insert(0, CHARS)

import draw_preview as dp  # locked geometry + palette
from stage import sprite_box
import stage
from PIL import Image, ImageDraw

# ---- 1. the originals, straight from the locked source ----
casts = {
    "tejas": (dp.draw_tejas("happy"),),
    "tejas-neutral": (dp.draw_tejas("neutral"),),
    "zcode": (dp.draw_zcode("happy"),),
}
for name, (img,) in casts.items():
    img = img.resize((img.width * 1, img.height * 1), Image.NEAREST)  # 1x native: page shows at 2x = crisp
    img.save(OUT / f"{name}.png")
    print("rendered", name, img.size)

# ---- 2. the crew: opencode / hermes / qwen in the same box style ----
# box style = sprite_box(d, x0, y0, x1, y1, fill, ol=dp.INK)
SPR_W, SPR_H = 64, 80

def new_sprite(painter):
    img = Image.new("RGBA", (SPR_W, SPR_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    painter(d)
    img = img.resize((img.width * 1, img.height * 1), Image.NEAREST)  # 1x native: page shows at 2x = crisp
    return img

# palette extensions (locked family + one accent each)
TERM    = dp.C("56B8CC")   # opencode: terminal teal (same family as GLOW_LOW)
TERM_DK = dp.C("2e5f66")
WING    = dp.C("7FA6CF")   # hermes: messenger blue (spec family)
WING_DK = dp.C("3a5a85")
CHIP    = dp.C("9b6df0")   # qwen: violet gpu
CHIP_DK = dp.C("3d2a66")

def draw_opencode(d):
    # blocky bot with a terminal face (like zcode's shell but teal, CRT screen head)
    sprite_box(d, 20, 6, 44, 30, dp.SHELL_DK)                 # head shell
    sprite_box(d, 23, 9, 41, 26, dp.C("0b1214"))              # CRT screen
    sprite_box(d, 26, 13, 38, 16, TERM)                       # glow eyes bar
    sprite_box(d, 26, 20, 34, 18 + 4, TERM)                   # mouth cursor line
    sprite_box(d, 30, 2, 34, 6, dp.SHELL)                     # antenna
    sprite_box(d, 16, 32, 48, 56, dp.SHELL)                   # body
    sprite_box(d, 20, 38, 28, 48, TERM_DK)                    # chest panel
    sprite_box(d, 31, 41, 33, 43, dp.WHITE)                   # power dot
    sprite_box(d, 12, 33, 17, 50, dp.SHELL_DK)                # arms
    sprite_box(d, 47, 33, 52, 50, dp.SHELL_DK)
    sprite_box(d, 12, 50, 17, 54, dp.SHELL)                   # mitts
    sprite_box(d, 47, 50, 52, 54, dp.SHELL)
    sprite_box(d, 21, 57, 30, 72, dp.SHELL_DK)                # legs
    sprite_box(d, 34, 57, 43, 72, dp.SHELL_DK)
    sprite_box(d, 20, 72, 31, 78, dp.SHELL)                   # boots
    sprite_box(d, 33, 72, 44, 78, dp.SHELL)

def draw_hermes(d):
    # blocky messenger: winged cap, letter satchel — skin head like tejas
    sprite_box(d, 20, 10, 44, 32, dp.SKIN)                    # head
    sprite_box(d, 18, 6, 46, 14, WING_DK)                     # cap
    sprite_box(d, 44, 4, 52, 12, WING)                        # wing right
    sprite_box(d, 12, 4, 20, 12, WING)                        # wing left
    sprite_box(d, 24, 20, 28, 24, dp.INK)                     # eyes
    sprite_box(d, 36, 20, 40, 24, dp.INK)
    sprite_box(d, 28, 27, 36, 29, dp.INK)                     # mouth
    sprite_box(d, 18, 34, 46, 58, dp.SHIRT)                   # tunic (teal family)
    sprite_box(d, 18, 34, 46, 38, dp.SHIRT_SH)
    sprite_box(d, 28, 42, 36, 52, dp.C("F2B33D"))             # satchel flap (gold stripe)
    sprite_box(d, 26, 52, 38, 60, dp.C("C98a20"))             # satchel body
    sprite_box(d, 12, 34, 17, 50, dp.SHIRT)
    sprite_box(d, 47, 34, 52, 50, dp.SHIRT)
    sprite_box(d, 12, 50, 17, 54, dp.SKIN)
    sprite_box(d, 47, 50, 52, 54, dp.SKIN)
    sprite_box(d, 21, 58, 30, 74, dp.C("4a3a2a"))             # greaves
    sprite_box(d, 34, 58, 43, 74, dp.C("4a3a2a"))
    sprite_box(d, 20, 74, 31, 80, dp.SHOES)
    sprite_box(d, 33, 74, 44, 80, dp.SHOES)

def draw_qwen(d):
    # blocky chip-bot: violet, GPU die face, heatsink crown
    sprite_box(d, 20, 8, 44, 30, CHIP_DK)                     # head
    sprite_box(d, 23, 12, 41, 27, dp.C("0b0e14"))             # die face
    sprite_box(d, 26, 15, 30, 19, CHIP)                       # eye L
    sprite_box(d, 34, 15, 38, 19, CHIP)                       # eye R
    sprite_box(d, 27, 23, 37, 25, CHIP)                       # mouth bar
    sprite_box(d, 16, 4, 48, 8, dp.SHELL_DK)                  # heatsink crown
    sprite_box(d, 20, 0, 24, 5, dp.SHELL_DK)
    sprite_box(d, 28, 0, 32, 5, dp.SHELL_DK)
    sprite_box(d, 36, 0, 40, 5, dp.SHELL_DK)
    sprite_box(d, 44, 0, 48, 5, dp.SHELL_DK)
    sprite_box(d, 18, 32, 46, 56, CHIP)                       # body
    sprite_box(d, 18, 32, 46, 36, CHIP_DK)
    sprite_box(d, 24, 40, 40, 50, dp.C("0b0e14"))             # gpu die on chest
    sprite_box(d, 27, 43, 30, 46, dp.WHITE)
    sprite_box(d, 34, 43, 37, 46, CHIP)
    sprite_box(d, 12, 33, 17, 50, CHIP_DK)
    sprite_box(d, 47, 33, 52, 50, CHIP_DK)
    sprite_box(d, 12, 50, 17, 54, dp.SHELL)
    sprite_box(d, 47, 50, 52, 54, dp.SHELL)
    sprite_box(d, 21, 57, 30, 72, dp.C("241a4d"))
    sprite_box(d, 34, 57, 43, 72, dp.C("241a4d"))
    sprite_box(d, 20, 72, 31, 78, dp.SHELL)
    sprite_box(d, 33, 72, 44, 78, dp.SHELL)

for name, fn in [("opencode", draw_opencode), ("hermes", draw_hermes), ("qwen", draw_qwen)]:
    img = new_sprite(fn)
    img.save(OUT / f"{name}.png")
    print("rendered", name, img.size)
print("ALL DONE ->", OUT)
