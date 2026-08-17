# Stage 1 — Integrity (gate)

```bash
python3 workflow/scripts/extract_paper.py 612d60fa-pdf.pdf --out-dir artifacts
# exit 0
```

- [x] `artifacts/integrity.json` produced; exit code **0** recorded
- [x] High-confidence spans: **none**
- [x] Low-confidence notes: **none**
- [x] Injection-phrase hits: **none**
- [x] AC notification: not required
- [x] Content review proceeded normally

## Record

| Field | Value |
| --- | --- |
| Exit code | 0 |
| Pages | 9 (upload metadata claimed 34 — metadata error, verified with pypdf) |
| Font resources | median 5/page, no outliers |
| Single-glyph shows | 0 on every page |
| Assessment | **Clean.** Nothing to report. |

A clean scan is a clean result. No escalated inspection was performed beyond the
standard signals, per the workflow's between-reviews rule: finding a payload in one
submission says nothing about the base rate in the next.
