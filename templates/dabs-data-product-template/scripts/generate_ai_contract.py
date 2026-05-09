#!/usr/bin/env python3
"""CLI wrapper to generate the AI Consumption Contract markdown from a contract.

Usage:
    python scripts/generate_ai_contract.py \
        --contract data-contract.yml \
        --out docs/ai-consumption-contract.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running this script from the subproject root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.contract import generate_ai_consumption_contract, load   # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", required=True, help="Path to data-contract.yml")
    parser.add_argument("--out", required=True, help="Path for the AI Consumption Contract markdown.")
    args = parser.parse_args()

    contract = load(args.contract)
    md = generate_ai_consumption_contract(contract)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md)

    print(f"AI Consumption Contract written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
