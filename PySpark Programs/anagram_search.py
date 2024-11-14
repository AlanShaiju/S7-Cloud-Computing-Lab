from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
from collections import Counter

# Initialize Spark session
spark = SparkSession.builder.appName("AnagramSearch").getOrCreate()

# Define anagram function
def sort_letters(word):
    return "".join(sorted(word))

# Register UDF
anagram_udf = udf(sort_letters, StringType())

# Read document as DataFrame
document_df = spark.read.text("path/to/document.txt")

# Transform words to sorted letters for anagram detection
anagrams_df = document_df.withColumn("sorted_word", anagram_udf(col("value")))

# Find and write anagrams to a new document
anagram_groups = anagrams_df.groupBy("sorted_word").count().filter(col("count") > 1)
anagram_groups.write.text("path/to/anagrams_output.txt")
