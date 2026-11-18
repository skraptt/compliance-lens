# First real run: Sonnet via Claude Code (prompt v1)

`python -m lens analyze demo/nordwind/profile.yaml --as-of 2026-11-18 --backend claude-code`, run on 2026-11-18 with the first prompt.

- Scored against the original key: 95/109 checks correct (87%), all 19 planted errors found (18 with the exact status), problem recall 98%, precision 83%.
- Scored against the key after three defensible alternatives were accepted: 98/109 checks correct (90%).

The mismatches came from three prompt problems:

- **Status that disagreed with the model's own explanation.** For example, T+1 was marked "contradicts" while the explanation said it counts as covered.
- **Problems counted under the wrong check.** For example, a one-month deadline lowered the status of an unrelated timeliness check.
- **Examples in a check read as requirements.** The model treated "e.g." lists and named teams as requirements.

Prompt v2 fixes these: the explanation now comes before the status, each check is judged on its own wording, and explicit rules define partial and contradicts.
