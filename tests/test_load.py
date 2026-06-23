from unittest.mock import patch, MagicMock
from load import load
import pytest
from exceptions import LoadError
import psycopg2

@patch("load.execute_values")
@patch("load.psycopg2.connect")
def test_load(mock_connect, mock_execute_values):
    fake_cursor = MagicMock()
    fake_conn = MagicMock()
    fake_conn.cursor.return_value.__enter__.return_value = fake_cursor

    mock_connect.return_value.__enter__.return_value = fake_conn

    load([{"shipment_id": "S001", "destination": "Monterey", "weight_kg": 5.0, "status": "delivered"}])

    mock_execute_values.assert_called_once_with(fake_cursor, """
                    INSERT INTO shipments (shipment_id, destination, weight_kg, status) 
                    VALUES %s
                """, [("S001", "Monterey", 5.0, "delivered")])
    
@patch("load.execute_values")
@patch("load.psycopg2.connect")
def test_pyscopg2_error(mock_connect, mock_execute_values):
    fake_cursor = MagicMock()
    fake_conn = MagicMock()
    fake_conn.cursor.return_value.__enter__.return_value = fake_cursor

    mock_connect.return_value.__enter__.return_value = fake_conn
    mock_execute_values.side_effect = psycopg2.Error("connection failed")

    with pytest.raises(LoadError, match="DB Error"):
        load([{"shipment_id": "S001", "destination": "Monterey", "weight_kg": 5.0, "status": "delivered"}])
        
def test_missing_key():
    with pytest.raises(LoadError, match="Missing keys"):
        load([{"shipment_id": "S001", "destination": "Monterey", "status": "delivered"}])