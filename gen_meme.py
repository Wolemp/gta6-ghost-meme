"""Draws meme.png (1080x1080): make.fun's ghost, 13 years into the wait for GTA 6.

Run:  python gen_meme.py   (needs Pillow; reads assets/mark-1024.png, the make.fun press-kit mascot)
Everything except the mascot is drawn here.
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = 1080
HERE = os.path.dirname(os.path.abspath(__file__))


def font(size):
    for name in ("impact.ttf", "Impact.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf"):
        for base in ("C:/Windows/Fonts/", ""):
            try:
                return ImageFont.truetype(base + name, size)
            except OSError:
                pass
    return ImageFont.load_default()


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def sky():
    img = Image.new("RGB", (W, W))
    d = ImageDraw.Draw(img)
    stops = [(0.0, (40, 10, 90)), (0.45, (190, 30, 140)), (0.7, (255, 110, 80)), (1.0, (255, 190, 90))]
    for y in range(W):
        t = y / W
        for i in range(len(stops) - 1):
            if stops[i][0] <= t <= stops[i + 1][0]:
                u = (t - stops[i][0]) / (stops[i + 1][0] - stops[i][0])
                d.line([(0, y), (W, y)], fill=lerp(stops[i][1], stops[i + 1][1], u))
                break
    return img


def sun(img):
    d = ImageDraw.Draw(img)
    cx, cy, r = 540, 600, 300
    for i in range(r, 0, -2):
        t = i / r
        d.ellipse([cx - i, cy - i, cx + i, cy + i], fill=lerp((255, 235, 120), (255, 90, 120), t))
    # retro stripes cut into the sun
    for k in range(8):
        y = cy + 20 + k * 30
        h = 3 + k * 2
        d.rectangle([cx - r, y, cx + r, y + h], fill=lerp((200, 40, 130), (255, 130, 90), 0.4 + k * 0.05))


def palm(d, x, base_y, height, lean, col):
    pts = []
    for i in range(21):
        t = i / 20
        pts.append((x + lean * t * t * height, base_y - height * t))
    for i in range(20):
        w = 26 - 12 * (i / 20)
        d.line([pts[i], pts[i + 1]], fill=col, width=int(w))
    tx, ty = pts[-1]
    # fronds: drooping leaf shapes (filled polygons along a curved spine)
    for ang in (-170, -140, -105, -75, -40, -10, 15, 165):
        a = math.radians(ang)
        dx, dy = math.cos(a), math.sin(a)
        spine = []
        for i in range(13):
            t = i / 12
            spine.append((tx + dx * 190 * t, ty + dy * 120 * t + 70 * t * t))
        left, right = [], []
        for i, (px, py) in enumerate(spine):
            t = i / 12
            wd = 24 * math.sin(math.pi * min(1, t * 1.1)) + 2
            left.append((px, py - wd))
            right.append((px, py + wd))
        d.polygon(left + right[::-1], fill=col)
    d.ellipse([tx - 16, ty - 16, tx + 16, ty + 16], fill=col)


def ground(img):
    d = ImageDraw.Draw(img)
    horizon = 760
    d.rectangle([0, horizon, W, W], fill=(30, 8, 60))
    # neon grid road
    for i in range(-14, 15):
        d.line([(540 + i * 28, horizon), (540 + i * 180, W)], fill=(255, 60, 170), width=3)
    y, step = horizon, 8
    while y < W:
        d.line([(0, y), (W, y)], fill=(255, 60, 170), width=3)
        y += step
        step = int(step * 1.35) + 1
    # distant skyline silhouettes
    random.seed(6)
    x = 0
    while x < W:
        w = random.randint(30, 70)
        h = random.randint(30, 110)
        d.rectangle([x, horizon - h, x + w, horizon], fill=(45, 10, 80))
        x += w + random.randint(0, 6)
    return img


def outlined(d, xy, text, f, fill, stroke=10, anchor="mm", sc=(20, 8, 40)):
    d.text(xy, text, font=f, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=sc)


def main():
    img = sky()
    sun(img)
    img = ground(img)
    d = ImageDraw.Draw(img)

    dark = (22, 5, 45)
    palm(d, 120, 800, 520, 0.35, dark)
    palm(d, 980, 800, 460, -0.35, dark)
    palm(d, 30, 880, 300, 0.25, dark)

    # make.fun's ghost, big, standing on the road, dusty with cobwebs and a beard of dust
    mark = Image.open(os.path.join(HERE, "assets", "mark-1024.png")).convert("RGBA")
    size = 600
    mark = mark.resize((size, size), Image.LANCZOS)
    gx, gy = (W - size) // 2, 330
    shadow = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).ellipse([gx + 70, gy + size - 90, gx + size - 70, gy + size - 20], fill=(0, 0, 0, 150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    img.paste(shadow, (0, 0), shadow)
    img.paste(mark, (gx, gy), mark)
    d = ImageDraw.Draw(img)

    # cobweb across the ghost's top-left shoulder
    cx, cy = gx + 130, gy + 135
    for a in range(0, 90, 18):
        r = math.radians(a)
        d.line([(cx, cy), (cx + math.cos(r) * 150, cy + math.sin(r) * 150)], fill=(235, 235, 245), width=3)
    for rad in (40, 80, 120, 150):
        pts = [(cx + math.cos(math.radians(a)) * rad, cy + math.sin(math.radians(a)) * rad) for a in range(0, 91, 15)]
        d.line(pts, fill=(235, 235, 245), width=3)

    # tally marks of the years, scratched on the road
    # captions
    outlined(d, (540, 95), "13 YEARS WAITING", font(112), (255, 255, 255))
    outlined(d, (540, 200), "FOR GTA 6", font(112), (255, 225, 80))
    outlined(d, (540, 985), "NOW I'M THE GHOST", font(108), (255, 255, 255))

    # sign in the scene: Leonida road sign carrying make.fun
    sx, sy = 850, 700
    d.rectangle([sx + 55, sy + 80, sx + 70, sy + 215], fill=(60, 60, 70))
    d.rounded_rectangle([sx - 40, sy, sx + 170, sy + 90], 14, fill=(20, 110, 90), outline=(255, 255, 255), width=5)
    d.text((sx + 65, sy + 28), "LEONIDA", font=font(36), fill=(255, 255, 255), anchor="mm")
    d.text((sx + 65, sy + 64), "make.fun", font=font(30), fill=(255, 225, 80), anchor="mm")

    img.save(os.path.join(HERE, "meme.png"), optimize=True)


if __name__ == "__main__":
    main()
