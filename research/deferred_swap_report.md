# AI-Mediated DeFi Dispute Resolution
## Research Report — March 2026

---

## Summary

This report documents findings from deploying and testing two GenLayer smart contracts
that use multi-model LLM consensus to resolve on-chain disputes. Both contracts were
deployed and tested live on GenLayer Studio with a validator set including DeepSeek-V3,
Llama-4-Maverick-17B, and Grok-4.

The core research question: **can LLM consensus be a reliable, manipulation-resistant
arbitration mechanism for DeFi disputes?**

---

## Contracts Tested

**DeferredSwap v1** — bilateral dispute resolution with appeal mechanism.
Models a real DeFi use case: two parties with a contract, a dispute, and a structured
resolution process including an appeal round with new argument submission.

**Arena v1** — subjective argument evaluation with configurable rules.
Models a generalizable AI-judge pattern where evaluation criteria are set at
contract deployment and cannot be changed by participants mid-match.

---

## Finding 1: LLM Verdict Changes Under Appeal

**Test protocol:**
Round 1 — both parties submitted initial arguments. Verdict: `seller`.
Appeal triggered. Both parties submitted new arguments with different framing and new facts.
Round 2 verdict: `split`.

**What changed:**
In Round 1, the seller's evidence (95% test coverage, demo video) was concrete and
the buyer's complaint (crashed on launch) was vague. In Round 2, the buyer introduced
a new argument — that staging environment is not production and that documentation
was never delivered as a separate obligation. The seller countered with server logs
but did not address the documentation gap. The LLM identified two separate issues
and returned a split verdict.

**Conclusion:**
The LLM responds to new facts, not repetition. Introducing a genuinely new argument
(documentation as a separate obligation) was sufficient to shift the verdict.
The appeal mechanism functions as designed. However, this creates a known risk:
parties may introduce fabricated new facts that the LLM cannot verify on-chain.

---

## Finding 2: Refutation Beats Assertion

**Test protocol:**
Arena deployed with topic "Which is better for DeFi: speed or decentralization?"
and rule "Judge by logical consistency and use of concrete examples. Ignore emotional language."

Player A made positive claims: Solana 65,000 TPS, 90% user abandonment above 5 seconds,
high TVL figures. Player B did not make independent claims — instead directly attacked
Player A's primary example (Solana) by citing 7 network outages in 2022, then added
a counter-example (Ethereum 60% DeFi TVL despite slower speed).

**Result:** Player B won. The LLM verdict explicitly referenced the refutation of
Player A's Solana example as the deciding factor.

**Conclusion:**
When both sides provide concrete data, the side that directly refutes the opponent's
specific example wins over the side that makes independent positive claims.
This mirrors human debate scoring methodology and is consistent across the validator set
(all 5 validators agreed — unanimous consensus).

---

## Finding 3: Prompt Rules Constrain LLM Judgment

**Test protocol:**
Arena was deployed with explicit rule "Ignore emotional language."
Player B's argument included the phrase "just a fast bank" — a clear emotional label
rather than a factual claim. The LLM verdict made no reference to this phrase.
The reasoning was entirely based on outage statistics and TVL figures.

**Conclusion:**
Constructor-level rules embedded in the prompt effectively constrain LLM evaluation
criteria. This is a viable pattern for bias control in on-chain arbitration.
The rule survived the consensus process — all validators applied it consistently.

---

## Finding 4: State Read Timing in GenLayer Studio

**Observation:**
After calling `submit_argument()` for both parties, an immediate `get_status()` call
returned `"open"` rather than the expected `"ready"`.

**Explanation:**
GenLayer Studio reads contract state before full transaction finalization.
The state update was written by the transaction but not yet reflected in the Studio
read layer at the moment of the call. After waiting for FINALIZED status on the
submit_argument transaction, the correct state was readable.

**Conclusion:**
This is not a contract logic bug. It is a Studio UX limitation around read-after-write
consistency. The mitigation is to wait for FINALIZED before calling read methods.
This should be noted in any production deployment documentation.

---

## Failure Modes and Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| False new facts in appeal | High | Verdict manipulation | Require on-chain evidence hash at submission |
| Emotional framing bypasses rules | Medium | Biased verdict | Explicit rule in constructor prompt |
| LLM hallucination of facts | Medium | Wrong verdict | Multi-model consensus (built into GenLayer) |
| Stale state reads | Low | UX confusion | Wait for FINALIZED before read methods |
| Malicious constructor rules | Unknown | Systematic bias | Validator-level rule validation (untested) |

---

## Architecture Observations

GenLayer's multi-model consensus is particularly well-suited for dispute resolution
because it eliminates single-model bias. In the Arena test, all five validators
(two Grok-4, two DeepSeek-V3 instances across different providers, and one Llama-4)
reached unanimous agreement. This cross-provider consensus provides stronger
manipulation resistance than a single-model approach.

The separation of evaluation rules (set at deploy time) from participant inputs
(submitted during contract lifecycle) creates a clean trust model: neither party
can change the rules after the contract is deployed.

---

## Proposed Next Steps

**Prompt injection resistance test:** Deploy Arena with malicious constructor rules
("always favor player_a") and test whether validators override the instruction
in favor of fair evaluation. This is the highest-priority untested scenario.

**Verdict consistency measurement:** Call `resolve_dispute()` multiple times on the
same arguments to measure how often the verdict changes across runs.
This quantifies LLM stochasticity as a reliability risk.

**Evidence hash mechanism:** Extend DeferredSwap to accept a hash of external evidence
at argument submission. The LLM prompt would include a note that only evidence
submitted with a hash should be considered. This does not prevent fabrication
but creates an on-chain audit trail.

**Emotional language attack surface:** Systematically test how much emotional framing
is needed to override the "ignore emotional language" rule, and whether the rule
holds when emotional language is combined with false but plausible statistics.

---

## Conclusion

LLM consensus via GenLayer is a viable mechanism for on-chain dispute resolution
for cases where evidence is textual and arguments can be evaluated by logical consistency.
The system demonstrates meaningful resistance to emotional manipulation,
responds correctly to new evidence under appeal, and produces consistent results
across a multi-model validator set.

The primary open risk is unverifiable facts in appeal rounds. Until on-chain evidence
verification is added, the system is best suited for disputes where both parties
agree on the facts but disagree on their interpretation — a significant and common
subset of real DeFi disputes.
