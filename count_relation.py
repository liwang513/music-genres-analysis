#encoding=utf-8
import codecs

# open the data file and tag file, and then parse them
data_file = codecs.open('Data.txt', 'r', 'utf-8')
tags_file = codecs.open('top_1000_tags.txt', 'r', 'utf-8')

data_lines = [line.strip().split('\t') for line in data_file]
tags_lines = [line.strip().split('\t') for line in tags_file]

# extract the 1000 most frequent tags
tags = [tags_lines[i][0] for i in range(1000)]

# my_map is a dictionary that store the "{artist: tags}" format pair
my_map = {}
for data_line in data_lines:
    artist_name = data_line[0]
    data_line.pop(0)
    my_map[artist_name] = data_line

# tag_map is a dictionary that store the "{tag: artists}" format pair
tag_map = {}
for tags_line in tags_lines:
    tag = tags_line[0]
    for name in my_map:
        if tag in my_map[name]:
            if tag not in tag_map:
                tag_map[tag] = [name]
            else:
                tag_map[tag].append(name)
                
# count the coefficient of two tags: coefficient = (the overlapping numbers of artist name) / (the minimum length of two names arrays)
def count(tag_1, tag_2):
    names_1 = tag_map[tag_1]
    names_2 = tag_map[tag_2]
    
    same = 0
    for name in names_1:
        if name in names_2:
            same += 1
    
    return "{0:.2f}".format(float(same)/min(len(names_1),len(names_2)))


# write down the result into a matrix
table = codecs.open('table.txt', 'w+', 'utf-8')
# the first line
table.write("TAGS")
for tag in tags:
    table.write('\t'+tag)
table.write('\n')
# rest of lines
for tag_1 in tags:
    table.write(tag_1)
    for tag_2 in tags:
        table.write('\t'+str(count(tag_1, tag_2)))
    table.write('\n')
    
                
