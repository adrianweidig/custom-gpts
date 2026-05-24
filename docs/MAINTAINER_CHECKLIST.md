# Maintainer-Checkliste

Diese Punkte erfordern Repository-Rechte oder bewusste Maintainer-Entscheidungen und wurden nicht automatisch geändert.

## GitHub Repository Settings

- Repository Description ist gesetzt: `Curated Custom GPT configurations, system prompts, knowledge files and documentation.`
- Topics sind gesetzt: `custom-gpt`, `prompt-engineering`, `chatgpt`, `openwebui`, `n8n`, `documentation`.
- Social Preview aus [`docs/assets/social-preview.png`](assets/social-preview.png) hochladen.
- Prüfen, ob Wiki und Projects für dieses Repository wirklich benötigt werden.
- Discussions aktivieren, wenn öffentliche Kollaboration über Fragen und Ideen gewünscht ist.

## Security

- Private Vulnerability Reporting aktivieren.
- Secret Scanning und Push Protection aktivieren, sofern im GitHub-Plan verfügbar.
- Dependabot Alerts und Dependabot Security Updates aktivieren.
- Code Scanning nur aktivieren, wenn künftig auswertbarer Anwendungscode hinzukommt. Für die aktuelle Markdown-/Asset-Sammlung ist kein CodeQL-Workflow eingerichtet.
- Security Policy nach Aktivierung des privaten Meldewegs erneut prüfen.

## Branch Protection

- Branch Protection oder Ruleset für `main` einrichten.
- Pull Requests vor Merge verlangen.
- Status Check `Repository Health` als required markieren, sobald der Workflow stabil grün läuft.
- Force Pushes auf `main` verbieten.

## Releases

- Entscheiden, ob versionierte GitHub Releases für kuratierte GPT-Stände gewünscht sind.
- Wenn ja, Namensschema und Changelog-Prozess festlegen.

## Lizenz und externe Assets

- MIT-Lizenz ist im Repository vorhanden.
- Für veröffentlichte GPT-Inhalte, Icons, fremde Quellen, Trainingsdaten, Marken und externe Medien bei Bedarf zusätzliche rechtliche Prüfung durchführen.
- Keine urheberrechtlich unklaren Bilder oder Logos als Social Preview verwenden.
