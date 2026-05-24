# Maintainer-Checkliste

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
- Social-Preview-PNG erstellt: [`docs/assets/social-preview.png`](assets/social-preview.png)

## GitHub Repository Settings

- Social Preview aus [`docs/assets/social-preview.png`](assets/social-preview.png) in GitHub hochladen. GitHub dokumentiert dafür den Upload über `Settings` -> `Social preview`; ein direkter REST-/GitHub-CLI-Upload wurde nicht verfügbar gemacht.
- Prüfen, ob Wiki und Projects weiterhin benötigt werden. Beide Funktionen waren bereits aktiviert und wurden nicht deaktiviert, um keine bestehenden externen Arbeitsflächen zu beeinflussen.

## Security

- Code Scanning nur aktivieren, wenn künftig auswertbarer Anwendungscode hinzukommt. Für die aktuelle Markdown-/Asset-Sammlung ist kein CodeQL-Workflow eingerichtet.

## Branch Protection

- Branch Protection ist eingerichtet. Bei künftigen Workflow-Umbenennungen muss der Required Status Check entsprechend angepasst werden.

## Releases

- Entscheiden, ob versionierte GitHub Releases für kuratierte GPT-Stände gewünscht sind.
- Wenn ja, Namensschema und Changelog-Prozess festlegen.

## Lizenz und externe Assets

- MIT-Lizenz ist im Repository vorhanden.
- Für veröffentlichte GPT-Inhalte, Icons, fremde Quellen, Trainingsdaten, Marken und externe Medien bei Bedarf zusätzliche rechtliche Prüfung durchführen.
- Keine urheberrechtlich unklaren Bilder oder Logos als Social Preview verwenden.
