# Release-Prozess

Dieses Repository hat aktuell keine versionierten Releases und keine Paketveröffentlichung. Änderungen werden über Git-Commits und Pull Requests nachvollzogen.

## Wann ein Release sinnvoll ist

Ein GitHub Release kann sinnvoll sein, wenn:

- mehrere GPT-Pakete einen stabilen öffentlichen Stand erreicht haben
- eine kuratierte Momentaufnahme für Nutzer referenzierbar sein soll
- größere strukturelle Änderungen abgeschlossen sind
- externe Dokumentation auf einen festen Stand verweisen soll

## Empfohlener Ablauf

1. Offene Pull Requests und Issues zum geplanten Stand prüfen.
2. `CHANGELOG.md` aktualisieren.
3. `git diff --check` ausführen.
4. Repository-Health-Workflow auf `main` grün prüfen.
5. Kritische Links, GPT-Ordner und Security-Hinweise manuell prüfen.
6. Git-Tag mit nachvollziehbarem Namen erstellen, falls eine Versionierung entschieden wurde.
7. GitHub Release Notes aus dem Changelog ableiten.

## Keine automatische Veröffentlichung

Dieses Repository enthält keine Release-Automation. Veröffentlichungen sollen bewusst durch Maintainer erfolgen.
