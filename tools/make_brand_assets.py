"""Generate favicon files and Open Graph share images.

    python tools/make_brand_assets.py

Writes src/static/favicon.svg, favicon-32.png, apple-touch-icon.png and
src/static/og/og-home.png + og-ai-video.png (1200x630).
Uses the self-hosted Fraunces + Figtree fonts. Edit TEXT to change the share cards.
The two pages are independent: the home card never mentions AI video and vice versa.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "src" / "static"
FONTS = STATIC / "fonts"
MEDIA = STATIC / "media"

CREAM = (251, 246, 239)
INK = (33, 26, 23)
INK2 = (91, 81, 75)
ACCENT = (179, 61, 14)
BLUSH = (248, 217, 221)
NIGHT = (18, 16, 16)
NIGHT_INK = (247, 239, 230)
NIGHT_INK2 = (196, 184, 173)
ACCENT_DARK = (240, 138, 82)

TEXT = {
    "home": {
        "eyebrow": "Data Scientist & AI Engineer · Brazil",
        "title": "AI and data systems that",
        "em": "hold up in production.",
        "foot": "LLMs · RAG · Databricks · Airflow · Machine learning",
    },
    "ai": {
        "eyebrow": "AI Video Creator · Brazil",
        "title": "Cinematic video,",
        "em": "made with AI.",
        "foot": "Game ad · 121 anime episodes · 27 series",
    },
}


def display(size: int, wonk: int = 1) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(FONTS / "fraunces-latin.woff2"), size)
    try:  # axes: opsz, wght, SOFT, WONK
        f.set_variation_by_axes([min(144, size), 560, 100, wonk])
    except Exception:
        pass
    return f


def sans(size: int, weight: int = 500) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(FONTS / "figtree-latin.woff2"), size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def sparkle(d: ImageDraw.ImageDraw, cx: float, cy: float, r: float, fill) -> None:
    """Four-point star, like the clips in her hair."""
    k = r * 0.22
    pts = [(cx, cy - r), (cx + k, cy - k), (cx + r, cy), (cx + k, cy + k),
           (cx, cy + r), (cx - k, cy + k), (cx - r, cy), (cx - k, cy - k)]
    d.polygon(pts, fill=fill)


def favicon() -> None:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="16" fill="#b33d0e"/>'
        '<path d="M32 8 L37.5 26.5 L56 32 L37.5 37.5 L32 56 L26.5 37.5 L8 32 L26.5 26.5 Z" fill="#fbf6ef"/>'
        "</svg>\n"
    )
    (STATIC / "favicon.svg").write_text(svg, encoding="utf-8")
    for size, name in ((32, "favicon-32.png"), (180, "apple-touch-icon.png")):
        S = size * 4
        im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.25), fill=ACCENT)
        sparkle(d, S / 2, S / 2, S * 0.375, CREAM)
        im.resize((size, size), Image.LANCZOS).save(STATIC / name)


def og(kind: str) -> None:
    W, H = 1200, 630
    t = TEXT[kind]
    dark = kind == "ai"
    bg, fg, sub, acc = (NIGHT, NIGHT_INK, NIGHT_INK2, ACCENT_DARK) if dark else (CREAM, INK, INK2, ACCENT)
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    text_w = 640

    if dark:
        frames = ["game-ad", "doomed-consort", "frozen-regret"]
        for i, slug in enumerate(frames):
            p = MEDIA / "video" / f"{slug}.webp"
            if not p.exists():
                continue
            fr = Image.open(p).convert("RGB")
            w, h = 150, 270
            if fr.width / fr.height > w / h:
                nw = int(fr.height * w / h)
                fr = fr.crop(((fr.width - nw) // 2, 0, (fr.width - nw) // 2 + nw, fr.height))
            fr = fr.resize((w, h), Image.LANCZOS)
            mask = Image.new("L", (w, h), 0)
            ImageDraw.Draw(mask).rounded_rectangle([0, 0, w, h], 16, fill=255)
            im.paste(fr, (720 + i * 160, 170 + (i % 2) * 40), mask)
    else:
        # Her portrait on a blush card, slightly tilted.
        card = Image.new("RGBA", (330, 420), (0, 0, 0, 0))
        ImageDraw.Draw(card).rounded_rectangle([0, 0, 329, 419], 36, fill=BLUSH + (255,))
        por = Image.open(MEDIA / "img" / "mica-illustration.webp").convert("RGBA")
        por.thumbnail((300, 400))
        card.alpha_composite(por, ((330 - por.width) // 2, 420 - por.height))
        mask = Image.new("L", card.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, 329, 419], 36, fill=255)
        card.putalpha(Image.composite(card.getchannel("A"), Image.new("L", card.size, 0), mask))
        card = card.rotate(2, resample=Image.BICUBIC, expand=True)
        im.paste(card, (800, 105), card)
        d = ImageDraw.Draw(im)

    sparkle(d, 76, 84, 13, acc)
    d.text((100, 84), "Micaelly Cristine", font=display(30), fill=fg, anchor="lm")
    d.text((64, 190), t["eyebrow"], font=sans(26, 600), fill=sub)

    size = 68
    f_title = display(size)
    words = t["title"].split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if d.textlength(test, font=f_title) > text_w and cur:
            lines.append(cur)
            cur = wd
        else:
            cur = test
    lines.append(cur)
    y = 240
    for ln in lines:
        d.text((64, y), ln, font=f_title, fill=fg)
        y += int(size * 1.08)
    d.text((64, y), t["em"], font=f_title, fill=acc)
    d.text((64, 560), t["foot"], font=sans(22, 500), fill=sub)

    out = STATIC / "og"
    out.mkdir(exist_ok=True)
    im.save(out / ("og-home.png" if kind == "home" else "og-ai-video.png"), optimize=True)


if __name__ == "__main__":
    favicon()
    og("home")
    og("ai")
    print("favicon + og images written")
