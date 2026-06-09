# Code-Review Refactoring Coach

Sprachen: [Deutsch](README.md) | [English](README.en.md)

Lokaler Projektordner für einen Custom GPT zur strukturierten Code-Review-, Refactoring- und Wartbarkeitsanalyse.

## Status

Konzipiertes GPT-Paket ohne öffentlichen ChatGPT-Link.

## Zweck

Dieser GPT prüft Codeänderungen, einzelne Dateien oder kleine Komponenten auf Verständlichkeit, Wartbarkeit, Fehleranfälligkeit, Testbarkeit, Sicherheit und sinnvolle Refactoring-Optionen. Er soll keine unnötigen Stilpräferenzen aufzwingen, sondern konkrete Risiken und Verbesserungen priorisieren.

## Enthaltene Dateien

- `customgpt_infos.md`: Name, Zielgruppe, Einsatzgebiete, Konfigurationshinweise und Testfälle.
- `fachwissen.md`: Review-Kriterien, Refactoring-Regeln, Risikobewertung und Teststrategie.
- `systemprompt.md`: Hauptlogik für Review-Verhalten, Ausgabeformat, Grenzen und Sicherheitsregeln.
- `bootloader.md`: kompakter Hinweistext für das Instructions-Feld.
- `beispiel.md`: Musterantwort für eine kompakte Code-Review.
- `beispiel.py`: bewusst kleines Beispielmodul für Review- und Refactoring-Demonstrationen.
- `beispiel_test.py`: passende Beispieltests zum Beispielmodul.

## Typische Nutzung

- Pull-Request-Review vorbereiten
- Legacy-Code refaktorieren
- Tests für kritische Randfälle ableiten
- Wartbarkeitsrisiken priorisieren
- Sicherheits- und Robustheitsprobleme in kleinen Codeausschnitten erkennen

## Voraussetzungen

- Der Nutzer stellt Code oder einen Diff bereit.
- Sprache, Laufzeit und Zielverhalten sollten angegeben werden, wenn sie relevant sind.
- Für produktive Änderungen bleiben lokale Tests und menschliche Review verbindlich.

## Hinweise

- Keine echten Secrets oder produktiven Kundendaten in Codebeispiele einfügen.
- Der GPT soll keine öffentlichen APIs, CLI-Flags oder Datenformate ohne ausdrücklichen Auftrag verändern.
- Bei Sicherheitsbefunden zuerst Risiko, betroffene Stelle und minimalen Fix erklären.
