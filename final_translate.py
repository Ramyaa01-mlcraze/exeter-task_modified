import sys
import csv
import time
import tracemalloc

#calculating the time for the execution
start_time = time.time()
tracemalloc.start()

#Read French Dictionary input file and store all the values in the dictionary
french_dict = {}
with open('french_dictionary.csv','r') as csv_file:
    c_r = csv.reader(csv_file)
    for row in c_r:
        french_dict[row[0]] = row[1]
csv_file.close()

#Read Find Words and store all the values in list
fw=[]
with open('find_words.txt','r') as f:
    for li in f:
        value = li.replace("\n","")
        fw.append(value)
f.close()

#Intializing a list for counting the replacement
freq_count = []
dict_count = dict.fromkeys(fw, 0)

#Read the file which need changes to it.
with open('t8.shakespeare.txt', 'r') as fil:
    lines = fil.read()
fil.close()


for i in fw:
    dict_count[i] += lines.count(i.lower())
    lines = lines.replace(i.lower(), french_dict[i])


for i in fw:
    dict_count[i] += lines.count(i.upper())
    lines = lines.replace(i.upper(), french_dict[i].upper())


for i in fw:
    dict_count[i] += lines.count(i.capitalize())
    lines = lines.replace(i.capitalize(), french_dict[i].capitalize())
    
for i in fw:
    freq_count.append([i, french_dict[i], dict_count[i]])


#Writing the translated file
with open('t8.shakespeare.translated.txt', 'w') as fi:
    fi.write(lines)
fi.close()

#Storing the frequency in csv file.
filename = "frequency.csv"  
with open(filename, 'w') as csvfile: 
    wrote = csv.writer(csvfile)
    wrote.writerow(['English','French','Frequency']) 
    wrote.writerows(freq_count) 
csvfile.close()

#printing the memory and  time of execution.
mem = tracemalloc.get_traced_memory()[1] - tracemalloc.get_traced_memory()[0]
tracemalloc.stop()
proc = (time.time() - start_time)

#Writing the Performance file
with open("Performance.txt",'w') as file:
  file.write(f"Time taken : {proc} seconds\n")
  file.write(f"Memory used : {mem} in MB")
file.close()
