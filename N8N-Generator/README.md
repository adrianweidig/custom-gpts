# n8n Workflow Architect

Lokaler Projektordner für den öffentlichen GPT `n8n Workflow Architect`.

## ChatGPT-Link

https://chatgpt.com/g/g-6a06f5d8d0ac81918ce368d8db8a9bf5-n8n-workflow-architect

## Zweck

Dieser GPT übersetzt natürlichsprachliche Anforderungen in importierbare n8n-Workflow-JSONs. Berücksichtigt werden Betriebsmodell, Dienste, Credentials, Sicherheitsgrenzen, Testbarkeit und Dokumentationsnähe.

## Enthaltene Dateien

- `customgpt_infos.md`: Positionierung, Zielgruppe, Einsatzgebiete und Gesprächsaufhänger.
- `fachwissen.md`: Regeln, Terminologie und Fachlogik rund um n8n, Nodes, Credentials und Sicherheitsgrenzen.
- `systemprompt.md`: Kernverhalten für Analyse, Rückfragen und JSON-Erzeugung.
- `bootloader.md`: kompakte Steuerdatei für die GPT-Hinweise.
- `beispiel.md`: importnahes Muster für einen sicheren n8n-Workflow-Entwurf mit Testdaten.
- `icon.png`: Symbolgrafik für die GPT-Darstellung.

## Typische Nutzung

Geeignet für neue Workflow-Entwürfe, die Sicherheitsprüfung von Automationsideen, Staging-Workflows, Cloud-vs-Self-hosted-Abwägungen und importierbare JSON-Outputs.

## Voraussetzungen

- ChatGPT-Zugang für die direkte Nutzung des öffentlichen GPTs.
- Grundkenntnisse zu n8n, Nodes, Credentials und Zielsystemen.
- Eine n8n-Testinstanz wird empfohlen, bevor erzeugte Workflows produktiv eingesetzt werden.

## Für Repo-Nutzer

Wenn du den GPT lokal nachvollziehen willst, kombiniere `customgpt_infos.md`, `fachwissen.md` und `systemprompt.md`. Für die Live-Nutzung kannst du direkt den ChatGPT-Link öffnen.

## Hinweise

- Importierte Workflows müssen vor produktiver Nutzung mit echten Credentials und Testdaten geprüft werden.
- Platzhalter für Zugangsdaten sind absichtlich vorgesehen und dürfen nicht durch echte Secrets im Repository ersetzt werden.
