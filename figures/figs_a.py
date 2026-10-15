from kit import Fig, WARN, tw
W = 1104


def f_thesis():
    f = Fig("01-1-thesis", W, 440, "Fig 1.1 · Thesis", "The assets moved to institutional chains. The managers have to follow.",
            "Issuance flows in from the left. Every manager on the right needs a way to act on it, around the clock, under its own rules.")
    assets = [("Tokenized treasuries", "T-bills, notes"), ("Money market funds", "Daily NAV"), ("Private credit", "Senior secured"),
              ("Repo and collateral", "Overnight, term"), ("Tokenized deposits", "Bank cash")]
    f.text(0, 12, "Issuers tokenize", "label")
    for i, (t, s) in enumerate(assets):
        y = 36 + i * 74
        f.box(0, y, 210, 56, t, s, align="left")
        f.path([(210, y + 28), (250, y + 28), (250, 210), (292, 210)] if False else [(210, y + 28), (300, 210)], "faint", arrow=False)
    # chain container
    f.container(300, 36, 250, 350, "Institutional chains")
    f.box(320, 70, 210, 150, "Canton Network", "Daml contracts", sub2="Private, permissioned", title_style="title-lg")
    f.box(320, 240, 210, 56, "Other institutional rails", "Next, by demand", kind="ghost")
    f.box(320, 312, 210, 56, "Public chains", "Ethereum and others", kind="ghost")
    # promorphic block
    bx, by, bw, bh = 640, 145, 180, 130
    f.rect(bx, by, bw, bh, fill="brand", stroke=None)
    f.mark(bx + bw / 2 - 12, by + 34, 0.75, on="onbrand")
    f.text(bx + bw / 2, by + 82, "Promorphic", "title-lg", "middle", fill="onbrand")
    f.text(bx + bw / 2, by + 104, "Mandates + agents", "sub", "middle", fill="onbrand")
    f.path([(bx, 210), (532, 145)], "brand")
    f.port(bx, 210, 6)
    mgrs = [("Onchain asset managers", "Funds, vaults, SMAs"), ("Portfolio managers", "Multi-asset books"),
            ("Fund treasuries", "Idle cash, reserves"), ("Allocators", "Fund-of-funds, FOs")]
    f.text(W, 12, "Managers act, via agents", "label", "end")
    for i, (t, s) in enumerate(mgrs):
        y = 56 + i * 82
        f.box(894, y, 210, 56, t, s, align="left")
        f.path([(894, y + 28), (820, 210)], "brand", arrow=False)
    f.legend(0, 424, [("brand-block", "Promorphic"), ("brand-line", "Action: manager to asset"), ("faint-line", "Issuance"), ("ghost", "Later")])
    f.write()


def f_before_after():
    f = Fig("01-2-before-after", W, 540, "Fig 1.2 · The job today and with Promorphic", "One manager, many issuers: from portals and spreadsheets to one mandate.")
    # left panel
    f.container(0, 16, 530, 480, "Today", dash=False, fill="s1")
    f.box(24, 60, 160, 56, "Portfolio manager", "9 to 6, weekdays", kind="inset")
    chans = ["Issuer portal", "Email and PDF", "Transfer agent", "Spreadsheet"]
    iss = ["Issuer A", "Issuer B", "Issuer C", "Issuer D"]
    for i, c in enumerate(chans):
        y = 48 + i * 86
        f.box(222, y, 140, 48, c, kind="inset")
        f.box(390, y, 116, 48, iss[i], kind="inset")
        f.path([(184, 88), (204, 88), (204, y + 24), (220, y + 24)], "faint", arrow=True)
        f.path([(362, y + 24), (388, y + 24)], "faint", dash=True)
    f.lines(24, 420, ["Each issuer has its own onboarding, cutoffs,", "forms and redemption windows. Rebalancing", "is a project. Nobody watches at 3am on Sunday."], "body", lh=19)
    # right panel
    f.container(574, 16, 530, 480, "With Promorphic", dash=False, fill="s1")
    f.box(598, 60, 160, 56, "Portfolio manager", "Sets the mandate", kind="inset")
    f.path([(758, 88), (806, 88)], "faint")
    mx, my, mw, mh = 808, 52, 136, 72
    f.rect(mx, my, mw, mh, fill="brand", stroke=None)
    f.text(mx + mw / 2, my + 26, "Promorphic", "title", "middle", fill="onbrand")
    f.text(mx + mw / 2, my + 48, "+ AI agent, 24/7", "sub", "middle", fill="onbrand")
    for i, v in enumerate(["T-bill vault", "MMF vault", "Credit vault", "Repo vault"]):
        y = 174 + i * 58
        f.box(964, y, 116, 44, v, kind="inset")
        f.path([(876, 124), (876, y + 22), (962, y + 22)], "brand", r=10)
    f.port(876, 124, 6)
    f.lines(598, 420, ["One mandate, one terminal. The agent watches", "every issuer, proposes or acts inside limits,", "and records why. Funds never leave", "the manager's own party."], "body", lh=19)
    f.legend(0, 524, [("brand-line", "Promorphic acts"), ("faint-line", "Manual step"), ("dash-line", "Off-ledger hand-off")])
    f.write()


def f_ecosystem():
    f = Fig("01-3-ecosystem", W, 470, "Fig 1.3 · Who is who", "Issuers distribute. Agents execute. Managers own the book and set the rules.",
            "Agent names are examples of models a manager can connect; naming them implies no partnership.")
    cx, cy, cw, ch = 432, 150, 240, 150
    f.rect(cx, cy, cw, ch, fill="brand", stroke=None)
    f.mark(cx + cw / 2 - 12, cy + 30, 0.75, on="onbrand")
    f.text(cx + cw / 2, cy + 82, "Promorphic", "title-lg", "middle", fill="onbrand")
    f.text(cx + cw / 2, cy + 106, "Mandates, gates, record", "sub", "middle", fill="onbrand")
    # customers top
    f.tag(W / 2, 12, "Customers", anchor="middle")
    f.box(392, 32, 320, 64, "Onchain asset and portfolio managers", "Own the funds. Sign the mandate.")
    f.path([(552, 96), (552, 148)], "brand")
    f.arrow_label(552, 122, "mandate")
    # agents left
    f.tag(160, 112, "Execution partners", anchor="middle")
    for i, a in enumerate(["Claude", "ChatGPT", "Gemini", "Your own agent"]):
        y = 132 + i * 64
        f.box(40, y, 240, 48, a, kind="ghost" if i == 3 else "plain")
        f.path([(280, y + 24), (430, 225)], "brand", arrow=(i == 1))
    f.arrow_label(356, 160, "decide, call tools", bg=True)
    # issuers right
    f.tag(W - 160, 112, "Distribution partners", anchor="middle")
    for i, a in enumerate(["Fund issuers", "Credit platforms", "Commodity issuers", "Banks: deposits, repo"]):
        y = 132 + i * 64
        f.box(824, y, 240, 48, a)
        f.path([(674, 225), (822, y + 24)], "brand", arrow=True)
    f.arrow_label(748, 160, "list as vaults", bg=True)
    # canton base
    f.rect(0, 410, W, 44, fill="s1")
    f.text(W / 2, 432, "Settles on Canton Network · investor-owned holdings · Daml contracts", "sub", "middle")
    f.path([(552, 300), (552, 408)], "brand")
    f.write()


def f_stack():
    f = Fig("02-1-stack", W, 690, "Fig 2.1 · The product", "Four layers. Promorphic is the one in the middle that makes the others safe to connect.")
    rows = [
        ("Agents", "Execution partners", ["Claude", "ChatGPT", "Gemini", "Your own agent"], "plain", "Third parties"),
        ("Promorphic", "The manager's layer", ["Mandate engine", "Agent gateway", "Policy gates", "Audit record"], "pm", "Promorphic moat"),
        ("Vaults", "Distribution partners", ["T-bill MMF", "Private credit", "Tokenized gold", "Repo"], "pm", "Promorphic curates"),
        ("Assets", "Issued on Canton", ["Issuers", "Transfer agents", "Custodians", "Cash tokens"], "inset", "Third parties"),
    ]
    y = 20
    for i, (lab, sub, items, kind, own) in enumerate(rows):
        h = 120
        f.rect(0, y, W, h, fill="s1")
        f.text(24, y + 40, lab, "title-lg")
        f.text(24, y + 64, sub, "sub")
        f.text(24, y + 92, own, "label-faint")
        bw, gap, x0 = 188, 20, 260
        for j, it in enumerate(items):
            bx = x0 + j * (bw + gap)
            if i == 1 and j == 1:
                f.rect(bx, y + 28, bw, 64, fill="brand", stroke=None)
                f.text(bx + bw / 2, y + 60, it, "title", "middle", fill="onbrand")
            else:
                f.box(bx, y + 28, bw, 64, it, kind="ghost" if (i == 0 and j == 3) else kind)
        if i < 3:
            f.path([(562, y + h), (562, y + h + 38)], "brand")
        y += h + 40
    f.legend(0, 674, [("brand-block", "Where agents plug in"), ("pm", "Promorphic-owned"), ("brand-line", "Where actions go")])
    f.write()


def f_modes():
    f = Fig("02-2-modes", W, 390, "Fig 2.2 · Operating modes", "Manual, Copilot, Autopilot: the same mandate, three levels of delegation.",
            "Every mode is enforced by the same mandate contract. Autopilot adds a size threshold above which the agent falls back to Copilot.")
    cols = [
        ("01 · Manual", "You decide, you act", ["Read the DD pack", "Subscribe and redeem", "Agent stays silent"], "Who acts: you", 0),
        ("02 · Copilot", "Agent proposes, you approve", ["Agent watches 24/7", "Proposal with reasons", "Approve in one click"], "Who acts: you, on its advice", 1),
        ("03 · Autopilot", "Agent acts inside limits", ["Executes within mandate", "Large moves need approval", "Notifies, records, explains"], "Who acts: the agent", 2),
    ]
    cw, gap = 352, 24
    for i, (t, s, bullets, who, lvl) in enumerate(cols):
        x = i * (cw + gap)
        f.rect(x, 16, cw, 330, fill="s1")
        f.text(x + 24, 48, t, "label")
        f.text(x + 24, 82, s, "title-lg")
        for k, b in enumerate(bullets):
            f.port(x + 28, 128 + k * 30, 5, fill="faint")
            f.text(x + 42, 128 + k * 30, b, "body-ink")
        # delegation meter
        f.text(x + 24, 246, "Delegation", "label-faint")
        for k in range(3):
            fill = "brand" if k <= lvl else None
            f.rect(x + 24 + k * 102, 262, 94, 10, fill=fill, stroke=None if fill else "hair", rx=0)
        f.text(x + 24, 306, who, "sub")
        if i < 2:
            f.path([(x + cw + 2, 181), (x + cw + gap - 2, 181)], "faint")
    f.text(0, 374, "Ship order: Manual and Copilot in v1. Autopilot once the audit record has a track record.", "body")
    f.write()


def f_components():
    f = Fig("03-1-components", W, 640, "Fig 3.1 · Architecture", "Components, and where each one runs.",
            "Partner agents never touch the ledger directly. They call gateway tools; Promorphic checks the mandate and exercises the choice.")
    # columns: off-ledger (left/top), on-ledger (bottom)
    f.container(0, 16, W, 320, "Promorphic off-ledger services")
    f.box(24, 52, 200, 64, "Terminal", "For the manager's team", kind="pm")
    f.box(24, 140, 200, 64, "AI agents", "Execution partners", kind="ghost")
    f.box(24, 228, 200, 64, "Notifications", "Email, Slack, webhook", kind="pm")
    # agent core
    f.rect(300, 52, 250, 240, fill="s2")
    f.text(316, 72, "Promorphic core", "label")
    f.rect(316, 90, 218, 70, fill="brand", stroke=None)
    f.text(425, 116, "Agent gateway", "title", "middle", fill="onbrand")
    f.text(425, 138, "MCP and API tools", "sub", "middle", fill="onbrand")
    f.box(316, 176, 218, 46, "Policy pre-check", "Simulates the mandate", kind="pm")
    f.box(316, 234, 218, 46, "Mandate engine", "Limits, modes, routing", kind="pm")
    # data
    f.box(626, 52, 210, 64, "DD registry", "Structured due diligence", kind="pm")
    f.box(626, 140, 210, 64, "Signal feeds", "NAV, rates, attestations", kind="pm")
    f.box(626, 228, 210, 64, "Audit store", "Every proposal, every check", kind="pm")
    f.box(894, 52, 186, 64, "Issuer data", "Notices, NAV files", kind="ghost")
    f.box(894, 140, 186, 64, "Market data", "Rates, prices", kind="ghost")
    f.box(894, 228, 186, 64, "Fund flows", "Subs, redemptions", kind="ghost")
    for y in (84, 172, 260):
        f.path([(892, y), (838, y)], "faint")
    f.path([(626, 172), (552, 172)], "faint")
    f.path([(626, 84), (590, 84), (590, 120), (552, 120)], "faint")
    f.path([(552, 256), (624, 256)], "faint")
    f.path([(226, 84), (298, 110)], "faint", arrow=True)
    f.path([(226, 172), (240, 172), (240, 132), (298, 132)], "brand", arrow=True)
    # ledger
    f.container(0, 380, W, 220, "Canton Network")
    f.box(24, 420, 260, 72, "Promorphic validator", "Participant node, MainNet", kind="pm")
    f.box(320, 420, 230, 72, "Mandate contract", "Limits, roles, revoke", kind="pm")
    f.box(586, 420, 230, 72, "Vault contracts", "Subscribe, redeem, terms", kind="pm")
    f.box(852, 420, 228, 72, "Investor holdings", "Owned by the investor", kind="inset")
    f.box(320, 516, 230, 60, "Proposal contracts", "Pending, approved", kind="pm")
    f.box(586, 516, 494, 60, "Issuer and cash instruments", "Canton token standard holdings, third-party", kind="plain")
    f.path([(425, 292), (425, 340), (154, 340), (154, 418)], "brand", r=10)
    f.arrow_label(290, 340, "exercise choice via JSON API")
    f.path([(284, 456), (318, 456)], "brand")
    f.path([(550, 456), (584, 456)], "brand")
    f.path([(816, 456), (850, 456)], "brand")
    f.legend(0, 624, [("pm", "Promorphic-owned"), ("ghost", "External source"), ("inset", "Investor-owned") if False else ("plain", "Third party"), ("brand-line", "Action path")])
    f.write()


def f_parties():
    f = Fig("03-2-parties", W, 520, "Fig 3.2 · Canton parties and rights", "Who signs what. The agent's party can only call the choices the mandate grants.",
            "Signatories must all agree to create a contract. A controller is the party allowed to exercise a choice on it.")
    parties = [("Investor", "The manager's party"), ("Promorphic operator", "Runs the service"), ("Agent", "Partner model's party"), ("Issuer", "Mints and redeems")]
    xs = [262, 474, 686, 898]
    cw = 206
    for i, (p, s) in enumerate(parties):
        if p == "Agent":
            f.rect(xs[i], 16, cw, 64, fill="brand", stroke=None)
            f.text(xs[i] + cw / 2, 38, p, "title", "middle", fill="onbrand")
            f.text(xs[i] + cw / 2, 60, s, "sub", "middle", fill="onbrand")
        else:
            f.box(xs[i], 16, cw, 64, p, s, kind="pm" if "Promorphic" in p else "plain")
        f.path([(xs[i] + cw / 2, 80), (xs[i] + cw / 2, 470)], "hair", arrow=False, dash=True)
    f.text(0, 48, "Contract", "label")
    rows = [
        ("Mandate", {0: "Signatory", 1: "Signatory", 2: "Controller: Rebalance"}, "Investor can amend, pause, revoke"),
        ("Proposal", {0: "Controller: Approve", 1: "Signatory", 2: "Creates"}, "Expires if not approved"),
        ("Holding", {0: "Owner", 3: "Registrar"}, "Never transferable to the agent"),
        ("Subscription", {0: "Requests", 3: "Controller: Accept"}, "Cash in, fund units out"),
        ("Redemption", {0: "Requests", 3: "Controller: Settle"}, "Units in, cash out"),
    ]
    for r, (name, cells, note) in enumerate(rows):
        y = 112 + r * 72
        f.rect(0, y, W, 52, fill="s1")
        f.text(16, y + 16, name, "label-ink")
        f.text(16, y + 36, note, "sub-faint", maxw=240)
        for c, txt in cells.items():
            cx = xs[c] + cw / 2
            w = tw(txt, "sub") + 20
            if c == 2:
                f.rect(cx - w / 2, y + 14, w, 24, fill="brand", stroke=None, rx=1)
                f.text(cx, y + 26, txt, "sub", "middle", fill="onbrand")
            else:
                f.rect(cx - w / 2, y + 14, w, 24, fill="s2", rx=1)
                f.text(cx, y + 26, txt, "sub", "middle", fill="ink")
    f.legend(0, 500, [("brand-block", "Agent's rights: narrow, revocable"), ("plain", "Other parties' rights")])
    f.write()


def f_two_keys():
    f = Fig("03-3-two-checks", W, 300, "Fig 3.3 · Defence in depth", "Every action is checked twice: once off-ledger to explain, once on-ledger to enforce.",
            "The pre-check gives fast, readable reasons. The contract is the authority: if the two disagree, the ledger wins and the action fails safe.")
    y = 48
    f.box(0, y - 32, 170, 64, "Agent proposes", "Action + reasons", kind="pm")
    f.box(220, y - 32, 190, 64, "Policy pre-check", "Off-ledger simulation", kind="pm")
    f.box(460, y - 32, 170, 64, "Mode gate", "Approve or auto", kind="pm")
    f.box(680, y - 32, 200, 64, "Mandate contract", "On-ledger, authoritative", kind="pm")
    f.rect(930, y - 32, 174, 64, fill="brand", stroke=None)
    f.text(1017, y - 10, "Settled", "title", "middle", fill="onbrand")
    f.text(1017, y + 12, "Recorded in audit", "sub", "middle", fill="onbrand")
    for a, b in [(170, 220), (410, 460), (630, 680), (880, 930)]:
        f.path([(a, y), (b - 2, y)], "brand")
    # rejects
    for x, lab in [(315, "Fails a gate"), (545, "Desk rejects"), (780, "Choice aborts")]:
        f.path([(x, y + 32), (x, 158)], "faint", dash=True)
        f.box(x - 80, 160, 160, 44, lab, kind="ghost")
    f.text(0, 262, "All three exits write the reason to the audit store. Nothing half-settles: a Canton transaction commits whole or not at all.", "body")
    f.write()


if __name__ == "__main__":
    for fn in [f_thesis, f_before_after, f_ecosystem, f_stack, f_modes, f_components, f_parties, f_two_keys]:
        fn()
    print("\n".join(WARN) or "no warnings")
