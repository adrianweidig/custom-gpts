# FAQ

Sprachen: [Deutsch](FAQ.md) | [English](../en/FAQ.md)

## Ist dieses Repository eine installierbare Anwendung?

Nein. Es ist eine Markdown- und Asset-Sammlung für mehrere Custom-GPT-Konfigurationen.

## Wie nutze ich einen GPT direkt?

Öffne den passenden ChatGPT-Link in der zentralen [`README.md`](../../README.md) oder in der README des jeweiligen GPT-Ordners.

## Wie prüfe ich einen GPT lokal?

Starte im jeweiligen Ordner mit `README.md` oder `README.en.md`. Lies danach `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` und vorhandene `beispiel.*` Dateien gemeinsam, weil diese Dateien zusammen Verhalten, Einordnung und erwartete Ergebnisqualität des GPTs beschreiben.

## Wofür sind `beispiel.md` oder `beispiel.*` Dateien gedacht?

Sie liefern ein vollständiges Musterergebnis. Bei Beratungs-, Analyse- oder Text-GPTs ist das meist `beispiel.md`. Bei Programmier- oder Dateigenerator-GPTs können es konkrete Artefakte wie `beispiel.py`, `beispiel_test.py`, `beispiel.html` oder `beispiel.json` sein.

## Warum sind manche Dateinamen oder IDs nicht eingedeutscht?

Technische Slugs, Modell-IDs, Dateinamen, URLs und Parameter bleiben bewusst stabil. Sie können in Prompt-Artefakten, Exporten oder Zielsystemen referenziert sein.

## Wie funktioniert Mehrsprachigkeit im Repository?

Deutsch ist Standard. Englische Alternativdateien liegen neben den deutschen Dateien, zum Beispiel `README.en.md`, `CONTRIBUTING.en.md` oder `docs/en/index.md`. GitHub übersetzt die normale Repository-Ansicht nicht automatisch; Nutzer wechseln über sichtbare Sprachlinks.

## Erkennen die GPTs automatisch die Systemsprache?

Das Repository selbst hat keine Runtime. Viele GPT-Artefakte reagieren auf die Sprache der Nutzeranfrage oder auf explizite Sprachvorgaben. Wenn keine zuverlässige Sprache erkennbar ist, gilt Deutsch als Fallback.

## Darf ich echte Zugangsdaten in Beispiele eintragen?

Nein. Echte Secrets, Tokens, Passwörter, API-Keys, Kundendaten und personenbezogene Daten gehören nicht in dieses Repository.

## Gibt es automatisierte Tests?

Es gibt keinen fachlichen Testlauf für GPT-Verhalten. Der Repository-Health-Workflow prüft Dokumentationsstruktur, lokale Markdown-Links, referenzierte Bilder, i18n-Pflichtdateien, UTF-8 und Unicode-Fixtures. Fachliche Prompt-Änderungen müssen zusätzlich manuell geprüft werden.

## Kann ich neue GPT-Pakete beitragen?

Ja, wenn Zweck, Zielgruppe, Dateien, Sicherheitsgrenzen, Sprachverhalten und mindestens ein Beispielartefakt klar dokumentiert sind. Öffne bei größeren Ergänzungen zuerst ein Issue.
