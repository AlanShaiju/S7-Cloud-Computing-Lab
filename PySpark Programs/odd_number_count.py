from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.appName("OddNumberCount").getOrCreate()

# Read CSV file with numeric data
csv_df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Filter for odd numbers in a specific column (e.g., 'number')
odd_numbers_df = csv_df.filter(col("number") % 2 != 0)
odd_number_count = odd_numbers_df.count()
print(f"Count of odd numbers: {odd_number_count}")
