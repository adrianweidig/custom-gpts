# Beispielantwort: vollständige Code-Review mit Refactoring- und Testvorschlag

## Nutzerauftrag

> Reviewe diese Python-Funktion. Sie liest Bestellungen aus CSV-Zeilen und berechnet den Gesamtbetrag. Bitte priorisiere echte Bugs vor Stilfragen und schlage Tests vor.

## Annahmen

- `row` stammt aus einer CSV-Datei und enthält genau drei Spalten: Bestell-ID, Menge, Einzelpreis.
- Negative Mengen und negative Preise sind fachlich nicht erlaubt.
- Eine leere Bestellliste darf fachlich `0.0` ergeben, solange dieses Verhalten dokumentiert ist.

## Findings

| Priorität | Stelle | Problem | Warum relevant | Minimaler Fix |
|---|---|---|---|---|
| P1 | `parse_order()` | Mengen `0` oder kleiner werden ohne Validierung akzeptiert. | Negative Mengen können Gesamtbeträge manipulieren oder Retouren unabsichtlich als Bestellung zählen. | Nach `int()` prüfen: `quantity > 0`. |
| P1 | `parse_order()` | Negative Einzelpreise werden akzeptiert. | Negative Preise senken Summen und können Abrechnungsdaten verfälschen. | Nach `float()` prüfen: `unit_price >= 0`. |
| P2 | `parse_order()` | Fehlende oder zusätzliche Spalten erzeugen unklare Fehler. | CSV-Importe scheitern dann mit schwer diagnostizierbaren Exceptions. | Zeilenlänge vor Entpacken prüfen und klare `ValueError` werfen. |
| P2 | `parse_order()` | Konvertierungsfehler werden nicht fachlich eingeordnet. | `ValueError` von `int()`/`float()` ist technisch korrekt, aber für Nutzer oder Logs wenig sprechend. | Optional mit Kontext neu werfen, wenn Importdiagnose wichtig ist. |

## Empfohlener Minimalcode

```python
def parse_order(row):
    """Parse one CSV row into an order dict."""
    if len(row) != 3:
        raise ValueError("expected order row with id, quantity and unit_price")

    order_id, quantity_raw, unit_price_raw = row
    quantity = int(quantity_raw)
    unit_price = float(unit_price_raw)

    if quantity <= 0:
        raise ValueError("quantity must be positive")
    if unit_price < 0:
        raise ValueError("unit_price must not be negative")

    return {
        "order_id": order_id,
        "quantity": quantity,
        "unit_price": unit_price,
    }
```

## Passende Regressionstests

| Test | Zweck | Erwartung |
|---|---|---|
| gültige Zeile | Happy Path absichern | Dict mit korrekten Typen |
| fehlende Spalte | CSV-Struktur validieren | `ValueError` mit verständlicher Meldung |
| Menge `0` | fachliche Grenze | `ValueError` |
| negative Menge | Manipulations-/Datenfehler verhindern | `ValueError` |
| negativer Preis | verfälschte Summe verhindern | `ValueError` |
| mehrere gültige Zeilen | Summenlogik prüfen | korrekte Gesamtsumme |

## Beispieltests

Siehe `beispiel_test.py`. Die Tests prüfen genau die oben genannten Risiken und sind bewusst klein gehalten, damit sie als Vorlage für andere Reviewfälle dienen.

## Nicht empfohlene Änderungen

- Kein Klassenmodell einführen, solange die Datenstruktur klein bleibt.
- Keine Rundungslogik erfinden, wenn Fachlogik zu Währung, Steuer oder Nachkommastellen fehlt.
- Keine automatische Fehlerkorrektur von CSV-Zeilen ohne klare Fachregel.

## Restrisiko

Ohne Domänenkontext bleibt offen, ob `unit_price = 0` erlaubt ist, etwa für kostenlose Artikel oder Kulanzbuchungen. Diese Regel sollte fachlich entschieden und dann als Test ergänzt werden.
