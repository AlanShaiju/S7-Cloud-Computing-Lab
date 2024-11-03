from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# Create a Spark session
spark = SparkSession.builder \
    .appName("Word Count") \
    .getOrCreate()

# Load the text file
input_file = "testfile.txt"  # Update with your file path
text_rdd = spark.sparkContext.textFile(input_file)

# Split each line into words, flatten the list, and count each word
word_counts = (text_rdd
               .flatMap(lambda line: line.split())  # Split each line into words
               .map(lambda word: (word, 1))          # Create pairs (word, 1)
               .reduceByKey(lambda a, b: a + b))     # Sum the counts for each word

# Convert to DataFrame for better readability (optional)
word_counts_df = word_counts.toDF(["word", "count"])

# Show the result
word_counts_df.show(truncate=False)

# Stop the Spark session
spark.stop()
