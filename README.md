# Frequency_words_Spark_vs_Sequential_Python
Assignment of Big Data course UPC-EETAC Catalunya

Developed by Gabriel D. Urrutia and Syed Haider Ali Kazmi  
# General Description

This code is for analyzing the differences between the execution of a frequency-word counter using two different methods, sequential python and parallel execution with spark

The code is divided in the following folders:
- Data_set_generator: Generates a .txt file that contains all the plain text information of cases related to a keyword between a range of years in the https://www.oldbaileyonline.org/
- Sequential_python: Implements a frequency-word counter using sequential python and a simple for loop taking as input the file returned from Data_set_generator
- Parallel_execution: Implements a frequency-word counter using spark parallel execution taking as input the file returned from Data_set_generator
- Comparision: Generates a full text of the deployment
