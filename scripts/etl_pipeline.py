from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import psycopg2
import pandas as pd

# Initialize Spark
spark = SparkSession.builder \
    .appName("TransactionETL") \
    .getOrCreate()

# Read data
df = spark.read.csv("data/transactions.csv", header=True, inferSchema=True)

# Transform: Clean and aggregate
df_clean = df.dropna().filter(col("amount") > 0)
df_agg = df_clean.groupBy("customer_id").sum("amount").withColumnRenamed("sum(amount)", "total_spend")

# Convert to Pandas for PostgreSQL
df_pandas = df_agg.toPandas()

# Write to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
cursor.execute(open("sql/create_table.sql", "r").read())
df_pandas.to_sql("transactions", conn, if_exists="replace", index=False)
conn.commit()
cursor.close()
conn.close()

print("ETL pipeline completed: Data written to PostgreSQL")
spark.stop()
