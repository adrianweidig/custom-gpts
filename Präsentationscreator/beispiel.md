# Beispiel: Mustervorlage für eine Web-Präsentation

## Beispielauftrag

> Erstelle eine browserbasierte Präsentation für einen 7-Minuten-Pitch: „Warum unser Team ein internes Wissensportal braucht“. Zielgruppe ist Management. Die Ausgabe soll als einzelne HTML-Datei funktionieren, modern wirken und eine klare Storyline haben.

## Musterantwort

## Konzept

| Element | Entscheidung |
|---|---|
| Ziel | Zustimmung für einen Pilot des Wissensportals |
| Zielgruppe | Management und Teamleitung |
| Ton | sachlich, entscheidungsorientiert, visuell ruhig |
| Dauer | 7 Minuten |
| Format | eine HTML-Datei ohne Build-Prozess |
| Interaktion | Pfeiltasten und sichtbare Fortschrittsanzeige |

## Storyline

1. Problem: Wissen ist verteilt und kostet Zeit.
2. Auswirkung: Support, Onboarding und Qualität leiden.
3. Lösung: kuratiertes internes Wissensportal.
4. Pilot: klein starten, messbar auswerten.
5. Entscheidung: Freigabe für vier Wochen Pilot.

## Folienstruktur

| Folie | Titel | Kernaussage | Visual |
|---|---|---|---|
| 1 | Wissen finden statt suchen | Das Team verliert Zeit in Chats, Tickets und Einzeldateien. | Split aus Suchaufwand und Zielzustand |
| 2 | Der aktuelle Zustand | Informationen liegen verteilt und ohne Ownership. | Drei Spalten: Chat, Ticket, Datei |
| 3 | Der Zielzustand | Ein kuratiertes Portal bündelt verlässliche Antworten. | Zentrum mit Wissensknoten |
| 4 | Pilot in vier Wochen | Wir starten klein und messen Nutzen. | Timeline |
| 5 | Entscheidung | Freigabe für Pilot, Owner und Messkriterien. | Entscheidungskarte |

## Beispiel-HTML-Ausschnitt

```html
<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Wissensportal Pitch</title>
  <style>
    :root {
      --bg: #0f172a;
      --panel: #f8fafc;
      --accent: #14b8a6;
      --text: #e5e7eb;
      --muted: #94a3b8;
    }
    body {
      margin: 0;
      font-family: system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
    }
    .slide {
      min-height: 100vh;
      display: grid;
      place-items: center;
      padding: 6vw;
    }
    .content {
      max-width: 1080px;
      width: 100%;
    }
    h1 {
      font-size: clamp(3rem, 8vw, 6.5rem);
      line-height: 0.95;
      margin: 0 0 1.5rem;
    }
    p {
      font-size: clamp(1.2rem, 2vw, 1.6rem);
      color: var(--muted);
      max-width: 780px;
    }
    .decision {
      background: var(--panel);
      color: #0f172a;
      border-left: 10px solid var(--accent);
      padding: 2rem;
      border-radius: 8px;
      margin-top: 2rem;
    }
  </style>
</head>
<body>
  <section class="slide">
    <div class="content">
      <h1>Wissen finden statt suchen</h1>
      <p>Ein internes Wissensportal reduziert Suchzeit, beschleunigt Onboarding und macht Antworten überprüfbar.</p>
      <div class="decision">
        <strong>Entscheidung heute:</strong> vier Wochen Pilot mit klarer Ownership und messbaren Supportfragen.
      </div>
    </div>
  </section>
</body>
</html>
```

## Qualitätscheck

- H1 ist groß genug für Präsentationsmodus.
- Keine Textwände.
- Jede Folie hat genau eine Kernaussage.
- Entscheidung ist sichtbar.
- HTML funktioniert ohne Build-Prozess.
- Keine externen Assets oder lokalen Pfade.

## Hinweise zur Weiterarbeit

Für eine vollständige Präsentation müssten die fünf Folien ausgearbeitet, Tastaturnavigation ergänzt und die Darstellung in Desktop- und Mobilansicht geprüft werden.
