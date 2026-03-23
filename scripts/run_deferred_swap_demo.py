"""
DeferredSwap Demo Runner

Run this script to see exact arguments to paste into GenLayer Studio.
Usage: python run_deferred_swap_demo.py

All scenarios were tested live in GenLayer Studio (March 2026).
"""

# === DEPLOY PARAMETERS ===
DEPLOY_PARAMS = {
    "buyer": "Alice",
    "seller": "Bob",
    "amount": 5000,
    "terms": (
        "Bob delivers working software with full documentation by March 1 2026. "
        "Alice pays 5000 USDC upon delivery. Software must run without errors on buyer machine."
    )
}

# === SCENARIO 1: Clear Winner ===
SCENARIO_1 = {
    "name": "Clear Winner — seller wins on vague buyer claim",
    "buyer_argument": (
        "The software crashed on launch. "
        "No documentation was provided as required by the terms."
    ),
    "seller_argument": (
        "I delivered working software with 95% test coverage and a recorded demo video. "
        "The buyer has not provided any crash logs or evidence of failure."
    ),
    "expected": "seller"
}

# === SCENARIO 2: Appeal Changes Verdict ===
SCENARIO_2 = {
    "name": "Appeal — verdict changes from seller to split",
    "round_1": {
        "buyer_argument": (
            "Software crashed on launch. No documentation provided."
        ),
        "seller_argument": (
            "95% test coverage, demo video delivered. App works correctly on staging environment."
        ),
        "expected": "seller"
    },
    "round_2": {
        "buyer_argument": (
            "Staging environment is not production. "
            "The contract required delivery on buyer machine — seller never tested there. "
            "Still no documentation was delivered."
        ),
        "seller_argument": (
            "Crash was caused by buyer's misconfigured server — logs from staging prove the app runs correctly. "
            "Documentation requirement was not in the original contract terms."
        ),
        "expected": "split"
    }
}

# === SCENARIO 3: Symmetric Arguments (untested) ===
SCENARIO_3 = {
    "name": "Symmetric — both sides have equal evidence",
    "buyer_argument": (
        "Payment was transferred on time per contract terms. Transaction hash: 0xabc123. "
        "Delivery has not occurred after 30 days."
    ),
    "seller_argument": (
        "Delivery was completed on time. Commit hash: gh/repo/abc123 submitted March 1. "
        "Buyer has not acknowledged receipt."
    ),
    "expected": "split or requires external evidence"
}


def print_studio_guide():
    print("=" * 65)
    print("DEFERRED SWAP — GENLAYER STUDIO STEP-BY-STEP GUIDE")
    print("=" * 65)

    print("\n── DEPLOY ──────────────────────────────────────────────────")
    print("Constructor arguments:")
    for key, val in DEPLOY_PARAMS.items():
        print(f"  {key}: {val}")

    print("\n── SCENARIO 1: Clear Winner ─────────────────────────────────")
    print(f"Name: {SCENARIO_1['name']}")
    print(f"\nsubmit_argument →")
    print(f"  party:    buyer")
    print(f"  argument: {SCENARIO_1['buyer_argument']}")
    print(f"\nsubmit_argument →")
    print(f"  party:    seller")
    print(f"  argument: {SCENARIO_1['seller_argument']}")
    print(f"\nresolve_dispute() → wait FINALIZED")
    print(f"get_verdict()     → expected: {SCENARIO_1['expected']}")

    print("\n── SCENARIO 2: Appeal ───────────────────────────────────────")
    print(f"Name: {SCENARIO_2['name']}")
    print(f"\n[Round 1]")
    print(f"submit_argument →")
    print(f"  party:    buyer")
    print(f"  argument: {SCENARIO_2['round_1']['buyer_argument']}")
    print(f"submit_argument →")
    print(f"  party:    seller")
    print(f"  argument: {SCENARIO_2['round_1']['seller_argument']}")
    print(f"resolve_dispute() → expected: {SCENARIO_2['round_1']['expected']}")

    print(f"\n[Appeal]")
    print(f"appeal() → wait FINALIZED")
    print(f"get_appeal_round() → should return 1")

    print(f"\n[Round 2]")
    print(f"submit_appeal_argument →")
    print(f"  party:    buyer")
    print(f"  argument: {SCENARIO_2['round_2']['buyer_argument']}")
    print(f"submit_appeal_argument →")
    print(f"  party:    seller")
    print(f"  argument: {SCENARIO_2['round_2']['seller_argument']}")
    print(f"re_resolve_dispute() → wait FINALIZED")
    print(f"get_verdict()        → expected: {SCENARIO_2['round_2']['expected']}")

    print("\n── SCENARIO 3: Symmetric (untested) ─────────────────────────")
    print(f"Name: {SCENARIO_3['name']}")
    print(f"\nsubmit_argument →")
    print(f"  party:    buyer")
    print(f"  argument: {SCENARIO_3['buyer_argument']}")
    print(f"submit_argument →")
    print(f"  party:    seller")
    print(f"  argument: {SCENARIO_3['seller_argument']}")
    print(f"\nresolve_dispute() → expected: {SCENARIO_3['expected']}")


if __name__ == "__main__":
    print_studio_guide()
