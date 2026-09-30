import pathlib
from PIL import Image, ImageDraw, ImageFont

OUT = pathlib.Path(__file__).parent.parent / "assets"
NAVY = (31, 58, 95, 255)
PAPER = (247, 245, 240, 255)
GOLD = (143, 106, 46, 255)
FONT_PATH = r"C:\Windows\Fonts\georgia.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\georgiab.ttf"


def make_icon(size, radius_ratio=0.22):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius_ratio), fill=NAVY)
    font = ImageFont.truetype(FONT_PATH, int(size * 0.42))
    bbox = d.textbbox((0, 0), "NC", font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((size / 2 - w / 2 - bbox[0], size / 2 - h / 2 - bbox[1]), "NC", font=font, fill=PAPER)
    return img


# favicon.svg
svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#1F3A5F"/>
  <text x="32" y="43" font-family="Georgia, 'Fraunces', serif" font-size="27" font-weight="500" fill="#F7F5F0" text-anchor="middle">NC</text>
</svg>
'''
(OUT / "favicon.svg").write_text(svg, encoding="utf-8")

make_icon(512).save(OUT / "android-chrome-512.png")
make_icon(192).save(OUT / "android-chrome-192.png")
make_icon(180, radius_ratio=0).convert("RGB").save(OUT / "apple-touch-icon.png")

icon16 = make_icon(16)
icon32 = make_icon(32)
icon48 = make_icon(48)
icon16.save(OUT / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])

# 1200x630 Open Graph banner
og = Image.new("RGB", (1200, 630), NAVY[:3])
d = ImageDraw.Draw(og)
name_font = ImageFont.truetype(FONT_PATH, 78)
role_font = ImageFont.truetype(FONT_PATH, 34)
tag_font = ImageFont.truetype(FONT_PATH, 24)

d.text((90, 220), "Nanak Chaudhuri", font=name_font, fill=PAPER)
d.text((90, 330), "Strategic Collections & Recovery Leader", font=role_font, fill=(200, 155, 92, 255))
d.text((90, 390), "~24 years  ·  Financial Services / NBFC  ·  Eastern India", font=tag_font, fill=(207, 227, 234, 255))
d.line([(90, 180), (300, 180)], fill=(200, 155, 92, 255), width=3)
og.save(OUT / "og-image.jpg", format="JPEG", quality=90)

print("Icons + OG banner generated.")
