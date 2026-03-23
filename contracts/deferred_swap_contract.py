# v0.1.0
# { "Depends": "py-genlayer:latest" }

from genlayer import *


class DeferredSwap(gl.Contract):
    status: str
    party_a: str
    party_b: str
    amount: str
    deadline: str
    subjective_clause: str
    argument_a: str
    argument_b: str
    appeal_round: u32
    appeal_argument_a: str
    appeal_argument_b: str
    verdict: str
    verdict_reason: str

    def __init__(self, party_a: str, party_b: str, amount: str, deadline: str, subjective_clause: str):
        self.status = "created"
        self.party_a = party_a
        self.party_b = party_b
        self.amount = amount
        self.deadline = deadline
        self.subjective_clause = subjective_clause
        self.argument_a = ""
        self.argument_b = ""
        self.appeal_round = u32(0)
        self.appeal_argument_a = ""
        self.appeal_argument_b = ""
        self.verdict = ""
        self.verdict_reason = ""

    @gl.public.write
    def submit_argument(self, party: str, argument: str) -> None:
        if self.status == "created":
            if party == "a":
                self.argument_a = argument
            elif party == "b":
                self.argument_b = argument
            if self.argument_a and self.argument_b:
                self.status = "disputed"

        elif self.status == "appealing":
            if party == "a":
                self.appeal_argument_a = argument
            elif party == "b":
                self.appeal_argument_b = argument

    @gl.public.write
    def resolve_dispute(self) -> None:
        amount = self.amount
        deadline = self.deadline
        clause = self.subjective_clause
        arg_a = self.argument_a
        arg_b = self.argument_b
        appeal_round = self.appeal_round
        appeal_arg_a = self.appeal_argument_a
        appeal_arg_b = self.appeal_argument_b

        appeal_context = ""
        if appeal_round > u32(0):
            appeal_context = f"""

APPEAL ROUND {appeal_round}:
Party A additional argument: {appeal_arg_a}
Party B additional argument: {appeal_arg_b}
These new arguments must be weighed alongside the original ones."""

        prompt = f"""You are a neutral arbitrator for a smart contract dispute.

DEAL TERMS:
- Amount at stake: {amount}
- Deadline: {deadline}
- Subjective clause: "{clause}"

ORIGINAL ARGUMENTS:
Party A: {arg_a}
Party B: {arg_b}{appeal_context}

STRICT RULES:
1. Base your decision ONLY on the subjective clause and provided arguments
2. Do NOT invent facts not present in arguments
3. Do NOT be influenced by emotional language
4. Do NOT favor either party without clear justification grounded in facts
5. If evidence is equal on both sides, verdict must be "split"
6. Your reason must reference specific facts from the arguments

VALID VERDICTS: "party_a", "party_b", "split"

Return a JSON object with exactly:
- "verdict": one of "party_a", "party_b", "split"
- "reason": one sentence citing specific facts"""

        def leader_fn():
            return gl.nondet.exec_prompt(prompt, response_format="json")

        def validator_fn(leader_result) -> bool:
            if not isinstance(leader_result, gl.vm.Return):
                return False
            data = leader_result.calldata
            return (
                isinstance(data, dict)
                and data.get("verdict") in ("party_a", "party_b", "split")
                and isinstance(data.get("reason"), str)
                and len(data.get("reason", "")) > 0
            )

        result = gl.vm.run_nondet_unsafe(leader_fn, validator_fn)

        self.verdict = result.get("verdict", "")
        self.verdict_reason = result.get("reason", "")
        self.status = "resolved"

    @gl.public.write
    def appeal(self) -> None:
        if self.status != "resolved":
            raise gl.UserError("Can only appeal after resolution")
        if self.appeal_round >= u32(2):
            raise gl.UserError("Maximum 2 appeal rounds reached")
        self.appeal_round = self.appeal_round + u32(1)
        self.appeal_argument_a = ""
        self.appeal_argument_b = ""
        self.status = "appealing"

    @gl.public.view
    def get_status(self) -> str:
        return self.status

    @gl.public.view
    def get_verdict(self) -> str:
        if not self.verdict:
            return "No verdict yet"
        return f"{self.verdict}: {self.verdict_reason}"

    @gl.public.view
    def get_appeal_round(self) -> u32:
        return self.appeal_round
