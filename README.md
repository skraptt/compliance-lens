# Compliance Lens

An open-source assistant that reads a company's internal compliance procedures and flags what they miss or get wrong under **REMIT** (EU wholesale energy market integrity), with the legal source for each finding. The engine runs from the command line today; the Word add-in will use the same engine on the paragraph you select.

> Personal project. Uses only public sources and fictional demo documents. Not legal advice.

## How it works

1. **Checklist** (`obligations/remit.yaml`): 41 REMIT obligations with 158 checks, plus a MAR block and 15 good-practice items. Every check is tagged `law`, `guidance` (ACER expectation) or `good_practice`. Only missing `law` checks are reported as gaps. Sources are verified through the [REMIT MCP](https://github.com/skraptt/remit-mcp).
2. **Profile**: what the company is (asset owner? algorithmic trader? broker?) decides which obligations apply.
3. **Documents**: each document is tagged with its type (inside information policy, market conduct, transaction reporting, ...). Checks run on their primary document; on other documents, a hit is shown as "may be covered elsewhere".
4. **Analysis**: Claude assesses each check against the numbered paragraphs (`covered / partial / missing / contradicts`), citing paragraph, quote and reason.
5. **Report**: conflicts, gaps, weak points, ACER expectations and recommendations, plus what is not yet in force.

## Try it

```bash
pip install pyyaml python-docx
export ANTHROPIC_API_KEY=...

# check the fictional Nordwind documents
python -m lens analyze demo/nordwind/profile.yaml --as-of 2026-11-18 --out runs/nordwind
open runs/nordwind/report.md

# score the run against the answer key
python -m lens eval runs/nordwind/findings.json demo/nordwind/answer_key.yaml
```

Offline options: `--dry-run` prints the prompts; `--mock-key demo/nordwind/answer_key.yaml` runs the pipeline with a fake model; `--replay responses.json` replays saved model output. Tests: `python -m unittest discover tests`.

## Demo: Nordwind Energy Trading GmbH (fictional)

`demo/nordwind/` holds three procedures with deliberate errors (19 planted), e.g. inside information published "within 24 hours" on the company website, no notification to ACER when publication is delayed, orders to trade excluded from reporting, exchange trades reported twice, algorithm records kept for three years. `answer_key.yaml` gives the expected result for every check. The `.docx` files are built from `demo/nordwind/src/*.md` with `scripts/md_to_docx.py`.

## Layout

```
obligations/remit.yaml        checklist (v0.3) · CHANGELOG.md · REMIT-obligations-review.md
examples/                     a sample report and findings (blind run on the Nordwind demo)
lens/                         engine: checklist selection, document reader, Claude call, report, eval
demo/nordwind/                profile, documents, answer key
reviews/                      independent legal reviews of the checklist
scripts/                      checklist checker, md -> docx
tests/                        offline tests
```

## Roadmap

1. ~~REMIT checklist~~ · 2. ~~engine + demo~~ (real-model evaluation pending) · 3. Word add-in: side panel, analyse selection · 4. whole-document scan with highlights and comments · 5. MAR and enforcement cases
