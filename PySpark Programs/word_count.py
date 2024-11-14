from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split,col

# Initialize Spark session
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read document as DataFrame
document_df = spark.read.text("path/to/document.txt")

# Perform word count
word_counts = document_df.select(explode(split(col("value"), "\\s+")).alias("word")).groupBy("word").count()
word_counts.show()
