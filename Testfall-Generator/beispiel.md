# Beispiel: Testfälle aus einer User Story

## Eingabe

Als registrierter Nutzer möchte ich mein Passwort zurücksetzen können, damit ich wieder Zugriff auf mein Konto bekomme.

Akzeptanzkriterien:

- Nutzer gibt seine E-Mail-Adresse ein.
- Wenn die E-Mail bekannt ist, wird ein Reset-Link versendet.
- Aus Sicherheitsgründen zeigt die Oberfläche immer dieselbe neutrale Bestätigung.
- Der Link ist zeitlich begrenzt.

## Annahmen

- Testdaten sind synthetisch.
- Die konkrete Ablaufzeit des Links ist nicht genannt und wird als prüfpflichtige Systemkonfiguration markiert.

## Testfälle

| ID | Priorität | Typ | Ziel | Vorbedingungen | Testdaten | Schritte | Erwartetes Ergebnis |
|---|---|---|---|---|---|---|---|
| TC-01 | Hoch | Positiv | Reset für bekannte E-Mail anfordern | Nutzerkonto existiert | `user-reset@example.invalid` | Reset-Seite öffnen, E-Mail eingeben, absenden | Neutrale Bestätigung erscheint; Reset-E-Mail wird erzeugt |
| TC-02 | Hoch | Security | Account Enumeration verhindern | keine | `unknown@example.invalid` | Reset-Seite öffnen, unbekannte E-Mail eingeben, absenden | Dieselbe neutrale Bestätigung wie bei bekannter E-Mail |
| TC-03 | Mittel | Negativ | ungültiges E-Mail-Format prüfen | keine | `not-an-email` | Formular absenden | Eingabevalidierung verhindert Absenden oder zeigt klare Fehlermeldung |
| TC-04 | Hoch | Regression | abgelaufenen Reset-Link ablehnen | abgelaufener Link vorhanden | synthetischer Link | abgelaufenen Link öffnen | Link wird abgelehnt; Nutzer kann neuen Reset anfordern |

## Ergänzende Randfälle

- mehrfaches Absenden innerhalb kurzer Zeit
- leere E-Mail
- Groß-/Kleinschreibung der E-Mail
- bereits verwendeter Reset-Link

## Offene Fragen

- Wie lange ist der Reset-Link gültig?
- Gibt es Rate-Limits pro Konto oder IP?
- Wird der Nutzer nach erfolgreichem Reset aus bestehenden Sessions ausgeloggt?
