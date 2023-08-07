from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split

# Create a SparkSession
spark = SparkSession.builder.appName("WordCountApp").getOrCreate()

# Read the input text file
input_file_path = "Custom_folder/file.txt"
text_df = spark.read.text(input_file_path)

# Split each line into words
words_df = text_df.select(explode(split(col("value"), " ")).alias("word"))

# Group by word and count occurrences
word_count_df = words_df.groupBy("word").count()

# Print the word count
word_count_df.show()

# Stop the SparkSession
spark.stop()
