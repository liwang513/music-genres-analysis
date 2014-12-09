Task:

Construct a data set that relates Last.fm tags to each other, revealing which genres (and other tags) are most associated. Analyse the relation of different tags for popular artists.



Solve Procedure:

1. I used the API to extract the top 1000 artists with their top 10 tags.

2. Iterate the total 10000 tags to count the frequency, and get the top 1000 tags.

3. create a 1000*1000 matrix to represent the relation of each two tags. (0 <- very unrelated  1 <- very related)



Files:

“Data.txt” is a TSV file that stores the top 1000 artists with their top 10 tags

“top_1000_tags.txt” is a TSV file that stores the top 1000 tags with their frequency

“table.txt” is a TSV file that represent the 1000*1000 tag matrix


“get_top_1000_tags.py” runs to get the top 1000 tags from the “Data.txt”

“count_relation.py” runs to create the matrix



Algorithm:

In the top 1000 tags, each tag can refer to several artists who is labeled with this tag. Therefore, for each tag, we can get an artist array for it.

Assume there is two tags, so we have two artist arrays. I count the coefficient of these two tags by use: (# of same tags) / (# of the smaller length of the two arrays). For example: suppose tag 1 has [“James”, “Helen”, “John”, “Terry”] and tag 2 has [“James”, “John”, “Eden”], the coefficient would be 2/min(3,4) = 2/3 = 0.67.

The idea comes because some tags are the sub-tags of a parent tag. Like “indie rock” is the sub of “rock”. They are definitely related, but the (# of same tags)/ (# of the merge of the two arrays) might get a very small number. However, (# of same tags)/(# of the smaller length of the two arrays) would be more accurate.