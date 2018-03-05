import collections 
wordcount = collections.Counter()
with open("f1.txt") as f1:
 for line in f1:
  wordcount.update(line.split())
for k,v in wordcount.iteritems():
 print k,v

