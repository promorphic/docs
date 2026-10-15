"""Terminal mockups. One theme (dark), brand tokens, amber only for the mark, the one primary
button per view, and Promorphic/agent action markers (small squares)."""
from pathlib import Path
import os
THEME = os.environ.get("PM_THEME", "dark")
SUFFIX = "-light" if THEME == "light" else ""
SRC = Path(__file__).parent / "src"

CSS = """
@font-face{font-family:SG;src:url(../fonts/Schibsted.ttf);font-weight:100 900}
@font-face{font-family:GM;src:url(../fonts/GeistMono.ttf);font-weight:100 900}
:root{--s0:#0b0c0e;--s1:#14161a;--s2:#1c1f24;--hair:#2a2e35;--ink:#f2efe8;--muted:#a8a49b;--faint:#8a867e;--brand:#f2b135;--onb:#14110a;
--sans:SG,sans-serif;--mono:GM,monospace}
*{box-sizing:border-box}html,body{margin:0;background:var(--s0)}
.frame{width:1536px;padding:40px 48px 40px;background:var(--s0);color:var(--ink);font-family:var(--sans)}
.eb{font-family:var(--mono);font-size:12px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);display:flex;align-items:center;gap:12px}
.eb:after{content:"";width:32px;height:1px;background:var(--hair)}
h1{font-weight:500;font-size:28px;letter-spacing:-.015em;line-height:1.2;margin:12px 0 28px}
.cap{font-family:var(--mono);font-size:12px;color:var(--faint);margin-top:20px}
.win{width:1440px;border:1px solid var(--hair);border-radius:4px;overflow:hidden;background:var(--s0)}
.top{height:52px;display:flex;align-items:center;gap:28px;padding:0 20px;border-bottom:1px solid var(--hair);background:var(--s1)}
.brandm{display:flex;align-items:center;gap:10px;font-weight:500;font-size:16px}
.nav{display:flex;gap:4px;font-size:14px;color:var(--muted)}
.nav span{padding:7px 12px;border-radius:2px}.nav .on{color:var(--ink);background:var(--s2)}
.sp{flex:1}
.sel{font-size:13px;border:1px solid var(--hair);padding:7px 12px;border-radius:2px;display:flex;gap:10px;align-items:center}
.sel .k{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:.1em;text-transform:uppercase}
.av{width:30px;height:30px;border-radius:50%;background:var(--s2);border:1px solid var(--hair);font-size:12px;display:flex;align-items:center;justify-content:center;color:var(--muted)}
.body{padding:24px;display:grid;gap:20px}
.lab{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.card{background:var(--s1);border:1px solid var(--hair);border-radius:2px;padding:18px 20px}
.kpi .v{font-family:var(--mono);font-size:30px;font-weight:500;letter-spacing:-.02em;margin-top:10px;font-variant-numeric:tabular-nums}
.kpi .s{font-family:var(--mono);font-size:12px;color:var(--muted);margin-top:6px}
table{width:100%;border-collapse:collapse;font-size:14px}
th{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);text-align:left;padding:10px 12px;border-bottom:1px solid var(--hair)}
td{padding:12px 12px;border-bottom:1px solid var(--hair);vertical-align:middle}
td.n,th.n{text-align:right;font-family:var(--mono);font-variant-numeric:tabular-nums}
.m{font-family:var(--mono);font-size:12px;color:var(--muted)}
.mi{font-family:var(--mono);font-size:13px}
.pill{font-family:var(--mono);font-size:11px;letter-spacing:.06em;padding:3px 8px;border:1px solid var(--hair);border-radius:999px;color:var(--muted);white-space:nowrap}
.pill.solid{background:var(--ink);color:var(--s0);border-color:var(--ink)}
.bar{position:relative;height:6px;background:var(--s2);width:120px;display:inline-block;vertical-align:middle;margin-right:10px}
.bar i{position:absolute;left:0;top:0;bottom:0;background:var(--muted)}
.bar b{position:absolute;top:-4px;bottom:-4px;width:2px;background:var(--ink)}
.btn{font-family:var(--sans);font-size:14px;font-weight:500;padding:10px 16px;border-radius:2px;border:1px solid var(--hair);background:transparent;color:var(--ink);display:inline-block}
.btn.p{background:var(--brand);color:var(--onb);border-color:var(--brand)}
.sq{display:inline-block;width:7px;height:7px;background:var(--brand);margin-right:8px;vertical-align:1px}
.sqf{display:inline-block;width:7px;height:7px;border:1px solid var(--faint);margin-right:8px;vertical-align:1px}
.row{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid var(--hair);font-size:14px}
.row:last-child{border-bottom:0}
.k2{font-family:var(--mono);font-size:12px;color:var(--muted)}
.h3{font-size:18px;font-weight:500;letter-spacing:-.01em}
.p{font-size:14px;line-height:1.6;color:var(--muted)}
.p b{color:var(--ink);font-weight:500}
.chip{font-family:var(--mono);font-size:12px;padding:6px 10px;border:1px solid var(--hair);border-radius:2px;color:var(--muted)}
.chip.on{color:var(--ink);border-color:var(--muted);background:var(--s2)}
.input{border:1px solid var(--hair);background:var(--s0);padding:10px 12px;font-family:var(--mono);font-size:15px;border-radius:2px}
.range{position:relative;height:4px;background:var(--s2);margin:14px 0 6px}
.range i{position:absolute;left:0;top:0;bottom:0;background:var(--muted)}
.range b{position:absolute;top:-6px;width:16px;height:16px;border-radius:50%;background:var(--ink);margin-left:-8px}
.strike{text-decoration:line-through;color:var(--faint)}
"""

INKC = "#14130f" if THEME == "light" else "#f2efe8"
MARK = (f'<svg width="20" height="20" viewBox="0 0 32 32"><rect width="18" height="11" fill="{INKC}"/>'
        f'<rect y="13" width="32" height="6" fill="#f2b135"/><rect x="14" y="21" width="18" height="11" fill="{INKC}"/></svg>')


if THEME == "light":
    CSS = CSS.replace(":root{--s0:#0b0c0e;--s1:#14161a;--s2:#1c1f24;--hair:#2a2e35;--ink:#f2efe8;--muted:#a8a49b;--faint:#8a867e;",
                      ":root{--s0:#f7f5f0;--s1:#ffffff;--s2:#ede9e1;--hair:#d9d4ca;--ink:#14130f;--muted:#5c5950;--faint:#6e6a60;")
    assert "--s0:#f7f5f0" in CSS


def top(active):
    nav = "".join(f'<span class="{"on" if n == active else ""}">{n}</span>' for n in ["Book", "Vaults", "Mandate", "Proposals", "Record"])
    return (f'<div class="top"><div class="brandm">{MARK}Promorphic</div><div class="nav">{nav}</div><div class="sp"></div>'
            '<div class="sel"><span class="k">Mandate</span>Northbeam Capital · Yield sleeve</div>'
            '<div class="sel"><span class="k">Mode</span>Copilot</div>'
            '<div class="sel"><span class="sq" style="margin:0"></span>Claude · watching</div><div class="av">JR</div></div>')


def page(name, eyebrow, title, inner, caption=None, active="Book"):
    cap = f'<div class="cap">{caption}</div>' if caption else ""
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="frame">'
            f'<div class="eb">{eyebrow}</div><h1>{title}</h1><div class="win">{top(active) if active else ""}{inner}</div>{cap}</div></body></html>')
    (SRC / f"{name}{SUFFIX}.html").write_text(html)


def wbar(w, lim):
    tick = f'<b style="left:{lim / 50 * 100}%"></b>' if lim < 50 else ""
    return f'<span class="bar"><i style="width:{w / 50 * 100}%"></i>{tick}</span>'


# ── M1 Book ──
def m_book():
    pos = [("Harbor Treasury MMF", "Harbor Funds", "MMF", "19.10", 39.6, 40, "4.31%", "T+0", "Listed"),
           ("Northgate T-Bill Fund", "Northgate AM", "T-bill", "9.64", 20.0, 40, "4.22%", "T+0", "Listed"),
           ("Meridian Credit I", "Meridian Capital", "Private credit", "6.27", 13.0, 15, "9.80%", "90d gate", "Watch"),
           ("Keel Overnight Repo", "Keel Bank", "Repo", "7.71", 16.0, 40, "4.58%", "T+0", "Listed"),
           ("Cash · USD token", "—", "Cash", "5.51", 11.4, 100, "—", "Instant", "—")]
    rows = ""
    for v, iss, t, val, w, lim, y, liq, st in pos:
        flag = '<span class="pill solid">Watch</span>' if st == "Watch" else (f'<span class="pill">{st}</span>' if st != "—" else '<span class="m">—</span>')
        rows += (f'<tr><td><div>{v}</div><div class="m">{iss}</div></td><td class="m">{t}</td><td class="n">${val}m</td>'
                 f'<td>{wbar(w, lim)}<span class="mi">{w:.1f}%</span> <span class="m">/ {lim if lim < 100 else "—"}{"%" if lim < 100 else ""}</span></td>'
                 f'<td class="n">{y}</td><td class="m">{liq}</td><td>{flag}</td></tr>')
    inner = f'''<div class="body" style="grid-template-columns:1fr 400px;align-items:start">
<div style="display:grid;gap:20px">
 <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
  <div class="card kpi"><div class="lab">Book value</div><div class="v">$48.23m</div><div class="s">+$41.2k today · NAV 14:00 ET</div></div>
  <div class="card kpi"><div class="lab">Blended yield</div><div class="v">5.06%</div><div class="s">7-day, net of fees</div></div>
  <div class="card kpi"><div class="lab">Same-day liquidity</div><div class="v">87.0%</div><div class="s">Floor 60% · Meridian counts as zero</div></div>
  <div class="card kpi"><div class="lab">Limits</div><div class="v">12 / 12</div><div class="s">1 trigger fired: Meridian gate</div></div>
 </div>
 <div class="card" style="padding:6px 8px 4px">
  <div style="display:flex;justify-content:space-between;align-items:center;padding:12px 12px 6px"><div class="lab">Positions</div><div class="m">Bar: weight · tick: mandate limit</div></div>
  <table><tr><th>Vault</th><th>Type</th><th class="n">Value</th><th>Weight / limit</th><th class="n">Yield</th><th>Liquidity</th><th>DD</th></tr>{rows}</table>
 </div>
</div>
<div style="display:grid;gap:16px">
 <div class="card" style="border-color:var(--muted)">
  <div class="lab"><span class="sq"></span>Proposal P-0142 · awaiting 2 approvals</div>
  <div class="h3" style="margin:14px 0 8px">Cut Meridian Credit I to 5% before the gate bites</div>
  <div class="p">Meridian notified a 90-day redemption gate at 06:12. Redeem <b>$3.86m (8.0% of book)</b> in the last open window and move it to <b>Northgate T-Bill Fund</b>. Harbor is skipped: it sits at 39.6% of a 40% limit.</div>
  <div style="display:flex;gap:10px;margin:16px 0 4px"><span class="btn p">Review and approve</span><span class="btn">Reject</span></div>
  <div class="m" style="margin-top:10px">7 of 7 gates pass · expires in 5h 48m</div>
 </div>
 <div class="card">
  <div class="lab" style="margin-bottom:6px">Agent activity</div>
  <div class="row"><span><span class="sqf"></span>Daily review: no action</span><span class="m">06:00</span></div>
  <div class="row"><span><span class="sq"></span>Issuer notice read: Meridian</span><span class="m">06:12</span></div>
  <div class="row"><span><span class="sq"></span>Proposal P-0142 created</span><span class="m">06:14</span></div>
  <div class="row"><span><span class="sqf"></span>Harbor NAV 1.0000, fresh</span><span class="m">14:02</span></div>
  <div class="row"><span><span class="sqf"></span>Sweep $240k → Harbor settled</span><span class="m">Mon</span></div>
 </div>
</div></div>'''
    page("10-1-book", "Mockup 1 · Book", "Home: the whole book against the mandate, and what the agent wants to do about it.", inner,
         "Fictional issuers and numbers. Ticks mark the mandate's per-vault limit; amber squares mark something the agent or Promorphic did.")


# ── M2 Vaults ──
def m_vaults():
    vs = [("Harbor Treasury MMF", "Harbor Funds", "MMF", "4.31%", "$612m", "T+0", "2026-10-01", "Listed", True),
          ("Northgate T-Bill Fund", "Northgate AM", "T-bill", "4.22%", "$1.04b", "T+0", "2026-09-24", "Listed", True),
          ("Keel Overnight Repo", "Keel Bank", "Repo", "4.58%", "$388m", "T+0", "2026-10-08", "Listed", True),
          ("Atlas Short Duration", "Atlas Partners", "Notes", "4.74%", "$205m", "T+1", "2026-09-30", "Listed", True),
          ("Meridian Credit I", "Meridian Capital", "Private credit", "9.80%", "$146m", "90d gate", "2026-10-15", "Watch", True),
          ("Sable Allocated Gold", "Sable Vaults", "Commodity", "—", "$97m", "T+2", "2026-09-12", "Listed", False),
          ("Crest Trade Finance", "Crest Credit", "Private credit", "8.15%", "$74m", "30d", "2026-08-29", "Listed", True)]
    rows = ""
    for n, iss, t, y, aum, liq, rev, st, inm in vs:
        rows += (f'<tr><td><div>{n}</div><div class="m">{iss}</div></td><td class="m">{t}</td><td class="n">{y}</td><td class="n">{aum}</td>'
                 f'<td class="m">{liq}</td><td class="m">{rev}</td><td>{"<span class=\'pill solid\'>Watch</span>" if st == "Watch" else "<span class=\'pill\'>Listed</span>"}</td>'
                 f'<td class="m">{"<span class=\'sq\'></span>In mandate" if inm else "Outside universe"}</td></tr>')
    inner = f'''<div class="body">
 <div style="display:flex;gap:10px;align-items:center">
  <div class="input" style="width:340px;color:var(--faint);font-family:var(--sans);font-size:14px">Search vaults, issuers, assets</div>
  <span class="chip on">All types</span><span class="chip">MMF</span><span class="chip">T-bill</span><span class="chip">Repo</span><span class="chip">Private credit</span><span class="chip">Commodity</span>
  <div class="sp"></div><span class="chip on">Canton</span><span class="chip">Agent eligible only</span>
 </div>
 <div class="card" style="padding:6px 8px 4px">
  <table><tr><th>Vault</th><th>Type</th><th class="n">Yield 7d</th><th class="n">Onchain AUM</th><th>Liquidity</th><th>Last DD review</th><th>Status</th><th>Your mandate</th></tr>{rows}</table>
 </div>
 <div class="m">14 vaults listed on Canton · 1 on watch · every row opens its DD pack</div>
</div>'''
    page("10-2-vaults", "Mockup 2 · Vaults", "The catalogue: every listed vault, its terms, and whether your mandate can hold it.", inner,
         "Fictional issuers. Vaults are the issuers' distribution channel; the catalogue is where a manager, or the manager's agent, finds them.", active="Vaults")


# ── M3 Vault detail ──
def m_vault_detail():
    def sec(title, rows):
        r = "".join(f'<div class="row"><span class="k2">{a}</span><span>{b}</span></div>' for a, b in rows)
        return f'<div class="card"><div class="lab" style="margin-bottom:6px">{title}</div>{r}</div>'
    inner = f'''<div class="body">
 <div style="display:flex;align-items:flex-end;gap:16px;border-bottom:1px solid var(--hair);padding-bottom:20px">
  <div><div class="lab">Vault · pm.v.harbor-mmf-01</div><div style="font-size:30px;font-weight:500;letter-spacing:-.02em;margin-top:8px">Harbor Treasury MMF</div>
  <div class="m" style="margin-top:6px">Harbor Funds · Money market fund · US T-bills and repo · Canton token standard</div></div>
  <div class="sp"></div>
  <div class="card kpi" style="min-width:170px"><div class="lab">Yield 7d</div><div class="v" style="font-size:24px">4.31%</div><div class="s">Net of fees</div></div>
  <div class="card kpi" style="min-width:170px"><div class="lab">NAV</div><div class="v" style="font-size:24px">1.0000</div><div class="s">Fresh · 14:02 ET</div></div>
  <div class="card kpi" style="min-width:170px"><div class="lab">Onchain AUM</div><div class="v" style="font-size:24px">$612m</div><div class="s">On Canton</div></div>
 </div>
 <div style="display:grid;grid-template-columns:1fr 1fr 420px;gap:20px;align-items:start">
  <div style="display:grid;gap:16px">{sec("Parties", [("Issuer", "Harbor Funds LLC"), ("Tokenization agent", "Named, licensed"), ("Custodian", "Named bank"), ("Auditor", "Named, annual")])}
   {sec("Legal", [("Wrapper", "Regulated fund"), ("Domicile", "Named jurisdiction"), ("Eligible", "Professional investors"), ("Sources", "Prospectus · 4 docs")])}</div>
  <div style="display:grid;gap:16px">{sec("Liquidity", [("Subscription cutoff", "14:00 ET"), ("Redemption", "T+0, same day"), ("Gates", "None stated"), ("Min ticket", "$10k")])}
   {sec("Promorphic review", [("Last review", "2026-10-01"), ("Attestation", "Monthly, on time"), ("NAV deviation, 90d", "0.00%"), ("Agent eligible", "Yes")])}</div>
  <div class="card" style="display:grid;gap:14px">
   <div class="lab">Subscribe</div>
   <div class="input">$ 1,000,000</div>
   <div class="row"><span class="k2">Est. units at NAV</span><span class="mi">1,000,000.00</span></div>
   <div class="row"><span class="k2">Next cutoff</span><span class="mi">14:00 ET · 2h 11m</span></div>
   <div class="row"><span class="k2">Weight after</span><span class="mi">41.7% <span class="m">/ 40%</span></span></div>
   <div class="p" style="border:1px solid var(--hair);padding:12px;border-radius:2px"><span class="sq"></span>Over your 40% per-vault limit. Max you can add from cash is <b>$0.19m</b>; Northgate has <b>$9.6m</b> of room.</div>
   <div style="display:flex;gap:10px"><span class="btn p">Subscribe $0.19m instead</span><span class="btn">Ask the agent</span></div>
  </div>
 </div>
</div>'''
    page("10-3-vault-detail", "Mockup 3 · Vault detail", "One vault: the DD pack in fields, and a subscribe panel that knows your mandate.", inner,
         "The DD pack is structured data, so the same fields the manager reads are the fields the agent reasons over.", active="Vaults")


# ── M4 Mandate editor ──
def m_mandate():
    def slider(lbl, val, pct, note):
        return (f'<div style="padding:12px 0;border-bottom:1px solid var(--hair)"><div style="display:flex;justify-content:space-between"><span>{lbl}</span>'
                f'<span class="mi">{val}</span></div><div class="range"><i style="width:{pct}%"></i><b style="left:{pct}%"></b></div><div class="m">{note}</div></div>')
    inner = f'''<div class="body" style="grid-template-columns:1fr 1fr 380px;align-items:start">
 <div class="card"><div class="lab">Limits</div>
  {slider("Max per vault", "40%", 40, "Today's max: Harbor 39.6%")}
  {slider("Max per issuer", "50%", 50, "Today's max: Harbor Funds 39.6%")}
  {slider("Min same-day liquidity", "60% → 65%", 65, "Today: 87.0% · still in bounds")}
  {slider("Max duration", "90 days", 45, "Today: 38 days weighted")}
 </div>
 <div style="display:grid;gap:16px">
 <div class="card"><div class="lab">Universe</div>
  <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:14px"><span class="chip on">MMF</span><span class="chip on">T-bill</span><span class="chip on">Repo</span><span class="chip on">Notes</span><span class="chip">Private credit</span><span class="chip">Commodity</span></div>
  <div class="m" style="margin-top:12px">6 of 14 listed vaults eligible</div></div>
 <div class="card"><div class="lab">Execution</div>
  <div class="row"><span class="k2">Agent</span><span>Claude, via gateway</span></div>
  <div class="row"><span class="k2">Mode</span><span style="display:flex;gap:6px"><span class="chip">Manual</span><span class="chip on">Copilot</span><span class="chip">Autopilot</span></span></div>
  <div class="row"><span class="k2">Auto threshold</span><span class="mi">$250,000</span></div>
  <div class="row"><span class="k2">Daily turnover</span><span class="mi">≤ 20%</span></div></div>
 </div>
 <div class="card" style="display:grid;gap:12px"><div class="lab">Version 3 → 4</div>
  <div class="row"><span class="k2">Min same-day liquidity</span><span class="mi">60% → 65%</span></div>
  <div class="row"><span class="k2">Private credit</span><span class="mi">15% → 0%</span></div>
  <div class="p">Removing private credit forces an exit from Meridian Credit I. The agent will propose it once v4 is active.</div>
  <div class="lab" style="margin-top:6px">Signatures</div>
  <div class="row"><span>J. Rao · PM</span><span class="pill">Signed</span></div>
  <div class="row"><span>A. Mensah · PM</span><span class="pill">Pending</span></div>
  <div class="row"><span>Promorphic · operator</span><span class="pill">Auto on valid</span></div>
  <span class="btn p" style="text-align:center">Send for signature</span>
 </div>
</div>'''
    page("10-4-mandate", "Mockup 4 · Mandate", "Edit the mandate like a term sheet. Every change shows what it does to today's book.", inner,
         "A new version is a new contract on Canton. It replaces the old one only when every required party has signed.", active="Mandate")


# ── M5 Proposal ──
def m_proposal():
    gates = [("Universe", "MMF, T-bill allowed"), ("Per vault", "Northgate 28.0% ≤ 40%"), ("Per issuer", "Northgate AM 28.0% ≤ 50%"),
             ("Liquidity", "95.0% ≥ 60%"), ("Duration", "31d ≤ 90d"), ("Turnover", "8.0% ≤ 20%"), ("Threshold", "$3.86m > $250k → approvals")]
    g = "".join(f'<div class="row"><span><span class="sqf" style="background:var(--muted);border-color:var(--muted)"></span>{a}</span><span class="m">{b}</span></div>' for a, b in gates)
    moves = [("Meridian Credit I", "13.0%", "5.0%", "Redeem $3.86m"), ("Harbor Treasury MMF", "39.6%", "39.6%", "—"),
             ("Northgate T-Bill Fund", "20.0%", "28.0%", "Subscribe $3.86m")]
    mv = "".join(f'<tr><td>{a}</td><td class="n">{b}</td><td class="n">{c}</td><td class="m">{d}</td></tr>' for a, b, c, d in moves)
    inner = f'''<div class="body" style="grid-template-columns:1fr 400px 360px;align-items:start">
 <div style="display:grid;gap:16px">
  <div><div class="lab"><span class="sq"></span>Proposal P-0142 · by Claude via gateway · 06:14</div>
  <div style="font-size:26px;font-weight:500;letter-spacing:-.02em;margin-top:10px">Cut Meridian Credit I to 5% before the gate bites</div></div>
  <div class="card"><div class="lab" style="margin-bottom:10px">Reason, as written by the agent</div>
   <div class="p" style="font-size:15px">At 06:12 Meridian Capital notified a <b>90-day redemption gate</b> effective in 10 business days. Your mandate v3 says a gate means <b>redeem</b>. The last window before the gate accepts at most $3.86m from this holder, so this proposal redeems that now and leaves 5.0% to exit when the gate lifts. The cash goes to Northgate, because Harbor sits at 39.6% of its 40% limit.</div>
   <div style="display:flex;gap:8px;margin-top:14px"><span class="chip">Evidence: issuer notice #M-2291</span><span class="chip">DD field: liquidity.gates</span><span class="chip">Mandate v3 §Risk triggers</span></div></div>
  <div class="card" style="padding:6px 8px 4px"><table><tr><th>Vault</th><th class="n">Weight now</th><th class="n">After</th><th>Action</th></tr>{mv}</table></div>
 </div>
 <div class="card"><div class="lab" style="margin-bottom:6px">Policy pre-check · 7 of 7</div>{g}
  <div class="m" style="margin-top:12px">The mandate contract re-checks all of these when the choice is exercised.</div></div>
 <div class="card" style="display:grid;gap:12px"><div class="lab">Approvals · 1 of 2</div>
  <div class="row"><span>J. Rao</span><span class="pill">Approved 07:02</span></div>
  <div class="row"><span>A. Mensah</span><span class="pill">You</span></div>
  <div class="row"><span class="k2">Expires</span><span class="mi">12:14 · 5h 12m</span></div>
  <div class="row"><span class="k2">Settles</span><span class="mi">Redeem T+0 · subscribe by 14:00</span></div>
  <span class="btn p" style="text-align:center">Approve and sign</span><span class="btn" style="text-align:center">Reject with a note</span>
 </div>
</div>'''
    page("10-5-proposal", "Mockup 5 · Proposal", "A proposal reads like a trade ticket with its reasoning attached.", inner,
         "Approving exercises the Approve choice from the approver's own party. Promorphic cannot approve on anyone's behalf.", active="Proposals")


# ── M6 Record ──
def m_record():
    ev = [("2026-10-15 07:31:04", "Promorphic", "Rebalance exercised · P-0142", "v3", "tx 1220…9f4a", "Settled"),
          ("2026-10-15 07:30:58", "A. Mensah", "Approve · P-0142", "v3", "tx 1220…77c1", "Signed"),
          ("2026-10-15 07:02:11", "J. Rao", "Approve · P-0142", "v3", "tx 1220…03be", "Signed"),
          ("2026-10-15 06:14:40", "Claude", "propose · P-0142 · 7/7 gates", "v3", "tx 1220…a810", "Proposed"),
          ("2026-10-15 06:12:09", "Meridian Capital", "Issuer notice · gate 90d", "—", "—", "Ingested"),
          ("2026-10-14 22:40:31", "Claude", "propose · sweep $1.2m → Keel", "v3", "—", "Rejected · turnover"),
          ("2026-10-10 02:10:55", "Promorphic", "Rebalance exercised · auto · $240k", "v3", "tx 1220…5d02", "Settled"),
          ("2026-10-10 02:10:41", "Claude", "propose · sweep $240k → Harbor", "v3", "tx 1220…c9e7", "Auto ≤ threshold")]
    rows = "".join(f'<tr><td class="mi">{a}</td><td>{("<span class=\'sq\'></span>" if b in ("Promorphic", "Claude") else "<span class=\'sqf\'></span>")}{b}</td><td>{c}</td><td class="m">{d}</td><td class="m">{e}</td><td><span class="pill{" solid" if f.startswith("Rejected") else ""}">{f}</span></td></tr>' for a, b, c, d, e, f in ev)
    inner = f'''<div class="body" style="grid-template-columns:1fr 380px;align-items:start">
 <div style="display:grid;gap:14px">
  <div style="display:flex;gap:10px;align-items:center"><span class="chip on">All</span><span class="chip">Agent</span><span class="chip">People</span><span class="chip">Issuers</span><span class="chip">Rejected</span><div class="sp"></div><span class="btn">Export CSV</span></div>
  <div class="card" style="padding:6px 8px 4px"><table><tr><th>Time (UTC)</th><th>Actor</th><th>Event</th><th>Mandate</th><th>Ledger</th><th>Result</th></tr>{rows}</table></div>
 </div>
 <div class="card"><div class="lab" style="margin-bottom:8px">Event detail</div>
  <div class="h3" style="margin-bottom:10px">propose · sweep $1.2m → Keel</div>
  <div class="row"><span class="k2">Actor</span><span>Claude via gateway</span></div>
  <div class="row"><span class="k2">Gate failed</span><span>Turnover</span></div>
  <div class="row"><span class="k2">Numbers</span><span class="mi">day total 22.4% &gt; 20%</span></div>
  <div class="row"><span class="k2">Ledger</span><span class="m">Never sent</span></div>
  <pre style="font-family:var(--mono);font-size:12px;color:var(--muted);background:var(--s0);border:1px solid var(--hair);padding:12px;margin:14px 0 0;line-height:1.6">{{"gate": "turnover",
 "limit": 0.20,
 "value": 0.224,
 "mandate": "pm.m.northbeam-01@v3",
 "agent": "claude",
 "reason_ref": "r-88f1"}}</pre></div>
</div>'''
    page("10-6-record", "Mockup 6 · Record", "Every proposal, check, signature and settlement, in one log the auditor can read.", inner,
         "Rejected proposals are kept too. A good record shows what the agent was stopped from doing, not only what it did.", active="Record")


# ── M7 Onboarding ──
def m_onboard():
    steps = ["Connect party", "Choose template", "Set limits", "Connect agent", "Sign"]
    st = "".join(f'<div style="flex:1;display:flex;align-items:center;gap:10px;padding:14px 0;border-top:2px solid {"var(--ink)" if i <= 3 else "var(--hair)"}">'
                 f'<span class="m">0{i + 1}</span><span style="color:{"var(--ink)" if i <= 3 else "var(--faint)"}">{s}</span></div>' for i, s in enumerate(steps))
    agents = [("Claude", "Anthropic · MCP", True), ("ChatGPT", "OpenAI · MCP", False), ("Gemini", "Google · MCP", False), ("Your own agent", "Any MCP or REST client", False)]
    ag = "".join(f'<div class="card" style="{"border-color:var(--ink)" if on else ""}"><div style="display:flex;justify-content:space-between"><span class="h3">{a}</span>'
                 f'<span class="pill{" solid" if on else ""}">{"Selected" if on else "Select"}</span></div><div class="m" style="margin-top:8px">{b}</div></div>' for a, b, on in agents)
    tools = [("read_context", "Book, limits, signals", True), ("read_dd", "Vault DD packs", True), ("propose", "Create a proposal", True),
             ("explain", "Attach reasons and evidence", True), ("rebalance", "Inside the mandate only", True), ("transfer_out", "Does not exist", False)]
    tl = "".join(f'<div class="row"><span class="mi {"" if ok else "strike"}">{"<span class=\'sq\'></span>" if ok else "<span class=\'sqf\'></span>"}{t}</span><span class="m">{d}</span></div>' for t, d, ok in tools)
    inner = f'''<div class="body">
 <div style="display:flex;gap:16px">{st}</div>
 <div style="display:grid;grid-template-columns:1fr 440px;gap:20px;align-items:start">
  <div><div class="h3" style="margin-bottom:6px">Connect an execution partner</div><div class="p" style="margin-bottom:16px">The agent decides; Promorphic checks, executes and records. You can switch agents later without touching the mandate.</div>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">{ag}</div></div>
  <div class="card"><div class="lab" style="margin-bottom:6px">Tools this agent will get</div>{tl}
   <div class="p" style="margin:14px 0">Credentials are scoped to <b>pm.m.northbeam-01</b> and expire with it. Pause or revoke them at any time.</div>
   <span class="btn p" style="display:block;text-align:center">Issue credentials</span></div>
 </div>
</div>'''
    page("10-7-onboarding", "Mockup 7 · Onboarding", "Pick the agent and see exactly which tools it gets, and which it never will.", inner,
         "Agent names are examples of models a manager can connect; naming them implies no partnership.", active=None)


if __name__ == "__main__":
    for fn in [m_book, m_vaults, m_vault_detail, m_mandate, m_proposal, m_record, m_onboard]:
        fn()
    print("ok")
