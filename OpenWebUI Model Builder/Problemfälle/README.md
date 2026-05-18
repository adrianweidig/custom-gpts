# Offline-Problemfall-Briefings für den OpenWebUI Model Builder

Dieser Ordner enthält Markdown-Briefings für allgemeine OpenWebUI-Aufgabenmodelle. Jede Datei ist als Eingabe für den Custom GPT `OpenWebUI Model Builder` formuliert.

Die Briefings sind bewusst **offline-first**:

- keine Websuche
- keine externe RAGFlow-/RAG-Abhängigkeit
- keine verpflichtenden Knowledge Bases
- Basismodell immer `coder`
- Jupyter/Python-Code-Interpreter als zentrale Zusatzfähigkeit

## Nutzung

1. Wähle ein Briefing aus, das zum gewünschten Aufgabenmodell passt.
2. Gib den Inhalt an den `OpenWebUI Model Builder` weiter.
3. Prüfe die erzeugte Modellkonfiguration vor dem Import in OpenWebUI.

Die Nutzer sollen später in OpenWebUI nicht nach Basismodellen wählen, sondern nach Problemen, zum Beispiel:

- „Ich muss ein Dokument analysieren.“
- „Ich muss eine Präsentation erstellen.“
- „Ich brauche Codegenerierung.“
- „Ich möchte Logs auswerten.“
- „Ich möchte ein Support-Ticket vorbereiten.“

## Wichtige Dateien

- `00_INDEX.md`: Übersicht über alle Problemfälle.
- `01_...` bis `25_...`: einzelne Briefings für konkrete Aufgabenmodelle.

## Hinweise

- Technische Modell-IDs und Dateinamen sind bewusst slug-fähig und werden nicht eingedeutscht.
- Die Briefings sind Vorlagen. Prüfe sie vor dem produktiven Einsatz gegen die konkrete OpenWebUI-Umgebung.
