import time
def differentWordsCounter_v2 (text) : # Word counter based on dictionaries
  counts = dict()
  for word in text :
    if word in counts:
      counts[word] += 1
    else :
      counts[word] = 1
  return sorted(counts.items(), key=lambda x: x[1], reverse=True)

print("Put the names of the files you want to evaluate")
files_to_evaluate[0] = input ( prompt )
files_to_evaluate[1] = input ( prompt )
files_to_evaluate[2] = input ( prompt )
for i in files_to_evaluate:
    start_time=time.time()
    file = open('/home/' + i, 'r')

    lines = file.read().split(" ")
    file_list = []
    for line in lines:
      file_list.append(line)

    for palabra, contador in differentWordsCounter_v2(file_list):
        print("{} : {}".format(palabra, contador))

    file = open('record_sequential_' + j ,'a')
    execution_time = str(time.time()-start_time)
    file.write(execution_time +'\n')
    print(f"the total execution time was: {(time.time()-start_time)}")
