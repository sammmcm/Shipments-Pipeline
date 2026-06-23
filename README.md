# Shipments ETL Pipeline

A modular ETL pipeline that extracts shipment records from a CSV file, validates and transforms the data, and loads clean records into a PostgreSQL database.

## Tech Stack

- Python 3.x
- PostgreSQL + psycopg2
- pytest

## Project Structure

```
shipments_pipeline/
├── data/
│   └── shipments.csv       # Input file with shipment records
├── sql/
│   └── create_table.sql    # DDL to create the shipments table
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── exceptions.py           # Custom pipeline exceptions
├── logger.py               # Centralized logger
├── extract.py              # Reads CSV into list of dicts
├── transform.py            # Validates and cleans rows
├── load.py                 # Inserts clean rows into PostgreSQL
├── main.py                 # Pipeline entrypoint
├── conftest.py             # Adds root to sys.path for pytest
├── requirements.txt
└── .env
```

## Setup

### 1. Clone the repo and create a virtual environment

```bash
git clone https://github.com/sammmcm/shipments-pipeline.git
cd shipments-pipeline
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the root directory:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

### 3. Create the database table

```bash
psql -U your_user -d your_database -f sql/create_table.sql
```

### 4. Run the pipeline

```bash
python main.py
```

## Running Tests

```bash
pytest tests/
```

## Transform Rules

Rows are skipped (with a warning log) if any of the following apply:

- `weight_kg` is not a positive number
- `destination` is empty
- `shipment_id` is empty
- `status` is empty
