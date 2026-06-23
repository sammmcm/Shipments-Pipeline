from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extras import execute_values
from logger import get_logger
from pathlib import Path
from exceptions import LoadError

load_dotenv()

logger = get_logger(__name__, Path("logs/errors.log"))

def load(data: list[dict]) -> None:
    """
    Loads the clean data into the table shipments.

    Args:
        data (list[dict]): Clean shipments data.
    
    Returns:
        None
    """
    conn = None
    try:
        structured_data = [
            (row["shipment_id"], row["destination"], row["weight_kg"], row["status"])
            for row in data
        ]
        with psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        ) as conn:
            with conn.cursor() as cursor:
                execute_values(cursor, """
                    INSERT INTO shipments (shipment_id, destination, weight_kg, status) 
                    VALUES %s
                """, structured_data)
                logger.info(f"Inserted {cursor.rowcount} rows into shipments.")
    except psycopg2.Error as e:
        logger.error(f"DB Error: {e}")
        raise LoadError(f"DB Error: {e}") from e
    except KeyError as e:
        logger.error(f"Missing keys in data: {e}")
        raise LoadError(f"Missing keys in data: {e}") from e
    finally:
        if conn:
            conn.close()