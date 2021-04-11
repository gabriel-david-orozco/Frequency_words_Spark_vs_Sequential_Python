# Frequency_words_Spark_vs_Sequential_Python
Assignment of Big Data course UPC-EETAC Catalunya

Developed by Gabriel D. Urrutia and Syed Haider Ali Kazmi  
# General Description

This code is for analyzing the differences between the execution of a frequency-word counter using two different methods, sequential python and parallel execution with spark

The code is divided in the following folders:
- Data_set_generator: Generates a .txt file that contains all the plain text information of cases related to a keyword between a range of years in the https://www.oldbaileyonline.org/. for execute it just run homework2.py modifying the number of files and the dates range you want to use for the test. This code was already ran for 2000 1000 and 500 files using the word "husband".
- Sequential_python: Implements a frequency-word counter using sequential python and a simple for loop taking as input the file returned from Data_set_generator. 
- Parallel_execution: Implements a frequency-word counter using spark parallel execution taking as input the file returned from Data_set_generator. It is important to mention that in order to execute the code for the spark version is necessary to run the main_script.sh in the summit-spark container putting the name of the files to evaluate + the number of machines + the number of cores in each machine. Moreover, each machine has to clone this repo in the /home directory for the code to work.

We ran the code in a cluster of 5 VM deployed in AWS london, each machine has 1 core and 1 GM of RAM. Besides, they are running docker containers in a spark cluster, for a tutorial of how to do this you can go to the following link: https://towardsdatascience.com/diy-apache-spark-docker-bb4f11c10d24. Cluster.png shows the aws deployment


# Performance conclusions
results.png shows the results, we ran 20 times for finding the error and adding and removing machines to the spark cluster in order to compare the performance according to the size of the cluster.

As we can see in results.png, using sequential python gave better results than spark, this is due to the computational resources used for maintaining the spark cluster synchronized. However, for enormously large files that are not able to run on sequential python or to improve the horizontal scalability capability of spark clusters
