# Sales ETL Pipeline - Project Explanation

# 1. Project Objective

The objective of this project is to build a simple ETL pipeline using PySpark. The pipeline reads sales data from a CSV file, cleans the data, transforms it, calculates total sales, and saves the output in Parquet format.

---

# 2. Project Overview

This project demonstrates the basic ETL (Extract, Transform, Load) process using PySpark.

Workflow:

CSV File → Read Data → Clean Data → Transform Data → Aggregate Data → Save as Parquet

---

# 3. Business Scenario

A company stores daily sales data in CSV files. Before creating reports, the data must be cleaned, transformed, and stored in an optimized format for faster analysis.

---

# 4. Technologies Used

- Python
- PySpark
- PyTest
- Git
- GitHub
- GitHub Actions
- Parquet

---

# 5. Project Structure

- data/ → Stores input CSV files.
- src/ → Contains ETL code.
- tests/ → Contains unit tests.
- docs/ → Project documentation.
- .github/ → GitHub Actions workflow.
- README.md → Project overview.
- requirements.txt → Project dependencies.
- .gitignore → Ignore unnecessary files.

---

# 6. Dataset Information

Input file: sales.csv

Columns:
- Order_ID
- Product
- Category
- Quantity
- Price

---

# 7. ETL Workflow

1. Read CSV file.
2. Remove duplicate records.
3. Calculate Total Amount.
4. Group sales by category.
5. Save data as Parquet.

---

# 8. Spark Session

## Purpose

Creates a Spark application.

## Why We Used It

SparkSession is the entry point for all PySpark operations.

## Alternative

SparkContext

## Why Not Used

SparkSession is the modern and recommended approach.

---

# 9. Reading CSV

## Purpose

Reads data from a CSV file.

## Why We Used It

CSV is a common file format for data exchange.

## Alternative

Read from Database, JSON, Excel, or Parquet.

## Why Not Used

CSV is simple and suitable for this demo project.

---

# 10. Cleaning Data

## Purpose

Removes duplicate records.

## Why We Used It

Duplicate records produce incorrect calculations.

## Alternative

distinct()

## Why Not Used

dropDuplicates() provides more flexibility and can remove duplicates based on selected columns.

---

# 11. Data Transformation

## Purpose

Creates a new column called Total_Amount.

Formula:

Total_Amount = Quantity × Price

## Why We Used It

To calculate total sales for each order.

## Alternative

SQL query

## Why Not Used

PySpark DataFrame API is easier to understand and maintain.

---

# 12. Aggregation

## Purpose

Calculates total sales for each category.

## Why We Used It

Business users usually need category-wise reports.

## Alternative

Spark SQL

## Why Not Used

DataFrame API is simple and readable.

---

# 13. Saving Data

## Purpose

Stores processed data.

## Why We Used It

Parquet is faster and compressed.

## Alternative

CSV, JSON, ORC

## Why Not Used

Parquet provides better performance for analytics.

---

# 14. Testing

## Purpose

Checks whether the transformation logic works correctly.

## Why We Used It

Testing helps identify issues before deployment.

## Alternative

unittest

## Why Not Used

PyTest is simpler and widely used.

---

# 15. GitHub Actions

## Purpose

Runs tests automatically whenever code is pushed.

## Why We Used It

It helps verify that the project works correctly after every change.

## Alternative

Jenkins, GitLab CI, Azure DevOps

## Why Not Used

GitHub Actions is free for GitHub repositories and easy to configure.

---

# 16. requirements.txt

Purpose:

Stores all Python packages required for the project.

Packages:
- pyspark
- pytest

---

# 17. .gitignore

Purpose:

Prevents unnecessary files from being uploaded to GitHub.

Examples:
- __pycache__/
- output/
- *.pyc

---

# 18. Challenges Faced

- Module import issue.
- GitHub Actions configuration.
- Python path issue.

These were fixed by updating the project structure and workflow configuration.

---

# 19. Future Improvements

- Use Delta Lake.
- Load data from a database.
- Add logging.
- Add exception handling.
- Deploy on Databricks.

---

# 20. Key Learnings

- ETL process.
- PySpark DataFrame operations.
- Unit testing using PyTest.
- GitHub Actions CI.
- Working with Parquet files.

---

# 21. Conclusion

This project demonstrates a complete beginner-friendly ETL pipeline using PySpark. It covers data reading, cleaning, transformation, aggregation, testing, and automated CI using GitHub Actions.
