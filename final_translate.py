#import all the necessary modules
import csv, sys, time
import os
import psutil

#function for reading the french dictionary input file
def french_dictionary():
    with open('french_dictionary.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #looping over the csv file
        for r in csv_reader:
            french_dict[r[0]] = [r[1],0]

#function for translating the shakespeare input file
def translation(input_file):
    print('Reading files.....')
    fp = open('t8.shakespeare.translate.txt', 'w')
    check_list = french_dict.keys()
    with open(input_file, 'r') as input_text:
        while True:
            line = input_text.readline() #reading all the lines of the input file
            if not line: #if it is not a line then the condition will stop
                break
            buffer = ''
            #iterate through all the words
            for word in line.split():
                filtered = filter(str.isalpha,word) #filter the words and capitalized words
                query = "".join(filtered) #join the filtered words
                if query in check_list: #check whether the word is in the french dictionary
                    success_query = french_dict[query][0]
                    french_dict[query][1] += 1
                    word = word.replace(query, success_query) #replace the words
                buffer += word + ' '
            buffer = buffer.strip()
            fp.write(buffer + '\n')
    fp.close()
    print(f'File {input_file} is translated from english to french')
    return True

def frequency_csv():
    print('Generating frequency file.....')
    with open('frequency.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['English', 'French', 'Frequency'])
        for words in french_dict:
            writer.writerow([words, french_dict[words][0], french_dict[words][1]])
    print('Done.')
    return True

def performance(process_time, memory_info):
    print('Generating performance.txt.....')
    with open('performance.txt', 'w') as file:
        file.write(f"Time to process : {process_time} seconds\n") 
        file.write(f"Memory used : {memory_info} MB")
    print('Done.')

if __name__ == '__main__':
    process_start_time = time.time() 
    french_dict = {}
    input_file = 't8.shakespeare.txt' #shakespeare input file

    if len(sys.argv) == 2: #checking whether there are 2 areguments
        input_file = sys.argv[1]

    french_dictionary()
    translation(input_file)
    frequency_csv()
    process_complete_time = time.time() #complete the process
    memory_used = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2 #memory used
    process_time = process_complete_time - process_start_time #calculating the process time

    performance(process_time, memory_used)#calling the function performance
