from kit import Fig, WARN, tw
W = 1104


def sequence(name, eyebrow, title, caption, parts, steps, note=None):
    """parts: list of (label, sub, kind). steps: (a, b, text, kind) with a==b for a self-note."""
    n = len(parts)
    colw = W / n
    xs = [colw * i + colw / 2 for i in range(n)]
    step_h = 46
    top = 80
    H = top + 20 + len(steps) * step_h + (70 if note else 30)
    f = Fig(name, W, H, eyebrow, title, caption, rules=False)
    bw = min(190, colw - 16)
    for i, (lab, sub, kind) in enumerate(parts):
        x = xs[i] - bw / 2
        if kind == "brand":
            f.rect(x, 0, bw, 56, fill="brand", stroke=None)
            f.text(xs[i], 19, lab, "title", "middle", fill="onbrand")
            f.text(xs[i], 39, sub, "sub", "middle", fill="onbrand")
        else:
            f.box(x, 0, bw, 56, lab, sub, kind=kind)
        f.path([(xs[i], 56), (xs[i], H - (60 if note else 16))], "hair", arrow=False, dash=True)
    y = top
    for k, (a, b, text, kind) in enumerate(steps):
        y = top + 20 + k * step_h
        f.text(14, y, f"{k + 1:02d}", "label-faint")
        if a == b:
            w = tw(text, "sub") + 24
            x0 = min(max(xs[a] - w / 2, 40), W - w)
            f.rect(x0, y - 15, w, 30, fill="s2")
            f.text(x0 + w / 2, y, text, "sub", "middle", fill="ink")
        else:
            x1, x2 = xs[a], xs[b]
            d = 1 if x2 > x1 else -1
            f.path([(x1 + d * 4, y + 8), (x2 - d * 6, y + 8)], kind, dash=(kind == "faint-dash"))
            f.port(x1, y + 8, 5, fill="brand" if kind == "brand" else "faint")
            mid = (x1 + x2) / 2
            f.text(mid, y - 6, text, "sub" if kind != "brand" else "sub", "middle", fill="ink" if kind == "brand" else None,
                   maxw=abs(x2 - x1) + colw - 40)
    if note:
        f.rect(0, H - 44, W, 40, fill="s1")
        f.text(16, H - 24, note, "body")
    f.write()


def seqs():
    sequence("07-1-onboarding", "Fig 7.1 · Flow · Onboarding", "From signed mandate to a connected agent.",
             "The mandate is created with both signatures. Gateway credentials are scoped to one mandate and expire with it.",
             [("Manager", "PM, approvers", "plain"), ("Promorphic", "Terminal, gateway", "brand"), ("Canton", "Ledger", "plain"), ("AI agent", "Execution partner", "plain")],
             [(0, 1, "KYB, connect the manager's party", "faint"),
              (1, 0, "Mandate drafted from a template", "faint"),
              (0, 2, "Sign mandate (investor signature)", "faint"),
              (1, 2, "Countersign as operator: mandate active", "brand"),
              (0, 1, "Pick an agent and a mode", "faint"),
              (1, 3, "Issue gateway credentials, scoped to the mandate", "brand"),
              (3, 1, "read_context(): first review of the book", "faint"),
              (1, 0, "Day-one report: book, limits, findings", "faint")])
    sequence("07-2-copilot", "Fig 7.2 · Flow · Copilot rebalance", "An issuer imposes a gate. The book is fixed before the PM's first coffee.",
             "Every step writes to the audit store. If approval does not arrive before the proposal's expiry, nothing moves.",
             [("Issuer", "Credit fund", "plain"), ("Promorphic", "Gateway, gates", "brand"), ("AI agent", "Execution partner", "plain"), ("Approvers", "2 of 3 PMs", "plain"), ("Canton", "Ledger", "plain")],
             [(0, 1, "Notice: redemption gate, 90 days", "faint"),
              (1, 2, "Event + context: book, mandate, DD", "faint"),
              (2, 1, "propose(redeem 8% credit, buy MMF) + reason", "faint"),
              (1, 1, "Policy pre-check: 7 of 7 gates pass", "faint"),
              (1, 4, "Create Proposal contract", "brand"),
              (1, 3, "Notify: one proposal to approve", "faint"),
              (3, 4, "Approve, two signatures", "faint"),
              (1, 4, "Exercise Rebalance: mandate re-checks limits", "brand"),
              (4, 0, "Redemption request, subscription request", "brand"),
              (1, 3, "Settled. Record and reason filed.", "faint")])
    sequence("07-3-autopilot", "Fig 7.3 · Flow · Autopilot sweep", "Saturday, 02:10. Idle cash goes to work without waking anyone.",
             "Size $240k is under the $250k threshold, so no approval is needed. The issuer's cutoff decides when it settles, not office hours.",
             [("Fund admin", "Flows feed", "plain"), ("Promorphic", "Gateway, gates", "brand"), ("AI agent", "Execution partner", "plain"), ("Canton", "Ledger", "plain"), ("Issuer", "MMF", "plain")],
             [(0, 1, "Subscriptions in: idle cash $3.24m", "faint"),
              (1, 2, "Event: idle above $3m sweep line", "faint"),
              (2, 1, "propose(subscribe $240k to MMF) + reason", "faint"),
              (1, 1, "Gates pass · size ≤ threshold · auto", "faint"),
              (1, 3, "Exercise Rebalance under mandate", "brand"),
              (3, 4, "Subscription request, queued for cutoff", "brand"),
              (4, 3, "Accept at Monday cutoff, units settle", "faint"),
              (1, 0, "Monday report: what moved and why", "faint")])
    sequence("07-4-stop", "Fig 7.4 · Flow · Pause and revoke", "One switch stops the agent. Holdings stay exactly where they are.",
             "Pause is reversible and any approver can use it. Revoke archives the mandate; a new one needs both signatures again.",
             [("Manager", "Any approver", "plain"), ("Canton", "Ledger", "plain"), ("Promorphic", "Gateway", "brand"), ("AI agent", "Execution partner", "plain")],
             [(0, 1, "Exercise Pause on the mandate", "faint"),
              (1, 2, "Mandate paused (ledger event)", "faint"),
              (2, 2, "Open proposals expire · tools read-only", "faint"),
              (3, 2, "propose(...)", "faint"),
              (2, 3, "Rejected: mandate paused", "faint"),
              (0, 1, "Exercise Revoke (CIO): mandate archived", "faint"),
              (2, 3, "Gateway credentials revoked", "brand")],
             note="Holdings never move during a stop. They were always the manager's, on the manager's party.")


def f_roadmap():
    f = Fig("09-1-roadmap", W, 350, "Fig 10.1 · Roadmap", "Earn delegation one step at a time.",
            "Each phase ships when the one before has a clean audit record. Phases are sequenced, not dated.")
    phases = [("Phase 0", "Catalogue", ["Canton vaults, DD packs", "Manual subscribe, redeem", "Terminal: book, vaults"]),
              ("Phase 1", "Copilot", ["Mandate contract", "Agent gateway: MCP, API", "Proposals, approvals, record"]),
              ("Phase 2", "Autopilot", ["Threshold execution", "Risk triggers, auto-exit", "Daily reports"]),
              ("Phase 3", "Collateral and rails", ["Repo and pledge", "Margin-call defence", "Second institutional chain"])]
    cw, gap = 258, 23.3
    f.path([(0, 44), (W, 44)], "faint", arrow=False)
    f.path([(0, 44), (cw / 2, 44)], "brand", arrow=False)
    for i, (p, name, items) in enumerate(phases):
        x = i * (cw + gap)
        cx = x + cw / 2
        if i == 0:
            f.port(cx, 44, 10)
            f.tag(cx, 14, "Now", brand=True, anchor="middle")
        else:
            f.node(cx, 44, 10)
        f.rect(x, 70, cw, 260, fill="s1")
        f.text(x + 20, 88, p, "label")
        f.text(x + 20, 120, name, "title-lg")
        for k, it in enumerate(items):
            f.port(x + 24, 168 + k * 32, 5, fill="faint")
            f.text(x + 38, 168 + k * 32, it, "body-ink", maxw=cw - 50)
        f.text(x + 20, 304, ["Proves: distribution", "Proves: agents are safe", "Proves: delegation pays", "Proves: the network"][i], "sub")
    f.write()


def f_risks():
    f = Fig("08-1-risks", W, 480, "Fig 8.1 · Failure modes", "What goes wrong, and what stops it.",
            "No single control is trusted alone. The last line is always the same: the agent cannot move value out of the manager's party.", rules=False)
    rows = [("The agent proposes a bad trade", "Seven gates off-ledger, the mandate on-ledger, approvals in Copilot"),
            ("The agent is prompt-injected", "It can only call Rebalance inside limits. No outflow choice exists"),
            ("Promorphic is compromised", "Operator is not an owner. Holdings cannot move; managers can pause"),
            ("Issuer data is wrong or stale", "Staleness limits, NAV deviation triggers, vault moves to Watch"),
            ("A settlement leg fails", "Canton commits whole or not at all. Retried, then alerted"),
            ("The mandate is too loose", "Templates, review on signing, Copilot as the default mode")]
    f.text(0, 10, "Risk", "label")
    f.text(470, 10, "Control", "label")
    for i, (r, c) in enumerate(rows):
        y = 34 + i * 74
        f.rect(0, y, 420, 58, fill="s1")
        f.text(20, y + 29, r, "title", maxw=390)
        f.path([(424, y + 29), (466, y + 29)], "brand")
        f.rect(470, y, W - 470, 58, fill="s1")
        f.port(477, y + 7, 6)
        f.text(490, y + 29, c, "body-ink", maxw=W - 500)
    f.write()


def f_screens():
    f = Fig("08-2-screen-map", W, 350, "Fig 9.1 · The terminal", "The book is home. Six screens sit one click from it.")
    f.rect(392, 140, 320, 90, fill="brand", stroke=None)
    f.text(552, 172, "Book", "title-lg", "middle", fill="onbrand")
    f.text(552, 198, "Positions, limits, proposals", "sub", "middle", fill="onbrand")
    around = [(0, 20, "Vaults", "Catalogue, filters"), (0, 140, "Vault detail", "DD pack, terms"), (0, 260, "Onboarding", "Party, mandate, agent"),
              (824, 20, "Mandate", "Limits, mode, roles"), (824, 140, "Proposal", "Reason, gates, approve"), (824, 260, "Record", "Audit log, export")]
    for x, y, t, s in around:
        f.box(x, y, 280, 70, t, s, kind="pm")
        if x == 0:
            f.path([(280, y + 35), (330, y + 35), (330, 185), (390, 185)], "faint", r=10)
        else:
            f.path([(824, y + 35), (774, y + 35), (774, 185), (714, 185)], "faint", r=10)
    f.write()


if __name__ == "__main__":
    seqs(); f_roadmap(); f_risks(); f_screens()
    print("\n".join(WARN) or "no warnings")
