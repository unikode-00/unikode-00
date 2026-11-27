"""Build self-contained GitHub profile artwork from pinned unikode brand assets.

Requires Python 3.10+, fonttools and brotli. Run from any directory.
The SVGs contain outlined type and no scripts, remote resources or animation.
"""
from pathlib import Path
from html import escape
import math
import random
import xml.etree.ElementTree as ET

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SOURCE = ASSETS / "source"

# Resolved from the accepted Design 3.0.0 dark shell tokens.
PALETTE = dict(ground="#1d1d1d", ink="#fafafa", body="#ebebeb",
               secondary="#a2a2a2", line="#6b6b6b", blue="#007efc")

def face(name, weight=400):
    f = TTFont(SOURCE / name)
    if "fvar" in f:
        f = instantiateVariableFont(f, {"wght": weight}, inplace=False)
    return f

FONTS = {
    "display": face("plus-jakarta-400.woff2", 300),
    "body": face("plus-jakarta-400.woff2", 400),
    "mono": face("jetbrains-mono-400.woff2", 400),
}

def text(value, x, y, size, kind="body", fill="ink"):
    f = FONTS[kind]
    glyphs = f.getGlyphSet()
    cmap = f.getBestCmap()
    paths, pos = [], 0
    for char in value:
        name = cmap.get(ord(char), ".notdef")
        pen = SVGPathPen(glyphs, ntos=lambda n: ("%.2f" % n).rstrip("0").rstrip("."))
        glyphs[name].draw(pen)
        d = pen.getCommands()
        if d:
            paths.append(f'<path transform="translate({pos} 0)" d="{d}"/>')
        pos += f["hmtx"][name][0]
    scale = size / f["head"].unitsPerEm
    return f'<g fill="{PALETTE.get(fill, fill)}" transform="translate({x} {y}) scale({scale:.7f} {-scale:.7f})" aria-label="{escape(value, quote=True)}">' + "".join(paths) + "</g>"

def wordmark(x, y, width):
    root = ET.parse(SOURCE / "unikode-wordmark-on-dark.svg").getroot()
    paths = "".join(ET.tostring(el, encoding="unicode") for el in root if not el.tag.endswith("title"))
    return f'<svg x="{x}" y="{y}" width="{width}" height="{width * 83 / 442:.3f}" viewBox="6 -81 442 83">{paths}</svg>'

def line(x1, y1, x2, y2, opacity=.5, width=.85):
    return f'<path d="M{x1:.2f},{y1:.2f} L{x2:.2f},{y2:.2f}" fill="none" stroke="{PALETTE["line"]}" stroke-opacity="{opacity}" stroke-width="{width}"/>'

def swarm(x, y, scale=1):
    """Two evidence flocks join a review node; asymmetric density and size."""
    rng = random.Random(27)
    points, groups = [], []
    for cx, cy, rx, ry, count, turn in [(116, 100, 94, 64, 47, -.2), (343, 94, 75, 52, 35, .3)]:
        group = []
        for i in range(count):
            angle = i * 2.3999632297 + turn
            radius = math.sqrt((i+.5)/count)
            px = cx + math.cos(angle)*radius*rx + rng.uniform(-4, 4)
            py = cy + math.sin(angle)*radius*ry + rng.uniform(-3, 3)
            group.append((px, py))
        points.extend(group)
        groups.append(group)
    pieces = []
    for group in groups:
        for i, p in enumerate(group):
            nearest = sorted(range(len(group)), key=lambda j: (p[0]-group[j][0])**2 + (p[1]-group[j][1])**2)
            for j in nearest[1:3]:
                if j > i:
                    pieces.append(line(*p, *group[j], opacity=.48))
    for group in groups:
        anchors = sorted(group, key=lambda p: (p[0]-230)**2 + (p[1]-228)**2)[:3]
        for px, py in anchors:
            pieces.append(f'<path d="M{px:.2f},{py:.2f} C{px:.2f},205 230,180 230,230" fill="none" stroke="{PALETTE["line"]}" stroke-width="1" stroke-opacity=".6"/>')
    for i, (px, py) in enumerate(points):
        radius = [2.2, 2.6, 3.1, 3.8, 5.2][(i*13)%5]
        ink = PALETTE["ink"] if i%4 == 0 else PALETTE["secondary"]
        pieces.append(f'<circle cx="{px:.2f}" cy="{py:.2f}" r="{radius}" fill="{ink}"/>')
    pieces.append(f'<circle cx="230" cy="230" r="9" fill="{PALETTE["blue"]}"/>')
    pieces.append(text("page-04", 64, 8, 20, "mono", "secondary"))
    pieces.append(text("page-09", 297, 8, 20, "mono", "secondary"))
    pieces.append(text("review", 194, 274, 20, "mono", "secondary"))
    return f'<g transform="translate({x} {y}) scale({scale})">' + "".join(pieces) + "</g>"

def shell(mobile=False):
    width, height = (640, 1540) if mobile else (1440, 690)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
      '<title id="title">unikode: I want git blame for a sentence.</title>',
      '<desc id="desc">Two fictional source pages give different ship dates. The .plan asks for a draft with both sources cited and the date left blank. Two connected swarms represent source evidence brought into review. The shell shows the actual diff between page-04.txt and page-09.txt.</desc>',
      f'<rect width="{width}" height="{height}" fill="{PALETTE["ground"]}"/>']
    if mobile:
        parts += [wordmark(40, 38, 260), text("~/unikode-00", 40, 136, 26, "mono", "secondary"),
                  text("$ cat .plan", 40, 218, 30, "mono", "secondary"),
                  text("I want git blame", 40, 310, 58, "display"),
                  text("for a sentence.", 40, 380, 58, "display")]
        for i, s in enumerate(["Two pages give two different", "ship dates. Either looks", "official on letterhead."]):
            parts.append(text(s, 40, 466+i*46, 34, fill="body"))
        for i, s in enumerate(["I build unikode for whoever", "signs that letter. Give them", "the draft, cite both pages,", "and leave the date blank."]):
            parts.append(text(s, 40, 662+i*46, 34, fill="body"))
        parts.append(swarm(62, 882, 1.1))
        parts.append(text("$ cd example", 40, 1268, 32, "mono", "secondary"))
        parts.append(text("$ diff page-04.txt page-09.txt", 40, 1312, 32, "mono", "secondary"))
        for i, s in enumerate(["1c1", "< The part shipped May 12.", "---", "> The part shipped May 21."]):
            parts.append(text(s, 40, 1372+i*42, 32, "mono", "body" if i in (1,3) else "secondary"))
    else:
        parts += [wordmark(64, 50, 250), text("~/unikode-00", 1137, 84, 22, "mono", "secondary"),
                  text("$ cat .plan", 64, 193, 24, "mono", "secondary"),
                  text("I want git blame", 64, 282, 66, "display"),
                  text("for a sentence.", 64, 361, 66, "display")]
        for i, s in enumerate(["Two pages give two different ship dates.", "Either looks official on letterhead."]):
            parts.append(text(s, 64, 433+i*36, 27, fill="body"))
        for i, s in enumerate(["I build unikode for whoever signs that letter.", "Give them the draft, cite both pages,", "and leave the date blank."]):
            parts.append(text(s, 64, 542+i*36, 27, fill="body"))
        parts.append(swarm(857, 156, 1.0))
        parts.append(text("$ cd example", 857, 470, 23, "mono", "secondary"))
        parts.append(text("$ diff page-04.txt page-09.txt", 857, 505, 23, "mono", "secondary"))
        for i, s in enumerate(["1c1", "< The part shipped May 12.", "---", "> The part shipped May 21."]):
            parts.append(text(s, 857, 548+i*31, 23, "mono", "body" if i in (1,3) else "secondary"))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"

if __name__ == "__main__":
    for mobile in (False, True):
        path = ASSETS / ("shell-mobile-v2.svg" if mobile else "shell-v2.svg")
        path.write_text(shell(mobile))
        print(f"Built {path.relative_to(ROOT)} ({path.stat().st_size:,} bytes)")
