# CustomGPTs

Sprachen: [Deutsch](README.md) | [English](README.en.md)

> **Maintenance-Status seit 24. Mai 2026:** Dieses Repository ist als öffentliche Referenz- und Vorlagensammlung abgeschlossen. Es findet keine aktive Weiterentwicklung mehr statt. Inhalte bleiben nutzbar, Issues und Pull Requests werden nicht verbindlich bearbeitet.

![CustomGPTs repository overview](docs/assets/repository-hero.png)

[![Repository Health](https://github.com/adrianweidig/custom-gpts/actions/workflows/repository-health.yml/badge.svg)](https://github.com/adrianweidig/custom-gpts/actions/workflows/repository-health.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/adrianweidig/custom-gpts)](https://github.com/adrianweidig/custom-gpts/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/adrianweidig/custom-gpts)](https://github.com/adrianweidig/custom-gpts/pulls)

Kuratiertes Repository für öffentliche Custom-GPT-Konfigurationen, Systemprompts, Wissensdateien, Bootloader, Icons und Begleitdokumentation.

Dieses Projekt ist kein installierbares Softwarepaket und keine zentrale Anwendung. Es ist eine nachvollziehbare Sammlung von GPT-Artefakten, die direkt über ChatGPT genutzt oder lokal geprüft, angepasst und weiterentwickelt werden können.

## Schnellzugriff

- [GPT-Übersicht](#öffentliche-chatgpt-links)
- [Repository-Struktur](#repository-struktur)
- [Lokale Nutzung](#lokale-nutzung)
- [Internationalisierung](#internationalisierung)
- [Qualitätschecks](#qualitätschecks)
- [Mitwirken](CONTRIBUTING.md)
- [English README](README.en.md)
- [Security Policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Changelog](CHANGELOG.md)

## Für wen ist dieses Repository gedacht?

- Menschen, die robuste Custom-GPT-Konfigurationen nachvollziehen oder weiterentwickeln möchten.
- Teams, die Prompt-, Wissens- und Bootloader-Artefakte sauber versionieren wollen.
- Nutzerinnen und Nutzer, die die öffentlichen GPTs direkt über ChatGPT einsetzen möchten.
- Maintainer, die einzelne GPT-Pakete fachlich prüfen, konsistent halten oder kollaborativ verbessern wollen.

## Was ist enthalten?

| Bereich | Zweck |
|---|---|
| Prompt- und Systemdateien | Rollenlogik, Grenzen, Antwortqualität und Steuerverhalten der GPTs |
| Wissensdateien | Fachliche Regeln, Qualitätsmaßstäbe und Strukturwissen |
| Bootloader | Kompakte Hinweise für GPT-Instructions |
| GPT-Metadaten | Positionierung, Zielgruppen, Gesprächsaufhänger und Einsatzgebiete |
| Icons | Symbolgrafiken für einzelne GPTs, sofern vorhanden |
| Problemfälle | Offline-orientierte Briefings für typische OpenWebUI-Modellaufgaben |
| Beispielartefakte | Musterantworten oder fertige Beispiel-Dateien wie `beispiel.md`, `beispiel.py` oder `beispiel_test.py` |

## Öffentliche ChatGPT-Links

| GPT | ChatGPT-Link | Lokaler Ordner |
|---|---|---|
| PromptForge | https://chatgpt.com/g/g-6a0ac654618c81919f30c2da2be089c8-promptforge | [`Promptgenerator`](Promptgenerator/README.md) |
| Unterrichtsfolien & Handout Builder | https://chatgpt.com/g/g-6a071be465ac8191b27a4b5fb5789b0a-unterrichtsfolien-handout-builder | [`Unterrichtsfolien & Handout Builder`](Unterrichtsfolien%20%26%20Handout%20Builder/README.md) |
| OpenWebUI Model Builder | https://chatgpt.com/g/g-6a070eda8fdc81918ab61d4c4f1aa136-openwebui-model-builder | [`OpenWebUI Model Builder`](OpenWebUI%20Model%20Builder/README.md) |
| n8n Workflow Architect | https://chatgpt.com/g/g-6a06f5d8d0ac81918ce368d8db8a9bf5-n8n-workflow-architect | [`N8N-Generator`](N8N-Generator/README.md) |
| CustomGPT Studio | https://chatgpt.com/g/g-6a06ef9be6fc819197d7b815debd0f57-customgpt-studio | [`Custom-GPT-Generator`](Custom-GPT-Generator/README.md) |
| KI-Integration Sicherheitsberater | https://chatgpt.com/g/g-6a06d83ba4808191bffb12f7aa4b043b-ki-integration-sicherheitsberater | [`KI-Integration Sicherheitsberater`](KI-Integration%20Sicherheitsberater/README.md) |
| Präsentationscreator | https://chatgpt.com/g/g-69fdf8ef05c08191bb3a5454c597baa7-prasentationscreator | [`Präsentationscreator`](Präsentationscreator/README.md) |

## Weitere konzipierte GPT-Pakete

Diese Pakete sind lokal vollständig vorbereitet, haben aber noch keinen öffentlichen ChatGPT-Link.

| GPT-Paket | Schwerpunkt | Lokaler Ordner |
|---|---|---|
| Code Review Coach | Code-Review, Refactoring, Security- und Testlückenanalyse | [`Code-Review Refactoring Coach`](Code-Review%20Refactoring%20Coach/README.md) |
| TestCase Studio | Testfallableitung aus Anforderungen, User Stories und Bugreports | [`Testfall-Generator`](Testfall-Generator/README.md) |
| Research Briefing Builder | Recherche-Briefings, Quellenvergleich und Unsicherheitsmarkierung | [`Research Briefing Builder`](Research%20Briefing%20Builder/README.md) |
| Decision Memo Builder | Entscheidungsvorlagen, Optionenvergleiche und Management-Memos | [`Entscheidungsvorlagen Builder`](Entscheidungsvorlagen%20Builder/README.md) |

## Repository-Struktur

| Pfad | Inhalt |
|---|---|
| [`Code-Review Refactoring Coach/`](Code-Review%20Refactoring%20Coach/README.md) | GPT-Paket für Code-Review, Refactoring und Tests inklusive Beispielcode |
| [`Custom-GPT-Generator/`](Custom-GPT-Generator/README.md) | Artefakte für `CustomGPT Studio`, einen GPT zum Entwurf vollständiger Custom-GPT-Pakete |
| [`Entscheidungsvorlagen Builder/`](Entscheidungsvorlagen%20Builder/README.md) | GPT-Paket für Entscheidungsvorlagen, Optionenvergleiche und Management-Memos |
| [`KI-Integration Sicherheitsberater/`](KI-Integration%20Sicherheitsberater/README.md) | Sicherheits- und Governance-GPT für KI-Einführung, Automatisierung und Betriebsmodelle |
| [`N8N-Generator/`](N8N-Generator/README.md) | GPT für importierbare n8n-Workflow-JSONs mit Sicherheitsannahmen und Testhinweisen |
| [`OpenWebUI Model Builder/`](OpenWebUI%20Model%20Builder/README.md) | GPT für OpenWebUI-Aufgabenmodelle, Modellpakete und Wissensdateien |
| [`OpenWebUI Model Builder/Problemfälle/`](OpenWebUI%20Model%20Builder/Problemf%C3%A4lle/README.md) | Kuratierte Briefings für häufige OpenWebUI-Einsatzfälle |
| [`Promptgenerator/`](Promptgenerator/README.md) | Artefakte für `PromptForge`, einen GPT für robuste Promptvorlagen |
| [`Präsentationscreator/`](Präsentationscreator/README.md) | GPT für browserbasierte, präsentationsfähige Web-Präsentationen |
| [`Research Briefing Builder/`](Research%20Briefing%20Builder/README.md) | GPT-Paket für Recherche-Briefings und Quellenbewertung |
| [`Testfall-Generator/`](Testfall-Generator/README.md) | GPT-Paket für Testfall-Design und QA-Vorbereitung |
| [`Unterrichtsfolien & Handout Builder/`](Unterrichtsfolien%20%26%20Handout%20Builder/README.md) | GPT für Unterrichtsfolien und druckbare Handouts |

## Lokale Nutzung

Für die meisten Inhalte ist keine Installation nötig.

1. Repository klonen oder lokal öffnen.
2. Einen GPT-Ordner aus der Übersicht auswählen.
3. Zuerst die jeweilige `README.md` lesen.
4. Danach `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` und vorhandene `beispiel.*` Dateien gemeinsam prüfen.
5. Für die direkte Live-Nutzung den passenden ChatGPT-Link aus der Tabelle öffnen.

Die einzelnen Artefakte haben unterschiedliche Rollen:

| Datei | Funktion |
|---|---|
| `customgpt_infos.md` | Name, Positionierung, Zielgruppe, Einsatzgebiete und Konfigurationshinweise |
| `systemprompt.md` | Hauptlogik für Rolle, Verhalten, Grenzen und Ausgabequalität |
| `fachwissen.md` | Fachliche Regeln und Strukturwissen |
| `bootloader.md` | Kompakter Hinweistext für GPT-Instructions |
| `beispiel.md` oder `beispiel.*` | Musterantwort, Musterdatei oder mehrere Beispielartefakte für die erwartete Ausgabequalität |
| `icon.png` | Symbolgrafik, falls im jeweiligen Ordner vorhanden |

## Internationalisierung

Deutsch ist die Standardsprache des Repositorys. GitHub zeigt die normale Repository-Ansicht nicht automatisch abhängig von der Besuchersprache an; deshalb sind Sprachversionen explizit über Dateien und Links organisiert.

- [`README.md`](README.md) ist die deutsche Startseite.
- [`README.en.md`](README.en.md) ist die englische Startseite.
- [`docs/de/`](docs/de/index.md) enthält die deutsche Dokumentationsroute.
- [`docs/en/`](docs/en/index.md) enthält die englische Dokumentationsroute.
- Englische Paketübersichten liegen als `README.en.md` neben den deutschen Paket-READMEs, sofern der Ordner für internationale Nutzer relevant ist.
- Deutsch bleibt der stabile Fallback, wenn keine Sprache zuverlässig ermittelt oder gewünscht wird.
- UTF-8 bleibt verbindlich; Umlaute, Akzente, nicht-lateinische Zeichen, Emojis und bidirektionale Texte dürfen nicht durch ASCII-Umschreibungen ersetzt werden.

Die GPT-Artefakte selbst bleiben fachliche Quellartefakte. Viele GPTs reagieren auf die Sprache der Nutzeranfrage; technische IDs, Dateinamen, Modellparameter und Importformate werden dabei nicht übersetzt.

## Qualitätsgrenzen

- Produktive Secrets, Tokens, Zugangsdaten, personenbezogene Daten und vertrauliche Kundendaten gehören nicht in dieses Repository.
- GPT-Artefakte müssen vor produktiver Nutzung fachlich geprüft werden, insbesondere bei Unterricht, Sicherheit, Automatisierung, Datenschutz und OpenWebUI-Modellimporten.
- Technische Slugs, Modell-IDs, Dateinamen, URLs und Parameter werden nicht automatisch eingedeutscht.
- Externe Medien, Schriften, Skripte und veröffentlichte Assets müssen vor Nutzung auf Lizenz, Datenschutz und Verfügbarkeit geprüft werden.

## Entwicklung

Es gibt keinen zentralen Dev-Server, keinen Paketmanager und keinen Build-Prozess. Änderungen sind in der Regel Markdown-, Prompt- oder Asset-Arbeiten.

Empfohlener Arbeitsablauf:

1. Vor Änderungen `git status --short --branch` prüfen.
2. Nur den betroffenen GPT-Unterordner ändern.
3. Zusammengehörige Dateien eines GPTs gemeinsam betrachten.
4. Beispielartefakte als Qualitätsanker pflegen: `beispiel.md` für Musterantworten, `beispiel.*` für konkrete Code- oder Dateiergebnisse.
5. Keine echten Credentials, API-Keys oder Kundendaten in Beispiele übernehmen.
6. Lokale Links, Tabellen, Überschriften und UTF-8-Umlaute prüfen.

## Qualitätschecks

Sichere lokale Prüfungen:

```powershell
git status --short --branch
git diff --check
```

Der GitHub-Workflow [`Repository Health`](.github/workflows/repository-health.yml) prüft zusätzlich, ob zentrale Community-Dateien vorhanden sind und ob lokale Markdown-Links sowie referenzierte Bilder auf vorhandene Dateien zeigen.

## Dokumentation

- [Contribution Guide](CONTRIBUTING.md)
- [Contribution Guide, English](CONTRIBUTING.en.md)
- [Security Policy](SECURITY.md)
- [Security Policy, English](SECURITY.en.md)
- [Support](SUPPORT.md)
- [Support, English](SUPPORT.en.md)
- [Changelog](CHANGELOG.md)
- [Changelog, English](CHANGELOG.en.md)
- [Dokumentation Deutsch](docs/de/index.md)
- [Documentation English](docs/en/index.md)
- [FAQ](docs/de/FAQ.md)
- [Release-Prozess](docs/de/RELEASE_PROCESS.md)
- [Maintainer-Checkliste](docs/de/MAINTAINER_CHECKLIST.md)
- [Internationalisierung](docs/de/I18N.md)
- [Codex Project Readiness](CODEX_PROJECT_READINESS.md)

## Mitwirken

Dieses Repository wird seit dem 24. Mai 2026 nicht mehr aktiv weiterentwickelt. Beiträge können weiterhin als Hinweise, Forks oder Pull Requests eingereicht werden, es gibt aber keine verbindliche Zusage für Review, Merge oder Support.

Geeignete Hinweise oder Beiträge sind zum Beispiel:

- Korrekturen an Dokumentation, Links, Tabellen oder Begriffen
- Verbesserungen an Prompt-Konsistenz und Struktur
- fachlich begründete Ergänzungen zu Wissensdateien
- neue oder verbesserte Problemfall-Briefings
- Hinweise auf unklare Sicherheits-, Datenschutz- oder Lizenzstellen

Details stehen in [`CONTRIBUTING.md`](CONTRIBUTING.md). Bitte melde Sicherheitsprobleme nicht öffentlich als Issue, sondern beachte [`SECURITY.md`](SECURITY.md).

## Lizenz

Dieses Repository steht unter der [MIT-Lizenz](LICENSE).

Die Lizenzentscheidung ist keine Rechtsberatung. Bei kommerziell wichtigen GPT-Paketen, Markenfragen, Trainingsdaten, fremden Quellen oder veröffentlichten Assets sollte die Lizenzlage zusätzlich rechtlich geprüft werden.

## Status

Das Repository ist öffentlich, GitHub-synchron und als kuratierte Artefaktsammlung nutzbar. Seit dem 24. Mai 2026 gilt es als Referenzstand ohne aktive Weiterentwicklung. Der aktuelle technische Readiness-Stand ist in [`CODEX_PROJECT_READINESS.md`](CODEX_PROJECT_READINESS.md) dokumentiert.
