# Maintainer-Checkliste

Sprachen: [Deutsch](MAINTAINER_CHECKLIST.md) | [English](../en/MAINTAINER_CHECKLIST.md)

Diese Datei dokumentiert erledigte Repository-Einstellungen und verbleibende Schritte, die GitHub-Rechte, UI-Zugriff oder bewusste Maintainer-Entscheidungen erfordern.

## Erledigt am 2026-05-24

- Repository Description gesetzt: `Curated Custom GPT configurations, system prompts, knowledge files and documentation.`
- Topics gesetzt: `custom-gpt`, `prompt-engineering`, `chatgpt`, `openwebui`, `n8n`, `documentation`.
- Discussions aktiviert.
- Security Policy veröffentlicht.
- Private Vulnerability Reporting aktiviert.
- Vulnerability Alerts aktiviert.
- Dependabot Security Updates aktiviert.
- Secret Scanning und Push Protection aktiviert.
- Branch Protection für `main` eingerichtet:
  - Required Status Check: `Documentation and link health`
  - aktueller Branch muss vor Merge aktuell sein
  - ein approving Review für Pull Requests erforderlich
  - stale Reviews werden bei neuen Commits verworfen
  - Conversation Resolution erforderlich
  - Force Pushes und Branch-Löschung deaktiviert
- Social-Preview-PNG erstellt: [`docs/assets/social-preview.png`](../assets/social-preview.png)
- Kuratierter Snapshot-Release `public-readiness-2026-05-24` vorbereitet.

## Erledigt am 2026-05-25

- Deutsche Standardstruktur mit englischen Alternativdateien ergänzt.
- `docs/de/` und `docs/en/` als explizite Dokumentationsrouten angelegt.
- Repository-Health-Workflow um i18n-, Sprachlink- und Unicode-Prüfungen erweitert.

## GitHub Repository Settings

- Social Preview aus [`docs/assets/social-preview.png`](../assets/social-preview.png) in GitHub hochladen. GitHub dokumentiert dafür den Upload über `Settings` -> `Social preview`; ein direkter REST-/GitHub-CLI-Upload wurde nicht verfügbar gemacht.
- Prüfen, ob Wiki und Projects weiterhin benötigt werden. Beide Funktionen waren bereits aktiviert und wurden nicht deaktiviert, um keine bestehenden externen Arbeitsflächen zu beeinflussen.
- GitHub Pages ist nicht als neue Infrastruktur aktiviert. Wenn später eine Projektwebsite ergänzt wird, soll Deutsch die Standardroute und Englisch die erste Alternativroute sein.

## Security

- Code Scanning nur aktivieren, wenn künftig auswertbarer Anwendungscode hinzukommt. Für die aktuelle Markdown-/Asset-Sammlung ist kein CodeQL-Workflow eingerichtet.

## Branch Protection

- Branch Protection ist eingerichtet. Bei künftigen Workflow-Umbenennungen muss der Required Status Check entsprechend angepasst werden.

## Releases

- Für kuratierte Dokumentationsstände wird das Tag-Schema `public-readiness-YYYY-MM-DD` verwendet.
- SemVer nur einführen, wenn künftig paketartige Artefakte mit klarer Kompatibilitätsaussage entstehen.

## Lizenz und externe Assets

- MIT-Lizenz ist im Repository vorhanden.
- Für veröffentlichte GPT-Inhalte, Icons, fremde Quellen, Trainingsdaten, Marken und externe Medien bei Bedarf zusätzliche rechtliche Prüfung durchführen.
- Keine urheberrechtlich unklaren Bilder oder Logos als Social Preview verwenden.
