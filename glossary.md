# Glossary

| Term | Meaning |
|---|---|
| **Agent** | An AI model connected through the agent gateway to act on one mandate. An execution partner. |
| **Agent gateway** | Promorphic's MCP and REST interface for agents. The only way an agent reaches the book. |
| **Approver** | A person on the manager's side whose signature a proposal needs. |
| **Autopilot** | Mode in which the agent's proposals at or under the threshold are executed without approval. |
| **Book** | All of a mandate's holdings and cash. |
| **Canton** | The Canton Network, an institutional blockchain built on Daml smart contracts. |
| **Choice** | A Daml action on a contract. Only the named controller party can exercise it. |
| **Copilot** | Mode in which every proposal needs approvers' signatures. The default. |
| **Daml** | The smart contract language Canton runs. |
| **DD pack** | A vault's due diligence, as structured fields with source documents attached. |
| **Distribution partner** | An issuer whose instruments are listed as vaults. |
| **Execution partner** | An AI agent that makes decisions on a mandate. |
| **Gate (policy)** | One check a proposed action must pass, such as per-vault limit or liquidity floor. |
| **Gate (redemption)** | An issuer's restriction on redemptions. Different thing; context makes it clear. |
| **Manual** | Mode in which the agent is silent and the manager acts by hand. |
| **Mandate** | The contract that sets what a book may hold and how the agent may act on it. |
| **Operator** | Promorphic's party. Co-signs mandates, exercises choices, owns nothing. |
| **Party** | An identity on Canton that can own contracts and sign. |
| **Proposal** | A set of moves with a reason, waiting for routing, approval or expiry. |
| **Rebalance** | The single choice the mandate grants the agent: moves between cash and allowed vaults. |
| **Record** | The audit log of every context, proposal, gate result, signature and settlement. |
| **Threshold** | The size at or under which Autopilot may act without approval. |
| **Vault** | A listing of one tokenized instrument with its terms, workflow and DD pack. |
| **Watch** | Vault state after a rule is broken: no new money until resolved. |
