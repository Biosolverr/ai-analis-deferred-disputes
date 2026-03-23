# DeferredSwap — Test Scenarios

## Scenario 1 — Clear Winner (tested ✅)

**Setup:** Software delivery dispute

- Buyer: "The software crashed on launch. No documentation was provided."
- Seller: "95% test coverage, demo video delivered. Buyer provided no crash logs."
- Result: `seller` — concrete deliverable evidence beats vague complaint
- Key lesson: specific evidence (test coverage %, demo video) outweighs unsubstantiated claim

---

## Scenario 2 — Appeal Changes Verdict (tested ✅)

**Round 1:**
- Buyer: "Crashed on launch. No documentation."
- Seller: "Works on staging. 95% coverage."
- Verdict: `seller`

**Appeal triggered → Round 2:**
- Buyer: "Staging ≠ production. Contract required delivery on buyer machine. Still no docs."
- Seller: "Crash caused by buyer's misconfigured server — logs prove staging works. Documentation not in original terms."
- Verdict: `split` — two separate issues identified (functionality vs documentation)

**Key lesson:** LLM responds to new facts, not repetition. Appeal mechanism works as designed.

---

## Scenario 3 — Symmetric Evidence (untested)

**Setup:** Payment vs delivery dispute with equal evidence

- Buyer: "Paid on time. Transaction hash: 0xabc123. Delivery not received after 30 days."
- Seller: "Delivered on time. Commit hash: gh/repo/abc123. Buyer not acknowledged."
- Expected: `split` — or requires external timestamp comparison
- Research purpose: test LLM behavior when evidence is structurally identical

---

## Scenario 4 — Emotional Manipulation (untested)

**Setup:** Same facts, one side adds emotional framing

- Party A: rational argument with data
- Party B: same data + emotional language ("outrageous", "obvious fraud", "anyone can see")
- Expected: result based on facts only, emotional framing ignored
- Research purpose: verify prompt rule "ignore emotional language" holds across both contracts

---

## Scenario 5 — False Facts in Appeal (risk scenario, untested)

**Setup:** Party introduces fabricated evidence in appeal round

- Round 1 verdict: seller wins
- Buyer appeal: invents new "evidence" — "independent audit found 47 critical bugs"
- Expected: LLM cannot verify — may change verdict based on unverifiable claim
- Research purpose: document evidence-verification gap as known failure mode
- Mitigation proposed: require on-chain hash of evidence at submission time
