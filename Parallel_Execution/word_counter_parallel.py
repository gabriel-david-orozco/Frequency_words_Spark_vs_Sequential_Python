from pyspark import SparkContext, SparkConf
import time
sc = SparkContext(appName="word_counter")

print("How many files you want to append?")
tolal_number_files = input ()

print("Put the names of the files you want to evaluate")
files_to_evaluate = []
for m in range(tolal_number_files):
    files_to_evaluate.append(input ())

print("Put the number of workers in the cluster")
machines = input ()
print("Put the number of cores in each machines")
cores = input ()
for i in files_to_evaluate:
    j = 1
    # Simply reading the context for spark and spliting using lines
    lineas = sc.textFile("/home/Frequency_words_Spark_vs_Sequential_Python/" + i ,minPartitions=2).flatMap(lambda line: line.split(" "))
    start_time = time.time()
    print("---------------------------Time counter has started---------------------------")
    # Map reduce for counting the number of words
    contarPalabras = lineas.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1 +v2)
    counted_list = contarPalabras.collect()
    print(counted_list)
    file = open('record_' +'cores_' cores + '_machines_' + machines + '_' + str(j) ,'a')
    execution_time = str(time.time()-start_time)
    file.write(execution_time +'\n')
    print(f"the total execution time was: {(time.time()-start_time)}")
    j += 1
    time.sleep(15)
