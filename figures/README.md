# Figures

Every diagram and mockup in these docs is generated from code here, so it stays sharp and consistent with the Promorphic brand (neutral grounds and text, hairline edges, amber only for Promorphic itself and its actions).

| File | Makes |
|---|---|
| `kit.py` | The figure kit: boxes, ports, connectors, legends, text-fit warnings |
| `figs_a.py` | Chapters 1 to 3: thesis, ecosystem, stack, modes, architecture |
| `figs_b.py` | Chapters 4 to 6: vaults, mandate, custody, gates, agent loop |
| `figs_c.py` | Chapters 7 to 10: flows, failure modes, screen map, roadmap |
| `mock.py` | The seven terminal mockups |
| `render.py` | Renders each page in headless Chromium at 2x |
| `build.py` | Runs everything and copies the PNGs to `../img` |

```
pip install playwright pillow
playwright install chromium
python3 build.py
```

Fonts: Schibsted Grotesk and Geist Mono, both under the SIL Open Font License, from github.com/google/fonts.
