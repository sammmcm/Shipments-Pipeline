from logger import get_logger
from exceptions import TransformationError
from pathlib import Path

logger = get_logger(__name__, Path("logs/errors.log"))

def transform(data: list[dict]) -> list[dict]:
    """
    Validates and transforms bad shipments data.

    Args:
        data (list[dict]): Raw shipment data.
    
    Returns:
        list[dict]: Clean shipment data.
    """
    if not data:
        raise TransformationError("Shipment list is empty.")

    clean_data = []

    for row in data:
        if not row["shipment_id"]:
            logger.warning(f"Skipping row with missing shipment_id: {row}")
            continue

        if not row["status"]:
            logger.warning(f"Skipping shipment {row['shipment_id']}: doesn't have a status.")
            continue

        if not row["destination"]:
            logger.warning(f"Skipping shipment {row['shipment_id']}: doesn't have a destination.")
            continue
        
        try:
            weight = float(row["weight_kg"])

            if weight > 0:
                row = {**row, "weight_kg": weight}
                clean_data.append(row)
            else:
                logger.warning(f"Skipping shipment {row['shipment_id']}: negative weight = {row['weight_kg']}")
        except ValueError:
            logger.warning(f"Skipping shipment {row['shipment_id']}: invalid value weight = {row['weight_kg']}")

    logger.info(f"Cleaned {len(clean_data)} rows in data.")
    return clean_data