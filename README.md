## Customer Transaction ETL Pipeline

### Overview

This project implements an ETL pipeline to process customer transaction data, simulating a banking analytics workflow. It uses PySpark for data transformation, PostgreSQL for storage, and Apache Airflow for orchestration, aligning with Barclays' data engineering practices.

### Features





- Data: Synthetic dataset of 1,000 transactions (columns: transaction_id, customer_id, amount, date, category).



- ETL Process:





- Extract: Reads CSV data using PySpark.



- Transform: Cleans data (removes nulls, filters invalid amounts) and aggregates total spend by customer.



- Load: Stores results in a PostgreSQL database.



- Orchestration: Airflow DAG automates data generation and ETL execution.



Environment: Dockerized PySpark setup for portability.

## Technologies





- PySpark: Data processing and transformation.



- PostgreSQL: Data storage and querying.



- Apache Airflow: Workflow orchestration.



- Docker: Containerized PySpark environment.

## Setup Instructions

### Prerequisites:





- Docker and Docker Compose



- Python 3.9+



- PostgreSQL (local or Docker)



- Apache Airflow (local or Astronomer free tier)

```bash
# Clone repository
git clone https://github.com/sanjeevikumarWD/customer-transaction-etl.git
cd customer-transaction-etl

# Build Docker image
docker build -t pyspark-etl -f docker/Dockerfile .

# Start PostgreSQL
docker run -d --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 postgres

# Initialize Airflow (local)
pip install apache-airflow
airflow db init
airflow webserver --port 8080 &
airflow scheduler &

# Copy DAG to Airflow
cp airflow/dags/transaction_etl_dag.py ~/airflow/dags/

# Run ETL
docker run --network host -v $(pwd)/data:/app/data -v $(pwd)/sql:/app/sql pyspark-etl

```



### Access Results:





- View Airflow UI at http://localhost:8080.



- Query PostgreSQL: psql -h localhost -U postgres -d postgres.

## Results





- Processed 1,000 transaction records.



- Aggregated total spend by customer, stored in PostgreSQL.



- Automated pipeline execution via Airflow.

### Learning Outcomes





- Gained hands-on experience with PySpark DataFrames, PostgreSQL, and Airflow.



- Simulated a financial data pipeline relevant to Barclays' data engineering roles.

### Future Improvements





- Add DBT for advanced SQL transformations.



- Integrate AWS S3 for data storage.



- Implement data governance checks.
