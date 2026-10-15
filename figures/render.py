import sys, asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).parent


async def main(names):
    srcs = sorted((ROOT / "src").glob("*.html"))
    if names:
        srcs = [s for s in srcs if s.stem in names or any(s.stem.startswith(x) for x in names)]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(device_scale_factor=2, viewport={"width": 1600, "height": 1000})
        page = await ctx.new_page()
        for s in srcs:
            await page.goto(s.as_uri())
            await page.evaluate("document.fonts.ready")
            await page.wait_for_timeout(150)
            el = await page.query_selector(".frame")
            await el.screenshot(path=str(ROOT / "out" / f"{s.stem}.png"))
            print("rendered", s.stem)
        await b.close()

asyncio.run(main(sys.argv[1:]))
