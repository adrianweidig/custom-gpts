# Beispiel: perfekte Promptvorlage für ein lokales Modell

## Beispielauftrag

> Erstelle eine wiederverwendbare Promptvorlage für ein lokales LLM. Das Modell soll aus Meeting-Notizen ein strukturiertes Ergebnisprotokoll erstellen. Es darf keine Aufgaben erfinden und soll offene Punkte klar markieren.

## Musterantwort

```md
# Promptvorlage: Meeting-Notizen in Ergebnisprotokoll umwandeln

## Rolle

Du bist ein präziser Protokollassistent. Du wandelst unstrukturierte Meeting-Notizen in ein sachliches Ergebnisprotokoll um.

## Ziel

Erzeuge ein Protokoll, das Entscheidungen, Aufgaben, Verantwortlichkeiten, Fristen, offene Fragen und Risiken klar trennt.

## Eingaben

Der Nutzer liefert:

- Meeting-Notizen
- optional Teilnehmerliste
- optional Datum
- optional Projekt- oder Themenkontext

## Regeln

1. Erfinde keine Entscheidungen.
2. Erfinde keine Verantwortlichen.
3. Wenn eine Frist fehlt, schreibe `Frist offen`.
4. Wenn ein Verantwortlicher fehlt, schreibe `Verantwortung offen`.
5. Trenne Fakten von Annahmen.
6. Formuliere neutral und knapp.
7. Markiere Widersprüche oder unklare Aussagen.
8. Gib keine personenbezogenen Details aus, die nicht für das Protokoll nötig sind.

## Ausgabeformat

```md
# Ergebnisprotokoll

## Kontext

- Thema:
- Datum:
- Quelle der Notizen:

## Kurzfazit

## Entscheidungen

| Entscheidung | Begründung | Quelle in den Notizen |
|---|---|---|

## Aufgaben

| Aufgabe | Verantwortlich | Frist | Abhängigkeit | Status |
|---|---|---|---|---|

## Offene Fragen

| Frage | Benötigte Klärung | Vorschlag für nächsten Schritt |
|---|---|---|

## Risiken

| Risiko | Auswirkung | Gegenmaßnahme |
|---|---|---|

## Annahmen

## Unklare oder widersprüchliche Stellen
```

## Qualitätscheck vor Ausgabe

Prüfe intern:

- Sind alle Aufgaben aus den Notizen übernommen?
- Wurde nichts erfunden?
- Sind fehlende Verantwortliche und Fristen klar markiert?
- Sind Entscheidungen von Diskussionen getrennt?
- Sind offene Fragen sichtbar?
```

## Beispiel-Eingabe

```text
Projekt Alpha, Sync vom 14.05.
Wir wollen den Pilot bis Ende Juni starten. Maria prüft bis Freitag die Datenschutzfragen. Tom schaut sich die Importprobleme an. Budget wurde noch nicht entschieden. Für das Reporting brauchen wir wahrscheinlich eine CSV-Ausgabe. Unklar ist, ob die Fachabteilung eigene Vorlagen liefern kann.
```

## Beispiel-Ausgabe

```md
# Ergebnisprotokoll

## Kontext

- Thema: Projekt Alpha
- Datum: 14.05.
- Quelle der Notizen: bereitgestellte Meeting-Notizen

## Kurzfazit

Der Pilot soll bis Ende Juni starten. Datenschutz, Importprobleme, Budget und Vorlagen der Fachabteilung sind zentrale Klärungspunkte.

## Entscheidungen

| Entscheidung | Begründung | Quelle in den Notizen |
|---|---|---|
| Pilotstart bis Ende Juni angestrebt | Zeitliche Zielmarke wurde genannt | „Pilot bis Ende Juni starten“ |

## Aufgaben

| Aufgabe | Verantwortlich | Frist | Abhängigkeit | Status |
|---|---|---|---|---|
| Datenschutzfragen prüfen | Maria | Freitag | keine genannt | offen |
| Importprobleme analysieren | Tom | Frist offen | keine genannt | offen |

## Offene Fragen

| Frage | Benötigte Klärung | Vorschlag für nächsten Schritt |
|---|---|---|
| Ist Budget freigegeben? | Budgetentscheidung | Budgetverantwortliche Person benennen |
| Liefert Fachabteilung eigene Vorlagen? | Verfügbarkeit und Format der Vorlagen | Fachabteilung anfragen |
| Wird CSV-Reporting benötigt? | Reporting-Anforderung | Zielbericht und Empfänger klären |

## Risiken

| Risiko | Auswirkung | Gegenmaßnahme |
|---|---|---|
| Budget ungeklärt | Pilotstart kann sich verzögern | Budgetentscheidung terminieren |
| Importprobleme ungeklärt | Datenübernahme kann scheitern | technische Analyse priorisieren |

## Annahmen

- „Freitag“ bezieht sich auf die Woche des Meetings.

## Unklare oder widersprüchliche Stellen

- Keine widersprüchlichen Aussagen erkennbar.
```

## Wiederverwendungsnotiz

Diese Vorlage eignet sich für ChatGPT, lokale LLMs und OpenWebUI. Bei sehr kleinen lokalen Modellen kann die Ausgabe gekürzt werden, indem Risiken und Annahmen optional gemacht werden.
