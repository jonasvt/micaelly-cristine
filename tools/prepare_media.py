"""Prepare web-ready media (videos, posters, images) from the raw files.

Raw files live in `source-materials/` (not committed: too big).
Output goes to `src/static/media/`, which IS committed and deployed.

Requirements: Python 3.10+, Pillow, and ffmpeg/ffprobe on PATH.

Usage:
    python tools/prepare_media.py            # build everything that is missing
    python tools/prepare_media.py --force    # rebuild everything
    python tools/prepare_media.py --only videos

To add a new AI video: put the source file somewhere under source-materials/,
add an entry to VIDEOS below (slug, source, poster_at), run this script, then
add a matching entry to content/ai-video.json using the same slug.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source-materials"
OUT = ROOT / "src" / "static" / "media"

ANIME_ZIPS = sorted((SRC / "animepocky").glob("Creator 5-*.zip"))

# ---------------------------------------------------------------------------
# Videos. `source` is either a path relative to source-materials/ or
# "zip:<member path>" for a file inside the AnimePocky "Creator 5" zips.
# `poster_at` = second used for the poster frame. `kind` = vertical | landscape.
# ---------------------------------------------------------------------------
VIDEOS = [
    # --- Episode grid (lower section). Different series from the header fan on purpose. ---
    {
        "slug": "americas-ex-husband",
        "source": "zip:Creator 5/America_s Favorite Ex-Husband/1- America_s Favorite Ex-Husband.mp4",
        "kind": "vertical",
        "poster_at": 18.0,
    },
    {
        "slug": "chained-by-loyalty",
        "source": "zip:Creator 5/Chained by Loyalty_ An Exclusive Chapter Reading with Damon Hayes/1- Chained by Loyalty_ An Exclusive Chapter Reading with Damon Hayes.mp4",
        "kind": "vertical",
        "poster_at": 9.1,
    },
    {
        "slug": "claiming-the-luna",
        "source": "zip:Creator 5/Claiming the Luna/2- Claiming the Luna.mp4",
        "kind": "vertical",
        "poster_at": 18.9,
    },
    {
        "slug": "shadows-between-us",
        "source": "zip:Creator 5/The Shadows Between Us/2 - The Shadows Between Us.mp4",
        "kind": "vertical",
        "poster_at": 7.4,
    },
    {
        "slug": "hidden-healer-goddess",
        "source": "zip:Creator 5/The Hidden Healer Goddess/2- The Hidden Healer Goddess.mp4",
        "kind": "vertical",
        "poster_at": 86.4,
    },
    # --- Header fan + cinematic ad (and Studio Diary, also in the grid). ---
    {
        "slug": "game-ad",
        "source": "game-ad/Example 02.mp4",
        "kind": "landscape",
        "poster_at": 22.4,
    },
    {
        "slug": "billionaire-hearts",
        "full": False,  # header fan only: poster + preview, no full episode
        "source": "zip:Creator 5/Billionaire Hearts and Fireworks/1- Billionaire Hearts and Fireworks.mp4",
        "kind": "vertical",
        "poster_at": 36.8,
    },
    {
        "slug": "doomed-consort",
        "full": False,  # header fan only: poster + preview, no full episode
        "source": "zip:Creator 5/The Doomed Consort/1- The Doomed Consort.mp4",
        "kind": "vertical",
        "poster_at": 18.3,
    },
    {
        "slug": "studio-diary",
        "source": "zip:Creator 5/Studio Diary EP 60 - A Day Filming with Me/1- Studio Diary EP 60 - A Day Filming with Me.mp4",
        "kind": "vertical",
        "poster_at": 35.0,
    },
    {
        "slug": "love-tides",
        "full": False,  # header fan only: poster + preview, no full episode
        "source": "zip:Creator 5/Love Tides EP 61 - Valentine by the Shore/1- Love Tides EP 61 - Valentine by the Shore.mp4",
        "kind": "vertical",
        "poster_at": 22.0,
    },
    {
        "slug": "frozen-regret",
        "full": False,  # header fan only: poster + preview, no full episode
        "source": "zip:Creator 5/Walking Away From My Alpha’s Frozen Regret/1 - Walking Away From My Alpha’s Frozen Regret.mp4",
        "kind": "vertical",
        "poster_at": 13.7,
    },
    {
        "slug": "mommy-kept-the-truth",
        "full": False,  # header fan only: poster + preview, no full episode
        "source": "zip:Creator 5/Daddy Lost the Past, Mommy Kept the Truth/1- Daddy Lost the Past, Mommy Kept the Truth.mp4",
        "kind": "vertical",
        "poster_at": 3.8,
    },
]

def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdin=subprocess.DEVNULL)


def resolve_video(source: str, tmp: Path) -> Path:
    if not source.startswith("zip:"):
        return SRC / source
    member = source[4:]
    for z in ANIME_ZIPS:
        with zipfile.ZipFile(z) as zf:
            if member in zf.namelist():
                target = tmp / Path(member).name
                with zf.open(member) as fsrc, open(target, "wb") as fdst:
                    shutil.copyfileobj(fsrc, fdst)
                return target
    raise FileNotFoundError(f"{member} not found in {ANIME_ZIPS}")


def build_video(v: dict, force: bool) -> None:
    vdir = OUT / "video"
    vdir.mkdir(parents=True, exist_ok=True)
    mp4 = vdir / f"{v['slug']}.mp4"
    poster = vdir / f"{v['slug']}.webp"
    full = v.get("full", True)
    if (mp4.exists() or not full) and poster.exists() and not force:
        print("skip", v["slug"])
        return
    with tempfile.TemporaryDirectory() as td:
        src = resolve_video(v["source"], Path(td))
        if v["kind"] == "landscape":
            vf = "scale=1280:-2,fps=30"
            crf = "23"
            poster_w = 1280
        else:
            vf = "scale=720:-2,fps=24"
            crf = "27"
            poster_w = 540
        if full:
            run([
                "ffmpeg", "-v", "error", "-y", "-i", str(src),
                "-vf", vf, "-c:v", "libx264", "-preset", "slow", "-crf", crf,
                "-profile:v", "high", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart",
                str(mp4),
            ])
        png = Path(td) / "poster.png"
        run([
            "ffmpeg", "-v", "error", "-y", "-ss", str(v["poster_at"]), "-i", str(src),
            "-frames:v", "1", "-vf", f"scale={poster_w}:-2", str(png),
        ])
        Image.open(png).convert("RGB").save(poster, "WEBP", quality=80, method=6)
    print("built", v["slug"], f"{mp4.stat().st_size / 1e6:.1f} MB" if full else "(poster only)")


PREVIEW_SECONDS = 4


def build_preview(v: dict, force: bool) -> None:
    """Tiny muted 4-second loop (360px wide) used by the animated poster fan
    in the AI page header. Cut from the web MP4, starting near the poster frame."""
    if v["kind"] != "vertical":
        return
    vdir = OUT / "video"
    out = vdir / f"{v['slug']}-preview.mp4"
    if out.exists() and not force:
        return
    start = max(0.0, v["poster_at"] - 0.5)
    with tempfile.TemporaryDirectory() as td:
        src = vdir / f"{v['slug']}.mp4"
        if not src.exists():
            src = resolve_video(v["source"], Path(td))
        _cut_preview(src, start, out)
    print("preview", v["slug"], f"{out.stat().st_size / 1e3:.0f} KB")


def _cut_preview(src: Path, start: float, out: Path) -> None:
    run([
        "ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(PREVIEW_SECONDS), "-i", str(src),
        "-vf", "scale=360:-2,fps=24", "-an", "-c:v", "libx264", "-preset", "slow", "-crf", "30",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out),
    ])


def build_images(force: bool) -> None:
    idir = OUT / "img"
    idir.mkdir(parents=True, exist_ok=True)
    # Illustrated portrait (transparent sticker version).
    avatar = idir / "mica-illustration.webp"
    if force or not avatar.exists():
        im = Image.open(SRC / "brand" / "96 Sem Título_20251218230015.png").convert("RGBA")
        im.thumbnail((640, 800))
        im.save(avatar, "WEBP", quality=86, method=6)
    print("images ok")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", choices=["videos", "images"])
    args = ap.parse_args()
    if shutil.which("ffmpeg") is None:
        print("ffmpeg not found on PATH", file=sys.stderr)
        return 1
    if args.only in (None, "videos"):
        for v in VIDEOS:
            build_video(v, args.force)
            build_preview(v, args.force)
    if args.only in (None, "images"):
        build_images(args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
