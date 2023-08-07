# import sys
 
# from pyspark import SparkContext, SparkConf
 
# if __name__ == "__main__":
	
# 	# create Spark context with necessary configuration
# 	sc = SparkContext("local","PySpark Word Count Exmaple")
	
# 	# read data from text file and split each line into words
# 	words = sc.textFile("file.txt").flatMap(lambda line: line.split(" "))
	
# 	# count the occurrence of each word
# 	wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
	
# 	# save the counts to output
# 	wordCounts.saveAsTextFile("output")

import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    # create Spark context with necessary configuration
    conf = SparkConf().setAppName("PySpark Word Count Example")
    sc = SparkContext(conf=conf)

    # read data from text file and split each line into words
    words = sc.textFile("file.txt").flatMap(lambda line: line.split(" "))

    # count the occurrence of each word
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

    # collect the counts and print the output
    results = wordCounts.collect()
    for (word, count) in results:
        print(f"{word}: {count}")

    # stop the Spark context
    sc.stop()
