# Example run: Nordwind demo, blind stand-in

These files come from a run of the v0.3 checklist on the fictional Nordwind documents, assessed as of 2026-11-18.

The prompts the engine builds (`python -m lens analyze ... --dry-run`) were not answered through the API. A separate Claude agent answered them instead, without access to `answer_key.yaml`. That agent's answers are in `responses.json`, and they were replayed through the pipeline:

```
python -m lens analyze demo/nordwind/profile.yaml --as-of 2026-11-18 --replay examples/nordwind-blind-run/responses.json --out runs/blind
python -m lens eval runs/blind/findings.json demo/nordwind/answer_key.yaml
```

Score against the answer key, after six defensible alternative answers were added to the key following this run:

- 108 of 109 checks correct (99%)
- all 19 planted errors found, each with the exact expected status
- problem recall 100%, problem precision 93%

A run through the API with `ANTHROPIC_API_KEY` set is the real measurement and is still to be done.
