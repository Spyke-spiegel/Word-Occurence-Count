filename = './wc_input/words.txt'
file = open(filename, 'r')
dic =dict()

for line in file:
    line = line.rstrip().rstrip('.').rstrip(',')
    wds = line.split()
    for w in wds:
        if w in dic:
            dic[w] = dic[w] + 1
        else:
            dic[w] = 1

result = open('wc_result.txt', 'w+')
for key in sorted(dic.keys(), key=str.lower):
    result.write("%s: %s\r\n" % (key, dic[key]))