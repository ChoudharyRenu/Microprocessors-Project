#import collections
#with open("f1.txt") as f1,open ("f2.txt") as f2:
#	for i,line in enumerate(f1):
#		for j in range (i,i+4):
#			wordcount = collections.Counter()
#			wordcount.update(line.split("\n"))
#		for k,v in wordcount.iteritems():
#  			print k,v
#		print "i value is updated",i


with open("f1.txt") as f1:
 wordlist1=list()
 line=f1.readline()
 #numlines=sum(1 for line in ("f1.txt"))
 while line:
  words=line.split("\n")
  wordlist1.append(words[0])
  line=f1.readline()
  #print words[0]

print wordlist1

freq1 = {}
for item in wordlist1:
 if item in freq1:
  freq1[item] = freq1.get(item)+1
 else:
  freq1[item] = 1

for k,v in freq1.items():
 print(str(k) + ':' + str(v))


with open("f2.txt") as f2:
 wordlist2=list()
 line=f2.readline()
 #numlines=sum(1 for line in ("f1.txt"))
 while line:
  words=line.split("\n")
  wordlist2.append(words[0])
  line=f2.readline()
  #print words[0]

freq2 = {}
for item in wordlist1:
 if item in freq2:
  freq2[item] = freq2.get(item)+1
 else:
  freq2[item] = 1

for k,v in freq1.items():
 print(str(k) + ':' + str(v))

count1=0
count2=0
for x,y in zip(freq1.iteritems(),freq2.iteritems()):
	if x == y:
		print "exact match"
		count1=count1+1
	
	else:
		print "no match"
		count2=count2+1

if count2 == 0:
	print "exact clones"
else :
	print "not exact clone"
