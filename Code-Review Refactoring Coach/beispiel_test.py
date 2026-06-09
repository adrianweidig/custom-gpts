import pytest

from beispiel import parse_order, total_amount


def test_parse_order_accepts_valid_row():
    assert parse_order(["A-100", "2", "19.50"]) == {
        "order_id": "A-100",
        "quantity": 2,
        "unit_price": 19.50,
    }


def test_parse_order_rejects_missing_columns():
    with pytest.raises(ValueError, match="expected order row"):
        parse_order(["A-100", "2"])


def test_parse_order_rejects_non_positive_quantity():
    with pytest.raises(ValueError, match="quantity must be positive"):
        parse_order(["A-100", "0", "19.50"])


def test_parse_order_rejects_negative_price():
    with pytest.raises(ValueError, match="unit_price"):
        parse_order(["A-100", "2", "-1"])


def test_total_amount_sums_rows():
    rows = [["A-100", "2", "10"], ["A-101", "3", "5"]]
    assert total_amount(rows) == 35
