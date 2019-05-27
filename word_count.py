import os

dic =dict()
result = open('wc_result.txt', 'w+')
folderPath = './wc_input/'

#Iterating over the folder wc_input
for file in os.listdir(folderPath):
    filename = os.fsdecode(file)
    print("file find in the folder Input = " + filename)
    data = open(folderPath + filename, "r")
    for line in data:
        #cleaning the data
        line = line.rstrip().rstrip('.').rstrip(',')
        wds = line.split()
        #counting Words
        for w in wds:
            if w in dic:
                dic[w] = dic[w] + 1
            else:
                dic[w] = 1
    #Ordering the data and writing the result in wc_result.txt
    result = open('wc_result.txt', 'w+')
    for key in sorted(dic.keys(), key=str.lower):
        result.write("%s: %s\r\n" % (key, dic[key]))