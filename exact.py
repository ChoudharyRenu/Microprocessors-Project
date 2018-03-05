with open("f1.txt") as f1,open ("f2.txt") as f2:
 countL=0
 countC=0
 for i,line1 in enumerate(f1) and for line2 in enumerate(f2):
  for j in range i to i+9:
    if line1==line2
       countL++;
  if(countL==10)
   countC++;

print "total number of exact clones is",countC
