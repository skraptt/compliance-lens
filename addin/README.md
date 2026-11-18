# Compliance Lens — Word add-in

A task pane for Word that checks the selected passage or the whole document against the REMIT checklist. The pane is plain HTML/JS, with no build step. It talks to a small local server (`python -m lens serve`) that holds your Anthropic API key and runs the engine.

```
Word ── task pane (https://localhost:3000/taskpane.html)
          │  /api/selection, /api/scan
          ▼
     python -m lens serve  ──►  Claude API
```

> **Only analyse documents you are allowed to send to the Anthropic API.** Do not use an employer's or client's internal procedures without permission. The fictional Nordwind documents in `demo/nordwind/` are made for testing.

## Set-up on a Mac (once)

1. **Python packages** (Python 3.10+):
   ```bash
   cd compliance-lens
   pip3 install pyyaml python-docx
   ```
2. **HTTPS certificate for localhost.** Word only loads add-ins over HTTPS. This command needs Node.js; it creates a certificate in `~/.office-addin-dev-certs/` and asks for your password to trust it:
   ```bash
   npx office-addin-dev-certs install
   ```
3. **Start the server** (keep this terminal open). Pick one way to reach Claude:
   ```bash
   # a) with your Claude subscription (Pro/Max): needs Claude Code installed and logged in
   python3 -m lens serve --backend claude-code

   # b) with an Anthropic API key (billed per use)
   export ANTHROPIC_API_KEY=sk-ant-...
   python3 -m lens serve
   ```
   With **a)**, the engine calls `claude -p` with every tool switched off, in an empty temporary folder, and without `ANTHROPIC_API_KEY`, so usage goes to your subscription. It counts against the same limits as your normal Claude use. A whole-document scan makes a few calls; a selection makes one.
   Open https://localhost:3000/taskpane.html in Safari. If the page loads without a certificate warning, the certificate works. Outside Word it will only say "Compliance Lens runs in Word".
4. **Sideload the manifest:**
   ```bash
   mkdir -p ~/Library/Containers/com.microsoft.Word/Data/Documents/wef
   cp addin/manifest.xml ~/Library/Containers/com.microsoft.Word/Data/Documents/wef/
   ```
   Restart Word and open a document. **Compliance Lens** appears at the right of the **Home** tab. If it does not, go to **Insert → Add-ins → My Add-ins**, where it is listed under developer add-ins.

## Use

1. **Setup:** tick the document type (e.g. *Inside information policy*). This is saved in the document. Then tick what is true for the company (asset owner, algorithmic trading, …). This is saved on your computer and decides which obligations apply.
2. **Selection:** select a paragraph and click **Analyse selection**. You get the checks this passage touches, marked as conflict, partial or covered, each with its legal source. With **Auto** on, each new selection is analysed after a 1.5-second pause. Results are cached, so selecting the same text again costs nothing.
3. **Document:** **Scan document** checks the whole text. Conflicts are highlighted pink, and gaps and weak points yellow. **Add comments** inserts a Word comment on each problem paragraph. Click a finding to jump to its paragraph. **Clear highlights** removes the colours set in this session.

Office.js has no mouse-hover event, so "hover" works on selection. Select or click into a passage and let Auto analyse it.

## Try it on the demo

Open `demo/nordwind/inside-information-policy.docx`. In Setup, tick *Inside information policy* and the profile flags *market participant*, *registered*, *owns or operates facilities* and *group facilities*. Then select §4.2 ("within 24 hours"). The pane should report conflicts with Article 4(1) and ACER's one-hour target.

## Troubleshooting

- **Blank pane or "Cannot reach the local server":** check that `python3 -m lens serve` is running and that Safari opens https://localhost:3000/taskpane.html without a warning.
- **Developer tools:** run `defaults write com.microsoft.Word OfficeWebAddinDeveloperExtras -bool true`, restart Word, then right-click the pane and choose **Inspect Element**.
- **Old version still showing:** quit Word and delete `~/Library/Containers/com.microsoft.Word/Data/Library/Caches/` and `~/Library/Containers/com.microsoft.Word/Data/Library/Application Support/Microsoft/Office/16.0/Wef/`, then start Word again.
- **Word on the web:** **Insert → Add-ins → Upload My Add-in** and choose `addin/manifest.xml`. The server must still run on your machine.

## Tests

`python -m unittest discover tests` runs the server tests and an end-to-end test of the pane in headless Chrome, with a fake Office.js and the Nordwind document. That test is skipped if Playwright or Chrome is missing. `node --test tests/logic.test.js` runs the pane logic tests. To regenerate the icons: `python scripts/make_icons.py addin/assets`.
