from logger import get_logger
from exceptions import ExtractionError
from pathlib import Path
import csv

logger = get_logger(__name__, Path("logs/errors.log"))

def extract(csv_file: Path) -> list[dict]:
    """
    Extracts the raw shipment data from a CSV file.

    Args:
        csv_file (Path): Path to the CSV file containing shipment records.
    
    Returns:
        list[dict]: All rows from the CSV as dictionaries.
    """
    try:
        with open(csv_file, "r") as f:
            content = list(csv.DictReader(f))
        logger.info(f"Extracted {len(content)} rows from {csv_file}")
        return content
    except FileNotFoundError as e:
        logger.error(f"File not found: {csv_file}")
        raise ExtractionError(f"File not found: {csv_file}") from e
    except csv.Error as e:
        logger.error(f"CSV contains malformed data: {csv_file}")
        raise ExtractionError(f"CSV contains malformed data: {csv_file}") from e