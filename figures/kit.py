"""Promorphic docs figure kit.

Brand rules (design/brand-guide.md): neutral grounds, neutral text, hairline edges,
ink-faint lines for what is possible, one amber line for what happens, amber squares
(ports) where Promorphic touches something, mono labels in ink-muted. Amber fill only
for Promorphic itself. No icons, no gradients, no shadows.
"""
from pathlib import Path
from PIL import ImageFont
import html as _html

ROOT = Path(__file__).parent
FONTS = ROOT / "fonts"
SRC = ROOT / "src"

C = dict(s0="#0b0c0e", s1="#14161a", s2="#1c1f24", hair="#2a2e35", ink="#f2efe8",
         muted="#a8a49b", faint="#8a867e", brand="#f2b135", onbrand="#14110a")

_font_cache = {}


def _font(kind, size, wght):
    key = (kind, size, wght)
    if key not in _font_cache:
        f = ImageFont.truetype(str(FONTS / ("Schibsted.ttf" if kind == "sans" else "GeistMono.ttf")), size)
        try:
            f.set_variation_by_axes([wght])
        except Exception:
            pass
        _font_cache[key] = f
    return _font_cache[key]


STYLES = {
    # name: (kind, size, weight, letter-spacing em, upper, fill)
    "title": ("sans", 15, 500, 0, False, "ink"),
    "title-lg": ("sans", 18, 500, -0.01, False, "ink"),
    "body": ("sans", 13, 400, 0, False, "muted"),
    "body-ink": ("sans", 13, 400, 0, False, "ink"),
    "sub": ("mono", 11, 400, 0.01, False, "muted"),
    "sub-faint": ("mono", 11, 400, 0.01, False, "faint"),
    "label": ("mono", 11, 500, 0.12, True, "muted"),
    "label-ink": ("mono", 11, 500, 0.12, True, "ink"),
    "label-faint": ("mono", 10.5, 500, 0.12, True, "faint"),
    "num": ("mono", 22, 500, -0.02, False, "ink"),
}

WARN = []


def tw(s, style):
    kind, size, wght, ls, up, _ = STYLES[style]
    s2 = s.upper() if up else s
    f = _font(kind, int(round(size)), wght)
    return f.getlength(s2) * (size / int(round(size))) + ls * size * len(s2)


def esc(s):
    return _html.escape(s, quote=False)


def n(v):
    s = f"{round(v + 0.0, 1):.1f}"
    return s[:-2] if s.endswith(".0") else s


class Fig:
    def __init__(self, name, w, h, eyebrow, title, caption=None, rules=True):
        self.name, self.w, self.h = name, w, h
        self.eyebrow, self.title, self.caption = eyebrow, title, caption
        self.el = []
        self.rules = rules

    # ── primitives ──
    def text(self, x, y, s, style="body", anchor="start", fill=None, maxw=None):
        kind, size, wght, ls, up, f = STYLES[style]
        if maxw and tw(s, style) > maxw:
            WARN.append(f"{self.name}: '{s}' {tw(s, style):.0f}px > {maxw:.0f}px")
        col = C[fill or f]
        s2 = s.upper() if up else s
        fam = "var(--sans)" if kind == "sans" else "var(--mono)"
        self.el.append(
            f'<text x="{n(x)}" y="{n(y)}" text-anchor="{anchor}" dominant-baseline="central" '
            f'style="font-family:{fam};font-size:{size}px;font-weight:{wght};letter-spacing:{ls}em" '
            f'fill="{col}">{esc(s2)}</text>')

    def lines(self, x, y, rows, style="body", anchor="start", lh=18, fill=None, maxw=None):
        for i, r in enumerate(rows):
            self.text(x, y + i * lh, r, style, anchor, fill, maxw)

    def rect(self, x, y, w, h, fill="s1", stroke="hair", dash=False, rx=2, sw=1):
        d = ' stroke-dasharray="4 4"' if dash else ""
        fl = "none" if fill is None else C[fill]
        st = "none" if stroke is None else C[stroke]
        self.el.append(f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{rx}" fill="{fl}" stroke="{st}" stroke-width="{sw}"{d}/>')

    def port(self, x, y, s=7, fill="brand"):
        self.el.append(f'<rect x="{n(x - s / 2)}" y="{n(y - s / 2)}" width="{s}" height="{s}" fill="{C[fill]}"/>')

    def node(self, x, y, s=8):
        self.el.append(f'<rect x="{n(x - s / 2)}" y="{n(y - s / 2)}" width="{s}" height="{s}" fill="{C["s0"]}" stroke="{C["faint"]}" stroke-width="1"/>')

    def mark(self, x, y, scale=0.75, on="ink"):
        col = C[on]
        self.el.append(
            f'<g transform="translate({n(x)} {n(y)}) scale({scale})">'
            f'<rect x="0" y="0" width="18" height="11" fill="{col}"/>'
            f'<rect x="0" y="13" width="32" height="6" fill="{C["brand"] if on == "ink" else col}"/>'
            f'<rect x="14" y="21" width="18" height="11" fill="{col}"/></g>')

    # ── boxes ──
    def box(self, x, y, w, h, title, sub=None, kind="plain", align="center", title_style="title", sub2=None):
        """kind: plain (third party / neutral), pm (Promorphic-owned: amber port on corner),
        brand (amber block = the Promorphic agent/layer itself), inset (surface-2), ghost (dashed)."""
        if kind == "brand":
            self.rect(x, y, w, h, fill="brand", stroke=None)
        elif kind == "inset":
            self.rect(x, y, w, h, fill="s2")
        elif kind == "ghost":
            self.rect(x, y, w, h, fill=None, dash=True)
        else:
            self.rect(x, y, w, h, fill="s1")
        tf = "onbrand" if kind == "brand" else None
        sf = "onbrand" if kind == "brand" else None
        rows = [r for r in [sub, sub2] if r]
        total = 20 + 16 * len(rows)
        cy = y + h / 2 - total / 2 + 9
        pad = 14
        if align == "center":
            tx, an = x + w / 2, "middle"
        else:
            tx, an = x + pad, "start"
        self.text(tx, cy, title, title_style, an, tf, maxw=w - 2 * pad)
        for i, r in enumerate(rows):
            self.text(tx, cy + 20 + i * 16, r, "sub", an, sf, maxw=w - 2 * pad)
        if kind == "pm":
            self.port(x + 7, y + 7, s=6)
        return (x, y, w, h)

    def container(self, x, y, w, h, label, dash=True, fill=None, label_style="label"):
        self.rect(x, y, w, h, fill=fill, dash=dash)
        lw = tw(label, label_style)
        self.rect(x + 12, y - 9, lw + 16, 18, fill="s0", stroke=None, rx=0)
        self.text(x + 20, y, label, label_style)

    def tag(self, x, y, s, brand=False, anchor="start"):
        """A boxed mono tag. brand=True: amber tag (on-brand text), like the site's tier headings."""
        w = tw(s, "label") + 16
        x0 = x if anchor == "start" else (x - w / 2 if anchor == "middle" else x - w)
        if brand:
            self.rect(x0, y - 10, w, 20, fill="brand", stroke=None, rx=1)
            self.text(x0 + 8, y, s, "label", fill="onbrand")
        else:
            self.rect(x0, y - 10, w, 20, fill="s0", rx=1)
            self.text(x0 + 8, y, s, "label")
        return w

    # ── connectors ──
    def path(self, pts, kind="faint", arrow=True, dash=False, r=8, start_port=False, both=False):
        d = _rounded(pts, r)
        col = {"faint": C["faint"], "brand": C["brand"], "hair": C["hair"], "ink": C["ink"]}[kind]
        sw = 2 if kind == "brand" else 1.25
        da = ' stroke-dasharray="5 5"' if dash else ""
        mk = f' marker-end="url(#a-{kind})"' if arrow else ""
        if both:
            mk += f' marker-start="url(#a-{kind})"' 
        self.el.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{da}{mk}/>')
        if start_port:
            self.port(*pts[0], s=6)

    def arrow_label(self, x, y, s, anchor="middle", style="sub-faint", bg=True):
        if bg:
            w = tw(s, style) + 10
            x0 = x - w / 2 if anchor == "middle" else (x - 5 if anchor == "start" else x - w + 5)
            self.rect(x0, y - 9, w, 18, fill="s0", stroke=None, rx=0)
        self.text(x, y, s, style, anchor)

    def legend(self, x, y, items):
        """items: list of (kind, text). kinds: pm, brand-line, faint-line, brand-block, plain, ghost, dash-line"""
        cx = x
        for kind, s in items:
            if kind == "pm":
                self.rect(cx, y - 7, 18, 14, fill="s1"); self.port(cx + 4, y - 3, s=4); off = 26
            elif kind == "plain":
                self.rect(cx, y - 7, 18, 14, fill="s1"); off = 26
            elif kind == "ghost":
                self.rect(cx, y - 7, 18, 14, fill=None, dash=True); off = 26
            elif kind == "brand-block":
                self.rect(cx, y - 7, 18, 14, fill="brand", stroke=None); off = 26
            elif kind == "brand-line":
                self.path([(cx, y), (cx + 24, y)], "brand", arrow=False); off = 32
            elif kind == "faint-line":
                self.path([(cx, y), (cx + 24, y)], "faint", arrow=False); off = 32
            elif kind == "dash-line":
                self.path([(cx, y), (cx + 24, y)], "faint", arrow=False, dash=True); off = 32
            self.text(cx + off, y, s, "sub")
            cx += off + tw(s, "sub") + 28

    # ── output ──
    def svg(self):
        rules = ""
        if self.rules:
            rules = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{self.h}" stroke="{C["hair"]}" stroke-width="1" opacity=".35"/>'
                            for x in range(64, self.w, 64))
        defs = "<defs>" + "".join(
            f'<marker id="a-{k}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse" markerUnits="userSpaceOnUse">'
            f'<path d="M1.5 1.5L8.5 5L1.5 8.5" fill="none" stroke="{c}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>'
            for k, c in [("faint", C["faint"]), ("brand", C["brand"]), ("hair", C["hair"]), ("ink", C["ink"])]) + "</defs>"
        return f'<svg width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" xmlns="http://www.w3.org/2000/svg">{defs}{rules}{"".join(self.el)}</svg>'

    def write(self):
        cap = f'<div class="cap">{esc(self.caption)}</div>' if self.caption else ""
        page = PAGE.format(w=self.w, eyebrow=esc(self.eyebrow), title=esc(self.title), svg=self.svg(), cap=cap)
        (SRC / f"{self.name}.html").write_text(page)


def _rounded(pts, r):
    p2 = [pts[0]]
    for p in pts[1:]:
        if p != p2[-1]:
            p2.append(p)
    pts = p2
    # drop collinear middle points
    q = [pts[0]]
    for i in range(1, len(pts) - 1):
        (x0, y0), (x1, y1), (x2, y2) = q[-1], pts[i], pts[i + 1]
        if (x1 - x0) * (y2 - y1) - (y1 - y0) * (x2 - x1) != 0:
            q.append(pts[i])
    q.append(pts[-1])
    pts = q
    if len(pts) == 2 or r == 0:
        return "M" + " L".join(f"{n(x)} {n(y)}" for x, y in pts)
    out = [f"M{n(pts[0][0])} {n(pts[0][1])}"]
    for i in range(1, len(pts) - 1):
        (x0, y0), (x1, y1), (x2, y2) = pts[i - 1], pts[i], pts[i + 1]
        import math
        d1 = math.hypot(x1 - x0, y1 - y0); d2 = math.hypot(x2 - x1, y2 - y1)
        rr = min(r, d1 / 2, d2 / 2)
        ax, ay = x1 - (x1 - x0) / d1 * rr, y1 - (y1 - y0) / d1 * rr
        bx, by = x1 + (x2 - x1) / d2 * rr, y1 + (y2 - y1) / d2 * rr
        out.append(f"L{n(ax)} {n(ay)} Q{n(x1)} {n(y1)} {n(bx)} {n(by)}")
    out.append(f"L{n(pts[-1][0])} {n(pts[-1][1])}")
    return " ".join(out)


PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:SG;src:url(../fonts/Schibsted.ttf);font-weight:100 900}}
@font-face{{font-family:GM;src:url(../fonts/GeistMono.ttf);font-weight:100 900}}
:root{{--sans:SG,sans-serif;--mono:GM,monospace}}
html,body{{margin:0;background:#0b0c0e}}
.frame{{width:{w}px;padding:40px 48px 36px;background:#0b0c0e;color:#f2efe8;font-family:var(--sans)}}
.eb{{font-family:var(--mono);font-size:12px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:#a8a49b;display:flex;align-items:center;gap:12px}}
.eb:after{{content:"";width:32px;height:1px;background:#2a2e35}}
h1{{font-weight:500;font-size:28px;letter-spacing:-.015em;line-height:1.2;margin:12px 0 28px}}
.cap{{font-family:var(--mono);font-size:12px;color:#8a867e;margin-top:20px;letter-spacing:.01em}}
svg{{display:block}}
</style></head><body><div class="frame"><div class="eb">{eyebrow}</div><h1>{title}</h1>{svg}{cap}</div></body></html>"""
