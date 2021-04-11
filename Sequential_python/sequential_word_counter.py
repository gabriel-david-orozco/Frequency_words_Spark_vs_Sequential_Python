import time
def differentWordsCounter_v2 (text) : # Word counter based on dictionaries text is a list type

  counts = dict()
  for word in text :
    if word in counts:
      counts[word] += 1
    else :
      counts[word] = 1
  return sorted(counts.items(), key=lambda x: x[1], reverse=True)

print("How many files you want to append?")
tolal_number_files = input ()

print("Put the names of the files you want to evaluate")
files_to_evaluate = []
for m in range(int(tolal_number_files)):
    files_to_evaluate.append(input ())

for k in range(1, 20):
    for i in files_to_evaluate:
        j = 0
        start_time=time.time()
        file = open('/home/Frequency_words_Spark_vs_Sequential_Python/' + i, 'r')
        lines = file.read().split(" ")
        file_list = []
        for line in lines:
          file_list.append(line)

        for palabra, contador in differentWordsCounter_v2(file_list):
            print("{} : {}".format(palabra, contador))

        file = open('record_sequential_' + str(j) ,'a')
        execution_time = str(time.time()-start_time)
        file.write(execution_time +'\n')
        print(f"the total execution time was: {(time.time()-start_time)}")
        j += 1
