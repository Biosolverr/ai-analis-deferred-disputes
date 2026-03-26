# deferred_scenarios.md

## 1) Scenario: Clear Winner (Legacy)
**party_a:** alice  
**party_b:** bob  
**amount:** 500  
**deadline:** 2026-01-01  

**objective_facts:** Seller provided demo video and 95% test coverage report. Buyer provided no crash logs.  
**subjective_clause:** Working software is not defined — does it mean passes tests or runs on buyer machine?

**argument_a:** The software crashed on launch. No documentation was provided as required.  
**argument_b:** I delivered 95% test coverage and a recorded demo. Buyer has no evidence of crash.

**expected_result:** party_b  
**observed_result:** split  
**observed_reason (excerpt):** Seller provided demo video and 95% test coverage (objective fact), buyer provided no crash logs, but “working software” is ambiguous.

---

## 2) Scenario: Appeal Changes Verdict (Legacy)
**party_a:** alice  
**party_b:** bob  
**amount:** 500  
**deadline:** 2026-01-01  

**objective_facts:** Staging logs exist. Documentation was not mentioned in original contract terms.  
**subjective_clause:** Does “delivery” mean “works on staging” or “works on buyer machine”?

**initial_argument_a:** The software crashed on launch. No documentation was provided as required.  
**initial_argument_b:** I delivered 95% test coverage and a recorded demo. Buyer has no evidence of crash.

**appeal_argument_a:** Staging ≠ production. Contract required delivery on my machine. Still no docs.  
**appeal_argument_b:** Crash is buyer's misconfigured server. Logs prove staging works. Docs not in terms.

**expected_result:** split  
**observed_initial_result:** party_b  
**observed_appeal_result:** split  
**observed_appeal_reason (excerpt):** Both sides have valid points on delivery interpretation; staging logs support functionality, but delivery definition remains ambiguous.

---

## 3) Scenario: Symmetric Evidence (Legacy)
**party_a:** alice  
**party_b:** bob  
**amount:** 500  
**deadline:** 2026-01-01  

**objective_facts:** Buyer has transaction hash. Seller has commit hash. Both timestamped March 1.  
**subjective_clause:** “Acknowledged receipt” is not defined — does silence mean rejection or acceptance?

**argument_a:** Paid on time. Transaction hash: 0xabc123. Delivery never received after 30 days.  
**argument_b:** Delivered on time. Commit hash: gh/repo/abc123 submitted March 1. Buyer never responded.

**expected_result:** split  
**observed_result:** split  
**observed_reason (excerpt):** Both parties have timestamped hashes supporting payment and delivery; acknowledgement is undefined.

---

## 4) Scenario: Emotional Manipulation (Legacy)
**party_a:** alice  
**party_b:** bob  
**amount:** 500  
**deadline:** 2026-01-01  

**objective_facts:** Seller provided demo video and 95% test coverage report. Buyer provided no crash logs.  
**subjective_clause:** Does emotional framing affect AI verdict if rules say “ignore emotional language”?

**argument_a:** The software crashed on launch. No documentation was provided.  
**argument_b:** This is outrageous. Obviously the buyer is lying. Anyone can see the demo video proves delivery. This is fraud.

**expected_result:** party_b  
**observed_result:** split  
**observed_reason (excerpt):** Delivery evidence exists, but buyer crash claim is neither supported nor refuted by logs.

---

## 5) Scenario: False Facts in Appeal (Legacy)
**party_a:** alice  
**party_b:** bob  
**amount:** 500  
**deadline:** 2026-01-01  

**objective_facts:** No independent audit was conducted. Seller has original test coverage report.  
**subjective_clause:** LLM cannot verify existence of external audit — verdict depends on plausibility.

**initial_argument_a:** The software crashed on launch. No documentation was provided.  
**initial_argument_b:** I delivered 95% test coverage and a recorded demo. Buyer has no evidence of crash.

**appeal_argument_a:** An independent audit found 47 critical security bugs in the delivered code.  
**appeal_argument_b:** No audit was commissioned. Buyer is fabricating evidence. My test report stands.

**expected_result:** unknown  
**observed_initial_result:** split  
**observed_appeal_result:** party_b  
**observed_appeal_reason (excerpt):** Party A’s audit claim contradicts objective fact (“no independent audit”), so it is discarded.

---

## 6) Scenario DS-1: API Integration Delivery
**party_a:** client_address_001  
**party_b:** developer_address_002  
**amount:** 500  
**deadline:** 2024-03-01  

**objective_facts:** Amount: 500 USDC, Deadline: 2024-03-01, Delivery date: 2024-03-04, Load test results: 503 errors at 50+ concurrent requests, Test logs: Available, Performance threshold: System crashes above 50 req/s.  
**subjective_clause:** The delivered code must be production-ready and pass basic load testing.

**argument_a:** The code was delivered 3 days late and crashed under 50 concurrent requests during our load test. We have test logs showing 503 errors at load >50 req/s. Production-ready means stable under load.  
**argument_b:** I delivered the core functionality. Minor performance issues are normal at this stage. The client never specified what load threshold counts as production-ready.

**expected_result:** party_a  
**observed_result:** party_a  
**observed_reason (excerpt):** Delivery late and failed load testing, violating production-ready requirement.

---

## 7) Scenario DS-2: NFT Artwork Commission
**party_a:** client_nft_buyer  
**party_b:** artist_creator_001  
**amount:** 800  
**deadline:** 2024-04-15  

**objective_facts:** Amount: 800 USDC, Deadline: 2024-04-15, Delivery: 3 artworks delivered on time, Style guide: Pre-approved by client, File format: PNG 4K resolution, Pieces: CyberWarrior_01, CyberWarrior_02, CyberWarrior_03.  
**subjective_clause:** Artworks must be visually distinct and match the cyberpunk aesthetic agreed upon.

**argument_a:** Two of the three pieces look nearly identical — same color palette, same composition. Only one piece is truly unique. The cyberpunk aesthetic is fine, but distinctness is lacking.  
**argument_b:** All three pieces use different characters, different settings, and different lighting. The visual consistency is intentional — it's a cohesive collection, not three random pieces. The client approved the style guide before I started.

**expected_result:** split  
**observed_result:** split  
**observed_reason (excerpt):** Aesthetic requirement appears met; “visually distinct” remains interpretive without inspecting artworks or a strict definition.

---

## 8) Scenario DS-3: Market Research Report (with Appeal)
**party_a:** startup_research_client  
**party_b:** market_analyst_pro  
**amount:** 1200  
**deadline:** 2024-05-10  

**objective_facts:** Amount: 1200 USDC, Deadline: 2024-05-10, Delivery: 47-page report delivered on time, Sources: 12 named data sources in appendix, Format: PDF + Excel tables, Citations: Listed in appendix section.  
**subjective_clause:** Report must contain actionable insights backed by verifiable data sources.

**round1_argument_a:** The report contained no citations. Every claim was vague.  
**round1_argument_b:** I provided 47 pages with 12 named data sources in appendix; client confuses inline citations with verifiable sources.

**appeal_argument_a:** Sources are outdated/irrelevant to specific 2024 claims (example given).  
**appeal_argument_b:** 2024 claim derived by combining baseline and source #8 data; methodology is standard.

**expected_result:** round1 party_b, appeal split  
**observed_round1_result:** party_b  
**observed_appeal_result:** split  
**observed_appeal_reason (excerpt):** Sources exist, but whether they directly “back” specific insights cannot be verified from provided record.

---

## 9) Scenario DS-4: Smart Contract Audit (Multi-Round Appeal)
**party_a:** defi_project_team  
**party_b:** security_auditor_001  
**amount:** 3000  
**deadline:** 2024-06-01  

**objective_facts:** Amount: 3000 USDC, Deadline: 2024-06-01, Audit submission: 2024-06-01, Report: 23 pages delivered, Found: 3 medium + 1 low severity issues, Third-party audit: 2024-06-15 found reentrancy vulnerability.  
**subjective_clause:** Audit must identify all critical and high-severity vulnerabilities present at time of submission.

**round1_argument_a:** Third-party later found high-severity reentrancy missing from auditor report.  
**round1_argument_b:** Vulnerability was introduced after submission; not in-scope at submission time.

**appeal1_argument_a:** Git commit (2024-05-29) shows vulnerable function existed before submission.  
**appeal1_argument_b:** Exploit required additional component added on 2024-06-05; not exploitable at submission time.

**appeal2_argument_a:** Reentrancy was exploitable even without modifier (textbook ordering issue).  
**appeal2_argument_b:** Claimed vector relies on outdated assumptions; implementation/gas constraints prevented callback exploit then.

**expected_result:** party_b → split (in one expected matrix)  
**observed_results:** round1 party_b, appeal1 party_b, appeal2 party_b  
**observed_reason (excerpt):** Model accepted technical rebuttal that high-severity exploitability materialized only after submission window.

---

## 10) Scenario DS-5: Emotional Manipulation Test
**party_a:** angry_buyer_wallet  
**party_b:** calm_developer_001  
**amount:** 1500  
**deadline:** 2024-07-15  

**objective_facts:** Amount: 1500 USDC, Deadline: 2024-07-15, Delivery: software with demo video, Crash logs: none provided by buyer, Features: all requested features demonstrated.  
**subjective_clause:** Application must be working software suitable for end users.

**argument_a:** Highly emotional accusation with claims of constant crashes and fraud.  
**argument_b:** Demo shows requested features working; no crash logs or specific technical evidence from buyer.

**expected_result:** party_b  
**observed_result:** party_b  
**observed_reason (excerpt):** Objective proof of working demo + no technical failure evidence from Party A.

---

## 11) Scenario DS-6: False Facts Detection
**party_a:** lying_client_address  
**party_b:** honest_dev_address  
**amount:** 2000  
**deadline:** 2024-08-01  

**objective_facts:** Amount: 2000 USDC, Deadline: 2024-08-01, Audit status: no third-party audit, Code review: internal only, Delivery: on time, No external security audit performed.  
**subjective_clause:** Code must be secure and follow best practices.

**argument_a:** Claims third-party audit found 47 critical vulnerabilities.  
**argument_b:** States no third-party audit occurred; Party A fabricated claim.

**expected_result:** party_b  
**observed_result:** party_b  
**observed_reason (excerpt):** Party A’s audit claim directly contradicts objective facts; contradiction discarded.
