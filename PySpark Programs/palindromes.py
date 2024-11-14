from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import BooleanType

# Initialize Spark session
spark = SparkSession.builder.appName("PalindromeCheck").getOrCreate()

# Define palindrome check function
def is_palindrome(word):
    return word == word[::-1]

# Register UDF
palindrome_udf = udf(is_palindrome, BooleanType())

# Read document as DataFrame
document_df = spark.read.text("path/to/document.txt")

# Identify palindromes
palindromes_df = document_df.withColumn("is_palindrome", palindrome_udf(col("value"))).filter(col("is_palindrome") == True)
palindromes_df.show()
