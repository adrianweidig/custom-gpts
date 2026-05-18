# layoutrichtlinien.md

**Version:** 1.0  
**Stand:** 15. Mai 2026  
**Zweck:** Verbindliche Layout-, Qualitäts-, Barrierefreiheits- und Kompatibilitätsrichtlinien für Unterrichtspräsentationen (`.pptx`) und Handouts/Arbeitsdokumente (`.docx`).  
**Ziel:** Dateien sollen nicht nur inhaltlich korrekt, sondern professionell gestaltet, drucktauglich, barrierearm, technisch stabil und ohne Reparaturdialog in Microsoft PowerPoint/Word nutzbar sein.

---

## 0. Sofortige Konsequenz aus dem Qualitätsproblem

Die bisherige Ausgabe war optisch unzureichend und technisch offenbar nicht sauber genug, weil die PowerPoint-Datei erst nach Download, Öffnen in PowerPoint und Reparatur funktionierte. Das darf künftig nicht passieren.

Diese Datei legt deshalb verbindlich fest:

1. **Keine PPTX/DOCX-Ausgabe ohne Render- und Kompatibilitätsprüfung.**
2. **Keine Präsentation darf ausgeliefert werden, wenn PowerPoint beim Öffnen einen Reparaturdialog anzeigen würde.**
3. **Folien und Handouts müssen auf Basis eines Designsystems erstellt werden, nicht „frei improvisiert“.**
4. **Layout, Lesbarkeit, Quellen, Barrierefreiheit und technische Validität sind gleichrangige Qualitätskriterien.**
5. **Bei medizinischen/pflegerischen Unterrichtsmaterialien muss Fachlichkeit vorsichtig, quellenbasiert und didaktisch reduziert formuliert werden.**

---

# Teil A – Grundprinzipien

## 1. Designziel

Unterrichtsmaterialien müssen drei Situationen gleichzeitig erfüllen:

- **Präsentation im Unterricht:** Beamer, Smartboard, Bildschirmfreigabe, hybride Lehre.
- **Nachnutzung durch Lernende:** Folien als Orientierung, Handout als Lernunterlage.
- **Druck/Archivierung:** A4-Druck, PDF-Export, spätere Bearbeitung durch Lehrkräfte.

Eine gute Folie ersetzt kein Skript. Ein gutes Handout ist kein Folienausdruck.

---

## 2. Prioritätenreihenfolge

Wenn Regeln miteinander konkurrieren, gilt diese Reihenfolge:

1. **Technische Öffnungsfähigkeit:** Datei muss ohne Reparaturdialog öffnen.
2. **Lesbarkeit und Barrierefreiheit:** Inhalt muss erkennbar, logisch und zugänglich sein.
3. **Didaktische Klarheit:** Lernende müssen erkennen, was wichtig ist.
4. **Fachliche Korrektheit:** Aussagen müssen sachlich, quellenbasiert und angemessen reduziert sein.
5. **Gestalterische Qualität:** ruhig, modern, konsistent, professionell.
6. **Dateigröße und Performance:** Datei soll nicht unnötig groß oder langsam sein.
7. **Dekoration:** nur, wenn sie dem Verständnis dient.

---

## 3. Verbindliche No-Gos

### 3.1 Allgemeine No-Gos

- Textwüsten
- zu kleine Schrift
- unruhige Hintergründe
- zufällige Farben
- zufällige Schriftarten
- Clipart-Optik
- überladene Folien
- unbeschriftete Abbildungen
- Tabellen mit winziger Schrift
- nicht erklärte Fachbegriffe
- Handout als bloße Sammlung von Folienminiaturen
- Quellenfolie ohne echte Quellen
- Platzhalter wie „Bild hier einfügen“ in finalen Dateien
- Behauptung „geprüft“, wenn keine Prüfung erfolgt ist

### 3.2 Technische No-Gos für PowerPoint

- Datei öffnet nur nach Reparatur
- beschädigte oder unvollständige Beziehungen im Open-XML-Paket
- manuell fehlerhaft gepatchtes XML
- fehlende Medien-Dateien trotz Referenz
- externe Bildverknüpfungen ohne Einbettung
- Makros, `.pptm`, aktive Inhalte
- nicht unterstützte Bildformate wie WebP in PPTX
- eingebettete Schriftdateien ohne Lizenzklarheit
- transparente/animierte Spezialeffekte, wenn dadurch Kompatibilität leidet
- Folienobjekte mit negativen, extremen oder außerhalb der Folie liegenden Koordinaten
- Shapes ohne gültige Größe
- leere Layout-/Master-Referenzen
- defekte Theme-Dateien

### 3.3 Technische No-Gos für Word

- Tabellen, die über Seitenränder laufen
- manuelle Leerzeilen als Layoutsystem
- Überschriften nur fett formatiert, aber ohne echte Word-Formatvorlage
- Bilder ohne Alternativtext
- nicht aktualisierbare Inhaltsverzeichnisse
- harte Seitenumbrüche ohne Layoutgrund
- exotische Schriftarten ohne Fallback
- Textfelder als Hauptlayout für Fließtext
- defekte Felder, Links oder Querverweise
- beschädigte DOCX-Datei ohne Renderprüfung

---

# Teil B – Designsystem

## 4. Einheitliches Designsystem statt Einzelfallgestaltung

Jede Präsentation und jedes Handout benötigt vor der Erstellung ein Mini-Designsystem:

1. **Dokumentformat**
2. **Farbpalette**
3. **Typografie**
4. **Abstände**
5. **Raster**
6. **Komponenten**
7. **Bildstil**
8. **Tabellenstil**
9. **Diagrammstil**
10. **Quellen- und Fußnotenstil**

Das Designsystem muss zuerst definiert und danach konsequent angewendet werden.

---

## 5. Empfohlenes neutrales Unterrichtsdesign

### 5.1 Farbpalette

Eine ruhige Standardpalette für Bildung, Pflege, Medizin und naturwissenschaftliche Themen:

| Rolle | Farbe | Hex | Verwendung |
|---|---:|---:|---|
| Primär dunkel | Navy | `#1F3A5F` | Titel, Kopfzeilen, Hauptakzente |
| Primär mittel | Blau | `#4F7CAC` | Hervorhebungen, Linien, Icons |
| Sekundär | Petrol | `#0F766E` | Merksätze, Praxisbezug |
| Warn-/Achtungston | Amber | `#B45309` | vorsichtige Hinweise, nicht für Flächenüberladung |
| Fehler/Risiko | Rot gedämpft | `#B91C1C` | Risiken, Kontraindikationen, Warnhinweise sparsam |
| Hintergrund hell | Off-White | `#F8FAFC` | Folienhintergrund, Infoboxen |
| Fläche hell | Hellblau | `#EAF2F8` | Lernzielboxen, Merksatzboxen |
| Text dunkel | Anthrazit | `#111827` | Haupttext |
| Text sekundär | Grau | `#4B5563` | Untertitel, Quellenhinweise |
| Linien | Hellgrau | `#D1D5DB` | Tabellenlinien, Trenner |

### 5.2 Farbregeln

- Maximal **1 Primärfarbe**, **1 Sekundärfarbe**, **1 Akzentfarbe** pro Dokument.
- Keine Regenbogenpaletten.
- Farbe nie als einzige Information verwenden. Immer zusätzlich Text, Icon, Muster oder Position nutzen.
- Für Unterrichtsmaterialien besser gedeckte Farben als Neonfarben verwenden.
- Große Flächen nie in gesättigtem Rot, Grün oder Blau, wenn Text darauf liegt.
- Dunkler Text auf hellem Hintergrund ist Standard.
- Weißer Text auf dunklem Hintergrund nur für Titelbereiche oder kurze Label.

### 5.3 Kontrastregeln

- Normaler Text: mindestens **4,5:1** Kontrast.
- Große Überschriften: mindestens **3:1**, besser 4,5:1.
- Icons, Linien, Diagrammobjekte: mindestens **3:1** gegen den Hintergrund.
- Für Druckversionen zusätzlich Graustufentest durchführen.
- Kein hellgrauer Text auf weißem Hintergrund.
- Kein farbiger Text auf farbigem Hintergrund ohne Messung.

---

## 6. Typografie

### 6.1 Standardschriftarten

Für maximale Kompatibilität werden Systemschriften verwendet:

| Kontext | Empfohlen |
|---|---|
| PowerPoint modern | Aptos, Arial, Segoe UI |
| Word modern | Aptos, Arial, Calibri |
| Fallback | Arial |
| Monospace bei Code/Werten | Consolas oder Courier New |

### 6.2 Warum keine exotischen Fonts?

- Fremde Fonts fehlen oft auf anderen Rechnern.
- Eingebettete Fonts können Lizenzprobleme verursachen.
- Fehlende Fonts verändern Umbrüche.
- Veränderte Umbrüche führen zu abgeschnittenem Text.
- PowerPoint- und Word-Kompatibilität ist mit Systemschriften stabiler.

### 6.3 Typografische Grundregeln

- Maximal zwei Schriftfamilien pro Datei.
- Maximal drei Schriftschnitte: Regular, Semibold/Bold, Italic.
- Keine dekorativen Fonts.
- Keine Light-/Thin-Schnitte für Unterrichtsmaterial.
- Keine dauerhaften Versalien für längere Texte.
- Keine Unterstreichung außer für Links.
- Fett nur für echte Hervorhebung, nicht für ganze Absätze.
- Kursiv sparsam verwenden.
- Fachbegriffe beim ersten Auftreten erklären.

---

## 7. Abstände und Weißraum

### 7.1 Grundregel

Weißraum ist kein „leerer Platz“, sondern ein Mittel zur Orientierung. Elemente brauchen Abstand, damit Lernende Struktur erkennen.

### 7.2 Empfohlenes Abstandssystem

Verwende Vielfache von 4 mm bzw. 8 px:

| Token | Verwendung |
|---|---|
| XS = 2–3 mm | Abstand zwischen Icon und Text |
| S = 4–5 mm | Abstand zwischen Listenpunkten |
| M = 8 mm | Abstand zwischen Gruppen |
| L = 12 mm | Abstand zwischen Hauptbereichen |
| XL = 16–20 mm | Außenabstände / große Abschnittstrennung |

### 7.3 Regeln

- Elemente nie an den Rand kleben.
- Zwischen Überschrift und Inhalt sichtbar mehr Abstand als innerhalb einer Liste.
- Verwandte Elemente enger, nicht verwandte Elemente weiter auseinander.
- Pro Folie mindestens 20–30 % freie Fläche anstreben.
- Handout-Seiten dürfen dichter sein als Folien, aber nie überfüllt.

---

# Teil C – PowerPoint-Richtlinien

## 8. Dateiformat und Folienformat

### 8.1 Pflichtformat

- Dateiformat: `.pptx`
- Seitenformat: **DIN A4 quer**
- Breite: **29,7 cm**
- Höhe: **21,0 cm**
- Keine Makros
- Keine aktiven Inhalte
- Keine extern benötigten Dateien

### 8.2 Warum A4 quer?

- gut druckbar
- geeignet für Handouts und PDF
- stabiler als Sonderformate
- passt zu Unterrichtsmaterialien
- ermöglicht konsistente Ableitung in Handouts

---

## 9. Folienmaster und Layouts

### 9.1 Mindestlayouts

Eine professionelle Unterrichtspräsentation braucht mindestens diese Layouts:

1. **Titelfolie**
2. **Abschnittstrenner**
3. **Standard-Inhaltsfolie**
4. **Zwei-Spalten-Folie**
5. **Bild/Text-Folie**
6. **Tabelle/Übersicht**
7. **Praxisfall**
8. **Merksatz**
9. **Fragen/Selbstcheck**
10. **Zusammenfassung**
11. **Quellenfolie**

### 9.2 Master-Regeln

- Wiederkehrende Elemente gehören in den Master.
- Nicht jedes Slide-Objekt einzeln improvisieren.
- Fußzeile, Seitennummer und Kursbezeichnung einheitlich.
- Keine zufällig verschobenen Titel.
- Keine wechselnden Titelpositionen.
- Keine wechselnden Textspaltenbreiten ohne Grund.
- Keine Layouts mit Platzhaltern, die im finalen Deck leer bleiben.

### 9.3 Standard-Folienstruktur

Empfohlenes A4-Querformat-Raster:

- Außenrand links/rechts: 14–16 mm
- Außenrand oben: 12–14 mm
- Außenrand unten: 12–14 mm
- Titelbereich: 18–25 mm Höhe
- Fußbereich: 8–10 mm Höhe
- Inhaltsbereich: dazwischen
- Raster: 12 Spalten oder 2 Hauptspalten
- Spaltengutter: 6–8 mm

---

## 10. PowerPoint-Schriftgrößen

### 10.1 Mindestgrößen

| Element | Mindestgröße | Empfehlungsbereich |
|---|---:|---:|
| Folientitel | 28 pt | 32–38 pt |
| Abschnittstitel | 34 pt | 38–46 pt |
| Untertitel | 18 pt | 20–24 pt |
| Haupttext | 18 pt | 20–24 pt |
| Listenpunkte | 18 pt | 20–22 pt |
| Tabelleninhalt | 14 pt | 16–18 pt |
| Diagrammbeschriftung | 14 pt | 16–18 pt |
| Quellenhinweis auf Folie | 9 pt | 10–11 pt |
| Fußzeile | 9 pt | 10–11 pt |

### 10.2 Harte Regel

Auf normalen Inhaltsfolien darf kein didaktisch wichtiger Text unter **18 pt** gesetzt werden. Alles darunter gehört ins Handout, in Notizen oder auf eine separate Detailfolie.

---

## 11. Folieninhalt

### 11.1 Eine Kernaussage pro Folie

Jede Folie braucht eine klare Antwort auf die Frage:

> Was sollen Lernende nach dieser Folie verstanden haben?

Wenn die Antwort aus drei verschiedenen Themen besteht, braucht es drei Folien.

### 11.2 Textmenge

Richtwerte:

- maximal 1 Hauptaussage pro Folie
- maximal 3–5 Listenpunkte
- maximal 7 Textzeilen im Inhaltsbereich
- maximal 8–12 Wörter pro Listenpunkt
- keine vollständigen Fließtextabsätze auf normalen Folien
- längere Erklärungen ins Handout oder in Sprechernotizen

### 11.3 Gute Folientitel

Schlecht:

- „Grundlagen“
- „Herz“
- „Blutdruck“
- „Zusammenfassung“

Besser:

- „Das Herz arbeitet als Druck- und Saugpumpe“
- „Der Blutdruck entsteht durch Herzleistung und Gefäßwiderstand“
- „Pflegebeobachtung verbindet Messwerte mit Symptomen“
- „Merksatz: Kreislaufwerte brauchen immer Kontext“

### 11.4 Titel als Aussage

Wenn möglich, soll der Titel bereits die Kernaussage enthalten. Dadurch ist die Folie auch beim schnellen Durchblättern verständlich.

---

## 12. Folientypen und Best Practices

### 12.1 Titelfolie

Enthält:

- Thema
- Zielgruppe
- Unterrichtseinheit / Modul
- optional Datum
- optional Name der Lehrkraft/Institution

Gestaltung:

- großer Titel
- ruhiger Hintergrund
- maximal ein dezentes Bild oder Icon
- keine langen Untertitel
- keine Quellenliste

### 12.2 Lernzielfolie

Gute Lernziele beginnen mit beobachtbaren Verben:

- erklären
- benennen
- unterscheiden
- beschreiben
- zuordnen
- anwenden
- anhand eines Beispiels erläutern
- Risiken erkennen

Nicht verwenden:

- „kennen alles“
- „verstehen vollständig“
- „werden sensibilisiert“ ohne beobachtbare Handlung

### 12.3 Agenda-Folie

- 4–6 Abschnitte
- nummeriert
- nicht zu detailliert
- aktueller Abschnitt kann später farblich markiert werden

### 12.4 Grundlagenfolie

- nur Begriffe, die für das weitere Verständnis notwendig sind
- keine Lexikonfülle
- Definitionen kurz
- komplexe Fachbegriffe im Handout ausführlicher

### 12.5 Prozessfolie

Geeignet für:

- Blutfluss
- Pflegeschritte
- diagnostische Denkwege
- Ursache-Wirkungs-Ketten

Regeln:

- von links nach rechts oder oben nach unten
- maximal 5 Prozessschritte
- einheitliche Pfeile
- klare Start- und Endpunkte
- kein Pfeilchaos

### 12.6 Vergleichsfolie

Geeignet für:

- Arterien vs. Venen
- kleiner vs. großer Kreislauf
- Systole vs. Diastole
- Sympathikus vs. Parasympathikus

Regeln:

- maximal 2–3 Vergleichsobjekte
- maximal 5 Vergleichskriterien
- kurze Formulierungen
- keine verschachtelten Tabellen

### 12.7 Praxisfall-Folie

Aufbau:

1. kurze Ausgangssituation
2. Beobachtungsfrage
3. Transferfrage
4. sichere Rahmung

Beispielstruktur:

> Frau M., 78 Jahre, wirkt blass und klagt über Schwindel beim Aufstehen.  
> Welche Beobachtungen sind pflegerisch relevant?  
> Welche Informationen müssen weitergegeben werden?

Keine konkreten Therapieanweisungen ohne Kontext, Leitlinie und institutionellen Standard.

### 12.8 Merksatz-Folie

- maximal 1–3 Merksätze
- visuell klar abgesetzt
- keine langen Absätze
- Merksätze müssen prüfbar und fachlich sauber sein

### 12.9 Wiederholungsfragen

- 3–5 Fragen pro Einheit
- Mischung aus Reproduktion, Verständnis, Transfer
- keine Fangfragen
- bei Multiple Choice klare und faire Antwortoptionen
- Lösungen optional im Handout oder auf separater Folie

### 12.10 Quellenfolie

Enthält:

- wichtigste Quellen
- Organisation/Autor
- Titel
- Jahr oder Abrufdatum
- URL oder Dateiname
- keine winzige Bleiwüste

Wenn viele Quellen verwendet wurden, nur Kurztitel in PPT und vollständiges Verzeichnis im Handout.

---

## 13. PowerPoint-Komponenten

### 13.1 Infobox

Verwendung:

- Lernziel
- Hinweis
- Merksatz
- Praxisbezug
- Achtung

Regeln:

- links farbiger Akzentstreifen
- heller Hintergrund
- klarer Titel
- maximal 3 Zeilen
- nicht mehr als eine Infobox pro Folie

### 13.2 Karten

Karten eignen sich für 2–4 parallele Informationen.

Regeln:

- gleiche Größe
- gleiche Ausrichtung
- gleiche Textmenge
- Icon optional
- nicht mehr als 4 Karten pro Folie

### 13.3 Icons

Regeln:

- ein Icon-Stil pro Deck
- keine Mischung aus 3D, Flat, Outline und Clipart
- Icons nur unterstützend, nicht dekorativ überladen
- Icon immer mit Textlabel
- ausreichender Kontrast

### 13.4 Linien und Trenner

- dünne Linien 0,5–1,0 pt
- nur zur Strukturierung
- keine Rahmen um alles
- keine zufälligen Unterstreichungen

---

## 14. Tabellen in PowerPoint

### 14.1 Tabellen nur, wenn sie wirklich helfen

Tabellen sind geeignet für Vergleiche oder strukturierte Daten, nicht für lange Textsammlungen.

### 14.2 Regeln

- maximal 4–5 Spalten
- maximal 6–8 Zeilen
- Kopfzeile klar abgesetzt
- Schrift mindestens 14 pt, besser 16 pt
- keine verschachtelten Tabellen
- keine vertikalen Texte
- keine übermäßigen Zellrahmen
- keine leeren Zellen ohne Grund
- keine Tabellen über den gesamten Folienrand hinaus

### 14.3 Wenn eine Tabelle zu groß ist

Dann:

- in zwei Folien aufteilen
- als Handout-Tabelle auslagern
- Kernaussagen statt Gesamttabelle zeigen
- Diagramm oder Vergleichskarten nutzen

---

## 15. Diagramme in PowerPoint

### 15.1 Diagrammgrundsatz

Ein Diagramm zeigt eine Aussage, nicht alle verfügbaren Daten.

### 15.2 Regeln

- Diagrammtitel als Aussage formulieren
- Achsen beschriften
- Einheiten angeben
- direkte Beschriftung statt unnötiger Legende
- maximal 4–6 Datenreihen
- kein 3D
- keine Schatteneffekte
- keine überflüssigen Gitterlinien
- Farbkodierung barrierearm
- Datenquelle nennen

### 15.3 Diagrammtypen

| Ziel | Geeigneter Typ |
|---|---|
| Entwicklung über Zeit | Liniendiagramm |
| Kategorien vergleichen | Balkendiagramm |
| Anteile grob zeigen | gestapelter Balken, selten Kreisdiagramm |
| Ursache-Wirkung | Flussdiagramm |
| Ablauf | Prozessgrafik |
| Hierarchie | Baumstruktur oder Ebenenmodell |

Kreisdiagramme nur bei sehr wenigen Kategorien und klarer Aussage verwenden.

---

## 16. Bilder in PowerPoint

### 16.1 Bildregeln

- Bild muss didaktischen Zweck haben.
- Bildquelle dokumentieren.
- Bild nicht verzerren.
- Bild nicht als Hintergrund für langen Text verwenden.
- Keine Stockfoto-Beliebigkeit.
- Medizinische Abbildungen nur aus seriösen Quellen oder als eigene schematische Darstellung.
- Keine urheberrechtlich unklaren Bilder ungeprüft einbetten.

### 16.2 Technische Bildregeln

- Fotos: JPEG
- Diagramme/Schemata/Screenshots: PNG
- Vektor nach Möglichkeit als PowerPoint-Shapes oder geprüfte SVG/EMF; bei Kompatibilitätsproblemen PNG verwenden
- WebP vermeiden
- TIFF vermeiden
- riesige Originalbilder vor Einbettung skalieren
- Bilder einbetten, nicht verlinken
- Dateinamen ohne Sonderzeichen
- keine externen Medienabhängigkeiten

### 16.3 Auflösung

| Nutzung | Richtwert |
|---|---:|
| Beamer/Bildschirm | 150 ppi ausreichend |
| hochwertiger Druck | 220–300 ppi |
| Icons/Schemata | als Vektor oder hochauflösendes PNG |

Bilder dürfen nicht unnötig riesig sein. Große Dateien erhöhen Fehler- und Performance-Risiken.

---

## 17. Animationen und Übergänge

### 17.1 Standard

Keine Animationen.

### 17.2 Zulässige Ausnahme

Animationen sind nur zulässig, wenn sie einen didaktischen Zweck haben, z. B.:

- Prozess schrittweise aufbauen
- Lösung nach Frage einblenden
- Aufmerksamkeit fokussieren

### 17.3 Regeln

- maximal eine einfache Animation pro Folie
- keine Soundeffekte
- keine schnellen Bewegungen
- keine komplexen Trigger
- keine Morph-Abhängigkeit, wenn Kompatibilität wichtig ist
- Präsentation muss auch ohne Animation verständlich bleiben

---

## 18. PowerPoint-Barrierefreiheit

### 18.1 Pflicht

- eindeutige Folientitel
- logische Lesereihenfolge
- Alternativtexte für relevante Bilder
- dekorative Bilder als dekorativ markieren, wenn Tool es unterstützt
- hoher Kontrast
- keine Information nur über Farbe
- keine winzigen Fußnoten
- klare Linktexte
- keine blinkenden Elemente
- Tabellen einfach halten
- Untertitel/Transkript für eingebundene Medien, wenn Medien verwendet werden

### 18.2 Lesereihenfolge

Die Lesereihenfolge muss logisch sein:

1. Folientitel
2. Hauptaussage
3. Inhalte von links nach rechts / oben nach unten
4. Bildunterschrift
5. Quelle/Fußzeile

Objekte dürfen nicht zufällig in der Reihenfolge liegen.

---

# Teil D – DOCX-Richtlinien

## 19. Dateiformat und Seitenformat

### 19.1 Pflichtformat

- Dateiformat: `.docx`
- Seitenformat: **DIN A4 hoch**
- Papiergröße: 21,0 × 29,7 cm
- druckfreundlich
- keine Makros
- keine aktiven Inhalte
- keine externen Bildverknüpfungen

### 19.2 Standardränder

Empfehlung:

- oben: 2,0 cm
- unten: 2,0 cm
- links: 2,2–2,5 cm
- rechts: 2,0–2,2 cm

Wenn Lochrand gewünscht:

- links: 2,8–3,0 cm
- rechts: 2,0 cm

---

## 20. Word-Formatvorlagen

### 20.1 Pflicht

DOCX-Dateien müssen echte Word-Formatvorlagen verwenden:

- Titel
- Untertitel
- Überschrift 1
- Überschrift 2
- Überschrift 3
- Standard
- Liste
- Tabellenbeschriftung
- Abbildungsbeschriftung
- Merksatz
- Infobox
- Quellenverzeichnis

### 20.2 Nicht zulässig

- Überschriften nur manuell fett und größer machen
- Listen mit Bindestrich manuell vortäuschen
- Layout mit Leerzeilen erzwingen
- Tabellen nur zur Positionierung von Text verwenden
- Textfelder als Hauptlayout

---

## 21. Word-Typografie

### 21.1 Schriftgrößen

| Element | Empfehlung |
|---|---:|
| Titel | 20–24 pt |
| Untertitel | 13–15 pt |
| Überschrift 1 | 16–18 pt |
| Überschrift 2 | 13–15 pt |
| Überschrift 3 | 12–13 pt |
| Fließtext | 11–12 pt |
| Tabellen | 9,5–11 pt |
| Fußnoten/Quellen | 8,5–10 pt |
| Bild-/Tabellenbeschriftung | 9–10 pt |

### 21.2 Zeilenabstand

- Fließtext: 1,15–1,35
- nach Absätzen: 6 pt
- vor Überschrift 1: 18 pt
- nach Überschrift 1: 6–9 pt
- vor Überschrift 2: 12 pt
- nach Überschrift 2: 4–6 pt

### 21.3 Absatzregeln

- ein Thema pro Absatz
- Absatzlänge meist 3–6 Sätze
- durchschnittlich 15–20 Wörter pro Satz anstreben
- keine endlosen Schachtelsätze
- wichtige Begriffe fett, aber sparsam
- Fließtext linksbündig, nicht blockgesetzt, wenn große Wortabstände entstehen

---

## 22. Dokumentstruktur für Unterrichtshandouts

Ein gutes Handout enthält mindestens:

1. Titel
2. Thema und Zielgruppe
3. Lernziele
4. kurze Einführung
5. Fachinhalte in klaren Abschnitten
6. zentrale Begriffe
7. Merksätze
8. Tabellen/Übersichten
9. Praxisbeispiel
10. Wiederholungsfragen
11. Selbstkontrollaufgaben oder Transferfragen
12. Zusammenfassung
13. Quellenverzeichnis

### 22.1 Handout ≠ Folienskript

Das Handout darf die Präsentation ergänzen, aber nicht einfach kopieren.

Präsentation:

- Orientierung
- Kernaussagen
- visuelle Struktur
- Impulse

Handout:

- Erklärung
- Definitionen
- Zusammenhänge
- Beispiele
- Wiederholung
- Quellen

---

## 23. Inhaltsverzeichnis

### 23.1 Wann ein Inhaltsverzeichnis sinnvoll ist

- ab ca. 6–8 Seiten
- bei mehreren Modulen
- bei komplexen medizinischen Themen
- bei Handouts, die später als Lernskript genutzt werden

### 23.2 Regeln

- automatisch auf Basis von Überschriften
- maximal 2–3 Ebenen
- nicht manuell tippen
- vor Ausgabe aktualisieren
- Seitenzahlen prüfen

---

## 24. Kopf- und Fußzeilen

### 24.1 Empfohlen

Kopfzeile:

- Thema oder Modul
- ggf. Kurs/Institution

Fußzeile:

- Seitenzahl
- Datum oder Version
- optional Kurzquelle/Autor

### 24.2 Regeln

- keine überladene Kopfzeile
- Fußzeile nicht größer als Fließtext
- Seitenzahlen immer vorhanden
- vertrauliche Angaben vermeiden

---

## 25. Tabellen in Word

### 25.1 Verwendung

Tabellen sind gut für:

- Vergleiche
- Begriffsübersichten
- Messwerte
- Beobachtungskriterien
- Schrittfolgen
- Zusammenfassungen

### 25.2 Regeln

- echte Tabellen nur für Daten, nicht für Layout
- Kopfzeile definieren
- Kopfzeile bei Seitenumbruch wiederholen
- keine vertikalen Texte
- keine verschachtelten Tabellen
- keine zu breiten Tabellen
- Tabellen nicht als Bild einfügen
- Zellabstände lesbar
- Tabellenbeschriftung verwenden
- Quellen bei Daten angeben

### 25.3 Tabellenbreite

- Tabelle auf Seitenbreite beschränken
- Spaltenbreiten manuell prüfen
- lange Begriffe umbrechen
- bei vielen Spalten Querformatseite oder separate Anlage erwägen
- niemals abgeschnitten ausliefern

---

## 26. Abbildungen in Word

### 26.1 Regeln

- jede relevante Abbildung hat Beschriftung
- jede relevante Abbildung hat Alternativtext
- Bild nicht verzerren
- Bildgröße passend zur Seite
- Textumbruch vorzugsweise „Mit Text in Zeile“ für Stabilität
- keine frei schwebenden Bilder, wenn Layout dadurch instabil wird
- keine Bilder über Seitenränder
- Quelle direkt in Beschriftung oder Quellenverzeichnis

### 26.2 Bildunterschrift

Format:

> Abbildung 1: Schematische Darstellung des Blutkreislaufs. Quelle: eigene Darstellung nach ...

### 26.3 Alt-Text

Guter Alt-Text:

- beschreibt Informationsgehalt
- nicht zu lang
- nicht „Bild von ...“ als Standard
- bei komplexen Abbildungen kurze Beschreibung plus Erklärung im Fließtext

Beispiel:

> Schematische Darstellung des großen und kleinen Blutkreislaufs mit Herz, Lunge und Körperkreislauf.

---

## 27. Word-Barrierefreiheit

### 27.1 Pflichtregeln

- echte Überschriftenhierarchie
- keine Überschriftsebene überspringen
- echte Listen
- Alternativtexte für Bilder
- einfache Tabellen mit Kopfzeile
- klare Linktexte
- ausreichender Farbkontrast
- keine Information nur durch Farbe
- Sprache des Dokuments festlegen
- keine eingescannten Textbilder
- Inhaltsverzeichnis bei längeren Dokumenten
- Dokumenttitel in Eigenschaften setzen

### 27.2 Hyperlinks

Schlecht:

- „hier klicken“
- „Link“
- lange nackte URL im Fließtext

Besser:

- „Leitlinie der Deutschen Gesellschaft für Kardiologie“
- „Microsoft: PowerPoint barrierefrei gestalten“
- „WCAG 2.2 Kontrastanforderungen“

Für Druckversionen kann die URL zusätzlich im Quellenverzeichnis stehen.

---

## 28. Merksatz- und Infoboxen in Word

### 28.1 Merksatzbox

Verwendung:

- zentrale Lernbotschaft
- kurze Zusammenfassung
- Prüfungsanker

Gestaltung:

- dezenter Hintergrund
- linker Akzentstreifen
- nicht zu dunkel
- Text 10,5–11,5 pt
- maximal 4–6 Zeilen
- keine Box über mehr als eine halbe Seite

### 28.2 Achtungsbox

Verwendung:

- fachliche Vorsicht
- medizinische Sicherheitsgrenzen
- Kontextabhängigkeit

Formulierungsbeispiel:

> Diese Darstellung dient der Ausbildung. Für konkrete Versorgungssituationen gelten ärztliche Anordnung, aktuelle Leitlinien und lokale Standards.

---

# Teil E – Gemeinsame Layoutregeln

## 29. Didaktische Reduktion

### 29.1 Ziel

Materialien sollen verständlich machen, nicht Vollständigkeit simulieren.

### 29.2 Regeln

- vom Lernziel her auswählen
- Nebendetails auslagern
- Fachbegriffe erklären
- erst Überblick, dann Details
- Beispiele einbauen
- Wiederholung ermöglichen
- Transferfragen stellen

### 29.3 Drei Ebenen

| Ebene | Präsentation | Handout |
|---|---|---|
| Orientierung | sehr stark | mittel |
| Erklärung | knapp | ausführlich |
| Details/Quellen | wenig | ausführlich |

---

## 30. Sprache

### 30.1 Grundregeln

- aktiv formulieren
- kurze Sätze
- klare Verben
- Fachbegriffe beim ersten Auftreten erklären
- keine unnötigen Nominalisierungen
- keine leeren Floskeln
- keine „Marketing-Sprache“
- keine Scheinsicherheit

### 30.2 Medizinische/pflegerische Sprache

Vermeiden:

- „immer“
- „nie“
- „muss in jedem Fall“
- „die richtige Therapie ist“
- „diagnostiziere“

Besser:

- „häufig“
- „typisch“
- „kann hinweisen auf“
- „im Unterrichtskontext“
- „abhängig von Situation und Standard“
- „ärztliche Anordnung und lokale Standards beachten“

---

## 31. Visualisierungslogik

### 31.1 Visualisierung nur mit Zweck

Eine Grafik muss mindestens eine dieser Funktionen erfüllen:

- Beziehung zeigen
- Ablauf zeigen
- Vergleich erleichtern
- Struktur sichtbar machen
- Aufmerksamkeit lenken
- Erinnerung unterstützen

Wenn sie nur schmückt, sollte sie weg.

### 31.2 Gute Visualisierung

- verständlich ohne lange Erklärung
- beschriftet
- konsistent
- ausreichend groß
- nicht überdekoriert
- mit Quelle versehen
- barrierearm

---

## 32. Quellen und Bildnachweise

### 32.1 Grundregeln

- keine erfundenen Quellen
- keine unklaren Bildquellen
- URLs nicht als winziger Text auf Folien quetschen
- vollständige Quellen im Handout
- Kurztitel auf Quellenfolie
- Abrufdatum für Webseiten
- bei eigenen Darstellungen „eigene Darstellung nach ...“

### 32.2 Quellenfolie PowerPoint

Beispiel:

> Quellen  
> - Microsoft Support: Make your PowerPoint presentations accessible, abgerufen am 15.05.2026  
> - W3C: Web Content Accessibility Guidelines 2.2, 2024/2025  
> - Fachquelle XY: Titel, Jahr

### 32.3 Quellenverzeichnis Word

Beispiel:

> Microsoft Support. Make your PowerPoint presentations accessible to people with disabilities. Abgerufen am 15.05.2026 von https://support.microsoft.com/...

---

# Teil F – Kompatibilitätsrichtlinien für PPTX/DOCX

## 33. Wichtig: Reparaturdialog verhindern

Eine Datei, die nur nach PowerPoint-Reparatur öffnet, gilt als **nicht auslieferbar**.

### 33.1 Pflicht-Gate

Vor Auslieferung muss gelten:

- Datei lässt sich als ZIP öffnen.
- ZIP-Integrität ist fehlerfrei.
- Alle XML-Dateien sind wohlgeformt.
- `[Content_Types].xml` ist vorhanden und plausibel.
- `_rels/.rels` ist vorhanden.
- alle referenzierten Parts existieren.
- keine Relationship verweist ins Leere.
- keine externen Links, wenn nicht ausdrücklich gewünscht.
- alle Folien haben gültige Slide-Parts.
- alle Slide-IDs sind eindeutig.
- Master, Layouts und Themes sind vorhanden und referenziert.
- Medien liegen im Paket und haben gültige Content Types.
- Präsentation rendert in mindestens einem Office-kompatiblen Renderer.
- Keine Reparaturmeldung beim Öffnen in Microsoft PowerPoint, falls PowerPoint-Prüfung verfügbar ist.

### 33.2 Bekannte Ursachen für Reparaturdialoge

- fehlende Bilddateien in `/ppt/media`
- falsche Content-Type-Einträge
- defekte oder doppelte Relationship-IDs
- ungültige XML-Zeichen
- unvollständige Theme-Datei
- fehlerhaft manuell erzeugte Diagramm-XML
- inkonsistente Slide-Master-Referenzen
- OLE-Objekte oder Medien, die nicht korrekt eingebettet wurden
- Shape-Geometrien mit ungültigen Werten
- externe Links auf lokale Pfade
- veraltete oder nicht unterstützte Features
- falsches ZIP-Repacking
- XML-Patches ohne Validierung

### 33.3 Konsequenz

Wenn eine Prüfung fehlschlägt:

1. Datei nicht ausliefern.
2. Fehlerquelle eingrenzen.
3. Datei neu erzeugen oder defekte Komponente entfernen.
4. erneut prüfen.
5. erst dann Downloadlink bereitstellen.

---

## 34. Robuste PPTX-Erzeugung

### 34.1 Sicherer Workflow

1. Sauberes Template oder minimal gültige PPTX verwenden.
2. Folien nur über stabile Bibliothek/API erzeugen.
3. Keine manuellen XML-Patches, außer zwingend notwendig.
4. Wenn XML-Patches nötig sind: danach Open-XML-Validierung.
5. Medien vor Einbettung normalisieren.
6. Nur Standardfonts verwenden.
7. Keine Makros.
8. Keine externen Links.
9. Datei speichern.
10. ZIP- und XML-Prüfung.
11. Rendering-Prüfung.
12. Öffnungstest/PowerPoint-Test, sofern verfügbar.
13. PDF-Export optional zur Sichtkontrolle.
14. Erst danach ausliefern.

### 34.2 Bibliotheksregeln

Bei programmatischer Erstellung:

- keine halbfertigen XML-Fragmente schreiben
- keine IDs selbst raten, wenn Bibliothek sie verwaltet
- Foliengrößen in korrekten Einheiten setzen
- alle Objekte innerhalb der Folie platzieren
- keine Nullbreite/Nullhöhe
- keine negativen Koordinaten
- keine Textbox mit automatisch abgeschnittenem Text
- nach Möglichkeit Standard-Layouts nutzen
- nur unterstützte Formen verwenden
- Bilder über API einfügen, nicht per ZIP-Manipulation

### 34.3 Medienregeln

- Bilder lokal im Paket einbetten
- keine Links auf `/mnt/data`, lokale Pfade oder Web-URLs
- Medien vorher konvertieren:
  - Fotos: JPEG
  - Transparenz/Screenshot/Schemata: PNG
  - Vektor nur nach Kompatibilitätsprüfung
- keine riesigen unskalierten Bilder
- keine Sonderzeichen in Dateinamen
- keine doppelten Medien mit widersprüchlichem Content Type

---

## 35. Robuste DOCX-Erzeugung

### 35.1 Sicherer Workflow

1. Sauberes DOCX-Template oder stabile Bibliothek verwenden.
2. Formatvorlagen definieren.
3. Inhalte strukturieren.
4. Bilder einbetten und beschriften.
5. Tabellen prüfen.
6. Dokumenteigenschaften setzen.
7. Accessibility-Check durchführen.
8. DOCX rendern.
9. Seitenbilder prüfen.
10. Fehler korrigieren.
11. erneut rendern.
12. erst dann ausliefern.

### 35.2 DOCX-Technikregeln

- Keine Textfelder für Fließtext.
- Bilder vorzugsweise „Mit Text in Zeile“.
- Tabellen nicht breiter als Seitenbereich.
- Keine negativen Einzüge.
- Keine manuell erzeugten defekten Felder.
- Inhaltsverzeichnis vor Auslieferung aktualisieren oder statisch sauber setzen.
- Keine Makros.
- Keine verknüpften externen Bilder.
- Dokument muss in Word und LibreOffice möglichst stabil öffnen.

---

## 36. Prüfworkflow vor Auslieferung

## 36.1 PowerPoint-Prüfung

### Pflichtprüfungen

- Dateiendung `.pptx`
- Datei ist ZIP-lesbar
- ZIP-Test bestanden
- XML-Dateien parsebar
- keine fehlenden Medien
- keine externen Relationships
- Foliengröße korrekt
- Folienanzahl plausibel
- Quellenfolie vorhanden
- keine leeren Platzhalter
- keine abgeschnittenen Texte nach Sichtprüfung
- keine Reparaturmeldung, sofern PowerPoint-Test verfügbar

### Sichtprüfung

Mindestens prüfen:

- Titelfolie
- Lernzielfolie
- eine typische Inhaltsfolie
- eine Tabelle/Übersicht
- eine Praxis-/Merksatzfolie
- Zusammenfassung
- Quellenfolie

### Harte Ablehnung

Nicht ausliefern, wenn:

- PowerPoint reparieren muss
- Datei nicht öffnet
- Layout massiv verrutscht
- Texte abgeschnitten sind
- Folien leer wirken
- Quellen fehlen
- Kontrast unlesbar ist

---

## 36.2 Word-Prüfung

### Pflichtprüfungen

- Dateiendung `.docx`
- A4 Hochformat
- echte Formatvorlagen
- Überschriftenhierarchie
- Tabellen nicht abgeschnitten
- Bilder nicht verzerrt
- Quellenverzeichnis vorhanden
- Wiederholungsfragen vorhanden
- Alt-Texte für relevante Bilder
- Seitenzahlen vorhanden
- Renderprüfung als PNG/PDF
- keine sichtbaren Platzhalter

### Harte Ablehnung

Nicht ausliefern, wenn:

- Seiten unlesbar sind
- Tabellen über den Rand laufen
- Layout verrutscht
- Überschriftenstruktur fehlt
- Handout nur Folien kopiert
- wichtige Fachbegriffe nicht erklärt sind
- Quellen fehlen
- Dokument nicht geöffnet oder gerendert werden kann

---

# Teil G – Layoutqualität: Bewertungsraster

## 37. Bewertungsraster für PowerPoint

| Kriterium | 0 Punkte | 1 Punkt | 2 Punkte | 3 Punkte |
|---|---|---|---|---|
| Technische Stabilität | öffnet nicht/repariert | öffnet mit Problemen | öffnet, kleine Warnungen | öffnet sauber |
| Format | falsch | teilweise passend | A4, aber Layout schwach | A4 perfekt genutzt |
| Designsystem | keines | inkonsistent | größtenteils einheitlich | konsequent |
| Lesbarkeit | unlesbar | klein/überladen | meist gut | sehr gut |
| Didaktik | unklar | teilweise | nachvollziehbar | sehr klar |
| Visualisierung | störend | dekorativ | unterstützend | erklärend |
| Quellen | fehlen | unvollständig | vorhanden | sauber |
| Barrierefreiheit | ignoriert | schwach | ordentlich | geprüft und gut |
| Praxistauglichkeit | kaum nutzbar | Nacharbeit nötig | nutzbar | direkt einsatzbereit |

Mindestanforderung: kein Kriterium unter 2, technische Stabilität muss 3 sein.

---

## 38. Bewertungsraster für DOCX

| Kriterium | 0 Punkte | 1 Punkt | 2 Punkte | 3 Punkte |
|---|---|---|---|---|
| Technische Stabilität | öffnet nicht | öffnet fehlerhaft | öffnet | öffnet und rendert sauber |
| Format | falsch | teilweise | A4 hoch | A4 hoch sauber |
| Struktur | chaotisch | teilweise | klar | sehr klar |
| Formatvorlagen | fehlen | uneinheitlich | vorhanden | konsequent |
| Lesbarkeit | schlecht | mäßig | gut | sehr gut |
| Eigenständigkeit | Folienkopie | wenig erklärt | verständlich | sehr gut erklärend |
| Tabellen/Bilder | defekt | schwach | nutzbar | sauber |
| Quellen | fehlen | lückenhaft | vorhanden | sauber |
| Aufgaben | fehlen | oberflächlich | vorhanden | didaktisch passend |

Mindestanforderung: kein Kriterium unter 2, technische Stabilität muss 3 sein.

---

# Teil H – Konkrete Layoutvorgaben für Unterrichtsmaterialien

## 39. Empfohlene PPTX-Struktur für 45–90 Minuten

1. Titel
2. Relevanz/Einstieg
3. Lernziele
4. Agenda
5. Vorwissen aktivieren
6. Grundlagen
7. Fachinhalt 1
8. Fachinhalt 2
9. Fachinhalt 3
10. Praxisbeispiel
11. Beobachtungs-/Transferaufgabe
12. Merksätze
13. Wiederholungsfragen
14. Zusammenfassung
15. Quellen

Für kürzere Einheiten können Folien zusammengelegt werden. Für längere Einheiten eher in Abschnitte teilen.

---

## 40. Empfohlene DOCX-Struktur für 45–90 Minuten

1. Titel
2. Zielgruppe und Thema
3. Lernziele
4. Warum das Thema wichtig ist
5. Grundbegriffe
6. Fachliche Erklärung
7. Übersichtstabelle
8. Praxisbezug
9. Merksätze
10. Typische Fehler/Missverständnisse
11. Wiederholungsfragen
12. Transferaufgabe
13. Zusammenfassung
14. Quellen

---

## 41. Unterrichtsmaterial für Pflege/Medizin

### 41.1 Zusätzliche Anforderungen

- sichere, nicht handlungsanweisende Formulierungen
- Abgrenzung von Unterricht und klinischer Entscheidung
- klare Erklärung von Normalwerten als Orientierungswerte, nicht absolute Diagnosekriterien
- Hinweis auf lokale Standards und ärztliche Anordnung, wo relevant
- keine Therapieempfehlungen für reale Personen
- anonymisierte Praxisfälle
- fachliche Unsicherheit transparent markieren

### 41.2 Formulierungsbausteine

- „Im Unterrichtskontext lässt sich allgemein erklären, dass ...“
- „Typische Beobachtungsaspekte können sein ...“
- „Die genaue Bewertung hängt von Patientensituation, ärztlicher Anordnung und lokalem Standard ab.“
- „Diese Darstellung ersetzt keine klinische Entscheidung.“
- „Bei akuter Gefährdung gelten Notfallstandard und institutionelle Vorgaben.“

---

# Teil I – Export und Dateigröße

## 42. Dateigröße

### 42.1 Richtwerte

| Datei | Zielgröße |
|---|---:|
| einfache PPTX 15 Folien | < 10 MB |
| bildreiche PPTX | < 30 MB |
| einfaches DOCX-Handout | < 5 MB |
| bildreiches DOCX | < 15 MB |

Größer ist nicht automatisch falsch, muss aber begründet sein.

### 42.2 Reduktion

- Bilder vor Einbettung skalieren
- JPEG für Fotos
- PNG für Diagramme
- nicht benötigte Bildbearbeitungsdaten entfernen
- keine doppelten Bilder mehrfach einbetten, wenn vermeidbar
- keine unnötigen Videos
- keine 300-dpi-Fotos, wenn sie nur klein dargestellt werden

---

## 43. PDF-Export

Wenn PDF zusätzlich gewünscht:

- aus finaler PPTX/DOCX exportieren
- PDF nach Export öffnen
- Seitenformat prüfen
- keine abgeschnittenen Inhalte
- Links prüfen
- bei Barrierefreiheit möglichst tagged PDF erzeugen
- PDF nicht als Ersatz für kaputte DOCX/PPTX verwenden

---

# Teil J – Prompt-/KI-Regeln für künftige Erstellung

## 44. Verbindliche Arbeitsanweisung für einen Unterrichtsmaterial-Generator

Bei jeder neuen PPTX/DOCX-Erstellung muss der Generator:

1. Thema und Zielgruppe erkennen.
2. Standardannahmen nennen, falls Angaben fehlen.
3. Designsystem definieren.
4. Inhaltliche Struktur erstellen.
5. Präsentation knapp halten.
6. Handout ausführlicher machen.
7. Quellen dokumentieren.
8. Dateien tatsächlich erzeugen.
9. Technische Validität prüfen.
10. Visuelle Renderprüfung durchführen.
11. Fehler korrigieren.
12. Downloadlinks erst nach Prüfung ausgeben.
13. Ehrlich sagen, wenn eine Prüfung nicht möglich war.

### 44.1 Verbotene Abschlussformulierungen

Nicht schreiben:

- „geprüft“, wenn nur Datei gespeichert wurde
- „PowerPoint-kompatibel“, wenn kein Öffnungs-/Validierungstest erfolgte
- „barrierefrei“, wenn nur grob gestaltet wurde
- „professionelles Layout“, wenn kein Designsystem verwendet wurde

Besser:

- „ZIP/XML-Prüfung bestanden; PowerPoint-Öffnungstest in dieser Umgebung nicht möglich.“
- „Renderprüfung durchgeführt; keine abgeschnittenen Inhalte sichtbar.“
- „Barrierearm nach Checkliste gestaltet, aber nicht zertifiziert barrierefrei.“

---

# Teil K – Checklisten

## 45. PowerPoint-Checkliste vor Download

### Technisch

- [ ] `.pptx`, nicht `.pptm`
- [ ] A4 quer, 29,7 × 21,0 cm
- [ ] ZIP-Test bestanden
- [ ] XML parsebar
- [ ] keine fehlenden Medien
- [ ] keine externen Bildlinks
- [ ] keine Makros
- [ ] keine Reparaturmeldung bekannt
- [ ] Datei öffnet in mindestens einem Renderer
- [ ] PDF/Screenshot-Render zur Sichtprüfung erzeugt, wenn möglich

### Layout

- [ ] einheitliche Titelposition
- [ ] einheitliche Fußzeile
- [ ] ausreichende Ränder
- [ ] keine Textüberläufe
- [ ] keine leeren Platzhalter
- [ ] ruhige Farben
- [ ] ausreichender Kontrast
- [ ] Schriftgrößen passend
- [ ] Tabellen lesbar
- [ ] Diagramme beschriftet
- [ ] Bilder nicht verzerrt

### Didaktik

- [ ] Lernziele vorhanden
- [ ] Agenda vorhanden
- [ ] eine Kernaussage pro Folie
- [ ] Praxisbezug vorhanden
- [ ] Merksätze vorhanden
- [ ] Wiederholungsfragen vorhanden
- [ ] Zusammenfassung vorhanden
- [ ] Quellenfolie vorhanden

### Barrierefreiheit

- [ ] Folientitel eindeutig
- [ ] Lesereihenfolge logisch
- [ ] Alt-Texte für relevante Bilder
- [ ] keine Information nur durch Farbe
- [ ] Linktexte verständlich
- [ ] Kontrast ausreichend

---

## 46. DOCX-Checkliste vor Download

### Technisch

- [ ] `.docx`
- [ ] A4 hoch
- [ ] ZIP/XML grundsätzlich intakt
- [ ] keine Makros
- [ ] keine externen Bildlinks
- [ ] Datei öffnet
- [ ] Renderprüfung erfolgt
- [ ] Tabellen laufen nicht über Seitenrand
- [ ] Bilder korrekt eingebettet
- [ ] Seitenzahlen vorhanden

### Layout

- [ ] Formatvorlagen verwendet
- [ ] Überschriftenhierarchie logisch
- [ ] ausreichende Ränder
- [ ] lesbare Schrift
- [ ] ausreichender Zeilenabstand
- [ ] Absätze nicht überladen
- [ ] Merksätze klar abgesetzt
- [ ] Tabellen sauber
- [ ] Abbildungen beschriftet
- [ ] Quellenverzeichnis sauber

### Didaktik

- [ ] Lernziele vorhanden
- [ ] Einführung vorhanden
- [ ] Fachbegriffe erklärt
- [ ] Beispiele vorhanden
- [ ] Merksätze vorhanden
- [ ] Wiederholungsfragen vorhanden
- [ ] Transferaufgabe vorhanden
- [ ] Zusammenfassung vorhanden
- [ ] Handout ist keine Folienkopie

### Barrierefreiheit

- [ ] echte Überschriften
- [ ] echte Listen
- [ ] Alt-Texte
- [ ] einfache Tabellen mit Kopfzeile
- [ ] klare Linktexte
- [ ] ausreichender Kontrast
- [ ] Sprache gesetzt
- [ ] Dokumenttitel gesetzt

---

# Teil L – Konkrete Standards für künftige Dateien

## 47. Standard für PowerPoint-Dateien

Jede neue Unterrichtspräsentation soll standardmäßig so aussehen:

- A4 Querformat
- heller Hintergrund
- dunkler Text
- ruhige Akzentfarbe
- klare Titelleiste oder konsistente Titelzone
- 12–16 mm Rand
- maximal 5 Punkte pro Folie
- Karten, Infoboxen und einfache Diagramme statt Textwüsten
- professionelle Icons nur sparsam
- keine Clipart
- keine dekorative Überfrachtung
- Fußzeile mit Modul, Seite, ggf. Kurzquelle
- Quellenfolie am Ende

## 48. Standard für Word-Handouts

Jedes neue Handout soll standardmäßig so aussehen:

- A4 Hochformat
- 2–2,5 cm Seitenränder
- klare Formatvorlagen
- Titelblatt oder kompakter Titelkopf
- Lernziele als Liste
- gut gegliederte Abschnitte
- Infoboxen für Merksätze
- Tabellen nur bei echtem Nutzen
- Praxisfälle in abgesetzten Boxen
- Fragen am Ende
- Quellenverzeichnis
- Seitenzahlen
- druckfreundlich in Farbe und Graustufen

---

# Teil M – Beispiele für gute Gestaltung

## 49. Beispiel: Schlechte Folie

Titel: „Herz-Kreislauf-System“

Inhalt:

- Das Herz ist ein muskuläres Hohlorgan, das sich aus verschiedenen Schichten zusammensetzt und Blut durch den Körper pumpt, wobei verschiedene Kreisläufe und Klappen beteiligt sind ...
- Arterien führen Blut vom Herzen weg ...
- Venen führen Blut zum Herzen ...
- Blutdruck ...
- Puls ...
- Pflegebeobachtung ...
- Erkrankungen ...

Problem:

- zu viel Inhalt
- keine Kernaussage
- keine Struktur
- keine visuelle Orientierung

## 50. Beispiel: Gute Folie

Titel:

> Das Herz hält den Blutfluss durch rhythmisches Pumpen aufrecht

Inhalt als 3 Karten:

1. **Pumpe:** erzeugt Druck und Blutfluss  
2. **Klappen:** lenken den Blutstrom  
3. **Gefäße:** verteilen und sammeln Blut  

Merksatz unten:

> Ohne Herzleistung, Gefäßsystem und Blutvolumen ist kein stabiler Kreislauf möglich.

---

## 51. Beispiel: Schlechter Handout-Abschnitt

> Das Herz-Kreislauf-System besteht aus Herz und Gefäßen. Es pumpt Blut. Arterien gehen weg. Venen gehen hin. Kapillaren tauschen aus. Der Blutdruck ist wichtig.

Problem:

- zu knapp
- unpräzise
- keine Zusammenhänge
- nicht lernförderlich

## 52. Beispiel: Guter Handout-Abschnitt

> Das Herz-Kreislauf-System versorgt Organe und Gewebe mit Sauerstoff und Nährstoffen und transportiert Stoffwechselprodukte ab. Das Herz wirkt dabei als Pumpe. Die Gefäße bilden das Leitungssystem. Arterien führen Blut vom Herzen weg, Venen führen Blut zum Herzen zurück. In den Kapillaren findet der Austausch zwischen Blut und Gewebe statt. Für die Pflege ist wichtig, Messwerte wie Puls und Blutdruck immer im Zusammenhang mit Beobachtungen wie Hautfarbe, Bewusstsein, Atmung, Schwindel oder Belastbarkeit zu betrachten.

---

# Teil N – Quellen und Referenzen

Diese Richtlinie stützt sich auf aktuelle, allgemein anerkannte Best Practices aus Office-Dokumentation, Barrierefreiheitsstandards, Plain-Language-Leitlinien, UX-/Lesbarkeitsliteratur und didaktischen UDL-Grundlagen.

## 53. Hauptquellen

1. Microsoft Support: Make your PowerPoint presentations accessible to people with disabilities  
   https://support.microsoft.com/en-us/office/make-your-powerpoint-presentations-accessible-to-people-with-disabilities-6f7772b2-2f33-4bd2-8ca7-dae3b2b3ef25

2. Microsoft Support: Make your Word documents accessible to people with disabilities  
   https://support.microsoft.com/en-us/office/make-your-word-documents-accessible-to-people-with-disabilities-d9bf3683-87ac-47ea-b91a-78dcacb3c66d

3. Microsoft Support: Improve accessibility with the Accessibility Checker  
   https://support.microsoft.com/en-us/office/improve-accessibility-with-the-accessibility-checker-a16f6de0-2f39-4a2b-8bd8-5ad801426c7f

4. Microsoft Support: Rules for the Accessibility Checker  
   https://support.microsoft.com/de-de/accessibility/office-accessibility/rules-for-the-accessibility-checker

5. W3C/WAI: Web Content Accessibility Guidelines (WCAG) 2.2  
   https://www.w3.org/TR/WCAG22/

6. W3C/WAI: WCAG 2 Overview  
   https://www.w3.org/WAI/standards-guidelines/wcag/

7. Microsoft Learn: Open XML SDK for Office  
   https://learn.microsoft.com/en-us/office/open-xml/open-xml-sdk

8. Microsoft Learn: Structure of a PresentationML document  
   https://learn.microsoft.com/en-us/office/open-xml/presentation/structure-of-a-presentationml-document

9. Microsoft Learn: Troubleshoot a damaged presentation in PowerPoint  
   https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/powerpoint/damaged-presentation

10. Microsoft Support: Reduce the file size of your PowerPoint presentations  
    https://support.microsoft.com/en-us/office/reduce-the-file-size-of-your-powerpoint-presentations-9548ffd4-d853-41e7-8e40-b606bca036b4

11. Nielsen Norman Group: Legibility, Readability, and Comprehension  
    https://www.nngroup.com/articles/legibility-readability-comprehension/

12. Nielsen Norman Group: Typography for Glanceable Reading  
    https://www.nngroup.com/articles/glanceable-fonts/

13. Digital.gov: Lists – Plain Language  
    https://digital.gov/guides/plain-language/design/lists

14. U.S. Office of Personnel Management: Plain Language  
    https://www.opm.gov/information-management/plain-language/

15. GOV.UK: Content design – Writing for GOV.UK  
    https://www.gov.uk/guidance/content-design/writing-for-gov-uk

16. CAST: Universal Design for Learning Guidelines 3.0  
    https://udlguidelines.cast.org

---

# Teil O – Definition of Done

Eine PPTX/DOCX-Datei ist erst fertig, wenn alle folgenden Aussagen wahr sind:

## 54. PowerPoint

- Die Datei ist eine gültige `.pptx`.
- Sie öffnet ohne Reparaturdialog.
- Sie hat DIN A4 Querformat.
- Sie nutzt ein konsistentes Designsystem.
- Sie enthält keine abgeschnittenen Texte.
- Sie enthält keine leeren Platzhalter.
- Sie ist lesbar und kontrastreich.
- Sie enthält Lernziele, Agenda, Fachinhalte, Praxisbezug, Zusammenfassung und Quellen.
- Sie enthält keine unnötigen Animationen oder Makros.
- Sie ist technisch geprüft.
- Sie ist visuell geprüft.

## 55. Word

- Die Datei ist eine gültige `.docx`.
- Sie öffnet und rendert sauber.
- Sie hat DIN A4 Hochformat.
- Sie nutzt echte Formatvorlagen.
- Sie ist kein Folienausdruck.
- Tabellen und Bilder sind sauber eingebunden.
- Sie enthält Lernziele, Einführung, Fachinhalte, Begriffe, Merksätze, Beispiele, Fragen, Zusammenfassung und Quellen.
- Sie ist druckfreundlich.
- Sie ist barrierearm aufgebaut.
- Sie ist technisch geprüft.
- Sie ist visuell geprüft.

---

# Teil P – Kurzfassung als harte Produktionsregeln

1. **Erst Designsystem, dann Datei.**
2. **Keine Datei ohne technische Prüfung.**
3. **Keine PPTX mit Reparaturdialog ausliefern.**
4. **Keine DOCX ohne Renderprüfung ausliefern.**
5. **Systemfonts statt exotischer Fonts.**
6. **Bilder einbetten, nicht verlinken.**
7. **Keine Makros.**
8. **A4 quer für PPTX, A4 hoch für DOCX.**
9. **Präsentation knapp, Handout erklärend.**
10. **Quellen nachvollziehbar dokumentieren.**
11. **Barrierefreiheit von Anfang an mitdenken.**
12. **Lesbarkeit schlägt Dekoration.**
13. **Weißraum ist Pflicht.**
14. **Tabellen nur, wenn sie lesbar bleiben.**
15. **Bei medizinischen Themen sicher und kontextabhängig formulieren.**
16. **Abschlussantwort muss ehrlich sagen, was geprüft wurde und was nicht.**

---

_Ende der Richtlinie._
