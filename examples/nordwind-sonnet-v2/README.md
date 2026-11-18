# Real run with prompt v2: Sonnet via Claude Code

`python -m lens analyze demo/nordwind/profile.yaml --as-of 2026-11-18 --backend claude-code`, run on 2026-11-18.

| | prompt v1 | prompt v2 |
|---|---|---|
| status accuracy | 87% | 95% (97% after key fixes) |
| on law checks | 82% | 96% (98%) |
| problem precision | 83% | 93% (94%) |
| problem recall | 98% | 100% |
| planted errors found (exact status) | 19/19 (18) | 19/19 (19) |

The v2 run was first scored against the key as it stood (95%). Two key fixes followed, giving the figures in brackets:

- **GP-10.c2 corrected.** The key had it as covered; it should be partial. The check also asks about disclosures, which the procedure does not mention.
- **DIS-01.c1: partial accepted.** Both models gave partial in every run.

In the remaining mismatches (DIS-06.c1, GP-08.c2, REP-03.c3), the explanation says the required element is absent but the status is partial. Prompt v3 adds a rule for this; it has not been run yet.

`report.md` is the report from this run.
