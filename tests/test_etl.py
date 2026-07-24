import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pyspark.sql import SparkSession
from src.etl import transform_data

spark = SparkSession.builder.master("local[*]").appName("Test").getOrCreate()


def test_total_amount_column():
    data = [(1, "Laptop", "Electronics", 2, 1000)]
    columns = ["Order_ID", "Product", "Category", "Quantity", "Price"]

    df = spark.createDataFrame(data, columns)

    result = transform_data(df)

    assert "Total_Amount" in result.columns
    assert result.collect()[0]["Total_Amount"] == 2000
