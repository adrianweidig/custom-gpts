# Beispiel: KI-Einführungsbewertung für ein internes Assistenzszenario

## Beispielauftrag

> Wir möchten einen KI-Assistenten für interne Supportanfragen einführen. Mitarbeitende sollen Fragen zu IT-Prozessen stellen können. Es gibt interne Dokumente, aber keine Kundendaten. Wir überlegen zwischen ChatGPT Team, Azure OpenAI und einer lokalen OpenWebUI-Instanz.

## Musterantwort

## Kurzfazit

Das Vorhaben ist grundsätzlich geeignet für einen kontrollierten Pilot, wenn Datenklassifikation, Berechtigungen, Logging, Prompt-Grenzen und Verantwortlichkeiten vorab geregelt werden. Die wichtigste Entscheidung ist nicht nur das Modell, sondern das Betriebs- und Governance-Modell.

## Annahmen

- Es sollen keine Kundendaten verarbeitet werden.
- Die Dokumente enthalten interne Prozessinformationen, aber keine hochvertraulichen Zugangsdaten.
- Der Assistent soll Antworten geben, aber keine Änderungen in IT-Systemen ausführen.

## Zielbild

| Bereich | Empfehlung |
|---|---|
| Use Case | interner IT-Support-Assistent |
| Datenklasse | intern, nicht öffentlich |
| Automationsgrad | zunächst nur Auskunft, keine Aktionen |
| Nutzerkreis | begrenzter Pilot mit definierten Rollen |
| Freigabe | IT-Security und Datenschutz vor Pilotstart |

## Optionenvergleich

| Kriterium | ChatGPT Team | Azure OpenAI | Lokale OpenWebUI |
|---|---|---|---|
| Einrichtung | schnell | mittel | höherer Betriebsaufwand |
| Governance | Plattformabhängig | gut in Enterprise-Umgebungen integrierbar | vollständig selbst zu gestalten |
| Datenkontrolle | abhängig von Vertrag und Einstellungen | stark über Tenant und Policies steuerbar | maximal lokal, aber eigener Betrieb |
| Wartung | gering | mittel | hoch |
| RAG-Anbindung | begrenzt je nach Setup | gut architekturierbar | flexibel, aber selbst zu betreiben |

## Hauptrisiken

| Risiko | Auswirkung | Gegenmaßnahme |
|---|---|---|
| interne Dokumente enthalten ungeprüfte sensible Inhalte | unbeabsichtigte Offenlegung | Dokumentenklassifikation und Bereinigung vor Upload |
| Nutzer geben Tickets mit personenbezogenen Daten ein | Datenschutzrisiko | Nutzungshinweise, technische Filter, Pilotregeln |
| Antworten wirken verbindlicher als sie sind | falsche Prozessausführung | Quellenhinweise, Unsicherheitsmarkierung, Eskalationsregeln |
| fehlende Ownership | veraltete Wissensbasis | fachliche Owner pro Dokumentenbereich |

## Mindestanforderungen vor Pilot

1. Datenklassifikation der Wissensquellen.
2. Entscheidung, welche Daten nicht in den Assistenten dürfen.
3. Rollen- und Zugriffskonzept.
4. Logging- und Aufbewahrungskonzept.
5. klare Nutzerhinweise: keine Secrets, keine personenbezogenen Daten, keine produktiven Zugangsdaten.
6. Testfragenkatalog mit erwarteten Antworten.
7. Eskalationspfad für unsichere oder kritische Antworten.

## Empfohlener Pilotplan

| Phase | Dauer | Ergebnis |
|---|---:|---|
| Vorbereitung | 1-2 Wochen | Datenquellen, Regeln, Testfragen |
| Technischer Pilot | 2 Wochen | Prototyp mit begrenztem Nutzerkreis |
| Auswertung | 1 Woche | Trefferqualität, Risiken, Nutzerfeedback |
| Entscheidung | 1 Meeting | Go, Anpassung oder Stopp |

## Klare Nicht-Empfehlung

Kein Start mit produktiven Tickets, echten Zugangsdaten, unbereinigten Dokumenten oder automatischen Aktionen in IT-Systemen.

## Offene Fragen

- Welche Dokumente enthalten personenbezogene Daten?
- Gibt es Betriebsrats- oder Compliance-Anforderungen?
- Wer ist fachlicher Owner der Wissensbasis?
- Soll der Assistent nur antworten oder später Aktionen auslösen?

## Entscheidungsvorlage

Empfohlen wird ein begrenzter Auskunfts-Pilot. Für schnelle Validierung ist ChatGPT Team möglich, sofern Vertrags- und Datenschutzeinstellungen passen. Für stärkere Enterprise-Governance ist Azure OpenAI naheliegend. Lokale OpenWebUI ist sinnvoll, wenn Datenkontrolle wichtiger ist als Betriebsaufwand.
