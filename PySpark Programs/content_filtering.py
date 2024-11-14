from pyspark.sql import SparkSession
from pyspark.sql.functions import col,avg
# Initialize Spark session
spark = SparkSession.builder.appName("FilterCSV").getOrCreate()

# Read CSV file
csv_df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Filter based on conditions (e.g., age and department)
filtered_df = csv_df.filter((col("age") > 25) & (col("department") == "Engineering"))
filtered_df.show()

# Analytical functions: group by and aggregate
analytics_df = csv_df.groupBy("department").avg("age").withColumnRenamed("avg(age)", "average_age")
analytics_df.show()
