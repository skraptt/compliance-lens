# Compliance Lens — Word add-in

A task pane for Word that checks the selected passage or the whole document against the REMIT checklist. The pane is plain HTML/JS, with no build step. It talks to a small local server (`python -m lens serve`). The server runs the engine and reaches Claude through Claude Code or your API key; the add-in never sees the key.

```
Word ── task pane (https://localhost:3000/taskpane.html)
          │  /api/selection, /api/scan
          ▼
     python -m lens serve  ──►  Claude API
```

> **Only analyse documents you are allowed to send to the Anthropic API.** Do not use an employer's or client's internal procedures without permission. The fictional Nordwind documents in `demo/nordwind/` are made for testing.

## Set-up

`./scripts/setup.sh` once, then `./scripts/start.sh` each time (see the main [README](../README.md#quick-start)). The scripts do the steps below. Follow these steps by hand if a script fails.

1. **Python packages** (Python 3.10+): `pip3 install -r requirements.txt`
2. **HTTPS certificate for localhost.** Word only loads add-ins over HTTPS. The following command needs Node.js. It creates a certificate in `~/.office-addin-dev-certs/` and asks for your password to trust it:
   ```bash
   npx office-addin-dev-certs install
   ```
3. **Start the server** and keep this terminal open. Choose one way to reach Claude:
   ```bash
   # a) with your Claude subscription (Pro/Max): needs Claude Code installed and logged in
   python3 -m lens serve --backend claude-code

   # b) with an Anthropic API key (billed per use)
   export ANTHROPIC_API_KEY=sk-ant-...
   python3 -m lens serve
   ```
   With **a)**, the engine calls `claude -p` with every tool switched off, in an empty temporary folder, and without `ANTHROPIC_API_KEY`. Usage therefore goes to your subscription and counts against the same limits as your normal Claude use. A whole-document scan makes a few calls; a selection makes one.

   To check the certificate, open https://localhost:3000/taskpane.html in Safari. If the page loads without a certificate warning, the certificate works. Outside Word, the page only says "Compliance Lens runs in Word".
4. **Sideload the manifest.**
   - **Word for Mac:** run the commands below, then restart Word. **Compliance Lens** appears at the right of the **Home** tab.
     ```bash
     mkdir -p ~/Library/Containers/com.microsoft.Word/Data/Documents/wef
     cp addin/manifest.xml ~/Library/Containers/com.microsoft.Word/Data/Documents/wef/
     ```
   - **Word on the web:** **Home → Add-ins → More Add-ins → My Add-ins → Upload My Add-in**, then choose `addin/manifest.xml`. Ignore the "Your administrator has not installed Web Add-ins" note; it appears on personal accounts. If the button disappears later, upload the manifest again.

## Use

1. **Setup:** tick the document type, for example *Inside information policy*. This is saved in the document. Then tick what is true for the company (asset owner, algorithmic trading, …). This is saved on your computer and decides which obligations apply. **Use the fictional demo company** fills in the Nordwind profile.
2. **Selection:** select a paragraph and click **Analyse selection**. You get the checks this passage touches, marked as conflict, partial or covered, each with its legal source. With **Auto** on, each new selection is analysed after a 1.5-second pause. Results are cached, so selecting the same text again costs nothing.
3. **Document:** **Scan document** checks the whole text. Conflicts are highlighted pink, and gaps and weak points yellow. **Add comments** inserts a Word comment on each problem paragraph. Click a finding to jump to its paragraph. **Clear highlights** removes the colours set in this session.

Office.js has no mouse-hover event, so "hover" works on selection. Select or click into a passage and let Auto analyse it.

## Try it on the demo

1. Open `demo/nordwind/inside-information-policy.docx`.
2. In Setup, tick *Inside information policy* and click **Use the fictional demo company**.
3. Select §4.2 ("within 24 hours"). The pane should report conflicts with Article 4(1) REMIT and with ACER's one-hour target.

## Troubleshooting

- **"No REMIT checks apply":** the company profile in Setup is empty or does not fit the document type. Tick at least the first question, or use the demo company.
- **Blank pane or "Cannot reach the local server":** check that `python3 -m lens serve` is running and that Safari opens https://localhost:3000/taskpane.html without a warning.
- **Developer tools:** run `defaults write com.microsoft.Word OfficeWebAddinDeveloperExtras -bool true`, restart Word, then right-click the pane and choose **Inspect Element**.
- **Old version still showing:** quit Word and delete `~/Library/Containers/com.microsoft.Word/Data/Library/Caches/` and `~/Library/Containers/com.microsoft.Word/Data/Library/Application Support/Microsoft/Office/16.0/Wef/`, then start Word again.

## Tests

`python -m unittest discover tests` runs the server tests and an end-to-end test of the pane in headless Chrome, with a fake Office.js and the Nordwind document. That test is skipped if Playwright or Chrome is missing. `node --test tests/logic.test.js` runs the pane logic tests. To regenerate the icons: `python scripts/make_icons.py addin/assets`.
