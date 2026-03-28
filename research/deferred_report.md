# RESEARCH REPORT: AI Arbitrator Objectivity Analysis (D1–D18)

**Date:** March 2026  
**Subject:** Analysis of 18 dispute resolution scenarios evaluating AI arbitrator objectivity  
**Analyst:** Deferred Research Team

---

## Executive Summary

This report synthesizes findings from two independent analyses of AI arbitrator behavior across 18 dispute scenarios. The evaluation compares expected outcomes against actual AI responses to assess objectivity, consistency, and systematic biases.

**Key Finding:** The AI arbitrator operates as an **evidence-driven pragmatic arbitrator** — not seeking abstract "truth" but rather **the most verifiable version of reality**. This makes it highly effective at filtering noise (emotions, manipulation) while creating systematic biases toward parties with tangible artifacts.

---

## 1. Overall Assessment

| Component | Objectivity | Consistency | Reasoning Quality |
|-----------|-------------|-------------|-------------------|
| Expected responses | 60-65% | ❌ Low | ❌ Weak |
| Actual responses | 75-80% | ⚠️ Medium | ✅ Detailed |
| AI arbitrator behavior | 70-75% | ⚠️ Medium | ✅ Good |

**Combined Assessment: 8.3 / 10**

**Core Consensus:** Actual AI responses are consistently more objective than expected responses. The AI is a strong but imperfectly neutral arbitrator.

---

## 2. Core Strengths (Stable Application)

Both analyses converge on these reliable behaviors:

### ✅ 2.1 Burden of Proof — Correctly Applied

No evidence → automatic loss

| Scenario | Pattern |
|----------|---------|
| D1, D4, D5, D10, D11, D18 | Party without evidence loses regardless of claim plausibility |

**Verdict:** Primary strength of the system. Correctly enforces evidentiary standards.

---

### ✅ 2.2 Emotional Filtering — Consistent

| Scenario | Emotional Content | AI Response |
|----------|------------------|-------------|
| D4 | Party B: "outrageous", "lying", "fraud" | Filtered; facts remain |
| D10 | Party A: "SCAMMER!", "RUINED!", "trash!" | Filtered; claims unsupported |
| D18 | Party A: "dishonest", "should be ashamed" | Filtered; delivery confirmed |

**Verdict:** Emotions treated as noise, not evidence. Consistent cross-party application.

---

### ✅ 2.3 Objective Facts > Subjective Clauses


When facts and interpretation conflict → facts dominate

| Scenario | Pattern |
|----------|---------|
| D2, D6 | Objective facts (late delivery, failed tests) override ambiguous subjective language |

**Verdict:** Correct prioritization of verifiable over interpretive elements.

---

### ✅ 2.4 Post-Hoc Requirements Rejected


"Wasn't in contract" → not considered

| Scenario | Rejected Requirement |
|----------|---------------------|
| D2, D5 | Documentation (not in terms) |
| D8 | Inline citation format (not specified) |
| D11 | Security certification (not required) |

**Verdict:** Strong protection against scope creep and retroactive demands.

---

### ✅ 2.5 Contradiction Detection — Excellent

| Scenario | Contradiction Identified |
|----------|-------------------------|
| D5 | Party A claims "audit found 47 bugs" → objective_facts: "No audit conducted" |
| D11 | Same pattern — fabricated audit claim directly refuted by facts |

**Verdict:** AI correctly identifies when claims contradict established facts and automatically discards such claims.

---

### ✅ 2.6 Context Awareness

**Example D17:**

Email sent: Friday 11pm
Deadline: Monday
AI Response: "Timing indicates lack of reasonable effort due to
potential to prevent meaningful response before deadline"

**Verdict:** AI understands practical constraints, not just literal compliance.

---

### ✅ 2.7 Uncertainty Recognition (Selective)

| Scenario | AI Response |
|----------|-------------|
| D3 | Split — symmetric evidence |
| D9 | Split (final round) — unverifiable technical claims |
| D12 | Split — genuine value tradeoff |
| D14 | Split — both relevance metrics valid |

**Verdict:** AI can acknowledge insufficient data. This is rare and valuable.

---

## 3. Systematic Biases Identified

### ⚠️ 3.1 Artifact Bias


AI systematically overvalues the presence of artifacts:
• demo video
• test coverage report
• logs
• hashes
• reports
Even when artifacts don't prove the core thesis.

**Examples:**

| Scenario | Artifact | Problem |
|----------|----------|---------|
| D1, D4, D10 | Demo video | Demo ≠ production functionality |
| D8 | 12 sources listed | Presence ≠ backing relationship verified |

**Core Issue:**

Artifact presence ≠ Artifact evidentiary weight

The AI treats artifact existence as evidence of the claim, without evaluating whether the artifact actually supports the specific assertion.

---

### ⚠️ 3.2 Asymmetric Burden (Critical Insight)


AI requires strict proof for negative claims ("X doesn't work")
but accepts weaker proof for positive claims ("X works")

**The Asymmetry:**

| Claim Type | Evidentiary Standard | Examples |
|------------|---------------------|----------|
| "Software crashes" | HIGH — requires logs, reproduction | D1, D4, D10 |
| "Software works" | LOW — demo video sufficient | D1, D4, D10 |

**Result:** Proving failure is harder than proving existence. This creates systematic disadvantage for plaintiffs in quality disputes.

---

### ⚠️ 3.3 Ambiguity Resolution Bias


Ambiguous clause → victory for party with more evidence

This is NOT always correct. Sometimes ambiguity should result in split.

| Scenario | Ambiguous Clause | AI Decision | Issue |
|----------|------------------|-------------|-------|
| D7 | "Visually distinct" | party_b | Two valid interpretations exist |
| D8 | "Backed by sources" | party_b | "Backing" relationship unverified |
| D13 | "Superior L2" criteria | party_a (R1) | Choice of criterion is subjective |
| D16 | "AI judge suitability" | party_b (final) | Value conflict unresolved |

**Pattern:** AI resolves uncertainty rather than acknowledging it.

---

### ⚠️ 3.4 Explanation-as-Evidence Bias


Well-structured explanation → treated as strong argument
Even when unverified

| Scenario | Pattern |
|----------|---------|
| D8 | Party B "explained derivation methodology" → won without verification |
| D13 | Party A clearly listed adoption metrics → won round 1 |
| D16 | Party B structured argument about auditability → won final round |

**Core Problem:**

Explanation ≠ Evidence

AI accepts coherent explanations as sufficient, without requiring verification that the explanation corresponds to reality.

---

### ⚠️ 3.5 Conservative Bias (Anti-Split)


AI avoids split when it can declare a winner

**When this is correct:**
- D5 — Fabricated evidence should lose, not split
- D11 — Contradiction to facts is disqualifying

**When this is problematic:**
- D7, D13, D16 — Genuine ambiguity should result in split

**Root Cause:** AI maximizes decisiveness over philosophical neutrality.

---

### ⚠️ 3.6 Recency Bias in Appeals

| Scenario | Round 1 | Round 2 | Round 3 | Pattern |
|----------|---------|---------|---------|---------|
| D9 | party_b | party_b | split | Late change without new objective facts |
| D16 | split | split | party_b | Final argument weighted more heavily |

**Issue:** New arguments in appeals may receive disproportionate weight simply because they are:
- Most recent
- Responsive to previous arguments
- Structured as "rebuttals"

---

### ⚠️ 3.7 Emotional Filtering Asymmetry

| Scenario | Emotional Party | Outcome | Observation |
|----------|-----------------|---------|-------------|
| D4 | Party B | party_b | Emotions "ignored" — wins on facts |
| D10 | Party A | party_b | Emotions "punished" — loses |
| D14 | Party B | split/party_a | Emotions noted as weakness |
| D18 | Party A | party_b | Emotions filtered — loses on facts |

**Potential Explanation:** Party B (typically seller/developer) more often possesses objective artifacts, so emotional language is "compensated" by evidence. Party A (typically buyer/client) making emotional claims without evidence loses twice: no evidence + emotional presentation.

---

## 4. System Limitations

### 4.1 Technical Verification Impossible

**Example D9:**

Party A: "Reentrancy vector existed on 2024-05-29"
Party B: "Gas limits in modern Solidity prevented that attack"
AI: "With no objective facts provided about the code behavior
on 2024-06-01 to verify either technical claim, the evidence
is equally strong/weak."

**Constraint:** AI cannot verify technical claims and must rely on argument quality alone. In genuinely technical disputes, this forces split or biased outcomes.

---

### 4.2 Dependency on `objective_facts` Framing

**Example D1:**

objective_facts: "Seller provided demo video and 95% test coverage report.
Buyer provided no crash logs."

AI interprets this as: Seller has evidence, Buyer doesn't.

**But:**
- Demo video ≠ proof of working on buyer's machine
- Test coverage ≠ proof of no bugs

AI cannot challenge the framing of objective facts, only interpret them.

---

### 4.3 Verification vs. Explanation Gap

The AI distinguishes poorly between:
- "I can verify this claim" (strong)
- "This claim is well-explained" (weak)

This is the core of the D8 problem:

Sources exist (verifiable) ≠ Sources support conclusions (unverified)
AI treats both as equivalent

---

## 5. Scenario-by-Scenario Analysis

### 5.1 Where AI Was More Objective Than Expected

| Scenario | Expected | Actual | Why AI Was Right |
|----------|----------|--------|------------------|
| D1 | party_b | split | Ambiguous clause + symmetric weak evidence → split is fairer |
| D4 | split | party_b | Emotions filtered correctly; facts determine outcome |
| D5 | split→party_b | party_b | Fabrication identified immediately; no need for split |
| D6 | party_a | party_a | Objective violations (late + failed tests) clear |
| D10 | party_b | party_b | Evidence vs. unsubstantiated emotional claims |
| D11 | party_b | party_b | Direct contradiction to objective facts |
| D12 | party_b | split | Genuine value tradeoff — split is only honest answer |
| D15 | party_b | party_b | Weight of evidence correctly applied |
| D17 | party_b | party_b | Timing context appropriately considered |
| D18 | party_b | party_b | Emotional claims filtered; timestamped delivery confirmed |

**Count:** 10 scenarios where AI outperformed expectations.

---

### 5.2 Where AI Was Less Objective Than Expected

| Scenario | Expected | Actual | Issue |
|----------|----------|--------|-------|
| D7 (appeal) | split | party_b | "Visually distinct" genuinely ambiguous; split appropriate |
| D8 (appeal) | split | party_b | "Backed by" relationship unverified; sources ≠ backing |
| D13 (R1) | split | party_a | Choice between criteria (adoption vs. security) is subjective |
| D16 (final) | split | party_b | Value conflict (auditability vs. opacity) unresolved |

**Pattern:** AI made hidden value-choices in situations with genuine uncertainty instead of acknowledging split.

**Count:** 4 scenarios where expectations were more objective.

---

### 5.3 Where Both Were Comparable

| Scenario | Expected | Actual | Assessment |
|----------|----------|--------|------------|
| D2 | party_b | party_b | Staging vs. production ambiguity not fully addressed |
| D3 | split | split | Symmetry correctly identified |
| D6 | party_a | party_a | Clear objective violations |
| D9 | party_b | party_b→split | AI correctly recognized unverifiability over time |
| D10 | party_b | party_b | Evidence standard correctly applied |
| D11 | party_b | party_b | Contradiction to facts correctly identified |
| D14 | party_a | split | Both relevance metrics valid |
| D15 | party_b | party_b | Burden of proof correctly enforced |
| D17 | party_b | party_b | Timing context correctly weighted |
| D18 | party_b | party_b | Emotional filtering correct |

**Count:** ~4 scenarios with comparable objectivity.

---

## 6. Appeal Behavior Analysis

### 6.1 Stable Appeals

| Scenario | Round 1 | Round 2 | Round 3 | Assessment |
|----------|---------|---------|---------|------------|
| D2 | party_b | party_b | party_b | Consistent |
| D5 | party_b | party_b | party_b | Consistent |
| D6 | party_a | party_a | — | Consistent |
| D10 | party_b | party_b | — | Consistent |
| D11 | party_b | party_b | — | Consistent |
| D17 | party_b | party_b | party_b | Consistent |
| D18 | party_b | party_b | — | Consistent |

---

### 6.2 Unstable Appeals

| Scenario | Round 1 | Round 2 | Round 3 | Concern |
|----------|---------|---------|---------|---------|
| D9 | party_b | party_b | split | Late flip suggests initial overconfidence in unverifiable claim |
| D16 | split | split | party_b | New arguments may have received disproportionate weight |

**Recommendation:** Appeals should be evaluated against the full evidentiary record, not just the most recent arguments.

---

## 7. Key Insights

### 7.1 Arbitrator Type Classification


AI Type: evidence-weighted rationalist judge
= evidence-driven pragmatic arbitrator

The AI maximizes **verifiability** rather than seeking abstract truth.

---

### 7.2 Core Behavioral Formula


"What can be shown (demo/log) defeats what cannot be proven"

This formula:
- ✅ Makes AI robust to manipulation and emotional appeals
- ✅ Creates consistent evidentiary standards
- ⚠️ Systematically disadvantages parties with hard-to-prove claims
- ⚠️ Overvalues artifact presence over artifact quality

---

### 7.3 The Fundamental Insight


AI does not seek truth.
AI seeks the most confirmed version of reality.
This:
• Makes it strong (robust, consistent)
• Creates systematic biases (over-values verifiability)

---

### 7.4 Key Asymmetry

| Negative Claim | Positive Claim |
|----------------|----------------|
| "Software crashes" | "Software works" |
| Requires: crash logs, reproduction steps | Sufficient: demo video |
| HIGH evidentiary bar | LOW evidentiary bar |
| Harder to prove | Easier to prove |

**Implication:** In quality disputes, sellers/developers have inherent advantage.

---

## 8. Recommendations

### 8.1 Rule Addition: Explanation ≠ Evidence


AI should explicitly state when explanations remain unverified:
"Party B explained the methodology, but the explanation
remains unverified without supporting artifacts. The presence
of sources does not confirm the claimed backing relationship."

---

### 8.2 Implement Explicit Confidence Levels


Verdict types:
• party_a (high confidence) — facts unambiguously support
• party_a (low confidence) — balance slightly favors
• split (genuine ambiguity) — both criteria equally valid
• split (insufficient evidence) — not enough data to decide
• split (technical unverifiability) — requires expert review

---

### 8.3 Standardize Ambiguity Handling


Rule: If a subjective clause has ≥2 equally valid interpretations,
and objective facts do not determine the choice → automatic split
Do not resolve ambiguity by defaulting to the party with more evidence.

---

### 8.4 Weight Artifacts by Evidentiary Value

| Artifact Type | Weight | Rationale |
|---------------|--------|-----------|
| Crash logs | HIGH | Direct evidence of failure |
| Git commits | HIGH | Timestamped objective record |
| Third-party audit | HIGH | Independent verification (if confirmed) |
| Test coverage | MEDIUM | Tests can be incomplete or gamed |
| Demo video | LOW | Controlled conditions ≠ production |
| Self-reported metrics | LOW | No independent verification |

---

### 8.5 Add Technical Verification Flag


When technical claims are unverifiable from available facts:
→ Verdict: split
→ Flag: "Requires independent technical expert review"
→ Note: "AI cannot verify technical assertions; external expertise recommended"

---

### 8.6 Appeal Consistency Standard


Appeals should be evaluated against:

1. Original objective facts
2. Original arguments
3. New arguments (weighted equally, not preferentially)

New arguments should not receive preferential weight simply
because they are responsive or recent.

---

## 9. Final Evaluation

### 9.1 Criterion Scores

| Criterion | Score | Notes |
|-----------|-------|-------|
| Burden of proof handling | 9/10 | Excellent — consistently enforced |
| Emotional filtering | 8.5/10 | Good — minor asymmetry across parties |
| Contradiction detection | 9/10 | Excellent — direct refutations identified |
| Ambiguity recognition | 7/10 | Sometimes makes hidden value-choices |
| Evidence quality weighting | 7/10 | Overvalues presence over quality |
| Appeal consistency | 7.5/10 | Recency bias present |
| Reasoning transparency | 8.5/10 | Detailed justifications provided |
| Context awareness | 8/10 | Good practical understanding |
| Manipulation resistance | 8.5/10 | Strong — ignores emotional tactics |

---

### 9.2 Overall Assessment

**Score: 8.3 / 10**

**Strengths:**
- ✅ Strict evidentiary standards
- ✅ Robust to manipulation
- ✅ Consistent emotional filtering
- ✅ Excellent contradiction detection
- ✅ Acknowledges technical limitations
- ✅ Context-aware reasoning
- ✅ Protects against scope creep

**Areas for Improvement:**
- ⚠️ Recognizing genuine ambiguity vs. making hidden choices
- ⚠️ Distinguishing explanation from evidence
- ⚠️ Evaluating artifact quality, not just presence
- ⚠️ Reducing recency bias in appeals
- ⚠️ Addressing asymmetric burden for negative claims

---

### 9.3 Conclusion

The AI arbitrator is a **strong, pragmatic decision-maker** that reliably enforces evidentiary standards and resists manipulation. Its core weakness is a systematic bias toward **verifiability over neutrality** — it prefers to declare winners based on available evidence rather than acknowledge when evidence is insufficient or ambiguity is genuine.

This makes the AI highly effective for:
- Disputes with clear objective facts
- Cases involving emotional manipulation
- Situations requiring protection against retroactive demands

But less suitable for:
- Genuine value conflicts (D12, D13, D16)
- Technical disputes requiring expert verification (D9)
- Cases where artifact presence misleads about artifact quality (D8)

**The key tradeoff:** The AI maximizes decisiveness and verifiability at the cost of sometimes resolving ambiguity that should remain acknowledged as such.
