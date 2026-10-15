# 8 · Risk and control

## Failure modes

![Failure modes and controls](img/fig-8-1-failure-modes.png)

No single control is trusted alone. The last line is always the same: the agent cannot move value out of the manager's party.

## Controls the manager holds

| Control | Who | Effect |
|---|---|---|
| Limits | Set in the mandate, signed | Enforced before every action, off-ledger and on-ledger |
| Approvals | Approver quorum (e.g. 2 of 3) | Required for every Copilot action and every Autopilot action above threshold |
| Pause | Any approver | Agent tools go read-only; open proposals expire |
| Revoke | Named party (e.g. CIO) | Mandate archived, credentials revoked |
| Record | Anyone with access; exportable | Every action, rejection and signature, with ledger references |

![Record mockup](img/mock-6-record.png)

Rejected proposals are kept. A good record shows what the agent was stopped from doing, not only what it did.

## Regulatory approach

- **Custody.** Promorphic does not hold client assets. Holdings sit on the manager's own party, and no Promorphic contract can move them out.
- **Decisions.** In Copilot, every decision is signed by the manager's approvers. Autopilot executes only inside limits the manager has signed, and is offered where the permissions for it are in place.
- **Distribution.** Vault eligibility, such as professional investors only, sits in the vault terms and is checked at every subscription.
- **Records.** The audit record supports a manager's own books-and-records duties.
