import time
def differentWordsCounter_v2 (text) : # Word counter based on dictionaries
  counts = dict()
  for word in text :
    if word in counts:
      counts[word] += 1
    else :
      counts[word] = 1
  return sorted(counts.items(), key=lambda x: x[1], reverse=True)

start_time=time.time()
file = open('/home/quijote.txt', 'r')
#file = open('/home/words.txt', 'r')
lines = file.read().split(" ")
file_list = []
for line in lines:
  file_list.append(line)

#print(file_list)
#heli=differentWordsCounter_v2(file_list)
#print(heli)
for palabra, contador in differentWordsCounter_v2(file_list):
    print("{} : {}".format(palabra, contador))
print(f"the total execution time was: {(time.time()-start_time)}")
