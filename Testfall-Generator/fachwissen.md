# Fachwissen für TestCase Studio

## 1. Grundprinzip

Ein guter Testfall ist prüfbar, eindeutig, reproduzierbar und fachlich relevant. Er enthält Vorbedingungen, Testdaten, Schritte und erwartetes Ergebnis.

## 2. Testfallstruktur

| Feld | Zweck |
|---|---|
| ID | eindeutige Referenz |
| Priorität | Risiko- oder Geschäftswert |
| Ziel | was geprüft wird |
| Vorbedingungen | notwendiger Startzustand |
| Testdaten | synthetische, sichere Daten |
| Schritte | konkrete Aktionen |
| Erwartetes Ergebnis | beobachtbares Ergebnis |
| Typ | positiv, negativ, Randfall, Regression |

## 3. Testarten

- Smoke-Test
- Akzeptanztest
- Regressionstest
- Negativtest
- Grenzwerttest
- Rollen- und Berechtigungstest
- Fehlerbehandlungs- und Recovery-Test

## 4. Heuristiken

- happy path plus mindestens ein Fehlerpfad
- leere Eingabe
- ungültiges Format
- Grenzwert
- doppelte Aktion
- abgelaufene Sitzung
- fehlende Berechtigung
- Netzwerk- oder Drittanbieterfehler

## 5. Testdatenregeln

- keine echten Kundendaten
- keine produktiven E-Mail-Adressen
- keine echten Tokens oder Passwörter
- synthetische Namen und IDs verwenden
- sensible Felder maskieren

## 6. Qualität

Testfälle sollen nicht nur viele Varianten aufzählen. Sie sollen erklären, welches Risiko sie abdecken und wie wichtig dieses Risiko ist.
