# Beispiel: vollständige Testfallspezifikation aus einer User Story

## Eingabe

Als registrierter Nutzer möchte ich mein Passwort zurücksetzen können, damit ich wieder Zugriff auf mein Konto bekomme.

Akzeptanzkriterien:

- Nutzer gibt seine E-Mail-Adresse ein.
- Wenn die E-Mail bekannt ist, wird ein Reset-Link versendet.
- Aus Sicherheitsgründen zeigt die Oberfläche immer dieselbe neutrale Bestätigung.
- Der Link ist zeitlich begrenzt.

## Ziel

Die Funktion soll sicherstellen, dass Nutzer einen Passwort-Reset anfordern können, ohne dass Angreifer über die Oberfläche herausfinden, ob eine E-Mail-Adresse registriert ist.

## Annahmen

- Testdaten sind synthetisch und nutzen `.invalid`-Domains.
- Die konkrete Ablaufzeit des Links ist nicht genannt und wird als prüfpflichtige Systemkonfiguration markiert.
- Der Versand der E-Mail kann in der Testumgebung über Mail-Capture oder Logprüfung validiert werden.

## Testfälle

| ID | Priorität | Typ | Ziel | Vorbedingungen | Testdaten | Schritte | Erwartetes Ergebnis |
|---|---|---|---|---|---|---|---|
| TC-01 | Hoch | Positiv | Reset für bekannte E-Mail anfordern | aktives Nutzerkonto existiert | `user-reset@example.invalid` | Reset-Seite öffnen, E-Mail eingeben, absenden | Neutrale Bestätigung erscheint; Reset-E-Mail wird erzeugt |
| TC-02 | Hoch | Security | Account Enumeration verhindern | keine | `unknown@example.invalid` | unbekannte E-Mail eingeben, absenden | Dieselbe neutrale Bestätigung wie bei bekannter E-Mail; kein sichtbarer Hinweis auf Nicht-Existenz |
| TC-03 | Mittel | Negativ | ungültiges E-Mail-Format prüfen | keine | `not-an-email` | Formular absenden | Eingabevalidierung verhindert Absenden oder zeigt klare Fehlermeldung ohne technische Details |
| TC-04 | Hoch | Regression | abgelaufenen Reset-Link ablehnen | abgelaufener Link vorhanden | synthetischer Link | abgelaufenen Link öffnen | Link wird abgelehnt; Nutzer kann neuen Reset anfordern |
| TC-05 | Hoch | Security | bereits verwendeten Reset-Link ablehnen | Link wurde erfolgreich genutzt | synthetischer Link | Link erneut öffnen | Link ist ungültig; keine erneute Passwortänderung möglich |
| TC-06 | Mittel | Abuse | Mehrfachanforderung prüfen | Konto existiert | `user-reset@example.invalid` | Reset mehrfach schnell anfordern | System verhält sich gemäß Rate-Limit oder erzeugt keine missbräuchliche Mail-Flut |
| TC-07 | Mittel | Accessibility | Bestätigung ist verständlich | keine | gültige E-Mail | Reset anfordern | Bestätigung ist ohne Fachbegriffe verständlich und per Tastatur erreichbar |

## Ergänzende Randfälle

- mehrfaches Absenden innerhalb kurzer Zeit
- leere E-Mail
- Groß-/Kleinschreibung der E-Mail
- bereits verwendeter Reset-Link
- Reset-Link nach Passwortänderung in anderer Session
- Nutzerkonto deaktiviert oder gesperrt

## Offene Fragen

- Wie lange ist der Reset-Link gültig?
- Gibt es Rate-Limits pro Konto oder IP?
- Wird der Nutzer nach erfolgreichem Reset aus bestehenden Sessions ausgeloggt?
- Wird ein Audit-Log geschrieben?
- Wie wird Support bei verlorenem zweiten Faktor eingebunden?

## Automatisierungshinweise

- TC-01 bis TC-05 eignen sich für Integrationstests.
- TC-02 muss Statuscode, Antworttext und Antwortzeit im Blick behalten, damit keine Seiteneffekte Account Enumeration ermöglichen.
- TC-06 ist eher ein Abuse-/Rate-Limit-Test und kann in einer dedizierten Testumgebung laufen.
