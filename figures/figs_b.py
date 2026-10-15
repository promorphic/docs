from kit import Fig, WARN, tw
W = 1104


def spec_sheet(f, x, y, w, title, sub, sections, cols=3, sec_h=None):
    """A raised spec card: header, then sections of key/value rows in a grid."""
    f.rect(x, y, w, 64, fill="s1")
    f.port(x + 7, y + 7, s=6)
    f.text(x + 24, y + 26, title, "title-lg")
    f.text(x + 24, y + 48, sub, "sub")
    gap = 16
    cw = (w - gap * (cols - 1)) / cols
    rows_per = max(len(s[1]) for s in sections)
    sh = sec_h or 52 + rows_per * 26
    for i, (name, rows) in enumerate(sections):
        cx = x + (i % cols) * (cw + gap)
        cy = y + 80 + (i // cols) * (sh + gap)
        f.rect(cx, cy, cw, sh, fill="s1")
        f.text(cx + 18, cy + 24, name, "label")
        f.path([(cx + 18, cy + 40), (cx + cw - 18, cy + 40)], "hair", arrow=False)
        for k, (key, val) in enumerate(rows):
            ry = cy + 60 + k * 26
            f.text(cx + 18, ry, key, "sub")
            f.text(cx + cw - 18, ry, val, "body-ink", "end")
            if tw(key, "sub") + tw(val, "body-ink") + 48 > cw:
                WARN.append(f"{f.name}: row overflow {key}/{val}")
    return y + 80 + ((len(sections) - 1) // cols + 1) * (sh + gap)


def f_vault_anatomy():
    f = Fig("04-1-vault-anatomy", W, 430, "Fig 4.1 · Vault anatomy", "A vault is one instrument, its terms, and a due diligence pack an agent can read.",
            "Example values. Every field is structured data in the DD registry; the PDF sources are attached, not the source of truth.", rules=False)
    spec_sheet(f, 0, 0, W, "T-bill MMF vault", "vault id  pm.v.tbill-mmf-01  ·  status  listed  ·  last review  2026-10-01", [
        ("Instrument", [("Type", "Money market fund"), ("Underlying", "US T-bills, repo"), ("Token", "Canton token standard"), ("Unit", "1 share, NAV-priced")]),
        ("Parties", [("Issuer", "Fund manager"), ("Tokenization agent", "Named, licensed"), ("Custodian", "Named bank"), ("Auditor", "Named, annual")]),
        ("Legal", [("Wrapper", "Regulated fund"), ("Domicile", "Named jurisdiction"), ("Eligible investors", "Professional only"), ("Docs", "Prospectus, KIID")]),
        ("Liquidity", [("Subscription cutoff", "14:00 ET"), ("Redemption notice", "T+0"), ("Settlement", "Same day"), ("Gates", "None stated")]),
        ("Pricing", [("NAV source", "Issuer feed"), ("Frequency", "Daily"), ("Staleness limit", "26 hours"), ("Yield, 7-day", "4.3%")]),
        ("Risk tags", [("Duration", "< 60 days"), ("Credit", "Sovereign"), ("Concentration", "Single issuer"), ("Agent eligible", "Yes")]),
    ])
    f.write()


def f_vault_lifecycle():
    f = Fig("04-2-lifecycle", W, 420, "Fig 4.2 · Lifecycles", "How a vault gets listed, and how a holding moves through it.",
            "The DD review never stops: a listed vault that breaks a rule moves to Watch, and the agent stops adding to it.")
    f.text(0, 12, "Vault", "label")
    states = [("Proposed", "Issuer applies"), ("DD review", "Promorphic checks"), ("Listed", "Open to mandates"), ("Watch", "No new money"), ("Delisted", "Exit only")]
    bw, gap = 196, 31
    for i, (t, s) in enumerate(states):
        x = i * (bw + gap)
        kind = "pm" if t in ("DD review",) else "plain"
        if t == "Listed":
            f.rect(x, 32, bw, 60, fill="s1", stroke="ink")
            f.text(x + bw / 2, 52, t, "title", "middle")
            f.text(x + bw / 2, 72, s, "sub", "middle")
        else:
            f.box(x, 32, bw, 60, t, s, kind=kind)
        if i < 4:
            f.path([(x + bw, 62), (x + bw + gap - 2, 62)], "faint")
    # watch back to listed
    x3 = 3 * (bw + gap); x2 = 2 * (bw + gap)
    f.path([(x3 + bw / 2, 92), (x3 + bw / 2, 122), (x2 + bw / 2, 122), (x2 + bw / 2, 94)], "faint", dash=True)
    f.arrow_label((x2 + x3 + bw) / 2, 122, "issue resolved")
    f.text(0, 196, "Holding", "label")
    hs = [("Subscribe", "Cash in, request"), ("Issuer accepts", "Before cutoff"), ("Held", "Units at NAV"), ("Redeem", "Notice period"), ("Cash settles", "Back to manager")]
    for i, (t, s) in enumerate(hs):
        x = i * (bw + gap)
        if t == "Held":
            f.rect(x, 216, bw, 60, fill="brand", stroke=None)
            f.text(x + bw / 2, 236, t, "title", "middle", fill="onbrand")
            f.text(x + bw / 2, 256, s, "sub", "middle", fill="onbrand")
        else:
            f.box(x, 216, bw, 60, t, s)
        if i < 4:
            f.path([(x + bw, 246), (x + bw + gap - 2, 246)], "brand")
    f.path([(x2 + bw / 2, 276), (x2 + bw / 2, 316), (x2 + bw / 2 + 290, 316)], "faint", dash=True)
    f.box(x2 + bw / 2 + 292, 296, 250, 40, "Switch: redeem + subscribe", kind="ghost")
    f.text(0, 370, "A switch between vaults is a redemption and a subscription in one Canton transaction where both issuers support it; otherwise two legs.", "body")
    f.legend(0, 400, [("brand-block", "The state the agent manages"), ("brand-line", "Settles on Canton"), ("dash-line", "Conditional path")])
    f.write()


def f_mandate():
    f = Fig("05-1-mandate", W, 430, "Fig 5.1 · Mandate anatomy", "The mandate is a contract. These are its terms.",
            "Example: a conservative yield sleeve at a fictional onchain asset manager. All limits are checked off-ledger before proposing and on-ledger before settling.", rules=False)
    spec_sheet(f, 0, 0, W, "Mandate · Northbeam Capital · Yield sleeve", "mandate id  pm.m.northbeam-01  ·  version 3  ·  signed by investor and operator  ·  expires 2027-10-15", [
        ("Universe", [("Allowed vaults", "6 of 14 listed"), ("Asset types", "MMF, T-bill, repo, notes"), ("Private credit", "≤ 15%"), ("New vaults", "Need approval")]),
        ("Limits", [("Max per vault", "40%"), ("Max per issuer", "50%"), ("Min same-day liquidity", "60%"), ("Max duration", "90 days")]),
        ("Risk triggers", [("NAV deviation", "> 0.25% → exit"), ("Attestation late", "> 48h → watch"), ("Gate imposed", "→ redeem"), ("Rating cut", "→ propose exit")]),
        ("Execution", [("Agent", "Claude, via gateway"), ("Mode", "Copilot"), ("Auto threshold", "$250k per action"), ("Daily turnover", "≤ 20% of book")]),
        ("Liquidity plan", [("Cash buffer", "$2m always"), ("Known outflows", "Redemptions, monthly"), ("Sweep in", "Above $3m idle"), ("Source", "Fund admin feed")]),
        ("Controls", [("Approvers", "2 of 3 PMs"), ("Pause", "Any approver"), ("Revoke", "CIO party"), ("Withdraw out", "Investor only")]),
    ])
    f.write()


def f_custody():
    f = Fig("05-2-custody", W, 520, "Fig 5.2 · The custody boundary", "The agent moves value inside your party. It cannot move it out.",
            "Withdrawals to any other party are not a choice the agent holds. There is no key to steal and no instruction to fake.")
    f.container(0, 30, 700, 440, "Investor's party · Northbeam Capital", dash=False, fill="s1")
    f.box(32, 220, 190, 60, "Cash token", "Stablecoin or deposit", kind="inset")
    vaults = [("T-bill MMF vault", 80), ("Repo vault", 200), ("Gold vault", 320)]
    for t, y in vaults:
        f.box(470, y, 200, 60, t, "Units, owned by you", kind="inset")
        f.path([(224, 250), (466, y + 30)], "brand", both=True)
    f.arrow_label(300, 190, "subscribe / redeem")
    f.path([(570, 142), (570, 196)], "brand", both=True)
    f.path([(570, 262), (570, 316)], "brand", both=True)
    f.arrow_label(570, 169, "switch")
    f.arrow_label(570, 289, "switch")
    f.box(32, 384, 190, 60, "Mandate", "Rights granted to agent", kind="pm")
    f.box(270, 384, 170, 60, "AI agent", "Calls Rebalance only")
    f.path([(222, 414), (268, 414)], "faint")
    f.path([(355, 384), (355, 312)], "faint", dash=True)
    f.arrow_label(355, 348, "instructs")
    # outside
    outs = [("External address", 80), ("Agent's own party", 200), ("Promorphic operator", 320)]
    for t, y in outs:
        f.box(820, y, 220, 60, t, "Not reachable", kind="ghost")
        f.path([(702, y + 30), (790, y + 30)], "faint", dash=True, arrow=False)
        f.path([(796, y + 18), (796, y + 42)], "ink", arrow=False)
    f.text(820, 420, "Outflows need the investor's", "body")
    f.text(820, 440, "own signature, every time.", "body")
    f.legend(0, 500, [("brand-line", "Agent may do"), ("dash-line", "Blocked: no such choice"), ("pm", "Promorphic contract")])
    f.write()


def f_gates():
    f = Fig("05-3-gates", W, 430, "Fig 5.3 · Policy gates", "Every action is rehearsed against the mandate before it is sent.",
            "Gates run in this order, cheapest first. The first failure stops the action and writes the gate and the numbers to the audit record.")
    gates = ["Universe", "Per vault", "Per issuer", "Liquidity", "Duration", "Turnover", "Threshold"]
    x0, step = 160, 106
    for lane, (y, fail) in enumerate([(92, None), (272, 3)]):
        f.text(0, y - 66, "Action A · move $400k to T-bill MMF" if lane == 0 else "Action B · move $900k to repo", "label-ink")
        f.box(0, y - 22, 140, 44, "Proposed", kind="pm")
        end = x0 + len(gates) * step
        stop = x0 + fail * step + step / 2 if fail is not None else end
        f.path([(140, y), (stop, y)], "brand" if fail is None else "brand", arrow=False, dash=True)
        for i, g in enumerate(gates):
            gx = x0 + i * step + step / 2
            failed = fail == i
            past = fail is not None and i > fail
            f.rect(gx - 3, y - 26, 6, 52, fill=("s2" if past else ("ink" if failed else "faint")), stroke=None, rx=0)
            f.text(gx, y + 44, g, "label-faint" if past else "label", "middle")
            if not past:
                f.text(gx, y - 38, "fail" if failed else "pass", "sub-faint" if not failed else "sub", "middle")
        if fail is None:
            f.path([(end, y), (end + 40, y)], "brand")
            f.rect(end + 42, y - 22, W - end - 42, 44, fill="brand", stroke=None)
            f.text(end + 42 + (W - end - 42) / 2, y, "Send", "title", "middle", fill="onbrand")
        else:
            f.path([(stop, y + 26), (stop, y + 70), (end + 40, y + 70)], "faint", dash=True, r=8)
            f.box(end + 42, y + 48, W - end - 42, 44, "Rejected", kind="ghost")
            f.arrow_label((stop + end) / 2, y + 70, "same-day liquidity 54% < 60% floor")
    f.legend(0, 414, [("brand-line", "Sent after a clean dry run"), ("dash-line", "Stopped, reason recorded")])
    f.write()


def f_loop():
    f = Fig("06-1-agent-loop", W, 300, "Fig 6.1 · The agent loop", "The agent decides. Promorphic checks, executes and records.",
            "The loop runs on events (an issuer notice, a NAV print, a cash need) and on a schedule, so a quiet book is still reviewed.")
    steps = [("Observe", "Feeds and ledger"), ("Assess", "Against mandate"), ("Propose", "Agent decides"), ("Check", "Policy gates"), ("Act", "Per mode"), ("Record", "Audit store")]
    bw, gap = 160, 28.8
    for i, (t, s) in enumerate(steps):
        x = i * (bw + gap)
        if t == "Act":
            f.rect(x, 40, bw, 64, fill="brand", stroke=None)
            f.text(x + bw / 2, 62, t, "title", "middle", fill="onbrand")
            f.text(x + bw / 2, 84, s, "sub", "middle", fill="onbrand")
        else:
            f.box(x, 40, bw, 64, t, s, kind="pm")
        f.text(x + bw / 2, 20, f"0{i + 1}", "label-faint", "middle")
        if i < 5:
            f.path([(x + bw, 72), (x + bw + gap - 2, 72)], "brand")
    last = 5 * (bw + gap) + bw / 2
    f.path([(last, 104), (last, 150), (bw / 2, 150), (bw / 2, 106)], "faint", dash=True, r=10)
    f.arrow_label(W / 2, 150, "next event or next scheduled review")
    rows = [("Observe", "Promorphic assembles holdings, NAVs, issuer notices, rates and fund flows into one context"),
            ("Assess", "The partner agent reads the context and the mandate; finds drift, risk and idle cash"),
            ("Propose", "The agent calls propose() with the smallest fix and a written reason; Promorphic takes it from there")]
    for i, (a, b) in enumerate(rows):
        f.text(0, 200 + i * 24, a, "label-ink")
        f.text(110, 200 + i * 24, b, "body")
    f.write()


def f_signals():
    f = Fig("06-2-signals", W, 460, "Fig 6.2 · What the agent watches", "Five kinds of signal in. Three kinds of output.",
            "Most days the output is a report that says nothing needs doing. That is the product working.")
    ins = [("Issuer events", "Gates, notices, delays"), ("Pricing", "NAV, deviation, staleness"), ("Market", "Rates, yields, spreads"),
           ("Portfolio", "Drift, concentration"), ("Fund", "Flows, redemptions")]
    f.text(0, 12, "Signals", "label")
    for i, (t, s) in enumerate(ins):
        y = 34 + i * 84
        f.box(0, y, 230, 60, t, s, align="left")
        f.path([(230, y + 30), (440, 220)], "faint", arrow=False)
        f.port(230, y + 30, 5, fill="faint")
    bx, by, bw, bh = 440, 150, 220, 140
    f.rect(bx, by, bw, bh, fill="brand", stroke=None)
    f.mark(bx + bw / 2 - 12, by + 30, 0.75, on="onbrand")
    f.text(bx + bw / 2, by + 82, "Promorphic", "title-lg", "middle", fill="onbrand")
    f.text(bx + bw / 2, by + 106, "context for the agent", "sub", "middle", fill="onbrand")
    outs = [("Proposal", "Moves + reason, to approve"), ("Alert", "Needs a human now"), ("Report", "Daily book, nothing to do")]
    f.text(W, 12, "Outputs", "label", "end")
    for i, (t, s) in enumerate(outs):
        y = 74 + i * 120
        f.box(874, y, 230, 60, t, s, align="left", kind="pm")
        f.path([(660, 220), (872, y + 30)], "brand")
    f.write()


def f_decision():
    f = Fig("06-3-routing", W, 400, "Fig 6.3 · Routing a proposal", "What happens to a proposal depends on the mode and its size.",
            "Example threshold $250k. Above it, Autopilot behaves like Copilot. The manager sets the number in the mandate.")
    f.box(0, 40, 170, 56, "Proposal", "Passed all gates", kind="pm")
    f.path([(170, 68), (226, 68)], "faint")
    f.box(228, 40, 150, 56, "Mode?", kind="inset")
    ys = {"Manual": 20, "Copilot": 150, "Autopilot": 280}
    for m, y in ys.items():
        f.path([(378, 68), (402, 68), (402, y + 28), (440, y + 28)], "faint", r=8)
        f.arrow_label(420 + 2, y + 10, m, anchor="start", style="label", bg=False) if False else None
        f.text(450 - 4, y + 2 - 8, m, "label", "start")
    f.box(440, 20, 220, 56, "Alert only", "Manager acts by hand", kind="plain")
    f.box(440, 150, 220, 56, "Approval queue", "Approvers sign on ledger")
    f.box(440, 280, 220, 56, "Size ≤ threshold?", kind="inset")
    f.path([(550, 280), (550, 208)], "faint")
    f.arrow_label(572, 244, "no", anchor="start")
    f.path([(660, 308), (860, 308)], "brand")
    f.arrow_label(760, 308, "yes")
    f.path([(660, 178), (860, 178)], "brand")
    f.arrow_label(790, 178, "approved")
    f.rect(862, 140, 242, 200, fill="brand", stroke=None)
    f.text(983, 220, "Execute", "title-lg", "middle", fill="onbrand")
    f.text(983, 246, "Mandate choice on Canton", "sub", "middle", fill="onbrand")
    f.text(983, 266, "then notify and record", "sub", "middle", fill="onbrand")
    f.write()


if __name__ == "__main__":
    for fn in [f_vault_anatomy, f_vault_lifecycle, f_mandate, f_custody, f_gates, f_loop, f_signals, f_decision]:
        fn()
    print("\n".join(WARN) or "no warnings")
