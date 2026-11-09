"""Compare Variant Three with the signs copied from stone 31."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "box_041" / "signs"


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def main():
    draft = load("variant_three.json")
    stone = load("stone_31.json")
    matches = 0
    for number, (a, b) in enumerate(zip(draft["line_1"], stone["line_1"]), start=1):
        same = a == b
        matches += same
        note = draft["notes"].get(str(number), "")
        print(f"sign {number}: draft={a:<14} stone={b:<14} {'match' if same else 'DIFFERENT'}  {note}")
    print(f"\nline 1: {matches}/{len(draft['line_1'])} match")
    print(f"line 2 in draft: {draft['line_2']}")
    print(f"line 2 on stone: {stone['line_2']}")


if __name__ == "__main__":
    main()
