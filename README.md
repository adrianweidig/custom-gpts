# CustomGPTs

Sammlung mehrerer Custom-GPT-Konfigurationen, Prompt-Artefakte und Begleitdokumente. Die einzelnen GPTs können direkt über ChatGPT genutzt oder lokal anhand ihrer Prompt-, Wissens- und Konfigurationsdateien nachvollzogen, angepasst und weiterentwickelt werden.

## Status

Dieses Repository ist ein kuratiertes Dokumentations- und Prompt-Artefakt-Repository. Es ist kein installierbares Softwarepaket und enthält keine zentrale Anwendung mit Build-Prozess. Ein einzelnes Hilfsskript im Ordner `Präsentationscreator/` erzeugt ein lokales, ignoriertes Workshop-Paket.

Produktive Secrets, Tokens, Zugangsdaten, personenbezogene Daten und vertrauliche Kundendaten gehören nicht in dieses Repository.

## Öffentliche ChatGPT-Links

| GPT | ChatGPT-Link | Lokaler Ordner |
|---|---|---|
| PromptForge | https://chatgpt.com/g/g-6a0ac654618c81919f30c2da2be089c8-promptforge | `Promptgenerator` |
| Unterrichtsfolien & Handout Builder | https://chatgpt.com/g/g-6a071be465ac8191b27a4b5fb5789b0a-unterrichtsfolien-handout-builder | `Unterrichtsfolien & Handout Builder` |
| OpenWebUI Model Builder | https://chatgpt.com/g/g-6a070eda8fdc81918ab61d4c4f1aa136-openwebui-model-builder | `OpenWebUI Model Builder` |
| n8n Workflow Architect | https://chatgpt.com/g/g-6a06f5d8d0ac81918ce368d8db8a9bf5-n8n-workflow-architect | `N8N-Generator` |
| CustomGPT Studio | https://chatgpt.com/g/g-6a06ef9be6fc819197d7b815debd0f57-customgpt-studio | `Custom-GPT-Generator` |
| KI-Integration Sicherheitsberater | https://chatgpt.com/g/g-6a06d83ba4808191bffb12f7aa4b043b-ki-integration-sicherheitsberater | `KI-Integration Sicherheitsberater` |
| Präsentationscreator | https://chatgpt.com/g/g-69fdf8ef05c08191bb3a5454c597baa7-prasentationscreator | `Präsentationscreator` |

## Schnellstart

1. Einen GPT in der Tabelle oben oder über die Projektübersicht auswählen.
2. Die jeweilige `README.md` im Unterordner lesen.
3. Danach `customgpt_infos.md`, `systemprompt.md` und die Fachdateien des Projekts prüfen.
4. Für die direkte Live-Nutzung den passenden ChatGPT-Link öffnen.

## Projektübersicht

### Promptgenerator

Lokaler Projektordner für den öffentlichen GPT `PromptForge`. Schwerpunkt ist die Erzeugung direkt nutzbarer Markdown-Promptvorlagen für ChatGPT, Custom GPTs, OpenWebUI, lokale LLMs und API-Workflows.

### Unterrichtsfolien & Handout Builder

Projekt für die Erstellung didaktisch aufbereiteter Unterrichtspräsentationen und druckbarer Handouts aus Curricula, Folien, Fachquellen und Notizen.

### OpenWebUI Model Builder

Projekt für die Konzeption vollständiger OpenWebUI-Modellpakete inklusive `model.json`, Prompt-Dateien, Wissensbasis und optionaler Begleitdateien. Enthält zusätzlich die Sammlung `Problemfälle/` mit offline-orientierten Problemfall-Briefings für typische Aufgabenmodelle.

### N8N-Generator

Projekt für importierbare n8n-Workflow-JSONs inklusive Sicherheitsannahmen, Credential-Platzhaltern und Testhinweisen.

### Custom-GPT-Generator

Projekt für den Entwurf vollständiger Custom-GPT-Pakete mit Struktur, Wissensbasis, Systemprompt und Bootloader.

### KI-Integration Sicherheitsberater

Projekt für sicherheitsbewusste Beratung zu KI-Einführung, Automatisierung, Agenten, Betriebsmodellen und Governance.

### Präsentationscreator

Projekt für browserbasierte, präsentationsfähige Web-Präsentationen mit Storyline, Animationen und moderner Bedienlogik. Der Ordner enthält zusätzlich das Python-Skript `generate_workshop_package.py`, das ein lokales Workshop-Paket nach `Präsentationscreator/workshop-ki-offline/` erzeugt. Dieser Ausgabeordner ist absichtlich ignoriert.

## Voraussetzungen

- ChatGPT-Konto für die direkte Nutzung der öffentlichen GPTs.
- Markdown-Editor oder Texteditor für lokale Anpassungen.
- Python 3, falls das Hilfsskript `Präsentationscreator/generate_workshop_package.py` geprüft oder ausgeführt werden soll.
- Fachliche Prüfung vor produktivem Einsatz, insbesondere bei Unterricht, Sicherheit, Automatisierung, Datenschutz und OpenWebUI-Modellimporten.

## Installation

Für die meisten Inhalte ist keine Installation nötig. Das Repository kann direkt als Markdown- und Asset-Sammlung genutzt werden.

Für das Python-Hilfsskript sind aktuell keine externen Python-Abhängigkeiten dokumentiert; es nutzt Standardbibliotheken.

## Lokale Entwicklung

Empfohlener Arbeitsablauf:

1. Nur den betroffenen GPT-Unterordner ändern.
2. `README.md`, `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md` und `bootloader.md` gemeinsam auf Konsistenz prüfen.
3. Dateinamen und technische IDs nur bewusst ändern, weil sie in Prompt- oder Exportartefakten referenziert sein können.
4. Keine echten Credentials, API-Keys oder Kundendaten in Beispiele übernehmen.

## Build, Tests und Checks

Es gibt keinen zentralen Build- oder Testprozess. Sinnvolle lokale Prüfungen sind:

```powershell
git status --short --branch
python -m py_compile "Präsentationscreator\generate_workshop_package.py"
```

Für Markdown-Dateien sollten zusätzlich interne Links, Tabellen, Überschriften, UTF-8-Umlaute und sichtbare Platzhalter geprüft werden. Wenn ein Workshop-Paket erzeugt wird, muss das Ergebnis im Browser kontrolliert werden.

## Nutzung

Die Inhalte sind pro GPT getrennt:

- `customgpt_infos.md`: Name, Positionierung, Zielgruppe, Einsatzgebiete und Konfigurationshinweise.
- `systemprompt.md`: Hauptlogik für Rolle, Verhalten, Grenzen und Ausgabequalität.
- `fachwissen.md`: fachliche Regeln und Strukturwissen.
- `bootloader.md`: kompakter Hinweistext für GPT-Instructions.
- `icon.png`: Symbolgrafik, falls im jeweiligen Ordner vorhanden.
- weitere Spezialdateien wie `fulldoc.md`, `layoutrichtlinien.md` oder `Problemfälle/`.

## Ordnerstruktur

- `Custom-GPT-Generator/`: GPT zur Erstellung vollständiger Custom-GPT-Projektpakete.
- `KI-Integration Sicherheitsberater/`: Beratungs-GPT für sichere KI- und Automatisierungseinführung.
- `N8N-Generator/`: GPT für importierbare n8n-Workflow-JSONs.
- `OpenWebUI Model Builder/`: GPT für OpenWebUI-Aufgabenmodelle und Modellpakete.
- `OpenWebUI Model Builder/Problemfälle/`: kuratierte Briefings für häufige OpenWebUI-Einsatzfälle.
- `Promptgenerator/`: GPT für robuste Promptvorlagen, öffentlich als `PromptForge`.
- `Präsentationscreator/`: GPT für hochwertige browserbasierte Präsentationen und lokales Workshop-Hilfsskript.
- `Unterrichtsfolien & Handout Builder/`: GPT für Unterrichtsfolien und druckbare Handouts.

## Wichtige Dateien

- `README.md`: zentrale Einstiegsdokumentation.
- `AGENTS.md`: projektspezifische Arbeitsregeln für Codex und andere Agenten.
- `.gitignore`: lokale Artefakte, Caches, Logs und generierte Workshop-Ausgabe.
- `LICENSE`: Lizenzhinweis für Repository-Inhalte.

## Hinweise für Codex und andere Agenten

- Vor Änderungen den Git-Status und die betroffenen Unterordner prüfen.
- Bestehende Prompt-, Modell- und Dokumentationsartefakte konservativ behandeln.
- Keine erzeugten Modellartefakte, JSON-Exporte, Icons oder Spezialdokumente löschen, solange ihr Zweck nicht eindeutig geklärt ist.
- Bei sprachlichen Korrekturen echte UTF-8-Umlaute verwenden, aber technische Slugs und Dateinamen nicht blind eindeutschen.
- Projektweite Formatierungswellen vermeiden.

## Lizenz

Dieses Repository steht unter der MIT-Lizenz. Siehe `LICENSE`.

Die Lizenzentscheidung ist eine technische Repository-Empfehlung und keine Rechtsberatung. Bei kommerziell wichtigen GPT-Paketen, Markenfragen, Trainingsdaten, fremden Quellen oder veröffentlichten Assets sollte die Lizenzlage zusätzlich rechtlich geprüft werden.
