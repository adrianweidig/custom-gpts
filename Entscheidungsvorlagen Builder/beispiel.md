# Beispiel: detailliertes Entscheidungsmemo

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
| Berechtigungssteuerung | mittel | hoch, je nach System | niedrig |
| Automatisierbarkeit | hoch | mittel | niedrig |

## Gewichtete Bewertung

| Kriterium | Gewicht | A: Markdown-Repo | B: Wiki | C: Status quo |
|---|---:|---:|---:|---:|
| Review-Fähigkeit | 25 % | 5 | 3 | 1 |
| Einstieg für Nichtentwickler | 20 % | 3 | 5 | 1 |
| Versionierung | 20 % | 5 | 3 | 1 |
| Pflegeaufwand | 15 % | 3 | 3 | 1 |
| Suchbarkeit | 10 % | 3 | 4 | 1 |
| Automatisierbarkeit | 10 % | 5 | 3 | 1 |

## Vorläufige Einordnung

Option A ist stärker, wenn technische Qualität, Review und Versionierung entscheidend sind. Option B ist stärker, wenn Fachbereiche regelmäßig selbst Inhalte pflegen sollen.

## Risiken und Annahmen

- Annahme: Technische Maintainer können Pull Requests prüfen.
- Risiko: Fachbereiche beteiligen sich weniger, wenn Git-Hürde zu hoch ist.
- Risiko: Wiki kann ohne Ownership schnell veralten.
- Annahme: Es gibt keine zwingende Vorgabe für ein bestehendes Enterprise-Wiki.
- Risiko: Berechtigungen werden zu spät modelliert und blockieren den Rollout.

## Offene Punkte

- Wer ist fachlicher Owner?
- Welche Dokumente müssen zugriffsbeschränkt sein?
- Welche Suchfunktion wird benötigt?
- Welche Personengruppe soll Inhalte tatsächlich bearbeiten?
- Müssen Inhalte auditierbar freigegeben werden?

## Nächste Schritte

1. Zweiwöchigen Pilot mit fünf Kernartikeln durchführen.
2. Pflegeprozess und Review-Verantwortung festlegen.
3. Nach Pilot Nutzbarkeit und Pflegeaufwand vergleichen.

## Entscheidungsvorschlag

Freigabe für einen Pilot mit Option A, wenn das erste Ziel technische Betriebsdokumentation ist. Parallel sollte geprüft werden, ob Fachbereiche später über vereinfachte Pull-Request-Vorlagen oder einen Wiki-Spiegel eingebunden werden können.

## Entscheidung, die noch nicht getroffen werden sollte

Keine dauerhafte Toolfestlegung, bevor der Pilot gezeigt hat, ob die wichtigsten Nutzergruppen Inhalte finden und pflegen können.
