# CustomGPTs

Sammlung mehrerer Custom-GPT-Konfigurationen, Prompt-Artefakte und Begleitdokumente. Das Repository ist so aufgebaut, dass die einzelnen GPTs sowohl direkt ueber ChatGPT genutzt als auch lokal anhand ihrer Prompt- und Wissensdateien nachvollzogen, angepasst und weiterentwickelt werden koennen.

## Oeffentliche ChatGPT-Links

| GPT | ChatGPT-Link | Lokaler Ordner |
|---|---|---|
| PromptForge | https://chatgpt.com/g/g-6a0ac654618c81919f30c2da2be089c8-promptforge | `Promptgenerator` |
| Unterrichtsfolien & Handout Builder | https://chatgpt.com/g/g-6a071be465ac8191b27a4b5fb5789b0a-unterrichtsfolien-handout-builder | `Unterrichtsfolien & Handout Builder` |
| OpenWebUI Model Builder | https://chatgpt.com/g/g-6a070eda8fdc81918ab61d4c4f1aa136-openwebui-model-builder | `OpenWebUI Model Builder` |
| n8n Workflow Architect | https://chatgpt.com/g/g-6a06f5d8d0ac81918ce368d8db8a9bf5-n8n-workflow-architect | `N8N-Generator` |
| CustomGPT Studio | https://chatgpt.com/g/g-6a06ef9be6fc819197d7b815debd0f57-customgpt-studio | `Custom-GPT-Generator` |
| KI-Integration Sicherheitsberater | https://chatgpt.com/g/g-6a06d83ba4808191bffb12f7aa4b043b-ki-integration-sicherheitsberater | `KI-Integration Sicherheitsberater` |
| Praesentationscreator | https://chatgpt.com/g/g-69fdf8ef05c08191bb3a5454c597baa7-prasentationscreator | `Präsentationscreator` |

## Schnellstart

1. Einen GPT in der Tabelle oben oder ueber die Projektuebersicht unten auswaehlen.
2. Die jeweilige `README.md` im Unterordner lesen.
3. Danach `customgpt_infos.md`, `systemprompt.md` und die Fachdateien des Projekts durchgehen.
4. Fuer die direkte Live-Nutzung den passenden ChatGPT-Link oeffnen.

## Projektuebersicht

### Promptgenerator

Lokaler Projektordner fuer den oeffentlichen GPT `PromptForge`. Schwerpunkt ist die Erzeugung direkt nutzbarer Markdown-Promptvorlagen fuer ChatGPT, Custom GPTs, OpenWebUI, lokale LLMs und API-Workflows.

### Unterrichtsfolien & Handout Builder

Projekt fuer die Erstellung didaktisch aufbereiteter Unterrichtspraesentationen und druckbarer Handouts aus Curricula, Folien, Fachquellen und Notizen.

### OpenWebUI Model Builder

Projekt fuer die Konzeption vollstaendiger OpenWebUI-Modellpakete inklusive `model.json`, Prompt-Dateien, Wissensbasis und optionaler Begleitdateien.
Enthaelt zusaetzlich die Sammlung `Problemfälle/` mit offline-orientierten Problemfall-Briefings fuer typische Aufgabenmodelle.

### N8N-Generator

Projekt fuer importierbare n8n-Workflow-JSONs inklusive Sicherheitsannahmen, Credential-Platzhaltern und Testhinweisen.

### Custom-GPT-Generator

Projekt fuer den Entwurf vollstaendiger Custom-GPT-Pakete mit Struktur, Wissensbasis, Systemprompt und Bootloader.

### KI-Integration Sicherheitsberater

Projekt fuer sicherheitsbewusste Beratung zu KI-Einfuehrung, Automatisierung, Agenten, Betriebsmodellen und Governance.

### Präsentationscreator

Projekt fuer browserbasierte, praesentationsfaehige Web-Praesentationen mit Storyline, Animationen und moderner Bedienlogik.

## Ordnerstruktur

- `Custom-GPT-Generator/`: GPT zur Erstellung vollstaendiger Custom-GPT-Projektpakete.
- `KI-Integration Sicherheitsberater/`: Beratungs-GPT fuer sichere KI- und Automatisierungseinfuehrung.
- `N8N-Generator/`: GPT fuer importierbare n8n-Workflow-JSONs.
- `OpenWebUI Model Builder/`: GPT fuer OpenWebUI-Aufgabenmodelle und Modellpakete.
- `OpenWebUI Model Builder/Problemfälle/`: kuratierte Briefings fuer haeufige OpenWebUI-Einsatzfaelle.
- `Promptgenerator/`: GPT fuer robuste Promptvorlagen, oeffentlich als `PromptForge`.
- `Präsentationscreator/`: GPT fuer hochwertige browserbasierte Praesentationen.
- `Unterrichtsfolien & Handout Builder/`: GPT fuer Unterrichtsfolien und druckbare Handouts.

## Struktur pro GPT

Die Unterordner enthalten je nach GPT unter anderem:

- `README.md` mit Zweck, Link und Dateierklaerung
- `systemprompt.md`
- `bootloader.md`
- `fachwissen.md`
- `customgpt_infos.md`
- `icon.png`
- weitere spezialisierte Dateien je nach Projekt

Nicht jeder Ordner enthaelt exakt alle Dateien. Manche Projekte haben zusaetzliche Spezialdateien wie `fulldoc.md`, `layoutrichtlinien.md` oder Problemfall-Sammlungen.

## Hinweis

Das Repository ist fuer Prompt-, Doku- und Konfigurationsartefakte gedacht. Produktive Secrets, Tokens oder Zugangsdaten gehoeren nicht in dieses Repository.
