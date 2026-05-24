# FAQ

## Ist dieses Repository eine installierbare Anwendung?

Nein. Es ist eine Markdown- und Asset-Sammlung für mehrere Custom-GPT-Konfigurationen.

## Wie nutze ich einen GPT direkt?

Öffne den passenden ChatGPT-Link in der zentralen [`README.md`](../README.md) oder in der README des jeweiligen GPT-Ordners.

## Wie prüfe ich einen GPT lokal?

Starte im jeweiligen Ordner mit `README.md`. Lies danach `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` und vorhandene `beispiel.*` Dateien gemeinsam, weil diese Dateien zusammen das Verhalten, die Einordnung und die erwartete Ergebnisqualität des GPTs beschreiben.

## Wofür sind `beispiel.md` oder `beispiel.*` Dateien gedacht?

Sie liefern ein vollständiges Musterergebnis. Bei Beratungs-, Analyse- oder Text-GPTs ist das meist `beispiel.md`. Bei Programmier- oder Dateigenerator-GPTs können es konkrete Artefakte wie `beispiel.py`, `beispiel_test.py`, `beispiel.html` oder `beispiel.json` sein.

## Warum sind manche Dateinamen oder IDs nicht eingedeutscht?

Technische Slugs, Modell-IDs, Dateinamen, URLs und Parameter bleiben bewusst stabil. Sie können in Prompt-Artefakten, Exporten oder Zielsystemen referenziert sein.

## Darf ich echte Zugangsdaten in Beispiele eintragen?

Nein. Echte Secrets, Tokens, Passwörter, API-Keys, Kundendaten und personenbezogene Daten gehören nicht in dieses Repository.

## Gibt es automatisierte Tests?

Es gibt keinen fachlichen Testlauf für GPT-Verhalten. Der Repository-Health-Workflow prüft Dokumentationsstruktur, lokale Markdown-Links und referenzierte Bilder. Fachliche Prompt-Änderungen müssen zusätzlich manuell geprüft werden.

## Kann ich neue GPT-Pakete beitragen?

Ja, wenn Zweck, Zielgruppe, Dateien, Sicherheitsgrenzen und mindestens ein Beispielartefakt klar dokumentiert sind. Öffne bei größeren Ergänzungen zuerst ein Issue.
