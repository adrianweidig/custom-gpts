# Beispielantwort: kompakte Code-Review

## Ausgangslage

Der Nutzer liefert eine Funktion, die Bestellungen aus CSV-Zeilen einliest und Summen berechnet. Der Code ist lauffähig, behandelt aber ungültige Eingaben schlecht.

## Findings

| Priorität | Stelle | Problem | Fix |
|---|---|---|---|
| P1 | `parse_order()` | Negative Mengen werden akzeptiert und senken dadurch die Gesamtsumme. | Menge nach der Konvertierung gegen `> 0` validieren. |
| P2 | `parse_order()` | Fehlende Spalten erzeugen schwer verständliche Indexfehler. | Länge der Zeile prüfen und eine klare `ValueError` werfen. |
| P2 | `total_amount()` | Leere Eingabe wird still zu `0.0`; je nach Fachlogik kann das korrekt oder ein Datenfehler sein. | Verhalten explizit dokumentieren oder optional validieren. |

## Minimaler Fix

```python
def parse_order(row):
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

## Tests

- gültige Zeile mit positiver Menge
- fehlende Spalte
- negative Menge
- negativer Preis
- leere Liste für `total_amount()`, wenn `0.0` fachlich erlaubt ist

## Restrisiko

Ohne Projektkontext ist unklar, ob leere Bestelllisten erlaubt sind. Das sollte fachlich entschieden und anschließend als Test festgehalten werden.
