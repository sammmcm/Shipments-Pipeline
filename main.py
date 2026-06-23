from exceptions import PipelineError
from logger import get_logger
from pathlib import Path
from extract import extract
from transform import transform
from load import load

logger = get_logger(__name__, Path("logs/errors.log"))

csv_file = Path("data/shipments.csv")

def run() -> None:
    try:
        raw = extract(csv_file)
        clean = transform(raw)
        load(clean)
    except PipelineError as e:
        logger.critical(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run()