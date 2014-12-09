#encoding=utf-8
import codecs

# open the data file and parse it
file = codecs.open('Data.txt', 'r', 'utf-8')
lines = [line.strip().split('\t') for line in file]

# use dictionary to count the frequency of every tag
my_map = {}
for line in lines:
    line.pop(0)
    
    for tag in line:
        if tag not in my_map:
            my_map[tag] = 1
        else:
            my_map[tag] = my_map[tag]+1

# return the sorted dictionary
my_map = sorted(my_map.items(), key=lambda x: -x[1])

# write the most frequent 1000 results into file
tag_file = codecs.open('top_1000_tags.txt', 'w+', 'utf-8')
for i in range(1000):
    tag_file.write(my_map[i][0]+'\t'+str(my_map[i][1])+'\n')
    