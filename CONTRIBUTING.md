# Mitwirken

Danke für dein Interesse an diesem Repository. Beiträge sind willkommen, wenn sie die vorhandenen GPT-Artefakte präziser, konsistenter oder besser nachvollziehbar machen.

## Geeignete Beiträge

- Korrekturen an README-Dateien, Links, Tabellen, Überschriften oder Rechtschreibung
- fachlich begründete Verbesserungen an `systemprompt.md`, `fachwissen.md`, `bootloader.md` oder `customgpt_infos.md`
- neue oder verbesserte Beispielartefakte wie `beispiel.md`, `beispiel.py`, `beispiel.html`, `beispiel.json` oder passende Testdateien
- neue oder verbesserte Problemfall-Briefings für den OpenWebUI Model Builder
- Hinweise auf unklare Sicherheits-, Datenschutz-, Lizenz- oder Nutzungsgrenzen
- Verbesserungen an GitHub-Vorlagen, Repository-Hygiene oder Dokumentationsnavigation

## Vor der Änderung

1. Lies die zentrale [`README.md`](README.md) und die README des betroffenen GPT-Ordners.
2. Prüfe, welche Artefakte zusammengehören. Bei einem GPT sind das meist `README.md`, `customgpt_infos.md`, `systemprompt.md`, `fachwissen.md`, `bootloader.md` und vorhandene `beispiel.*` Dateien.
3. Öffne bei größeren Änderungen zuerst ein Issue, damit Ziel, Umfang und Risiken klar sind.

## Lokale Prüfung

Dieses Repository hat keinen Paketmanager, keinen Dev-Server und keinen zentralen Build.

Sichere Standardchecks:

```powershell
git status --short --branch
git diff --check
```

Prüfe zusätzlich manuell:

- lokale Markdown-Links und Bildpfade
- Tabellen und Überschriften
- UTF-8-Umlaute in deutschem Fließtext
- unveränderte technische Slugs, Modell-IDs, Dateinamen und URLs
- keine echten Secrets, Tokens, Passwörter, API-Keys, Kundendaten oder personenbezogenen Daten

## Pull-Request-Prozess

1. Halte den Diff klein und auf ein Thema begrenzt.
2. Erkläre im Pull Request, welches GPT-Paket oder welche Dokumentation betroffen ist.
3. Beschreibe fachliche Auswirkungen, falls Prompt-Verhalten verändert wird.
4. Liste ausgeführte Prüfungen.
5. Verlinke zugehörige Issues, wenn vorhanden.

## Stilregeln

- Schreibe klare, konkrete deutsche Dokumentation.
- Nutze echte UTF-8-Umlaute in Fließtext.
- Ändere technische IDs, Slugs, Dateinamen, URLs und Modellparameter nur bewusst.
- Vermeide großflächige Umformulierungen ohne fachlichen Grund.
- Lösche Icons, Exportartefakte, Spezialdokumente oder Problemfälle nur, wenn eindeutig geklärt ist, dass sie nicht mehr gebraucht werden.

## Security

Melde Sicherheitsprobleme nicht öffentlich als Issue. Beachte stattdessen [`SECURITY.md`](SECURITY.md).

## Verhalten

Für die Zusammenarbeit gilt der [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Kritik soll konkret, respektvoll und auf das Repository bezogen sein.
