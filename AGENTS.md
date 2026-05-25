# AGENTS.md

## Projektüberblick

Dieses Repository enthält Custom-GPT-Konfigurationen, Systemprompts, Wissensdateien, Bootloader, Icons und Begleitdokumentation. Es ist primär ein Markdown-/Prompt-Artefakt-Repository und keine zentrale Softwareanwendung.

## Wichtige Verzeichnisse

- `Custom-GPT-Generator/`: Artefakte für `CustomGPT Studio`.
- `Code-Review Refactoring Coach/`: Code-Review-, Refactoring- und Testbeispiel-GPT.
- `Entscheidungsvorlagen Builder/`: Entscheidungs- und Management-Memo-GPT.
- `KI-Integration Sicherheitsberater/`: Sicherheits- und Governance-GPT.
- `N8N-Generator/`: n8n-Workflow-GPT.
- `OpenWebUI Model Builder/`: OpenWebUI-Modellpaket-GPT.
- `OpenWebUI Model Builder/Problemfälle/`: offline-first Problemfall-Briefings.
- `Promptgenerator/`: Artefakte für `PromptForge`.
- `Präsentationscreator/`: Web-Präsentations-GPT.
- `Research Briefing Builder/`: Recherche-, Quellen- und Briefing-GPT.
- `Testfall-Generator/`: Testfall- und QA-Vorbereitungs-GPT.
- `Unterrichtsfolien & Handout Builder/`: Unterrichtsfolien- und Handout-GPT.

## Installation

Es gibt keinen zentralen Installationsschritt. Die meisten Dateien sind Markdown- und Asset-Artefakte.

## Entwicklungsbefehle

Es gibt keinen Dev-Server und keinen zentralen Build. Nützliche Prüfungen:

```powershell
git status --short --branch
git diff --check
python scripts/validate_repository_i18n.py
```

Der GitHub-Workflow `Repository Health` prüft zentrale Community-Dateien, i18n-Pflichtdateien, lokale Markdown-Links, Bildpfade, UTF-8 und Unicode-Fixtures.

## Tests, Build, Linting und Formatierung

- Kein zentrales Testframework vorhanden.
- Kein Paketmanager oder Lockfile vorhanden.
- Der vorhandene Repository-Health-Workflow ist ein Dokumentations- und Linkcheck, kein fachlicher Test der GPT-Ausgaben.
- Kein automatisches globales Formatting ausführen.
- Markdown-Änderungen manuell auf Überschriften, Tabellen, Links, UTF-8-Umlaute und fachliche Konsistenz prüfen.

## Coding- und Dokumentationskonventionen

- Kleine, zielgenaue Änderungen mit minimalem Diff.
- Deutsche Fließtexte mit echten UTF-8-Umlauten schreiben.
- Deutsch ist die Standardsprache. Englische Alternativdateien wie `README.en.md`, `CONTRIBUTING.en.md`, `CHANGELOG.en.md`, `SECURITY.en.md`, `SUPPORT.en.md`, `CODE_OF_CONDUCT.en.md` und `docs/en/*` konsistent halten.
- Zentrale deutsche Dokumentation liegt unter `docs/de/`; englische Dokumentation liegt unter `docs/en/`. Top-Level-README und Community-Dateien bleiben deutsch.
- Jede zentrale mehrsprachige Markdown-Datei beginnt mit konkreten Sprachlinks.
- Keine ASCII-Umschreibungen deutscher Umlaute in Fließtexten verwenden, z. B. `vollstaendig`, `fuer`, `ueber`, `pruefen`, `unterstuetzt` statt `vollständig`, `für`, `über`, `prüfen`, `unterstützt`.
- Technische Slugs, IDs, Dateinamen, URLs und Modellparameter nicht blind eindeutschen.
- Dateien als UTF-8 ohne unnötige Encoding-Wechsel pflegen; `.editorconfig` und `.gitattributes` sind dafür verbindlich.
- Prompt-Artefakte eines GPTs gemeinsam betrachten: `README.md`, `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` und vorhandene `beispiel.*` Dateien.
- Neue oder grundlegend überarbeitete GPT-Pakete sollen mindestens ein Beispielartefakt enthalten: `beispiel.md` für Musterantworten oder passende `beispiel.*` Dateien für konkrete Code-, JSON-, HTML- oder Dokumentartefakte.
- Beispielartefakte müssen vollständig, realistisch und frei von echten Secrets, Kundendaten oder personenbezogenen Daten sein.
- Öffentliche Community-Dateien wie `CONTRIBUTING.md`, `CONTRIBUTING.en.md`, `SECURITY.md`, `SECURITY.en.md`, `SUPPORT.md`, `SUPPORT.en.md`, `CHANGELOG.md`, `CHANGELOG.en.md`, `.github/ISSUE_TEMPLATE/*` und `.github/PULL_REQUEST_TEMPLATE.md` konsistent halten, wenn sich Repository-Prozesse ändern.
- Keine großflächigen Umformulierungen, wenn dadurch Prompt-Verhalten oder fachliche Bedeutung unklar verändert würde.
- Icons und binäre Assets nicht ohne klaren Auftrag verändern.

## Git-Regeln

- Vor Änderungen `git status --short --branch` prüfen.
- Nutzer- oder Fremdänderungen nicht überschreiben.
- Keine destruktiven Git-Befehle ohne ausdrücklichen Auftrag, insbesondere kein `reset`, `checkout --`, `restore`, `clean`, Rebase oder Force-Push.
- Pull, Push, Merge und Rebase nicht ungefragt ausführen.
- Unklare Altlasten dokumentieren statt löschen.

## Sicherheit und Secrets

- Keine Secrets, Tokens, API-Keys, Passwörter, echten Credentials oder produktiven URLs eintragen.
- Platzhalter müssen offensichtlich sein, zum Beispiel `YOUR_API_KEY`.
- Keine personenbezogenen Daten, Kundendaten oder vertraulichen Architekturdetails ergänzen.
- Sicherheits-, Datenschutz- und Rechtsaussagen als prüfpflichtig behandeln, wenn sie produktive Nutzung betreffen.
- Bei Security- oder Readiness-Arbeiten GitHub-Alerts über Code Scanning, Dependabot und Secret Scanning prüfen, soweit API-Zugriff vorhanden ist.
- Für lokale Secret-Prüfungen mindestens eine gezielte Muster- oder Scanner-Prüfung durchführen; gefundene Werte nie vollständig ausgeben.
- GitHub-Actions-Workflows mit minimalen `permissions`, begrenzter Laufzeit und ohne unnötig persistierte Credentials konfigurieren.
- CodeQL oder andere Code-Scanner nur ergänzen, wenn das Repository tatsächlich auswertbare Anwendungssprache oder Build-Artefakte enthält.

## Regeln für Datei-Löschungen

Nur löschen, wenn eindeutig klar ist, dass die Datei generiert, temporär oder nicht mehr benötigt ist. Vor dem Löschen prüfen:

- Wird die Datei in Markdown, Skripten oder Konfigurationen referenziert?
- Gehört sie zu einem Custom-GPT-Paket, Icon, Problemfall, Export oder Spezialdokument?
- Könnte sie für Import, Veröffentlichung, historische Nachvollziehbarkeit oder Nutzerverständnis relevant sein?

Bei Unsicherheit: nicht löschen, sondern im Abschlussbericht als prüfpflichtig markieren.

## Definition of Done

Eine Änderung ist fertig, wenn:

- der Git-Diff klein und nachvollziehbar ist,
- keine Funktionalität absichtlich verändert wurde,
- relevante Markdown- und Prompt-Dateien konsistent bleiben,
- sinnvolle Checks ausgeführt oder nachvollziehbar begründet ausgelassen wurden,
- keine Secrets oder sensiblen Daten hinzugefügt wurden,
- der finale Bericht geänderte Dateien, Checks, Risiken und offene Punkte nennt.

## Prüfpflicht vor Abschluss

Vor dem Abschluss ausführen oder begründet auslassen:

```powershell
git diff --check
python scripts/validate_repository_i18n.py
git status --short --branch
```

Zusätzlich README, `AGENTS.md`, Lizenzhinweis und `.gitignore` auf Konsistenz prüfen, wenn diese Dateien geändert wurden.
