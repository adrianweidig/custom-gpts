# Testfall-Generator

Sprachen: [Deutsch](README.md) | [English](README.en.md)

Lokaler Projektordner für einen Custom GPT zur Ableitung strukturierter Testfälle aus Anforderungen, User Stories, Bugreports und Akzeptanzkriterien.

## Status

Konzipiertes GPT-Paket ohne öffentlichen ChatGPT-Link.

## Zweck

Dieser GPT erstellt nachvollziehbare Testfall-Sammlungen mit Vorbedingungen, Testdaten, Schritten, erwarteten Ergebnissen, Randfällen und Risikohinweisen. Er eignet sich für manuelle Tests, Regressionstests und die Vorbereitung automatisierter Tests.

## Enthaltene Dateien

- `customgpt_infos.md`: Positionierung, Zielgruppe, Einsatzgebiete und Einrichtungsinformationen.
- `fachwissen.md`: Testdesign-Regeln, Testarten, Risikoheuristiken und Qualitätskriterien.
- `systemprompt.md`: Hauptlogik für Testfallableitung, Rückfragen, Grenzen und Ausgabeformate.
- `bootloader.md`: kompakter Hinweistext für das Instructions-Feld.
- `beispiel.md`: Muster-Testfallspezifikation aus einer Beispiel-User-Story.

## Typische Nutzung

- Akzeptanzkriterien in Testfälle überführen
- Bugfix-Regressionen planen
- Randfälle und Negativtests ergänzen
- manuelle Tests in klare Tabellen bringen
- Testideen für spätere Automatisierung vorbereiten

## Hinweise

- Der GPT ersetzt keine Ausführung gegen das echte System.
- Testdaten dürfen keine echten Kundendaten, Secrets oder produktiven Personenbezüge enthalten.
