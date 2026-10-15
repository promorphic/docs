"""Build docs.promorphic.xyz from the markdown in this repo.

    pip install markdown
    python3 build_site.py          # writes _site/

One page per chapter, a sidebar, the Promorphic brand (dark, neutral ink, amber only for
the mark and the active page marker), fonts served locally. No JavaScript.
"""
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
OUT = ROOT / "_site"
DOMAIN = "docs.promorphic.xyz"

PAGES = [
    ("README.md", "index.html", "Overview"),
    ("01-thesis.md", "thesis.html", "1 · Thesis"),
    ("02-product.md", "product.html", "2 · Product"),
    ("03-architecture.md", "architecture.html", "3 · Architecture"),
    ("04-vaults.md", "vaults.html", "4 · Vaults"),
    ("05-mandate.md", "mandate.html", "5 · Mandate"),
    ("06-agents.md", "agents.html", "6 · Agents"),
    ("07-flows.md", "flows.html", "7 · Flows"),
    ("08-risk-and-control.md", "risk-and-control.html", "8 · Risk and control"),
    ("09-terminal.md", "terminal.html", "9 · The terminal"),
    ("10-roadmap.md", "roadmap.html", "10 · Roadmap"),
    ("glossary.md", "glossary.html", "Glossary"),
]
LINKS = {src: dst for src, dst, _ in PAGES}

MARK = ('<svg width="18" height="18" viewBox="0 0 32 32" aria-hidden="true"><rect width="18" height="11" fill="#f2efe8"/>'
        '<rect y="13" width="32" height="6" fill="#f2b135"/><rect x="14" y="21" width="18" height="11" fill="#f2efe8"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" fill="#0b0c0e"/>'
           '<g transform="translate(4 4) scale(.75)"><rect width="18" height="11" fill="#f2efe8"/><rect y="13" width="32" height="6" fill="#f2b135"/>'
           '<rect x="14" y="21" width="18" height="11" fill="#f2efe8"/></g></svg>')

CSS = """
@font-face{font-family:"Schibsted Grotesk";src:url(assets/Schibsted.ttf);font-weight:100 900;font-display:swap}
@font-face{font-family:"Geist Mono";src:url(assets/GeistMono.ttf);font-weight:100 900;font-display:swap}
:root{--s0:#0b0c0e;--s1:#14161a;--s2:#1c1f24;--hair:#2a2e35;--ink:#f2efe8;--muted:#a8a49b;--faint:#8a867e;--brand:#f2b135;
--sans:"Schibsted Grotesk","Helvetica Neue",Arial,sans-serif;--mono:"Geist Mono","SF Mono",Menlo,monospace}
*{box-sizing:border-box}
html{background:var(--s0);color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased}
body{margin:0}
a{color:var(--ink);text-decoration:underline;text-decoration-color:var(--hair);text-underline-offset:3px}
a:hover{text-decoration-color:var(--ink)}
.top{position:sticky;top:0;z-index:2;height:56px;display:flex;align-items:center;gap:12px;padding:0 24px;background:var(--s0);border-bottom:1px solid var(--hair)}
.top .name{font-weight:500;font-size:16px;text-decoration:none;display:flex;gap:10px;align-items:center}
.top .tag{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.top .sp{flex:1}.top .out{font-size:14px;color:var(--muted);text-decoration:none}
.wrap{display:grid;grid-template-columns:260px minmax(0,1fr);max-width:1440px;margin:0 auto}
nav{position:sticky;top:56px;align-self:start;height:calc(100vh - 56px);overflow:auto;padding:28px 16px 28px 24px;border-right:1px solid var(--hair)}
nav .lab{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 12px 12px}
nav a{display:block;padding:7px 12px;font-size:14px;color:var(--muted);text-decoration:none;border-left:2px solid transparent}
nav a:hover{color:var(--ink)}
nav a.on{color:var(--ink);border-left-color:var(--brand);background:var(--s1)}
main{padding:48px 56px 96px;min-width:0}
article{max-width:1100px}
article>p:has(img){max-width:none}
article>p:not(:has(img)),article>ul,article>ol,article>h1,article>h2,article>h3,article>blockquote{max-width:720px}
h1{font-weight:500;font-size:44px;line-height:1.08;letter-spacing:-.025em;margin:0 0 28px}
h2{font-weight:500;font-size:26px;letter-spacing:-.015em;margin:56px 0 16px;padding-top:28px;border-top:1px solid var(--hair)}
h3{font-weight:500;font-size:19px;margin:36px 0 10px}
p,li{font-size:17px;line-height:1.65;color:var(--muted)}
p strong,li strong,td strong{color:var(--ink);font-weight:500}
em{font-style:normal;color:var(--faint)}
code{font-family:var(--mono);font-size:.86em;background:var(--s2);border:1px solid var(--hair);padding:1px 6px;border-radius:2px;color:var(--ink)}
pre{background:var(--s1);border:1px solid var(--hair);padding:16px 18px;border-radius:2px;overflow:auto;max-width:720px}
pre code{background:none;border:0;padding:0;font-size:14px;line-height:1.6}
del{color:var(--faint)}
img{display:block;width:100%;height:auto;border:1px solid var(--hair);border-radius:2px;margin:28px 0}
table{width:100%;border-collapse:collapse;margin:24px 0;font-size:15px;display:block;overflow-x:auto}
th{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);text-align:left;padding:10px 14px;border-bottom:1px solid var(--hair);white-space:nowrap}
td{padding:12px 14px;border-bottom:1px solid var(--hair);color:var(--muted);line-height:1.5;vertical-align:top}
td:first-child{color:var(--ink)}
.pager{display:flex;justify-content:space-between;gap:16px;margin-top:72px;padding-top:24px;border-top:1px solid var(--hair);max-width:1100px}
.pager a{display:block;padding:16px 20px;border:1px solid var(--hair);background:var(--s1);text-decoration:none;min-width:240px;border-radius:2px}
.pager a:hover{background:var(--s2)}
.pager .k{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.pager .next{text-align:right;margin-left:auto}
footer{font-family:var(--mono);font-size:12px;color:var(--faint);margin-top:48px}
@media (max-width:900px){.wrap{grid-template-columns:1fr}nav{position:sticky;top:56px;z-index:1;background:var(--s0);height:auto;display:flex;overflow-x:auto;gap:4px;border-right:0;border-bottom:1px solid var(--hair);padding:8px 12px}nav .lab{display:none}nav a{white-space:nowrap;border-left:0;border-bottom:2px solid transparent}nav a.on{border-bottom-color:var(--brand)}
main{padding:32px 16px 64px}h1{font-size:34px}.pager{flex-direction:column}.pager a{min-width:0}.top .tag{display:none}}
"""

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Promorphic docs</title>
<meta name="description" content="Promorphic: AI treasury management for tokenized assets. Mandates, agents and vaults on Canton.">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/docs.css">
</head><body>
<header class="top"><a class="name" href="index.html">{mark}Promorphic</a><span class="tag">Docs</span><span class="sp"></span>
<a class="out" href="https://promorphic.xyz">promorphic.xyz</a></header>
<div class="wrap"><nav aria-label="Chapters"><div class="lab">Contents</div>{nav}</nav>
<main><article>{body}</article>{pager}<footer>© 2026 Promorphic · Examples, issuers and numbers are fictional.</footer></main></div>
</body></html>"""


def convert(md_text):
    md_text = re.sub(r"~~(.+?)~~", r"<del>\1</del>", md_text)
    # chapter links: foo.md -> foo.html, figures/ links -> GitHub source
    for src, dst in LINKS.items():
        md_text = md_text.replace(f"]({src})", f"]({dst})")
    md_text = re.sub(r"\]\((figures/[^)]*)\)", r"](https://github.com/promorphic/docs/tree/main/\1)", md_text)
    html = markdown.markdown(md_text, extensions=["tables", "fenced_code", "toc", "attr_list"])
    # every figure opens full size, which matters on a phone
    return re.sub(r'(<img [^>]*src="([^"]+)"[^>]*>)', r'<a href="\2">\1</a>', html)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    shutil.copytree(ROOT / "img", OUT / "img")
    for f in ["Schibsted.ttf", "GeistMono.ttf"]:
        shutil.copy(ROOT / "figures" / "fonts" / f, OUT / "assets" / f)
    (OUT / "assets" / "docs.css").write_text(CSS)
    (OUT / "assets" / "favicon.svg").write_text(FAVICON)
    for i, (src, dst, label) in enumerate(PAGES):
        body = convert((ROOT / src).read_text())
        title = re.search(r"<h1[^>]*>(.*?)</h1>", body)
        title = re.sub("<[^>]+>", "", title.group(1)) if title else label
        nav = "".join(f'<a href="{d}"{" class=on" if d == dst else ""}>{l}</a>' for _, d, l in PAGES)
        prev_ = f'<a class="prev" href="{PAGES[i-1][1]}"><span class="k">Previous</span>{PAGES[i-1][2]}</a>' if i > 0 else ""
        next_ = f'<a class="next" href="{PAGES[i+1][1]}"><span class="k">Next</span>{PAGES[i+1][2]}</a>' if i < len(PAGES) - 1 else ""
        html = PAGE.format(title=title, mark=MARK, nav=nav, body=body, pager=f'<div class="pager">{prev_}{next_}</div>')
        (OUT / dst).write_text(html)
    (OUT / "CNAME").write_text(DOMAIN + "\n")
    (OUT / ".nojekyll").write_text("")
    print(f"built {len(PAGES)} pages into {OUT}")


if __name__ == "__main__":
    main()
