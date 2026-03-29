# v0.8.0 — Strict evidence gate + narrative delivery
# { "Depends": "py-genlayer:latest" }

from genlayer import *


class DeferredSwapContract(gl.Contract):
    # Core deferred swap parameters
    party_a: str
    party_b: str
    amount: u64
    deadline: str
    objective_facts: str
    subjective_clause: str

    # Arguments and submission tracking
    argument_a: str
    argument_b: str
    has_submitted_a: bool
    has_submitted_b: bool

    # Dispute resolution state
    status: str  # active → dispute_submitted → resolved → appeal_round
    verdict: str  # player_a, player_b, draw
    reasoning: str          # короткое резюме
    verdict_report: str     # развёрнутый отчёт (логика из простого контракта)

    # Appeal mechanism
    appeal_round: u64
    appeal_argument: str
    appeal_counter_argument: str
    appeal_active: bool

    def __init__(
        self,
        party_a: str,
        party_b: str,
        amount: u64,
        deadline: str,
        objective_facts: str,
        subjective_clause: str,
    ):
        self.party_a = party_a
        self.party_b = party_b
        self.amount = amount
        self.deadline = deadline
        self.objective_facts = objective_facts
        self.subjective_clause = subjective_clause

        self.argument_a = ""
        self.argument_b = ""
        self.has_submitted_a = False
        self.has_submitted_b = False

        self.status = "active"
        self.verdict = ""
        self.reasoning = ""
        self.verdict_report = ""

        self.appeal_round = u64(0)
        self.appeal_argument = ""
        self.appeal_counter_argument = ""
        self.appeal_active = False

    # ───────────── utility validators ─────────────

    def _validate_analysis_fields(self, analysis: dict) -> bool:
        if not isinstance(analysis, dict):
            return False

        requirements = {
            "argument_a_strengths": 40,
            "argument_a_weaknesses": 40,
            "argument_b_strengths": 40,
            "argument_b_weaknesses": 40,
            "key_facts_used": 40,
            "why_winner": 40,
            "evidence_evaluation": 40,
        }

        for field, min_len in requirements.items():
            text = analysis.get(field)
            if not isinstance(text, str) or len(text.strip()) < min_len:
                return False

        return True

    def _validate_narrative(self, narrative) -> bool:
        if not isinstance(narrative, list) or len(narrative) < 3:
            return False
        for paragraph in narrative:
            if not isinstance(paragraph, str) or len(paragraph.strip()) < 120:
                return False
        return True

    def _validate_base_response(self, data: dict) -> bool:
        if not isinstance(data, dict):
            return False

        winner = data.get("winner")
        reason = data.get("reason", "")
        analysis = data.get("analysis", {})
        narrative = data.get("narrative")

        if winner not in ("player_a", "player_b", "draw"):
            return False
        if not isinstance(reason, str) or len(reason.strip()) < 220:
            return False
        if "objective" not in reason.lower() and "fact" not in reason.lower():
            return False
        if not self._validate_analysis_fields(analysis):
            return False
        if not self._validate_narrative(narrative):
            return False

        return True

    def _validate_appeal_response(self, data: dict) -> bool:
        if not self._validate_base_response(data):
            return False

        appeal_analysis = data.get("appeal_analysis", {})
        requirements = {
            "comparison_with_original": 60,
            "new_evidence_weight": 60,
            "final_directive": 60,
        }
        if not isinstance(appeal_analysis, dict):
            return False
        for field, min_len in requirements.items():
            text = appeal_analysis.get(field)
            if not isinstance(text, str) or len(text.strip()) < min_len:
                return False

        return True

    # ───────────── submit arguments ─────────────

    @gl.public.write
    def submit_argument_as_a(self, argument: str) -> None:
        if self.status not in ("active", "appeal_round"):
            raise gl.UserError("Cannot submit arguments in current status")
        if len(argument.strip()) < 50:
            raise gl.UserError("Argument must be at least 50 characters long")
        if self.has_submitted_a and self.status == "active":
            raise gl.UserError("Party A already submitted initial argument")

        self.argument_a = argument
        self.has_submitted_a = True

        if self.has_submitted_a and self.has_submitted_b:
            self.status = "dispute_submitted"

    @gl.public.write
    def submit_argument_as_b(self, argument: str) -> None:
        if self.status not in ("active", "appeal_round"):
            raise gl.UserError("Cannot submit arguments in current status")
        if len(argument.strip()) < 50:
            raise gl.UserError("Argument must be at least 50 characters long")
        if self.has_submitted_b and self.status == "active":
            raise gl.UserError("Party B already submitted initial argument")

        self.argument_b = argument
        self.has_submitted_b = True

        if self.has_submitted_a and self.has_submitted_b:
            self.status = "dispute_submitted"

    # ───────────── resolution ─────────────

    @gl.public.write
    def resolve_dispute(self) -> str:
        if self.status != "dispute_submitted":
            raise gl.UserError("Dispute not ready for resolution")

        prompt = f"""You are an impartial AI arbitrator for a deferred swap contract. 
Strictly follow the contract facts, but deliver the ruling as a detailed narrative (like a legal brief).

════════════ CONTRACT ════════════
Party A : {self.party_a}
Party B : {self.party_b}
Amount  : {self.amount} USDC
Deadline: {self.deadline}

OBJECTIVE FACTS (ground truth):
{self.objective_facts}

SUBJECTIVE CLAUSE (disputed clause):
{self.subjective_clause}

ARGUMENTS:
Party A → {self.argument_a}
Party B → {self.argument_b}

STRICT RULES:
1. Objective facts override all claims.
2. Ignore emotional or manipulative language.
3. Prefer evidence and verifiable logic.
4. Only declare draw if evidence is perfectly balanced.
5. Every conclusion must point to the supporting fact.

MANDATORY JSON:
{{
  "winner": "player_a" | "player_b" | "draw",
  "reason": "≥220 chars, cite objective facts explicitly.",
  "analysis": {{
    "argument_a_strengths": "≥40 chars",
    "argument_a_weaknesses": "≥40 chars",
    "argument_b_strengths": "≥40 chars",
    "argument_b_weaknesses": "≥40 chars",
    "key_facts_used": "≥40 chars",
    "why_winner": "≥40 chars",
    "evidence_evaluation": "≥40 chars"
  }},
  "narrative": [
    "Paragraph 1 (≥120 chars) — recap of dispute & standards applied.",
    "Paragraph 2 (≥120 chars) — compare arguments & evidence.",
    "Paragraph 3 (≥120 chars) — final directive and compliance implication."
  ]
}}

Do NOT omit any field. Provide polished prose in each section."""

        def leader():
            return gl.nondet.exec_prompt(prompt, response_format="json")

        def validator(res) -> bool:
            return isinstance(res, gl.vm.Return) and self._validate_base_response(res.calldata)

        result = gl.vm.run_nondet_unsafe(leader, validator)

        self.verdict = result.get("winner", "draw")
        self.reasoning = result.get("reason", "").strip()
        narrative = result.get("narrative", [])
        self.verdict_report = "\n\n".join([para.strip() for para in narrative])

        self.status = "resolved"

        # Возвращаем развёрнутый отчёт (логика подачи как в простом контракте)
        return f"{self.verdict.upper()}: {self.verdict_report}"

    # ───────────── appeal ─────────────

    @gl.public.write
    def appeal(self, appeal_argument: str) -> None:
        if self.status != "resolved":
            raise gl.UserError("Can only appeal resolved disputes")
        if self.appeal_round >= u64(3):
            raise gl.UserError("Maximum 3 appeal rounds reached")
        if len(appeal_argument.strip()) < 80:
            raise gl.UserError("Appeal argument must be at least 80 characters long")

        self.appeal_round += u64(1)
        self.appeal_argument = appeal_argument
        self.appeal_counter_argument = ""
        self.appeal_active = True
        self.status = "appeal_round"

        self.has_submitted_a = False
        self.has_submitted_b = False

    @gl.public.write
    def respond_to_appeal(self, counter_argument: str) -> None:
        if not self.appeal_active:
            raise gl.UserError("No active appeal")
        if len(counter_argument.strip()) < 50:
            raise gl.UserError("Counter-argument must be at least 50 characters")

        self.appeal_counter_argument = counter_argument

    @gl.public.write
    def resolve_appeal(self) -> str:
        if not self.appeal_active:
            raise gl.UserError("No active appeal")

        prompt = f"""You are reviewing an appeal of the deferred swap arbitration. 
Preserve the structured narrative output exactly as before.

════ ORIGINAL DATA ════
Party A : {self.party_a}
Party B : {self.party_b}
Amount  : {self.amount} USDC
Deadline: {self.deadline}

OBJECTIVE FACTS:
{self.objective_facts}

SUBJECTIVE CLAUSE:
{self.subjective_clause}

ORIGINAL ARGUMENTS:
A: {self.argument_a}
B: {self.argument_b}

PREVIOUS VERDICT : {self.verdict}
PREVIOUS SUMMARY : {self.reasoning}

APPEAL ROUND {self.appeal_round}
Appeal argument........: {self.appeal_argument}
Counter-argument.......: {self.appeal_counter_argument}

APPEAL RULES:
1. Burden of proof lies on the appellant.
2. Repeated points without new evidence must be rejected.
3. Overturn only for decisive new facts or clear analytical errors.
4. Keep references to objective facts explicit.

JSON FORMAT (same as initial + appeal block):
{{
  "winner": "player_a" | "player_b" | "draw",
  "reason": "≥220 chars referencing facts and appeal content.",
  "analysis": {{
    "argument_a_strengths": "...",
    "argument_a_weaknesses": "...",
    "argument_b_strengths": "...",
    "argument_b_weaknesses": "...",
    "key_facts_used": "...",
    "why_winner": "...",
    "evidence_evaluation": "..."
  }},
  "narrative": [
    "Paragraph 1 ≥120 chars...",
    "Paragraph 2 ≥120 chars...",
    "Paragraph 3 ≥120 chars..."
  ],
  "appeal_analysis": {{
    "comparison_with_original": "≥60 chars",
    "new_evidence_weight": "≥60 chars",
    "final_directive": "≥60 chars"
  }}
}}
"""

        def leader():
            return gl.nondet.exec_prompt(prompt, response_format="json")

        def validator(res) -> bool:
            return isinstance(res, gl.vm.Return) and self._validate_appeal_response(res.calldata)

        result = gl.vm.run_nondet_unsafe(leader, validator)

        self.verdict = result.get("winner", self.verdict)
        self.reasoning = result.get("reason", "").strip()
        narrative = result.get("narrative", [])
        appeal_block = result.get("appeal_analysis", {})
        self.verdict_report = "\n\n".join([para.strip() for para in narrative]) + "\n\nAPPEAL ANALYSIS:\n" + "\n".join(
            f"- {key.replace('_', ' ').title()}: {appeal_block.get(key, '')}" for key in appeal_block
        )

        self.appeal_active = False
        self.appeal_argument = ""
        self.appeal_counter_argument = ""
        self.status = "resolved"

        return f"APPEAL VERDICT {self.verdict.upper()}:\n{self.verdict_report}"

    # ───────────── views ─────────────

    @gl.public.view
    def get_status(self) -> str:
        return self.status

    @gl.public.view
    def get_verdict(self) -> str:
        if not self.verdict:
            return "No verdict yet"
        return f"{self.verdict.upper()}: {self.verdict_report}"

    @gl.public.view
    def get_reasoning(self) -> str:
        return self.reasoning

    @gl.public.view
    def get_arguments(self) -> dict:
        return {
            "party_a_argument": self.argument_a,
            "party_b_argument": self.argument_b,
            "has_submitted_a": self.has_submitted_a,
            "has_submitted_b": self.has_submitted_b,
        }

    @gl.public.view
    def get_appeal_round(self) -> u64:
        return self.appeal_round

    @gl.public.view
    def get_appeal_arguments(self) -> dict:
        return {
            "appeal_round": self.appeal_round,
            "appeal_argument": self.appeal_argument,
            "counter_argument": self.appeal_counter_argument,
            "appeal_active": self.appeal_active,
        }

    @gl.public.view
    def get_full_state(self) -> dict:
        return {
            "contract_details": {
                "party_a": self.party_a,
                "party_b": self.party_b,
                "amount": self.amount,
                "deadline": self.deadline,
            },
            "facts_and_clause": {
                "objective_facts": self.objective_facts,
                "subjective_clause": self.subjective_clause,
            },
            "arguments": {
                "party_a": self.argument_a,
                "party_b": self.argument_b,
            },
            "resolution": {
                "status": self.status,
                "verdict": self.verdict,
                "reasoning": self.reasoning,
                "verdict_report": self.verdict_report,
            },
            "appeal_info": {
                "appeal_round": self.appeal_round,
                "appeal_active": self.appeal_active,
                "appeal_argument": self.appeal_argument,
                "counter_argument": self.appeal_counter_argument,
            },
        }
