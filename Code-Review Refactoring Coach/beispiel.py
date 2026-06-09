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


def total_amount(rows):
    orders = [parse_order(row) for row in rows]
    return sum(order["quantity"] * order["unit_price"] for order in orders)
