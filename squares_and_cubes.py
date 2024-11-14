from pyspark.sql import SparkSession
from pyspark.sql.functions import col, pow

# Initialize Spark session
spark = SparkSession.builder.appName("SquaresAndCubes").getOrCreate()

# Read CSV file
csv_df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Compute squares and cubes
computed_df = csv_df.withColumn("square", pow(col("number"), 2)).withColumn("cube", pow(col("number"), 3))

# Write updated DataFrame back to CSV
computed_df.write.csv("path/to/output.csv", header=True, mode="overwrite")
