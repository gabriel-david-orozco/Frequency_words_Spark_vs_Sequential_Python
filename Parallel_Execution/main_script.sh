#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
    echo "Hello $i"
    $SPARK_HOME/bin/spark-submit --conf spark.executor.cores=1 --conf spark.executor.memory=1G --master spark://spark-master:7077 /home/Frequency_words_Spark_vs_Sequential_Python/Parallel_Execution/word_counter_parallel.py 1 1 500_husband_cleaned.txt
done
