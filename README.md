# CustomGPTs

Sammlung mehrerer Custom-GPT-Konfigurationen, Prompt-Artefakte und Begleitdokumente. Das Repository ist so aufgebaut, dass die einzelnen GPTs sowohl direkt über ChatGPT genutzt als auch lokal anhand ihrer Prompt- und Wissensdateien nachvollzogen, angepasst und weiterentwickelt werden können.

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

1. Einen GPT in der Tabelle oben oder über die Projektübersicht unten auswählen.
2. Die jeweilige `README.md` im Unterordner lesen.
3. Danach `customgpt_infos.md`, `systemprompt.md` und die Fachdateien des Projekts durchgehen.
4. Für die direkte Live-Nutzung den passenden ChatGPT-Link öffnen.

## Voraussetzungen

- Für die Live-Nutzung wird ein ChatGPT-Konto benötigt.
- Für die lokale Prüfung reicht ein Markdown-Editor oder ein Texteditor.
- Für eigene Anpassungen sollten die jeweiligen `README.md`-, `systemprompt.md`- und Fachdateien gemeinsam betrachtet werden.
- Secrets, Tokens und Zugangsdaten dürfen nicht in dieses Repository eingetragen werden.

## Projektübersicht

### Promptgenerator

Lokaler Projektordner für den öffentlichen GPT `PromptForge`. Schwerpunkt ist die Erzeugung direkt nutzbarer Markdown-Promptvorlagen für ChatGPT, Custom GPTs, OpenWebUI, lokale LLMs und API-Workflows.

### Unterrichtsfolien & Handout Builder

Projekt für die Erstellung didaktisch aufbereiteter Unterrichtspräsentationen und druckbarer Handouts aus Curricula, Folien, Fachquellen und Notizen.

### OpenWebUI Model Builder

Projekt für die Konzeption vollständiger OpenWebUI-Modellpakete inklusive `model.json`, Prompt-Dateien, Wissensbasis und optionaler Begleitdateien.
Enthält zusätzlich die Sammlung `Problemfälle/` mit offline-orientierten Problemfall-Briefings für typische Aufgabenmodelle.

### N8N-Generator

Projekt für importierbare n8n-Workflow-JSONs inklusive Sicherheitsannahmen, Credential-Platzhaltern und Testhinweisen.

### Custom-GPT-Generator

Projekt für den Entwurf vollständiger Custom-GPT-Pakete mit Struktur, Wissensbasis, Systemprompt und Bootloader.

### KI-Integration Sicherheitsberater

Projekt für sicherheitsbewusste Beratung zu KI-Einführung, Automatisierung, Agenten, Betriebsmodellen und Governance.

### Präsentationscreator

Projekt für browserbasierte, präsentationsfähige Web-Präsentationen mit Storyline, Animationen und moderner Bedienlogik.

## Ordnerstruktur

- `Custom-GPT-Generator/`: GPT zur Erstellung vollständiger Custom-GPT-Projektpakete.
- `KI-Integration Sicherheitsberater/`: Beratungs-GPT für sichere KI- und Automatisierungseinführung.
- `N8N-Generator/`: GPT für importierbare n8n-Workflow-JSONs.
- `OpenWebUI Model Builder/`: GPT für OpenWebUI-Aufgabenmodelle und Modellpakete.
- `OpenWebUI Model Builder/Problemfälle/`: kuratierte Briefings für häufige OpenWebUI-Einsatzfälle.
- `Promptgenerator/`: GPT für robuste Promptvorlagen, öffentlich als `PromptForge`.
- `Präsentationscreator/`: GPT für hochwertige browserbasierte Präsentationen.
- `Unterrichtsfolien & Handout Builder/`: GPT für Unterrichtsfolien und druckbare Handouts.

## Struktur pro GPT

Die Unterordner enthalten je nach GPT unter anderem:

- `README.md` mit Zweck, Link und Dateierklärung
- `systemprompt.md`
- `bootloader.md`
- `fachwissen.md`
- `customgpt_infos.md`
- `icon.png`
- weitere spezialisierte Dateien je nach Projekt

Nicht jeder Ordner enthält exakt alle Dateien. Manche Projekte haben zusätzliche Spezialdateien wie `fulldoc.md`, `layoutrichtlinien.md` oder Problemfall-Sammlungen.

## Hinweis

Das Repository ist für Prompt-, Doku- und Konfigurationsartefakte gedacht. Produktive Secrets, Tokens oder Zugangsdaten gehören nicht in dieses Repository.
