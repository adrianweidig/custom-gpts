# Beispiel: Entscheidungsmemo

## Entscheidung

Soll das Team für interne Dokumentation ein leichtgewichtiges Markdown-Repository oder ein Wiki verwenden?

## Kurzempfehlung

Empfohlen wird ein Markdown-Repository, wenn Versionierung, Review und technische Nähe wichtiger sind als nichttechnische Bearbeitung im Browser. Ein Wiki ist vorzuziehen, wenn Fachbereiche ohne Git-Kenntnisse regelmäßig selbst pflegen sollen.

## Kontext

Das Team dokumentiert Betriebsabläufe, Architekturentscheidungen und wiederkehrende Supportlösungen. Bisher liegen Informationen verteilt in Chats, Tickets und einzelnen Dateien.

## Optionen

| Option | Beschreibung |
|---|---|
| A: Markdown-Repository | Dokumentation als versionierte Markdown-Dateien mit Pull Requests |
| B: Wiki | Browserbasierte Dokumentation mit einfacher Bearbeitung |
| C: Status quo | Keine zentrale Lösung |

## Entscheidungsmatrix

| Kriterium | A: Markdown-Repo | B: Wiki | C: Status quo |
|---|---|---|---|
| Review-Fähigkeit | hoch | mittel | niedrig |
| Einstieg für Nichtentwickler | mittel | hoch | niedrig |
| Versionierung | hoch | mittel | niedrig |
| Pflegeaufwand | mittel | mittel | hoch |
| Suchbarkeit | mittel | hoch | niedrig |

## Risiken und Annahmen

- Annahme: Technische Maintainer können Pull Requests prüfen.
- Risiko: Fachbereiche beteiligen sich weniger, wenn Git-Hürde zu hoch ist.
- Risiko: Wiki kann ohne Ownership schnell veralten.

## Offene Punkte

- Wer ist fachlicher Owner?
- Welche Dokumente müssen zugriffsbeschränkt sein?
- Welche Suchfunktion wird benötigt?

## Nächste Schritte

1. Zweiwöchigen Pilot mit fünf Kernartikeln durchführen.
2. Pflegeprozess und Review-Verantwortung festlegen.
3. Nach Pilot Nutzbarkeit und Pflegeaufwand vergleichen.
