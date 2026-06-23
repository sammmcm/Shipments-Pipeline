import pytest
from transform import transform
from exceptions import TransformationError

@pytest.fixture
def valid_row():
    return {"shipment_id": "S001", "destination": "Monterey", "weight_kg": "5.0", "status": "delivered"}

def test_transform_valid_row(valid_row):
    result = transform([valid_row])
    assert len(result) == 1

@pytest.mark.parametrize("weight_kg, expected_len", [
    ("5.0", 1),
    ("-5.0", 0),
    ("five", 0),
    ("0", 0)
])

def test_transform_invalid_weight_validation(valid_row, weight_kg, expected_len):
    valid_row["weight_kg"] = weight_kg
    result = transform([valid_row])
    assert len(result) == expected_len

def test_transform_invalid_shipment_id(valid_row):
    valid_row["shipment_id"] = ""
    result = transform([valid_row])
    assert len(result) == 0

def test_transform_invalid_destination(valid_row):
    valid_row["destination"] = ""
    result = transform([valid_row])
    assert len(result) == 0

def test_transform_invalid_status(valid_row):
    valid_row["status"] = ""
    result = transform([valid_row])
    assert len(result) == 0

def test_transform_empty_list():
    with pytest.raises(TransformationError):
        transform([])