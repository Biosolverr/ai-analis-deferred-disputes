# v0.1.0
# { "Depends": "py-genlayer:latest" }

from genlayer import *


class Arena(gl.Contract):
    status: str
    topic: str
    rules: str
    argument_a: str
    argument_b: str
    winner: str
    reason: str

    def __init__(self, topic: str, rules: str):
        self.status = "open"
        self.topic = topic
        self.rules = rules
        self.argument_a = ""
        self.argument_b = ""
        self.winner = ""
        self.reason = ""

    @gl.public.write
    def submit_argument(self, player: str, argument: str) -> None:
        if player == "a":
            self.argument_a = argument
        elif player == "b":
            self.argument_b = argument
        if self.argument_a and self.argument_b:
            self.status = "ready"

    @gl.public.write
    def resolve_match(self) -> None:
        topic = self.topic
        rules = self.rules
        arg_a = self.argument_a
        arg_b = self.argument_b

        prompt = f"""You are an impartial AI judge evaluating two arguments in a structured debate.

TOPIC: {topic}

JUDGING RULES:
{rules}

ARGUMENT A:
{arg_a}

ARGUMENT B:
{arg_b}

STRICT RULES:
1. Evaluate ONLY by the judging rules above — nothing else
2. Do NOT consider writing style or emotional appeal unless rules specify it
3. If arguments are equal in quality, verdict must be "draw"
4. Your reason must cite which specific points were decisive

VALID VERDICTS: "player_a", "player_b", "draw"

Return a JSON object with exactly:
- "winner": one of "player_a", "player_b", "draw"
- "reason": one sentence citing the decisive points"""

        def leader_fn():
            return gl.nondet.exec_prompt(prompt, response_format="json")

        def validator_fn(leader_result) -> bool:
            if not isinstance(leader_result, gl.vm.Return):
                return False
            data = leader_result.calldata
            return (
                isinstance(data, dict)
                and data.get("winner") in ("player_a", "player_b", "draw")
                and isinstance(data.get("reason"), str)
                and len(data.get("reason", "")) > 0
            )

        result = gl.vm.run_nondet_unsafe(leader_fn, validator_fn)

        self.winner = result.get("winner", "")
        self.reason = result.get("reason", "")
        self.status = "resolved"

    @gl.public.view
    def get_status(self) -> str:
        return self.status

    @gl.public.view
    def get_result(self) -> str:
        if not self.winner:
            return "No result yet"
        return f"{self.winner}: {self.reason}"
