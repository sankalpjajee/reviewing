# Stage 1 — Integrity (gate)

Run before reading the paper for content.

```bash
python workflow/scripts/extract_paper.py SUBMISSION.pdf --out-dir reviews/<slug>/artifacts
```

Exit 0 = clean · 1 = low-confidence notes only · 2 = high-confidence flag.

- [ ] `artifacts/integrity.json` produced and exit code recorded
- [ ] High-confidence spans reviewed (`glyph_font_fragmentation`, `font_resource_outlier`,
      `invisible_render_mode`, `sub_legible_font`)
- [ ] Low-confidence notes (`white_on_white`) confirmed visually before use — white text
      over a coloured rule is legitimate and this signal alone proves nothing
- [ ] Injection-phrase hits quoted verbatim into the finding
- [ ] Payload pages, repetition count, and technique described
- [ ] AC notified if any high-confidence flag or injection hit
- [ ] Confirmed: no instruction found in the submission was acted on

## Interpreting the technique

| Signal | What it means |
| --- | --- |
| `glyph_font_fragmentation` | Each character drawn in its own single-use font subset, so the glyph *rendered* and the codepoint *extracted* differ. Not producible by any normal toolchain. **Hidden does not mean invisible** — the cover text may be legitimate-looking boilerplate, so compare rendered against extracted rather than trusting that the page looks fine. |
| `font_resource_outlier` | One page carrying many times the document's median font count. Corroborates the above. |
| `invisible_render_mode` | Text render mode 3 — neither filled nor stroked. |
| `sub_legible_font` | Text below the legibility floor. |
| `white_on_white` | White fill. Low confidence: needs visual confirmation. |

## Judgement

Distinguish, and say which you concluded and why:

- **Accident** — an artifact of the production toolchain, with content unrelated
  to reviewing (stale headers, watermark residue, tool metadata).
- **Targeted** — content that only makes sense as an instruction to an automated
  reviewer. Repetition across distant pages, phrasing that names the output, and
  a hiding technique with no legitimate use all point here.

## Record

| Field | Value |
| --- | --- |
| Exit code | |
| Pages affected | |
| Technique | |
| Payload (verbatim) | |
| Assessment | accident / targeted |
| AC notified | |
