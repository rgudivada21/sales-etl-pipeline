from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum


def create_spark_session():
    return SparkSession.builder.appName("Sales ETL Pipeline").getOrCreate()


def read_sales_data(spark, file_path):
    return spark.read.csv(
        file_path,
        header=True,
        inferSchema=True
    )


def clean_data(df):
    return df.dropDuplicates()


def transform_data(df):
    return df.withColumn(
        "Total_Amount",
        col("Quantity") * col("Price")
    )


def category_sales(df):
    return df.groupBy("Category").agg(
        sum("Total_Amount").alias("Total_Sales")
    )


def save_parquet(df, output_path):
    df.write.mode("overwrite").parquet(output_path)


def main():
    spark = create_spark_session()

    input_path = "data/sales.csv"
    output_path = "output/sales_parquet"

    df = read_sales_data(spark, input_path)
    df = clean_data(df)
    df = transform_data(df)

    print("Sales Data")
    df.show()

    print("Category Sales")
    category_sales(df).show()

    save_parquet(df, output_path)

    spark.stop()


if __name__ == "__main__":
    main()
