# Stage 3 — Numeric and statistical audit

```bash
python workflow/scripts/audit_numbers.py reviews/<slug>/artifacts/checks.json \
    --json reviews/<slug>/artifacts/numeric_audit.json
```

## Arithmetic

- [ ] Table totals equal the sum of their parts
- [ ] Percentages recompute from the counts
- [ ] Every number the prose *derives* from a table is checked (`ratio`, `pct_change`, `delta`)
- [ ] Every counting claim is checked with `count_true`, not read
- [ ] Worked examples in appendices are consistent with thresholds defined in the body
- [ ] Tolerances set to absorb the paper's rounding, so a FAIL is a real disagreement

## Statistical treatment

- [ ] Number of runs and seeds — stated anywhere?
- [ ] Error bars or CIs on the claims that carry the paper
- [ ] Significance tests where a comparison is asserted
- [ ] Chance performance computed independently and compared to reported accuracy
- [ ] Any CI reported on an incidental result while the headline result has none
- [ ] Metric definitions unambiguous (what counts as correct, how failures are scored)
- [ ] Denominators stated for every rate

## Record

| Check | Result | Finding? |
| --- | --- | --- |
