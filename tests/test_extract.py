import pytest
from exceptions import ExtractionError
from extract import extract
from pathlib import Path

def test_extract_valid_file_and_content(tmp_path):
    csv_file = tmp_path /"shipments.csv"
    csv_file.write_text("shipment_id,destination,weight_kg,status\nS001,Monterey,5.0,delivered\n")

    result = extract(csv_file)
    assert len(result) == 1
    assert result[0]["shipment_id"] == "S001"

def test_extract_no_content(tmp_path):
    csv_file = tmp_path /"shipments.csv"
    csv_file.write_text("shipment_id,destination,weight_kg,status")

    result = extract(csv_file)
    assert len(result) == 0

def test_extract_invalid_file():
    with pytest.raises(ExtractionError, match="File not found"):
        extract(Path("data/shiments.csv"))