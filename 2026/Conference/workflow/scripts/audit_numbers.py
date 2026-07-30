#!/usr/bin/env python3
"""Stage 3 - machine-check the arithmetic a paper asserts about its own tables.

Reviewers routinely accept derived numbers because recomputing them by hand is
tedious. This makes the recomputation cheap and, more importantly, forces the
reviewer to transcribe the paper's numbers into a file where a disagreement
between the table and the prose becomes visible rather than plausible.

Each check names the claim it is testing and where in the paper that claim lives,
so a failure lands in the review already carrying its citation.

Check kinds
-----------
sum         parts sum to total
percent     100 * value / total equals the stated percentage
ratio       numerator / denominator equals the stated value (optionally scaled)
pct_change  100 * (new - old) / old equals the stated percentage change
delta       new - old equals the stated difference
compare     a relational assertion the prose makes, e.g. chain > label on a field
count_true  how many of several relations hold, against the number the prose claims

Usage:
    python audit_numbers.py CHECKS.json [--tolerance 0.05] [--json REPORT.json]

Exit status is 0 when every check passes and 1 when any fails.
"""

from __future__ import annotations

import argparse
import json
import operator
import sys
from pathlib import Path

OPS = {
    ">": operator.gt, ">=": operator.ge,
    "<": operator.lt, "<=": operator.le,
    "==": operator.eq, "!=": operator.ne,
}


class CheckError(Exception):
    pass


def _num(check: dict, key: str) -> float:
    if key not in check:
        raise CheckError(f"missing required field {key!r}")
    try:
        return float(check[key])
    except (TypeError, ValueError):
        raise CheckError(f"field {key!r} is not numeric: {check[key]!r}")


def _relation(rel: dict) -> tuple[bool, str]:
    op = rel.get("op")
    if op not in OPS:
        raise CheckError(f"unknown operator {op!r}")
    left, right = float(rel["left"]), float(rel["right"])
    tol = float(rel.get("tolerance", 0.0))
    if op in ("==", "!="):
        equal = abs(left - right) <= tol
        held = equal if op == "==" else not equal
    else:
        # Slack the comparison in the direction that favours the paper, so a
        # "matches or exceeds" claim is not failed on a rounding artefact.
        slack = tol if op in (">", ">=") else -tol
        held = OPS[op](left + slack, right)
    return held, f"{rel.get('name', '')} {left} {op} {right}".strip()


def run_check(check: dict, default_tol: float) -> dict:
    kind = check.get("kind")
    tol = float(check.get("tolerance", default_tol))
    result = {
        "id": check.get("id", "<unnamed>"),
        "kind": kind,
        "location": check.get("location", ""),
        "claim": check.get("claim", ""),
        "status": "PASS",
        "detail": "",
    }

    try:
        if kind == "sum":
            parts = [float(p) for p in check["parts"]]
            total, got = _num(check, "total"), sum(parts)
            result["detail"] = f"sum(parts)={got:g} vs stated total={total:g} (n_parts={len(parts)})"
            ok = abs(got - total) <= tol

        elif kind == "percent":
            value, total, stated = _num(check, "value"), _num(check, "total"), _num(check, "stated")
            got = 100.0 * value / total
            result["detail"] = f"100*{value:g}/{total:g}={got:.4f} vs stated {stated:g}"
            ok = abs(got - stated) <= tol

        elif kind == "ratio":
            num, den, stated = _num(check, "numerator"), _num(check, "denominator"), _num(check, "stated")
            scale = float(check.get("scale", 1.0))
            got = scale * num / den
            result["detail"] = f"{scale:g}*{num:g}/{den:g}={got:.4f} vs stated {stated:g}"
            ok = abs(got - stated) <= tol

        elif kind == "pct_change":
            old, new, stated = _num(check, "old"), _num(check, "new"), _num(check, "stated")
            got = 100.0 * (new - old) / old
            result["detail"] = f"100*({new:g}-{old:g})/{old:g}={got:.4f} vs stated {stated:g}"
            ok = abs(got - stated) <= tol

        elif kind == "delta":
            old, new, stated = _num(check, "old"), _num(check, "new"), _num(check, "stated")
            got = new - old
            result["detail"] = f"{new:g}-{old:g}={got:.4f} vs stated {stated:g}"
            ok = abs(got - stated) <= tol

        elif kind == "compare":
            ok, desc = _relation({**check, "tolerance": tol})
            result["detail"] = f"relation {desc} -> {'holds' if ok else 'does not hold'}"

        elif kind == "count_true":
            outcomes = []
            for rel in check["relations"]:
                held, desc = _relation({**rel, "tolerance": rel.get("tolerance", tol)})
                outcomes.append((held, desc))
            got = sum(1 for held, _ in outcomes if held)
            stated = int(check["stated"])
            lines = "; ".join(f"{desc} -> {'T' if held else 'F'}" for held, desc in outcomes)
            result["detail"] = f"{got} of {len(outcomes)} relations hold (paper says {stated}) :: {lines}"
            ok = got == stated

        else:
            raise CheckError(f"unknown check kind {kind!r}")

    except CheckError as exc:
        result["status"] = "ERROR"
        result["detail"] = str(exc)
        return result
    except (KeyError, ZeroDivisionError) as exc:
        result["status"] = "ERROR"
        result["detail"] = f"{type(exc).__name__}: {exc}"
        return result

    result["status"] = "PASS" if ok else "FAIL"
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("checks", type=Path)
    ap.add_argument("--tolerance", type=float, default=0.05,
                    help="absolute tolerance, generous enough to absorb the paper's own rounding")
    ap.add_argument("--json", type=Path, help="also write the machine-readable report here")
    args = ap.parse_args()

    spec = json.loads(args.checks.read_text())
    checks = spec["checks"] if isinstance(spec, dict) else spec
    results = [run_check(c, args.tolerance) for c in checks]

    width = max((len(r["id"]) for r in results), default=10)
    for r in results:
        marker = {"PASS": "ok  ", "FAIL": "FAIL", "ERROR": "ERR "}[r["status"]]
        print(f"{marker} {r['id']:<{width}}  {r['detail']}")
        if r["status"] != "PASS" and r["claim"]:
            print(f"     paper claims: {r['claim']}  [{r['location']}]")

    failed = [r for r in results if r["status"] == "FAIL"]
    errored = [r for r in results if r["status"] == "ERROR"]
    print(f"\n{len(results) - len(failed) - len(errored)} passed, {len(failed)} failed, {len(errored)} errored")

    if args.json:
        args.json.write_text(json.dumps({"results": results}, indent=2))

    return 1 if failed or errored else 0


if __name__ == "__main__":
    sys.exit(main())
