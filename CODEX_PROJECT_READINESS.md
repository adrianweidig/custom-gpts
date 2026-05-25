# Codex Project Readiness

Sprachen: [Deutsch](CODEX_PROJECT_READINESS.md) | [English](CODEX_PROJECT_READINESS.en.md)

## Zusammenfassung

Das Projekt wurde im aktuellen Arbeitskontext geprüft. Es ist ein arbeitsfähiges Markdown-/Prompt-Artefakt-Repository ohne zentrale Softwareanwendung, ohne Paketmanager und ohne fachliches Testframework. Git und GitHub sind eingerichtet. Für öffentliche Nutzung wurden Community-Dokumentation, Issue-/PR-Vorlagen, ein Repository-Health-Workflow und eine explizite deutsch/englische Dokumentationsstruktur ergänzt.

## Projektroot

`E:\Codex_Workspace\repos\custom-gpts`

Ermittelt über `git rev-parse --show-toplevel`.

## Projekttyp

Dokumentations- und Prompt-Artefakt-Repository für mehrere Custom-GPT-Konfigurationen.

Wichtige Inhalte:

- zentrale Projektdokumentation in `README.md`
- englische Startseite in `README.en.md`
- projektspezifische Codex-Regeln in `AGENTS.md`
- GPT-Unterordner mit `README.md`, `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` und teils Assets
- neue GPT-Unterordner können zusätzlich `beispiel.md` oder passende `beispiel.*` Dateien als Musterartefakte enthalten
- Problemfall-Briefings unter `OpenWebUI Model Builder/Problemfälle/`

## Git-Status

- Repository vorhanden.
- Aktueller Branch: `main`.
- Upstream: `origin/main`.
- Arbeitsbaum war vor der Public-Readiness-Überarbeitung sauber.
- Nach der Überarbeitung enthält der Arbeitsbaum ausschließlich Dokumentations-, GitHub- und Repository-Hygieneänderungen.

## GitHub-Synchronität

- Remote: `https://github.com/adrianweidig/custom-gpts.git`
- GitHub-Repository: `adrianweidig/custom-gpts`
- Sichtbarkeit laut GitHub CLI: `PUBLIC`
- Default-Branch laut GitHub CLI: `main`
- `git fetch --prune origin` erfolgreich.
- Lokale und Remote-Commits waren nach Fetch synchron: `0 0` für `HEAD...origin/main`.
- GitHub CLI ist authentifiziert.

## Abhängigkeiten

Keine zentralen Abhängigkeiten vorhanden.

Nicht gefunden:

- `package.json`
- JavaScript-/Node-Lockfiles
- `pyproject.toml`
- `requirements.txt`
- `Cargo.toml`
- `go.mod`
- Docker- oder Compose-Manifeste

Es ist keine Installation erforderlich.

## Tests und Builds

Es gibt keinen zentralen Build-, fachlichen Test-, Lint- oder Typecheck-Prozess. Als passende lokale Prüfungen wurden bzw. werden verwendet:

- `git diff --check`
- `python scripts/validate_repository_i18n.py`
- `git status --short --branch`
- Repository-Health-Linkcheck für lokale Markdown-Links und zentrale Community-Dateien

Markdown-Inhalte sind manuell und konservativ zu prüfen, wenn fachliche Prompt-Artefakte geändert werden.

## Startfähigkeit

Es gibt keinen Dev-Server und keine zentrale Anwendung. Das Projekt ist direkt über die Markdown- und Asset-Dateien nutzbar.

## Codex-Nutzbarkeit

Codex kann das Projekt sinnvoll bearbeiten:

- `AGENTS.md` enthält klare Projektregeln.
- `README.md` beschreibt Struktur, Nutzung, Arbeitsweise und Community-Prozesse.
- `.gitignore` schließt typische lokale Artefakte, Caches, Logs und `.env`-Dateien aus.
- `.github/` enthält Issue-/PR-Vorlagen und einen Repository-Health-Workflow.
- `docs/de/` und `docs/en/` enthalten explizite mehrsprachige Dokumentationsrouten.
- Die Projektstruktur ist klein und nachvollziehbar.

## Geprüfte alte Pfade

Es wurden Suchtreffer für lokale Pfadmuster und Platzhalter geprüft. Die gefundenen lokalen Pfade sind instruktive Negativbeispiele oder Medienregeln, keine offensichtlich veralteten Projektverweise:

- `Präsentationscreator/systemprompt.md`: Verbot lokaler Medienpfade wie `C:\`, `/mnt/`, `file://`
- `Präsentationscreator/fachwissen.md`: Liste verbotener Ausgaben und lokaler Pfadmuster wie `C:\` oder `/mnt/`
- `Unterrichtsfolien & Handout Builder/layoutrichtlinien.md`: Regel gegen `/mnt/data` und lokale Pfade

Keine Korrektur erforderlich.

## Durchgeführte Änderungen

- `README.md` öffentlichkeitsreif überarbeitet.
- `README.en.md`, englische Community-Dateien, englische Paket-READMEs sowie `docs/de/` und `docs/en/` ergänzt.
- Community-Dateien für Contribution, Security, Support, Code of Conduct und Changelog ergänzt.
- `.github`-Vorlagen, Dependabot-Konfiguration und Repository-Health-Workflow ergänzt.
- `docs/` mit FAQ, Release-Prozess, Maintainer-Checkliste und Hero-SVG ergänzt.
- `scripts/validate_repository_i18n.py` für i18n-, Sprachlink-, Unicode-, UTF-8- und Linkvalidierung ergänzt.
- Social-Preview-PNG ergänzt.
- `.editorconfig` und `.gitattributes` ergänzt.
- `AGENTS.md` an den neuen Repository-Health-Workflow angepasst.
- GitHub-Description, Topics, Discussions, Security-Funktionen und Branch Protection über GitHub CLI/API gesetzt.
- Kuratierter Public-Readiness-Snapshot als GitHub Release vorbereitet.

## Nicht durchgeführte Änderungen

- Keine fachlichen Prompt-Artefakte umformuliert.
- Keine Abhängigkeiten installiert.
- Keine Build-, Test- oder Startskripte ergänzt.
- Kein CodeQL-Workflow ergänzt, weil das Repository aktuell keine auswertbare Anwendungssprache enthält.
- Keine Dateien gelöscht.
- Keine lokalen Backups oder Projektkopien erzeugt.

## Sensible oder ausgeschlossene Dateien

- `.gitignore` ignoriert `.env`, `.env.*`, Logs, temporäre Dateien und typische Cache-Verzeichnisse.
- Keine versionierten Dateien mit sensiblen Dateinamen wie `.env`, private Schlüssel, Credential-, Token- oder Passwortdateien gefunden.
- Textsuche fand nur offensichtliche Platzhalter wie `YOUR_API_KEY` und keine echten Secrets.

## Fehler und Warnungen

- Ein kombinierter PowerShell-Befehl mit `@{u}` wurde von PowerShell als Hashliteral interpretiert und daher nicht verwendet. Die Upstream-Prüfung wurde anschließend sicher gegen `origin/main` wiederholt.
- Das GitHub-Repository ist öffentlich. Das ist kein Fehler, aber wegen Prompt-, Asset- und Dokumentationsinhalten bewusst zu beachten.

## Offene manuelle Aufgaben

Keine zwingenden manuellen Aufgaben.

- Social Preview aus `docs/assets/social-preview.png` über die GitHub-Weboberfläche hochladen.
- Prüfen, ob Wiki und Projects weiterhin benötigt werden.
- Fachliche und rechtliche Prüfung vor produktiver Veröffentlichung einzelner GPT-Artefakte durchführen.

## Endzustand

Das Projekt ist direkt arbeitsfähig und für öffentliche Nutzung besser vorbereitet. Die vorgenommenen Änderungen betreffen Dokumentation, GitHub-Kollaboration und Repository-Hygiene; der fachliche Kern der GPT-Artefakte blieb unverändert.
