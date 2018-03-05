with open("f1.txt") as f1,open ("f2.txt") as f2:
 countL=0
 countC=0
 for i,line1 in enumerate(f1) and for line2 in enumerate(f2):
  for j in range i to i+9:
    if line1 == line2:
       countL = countL + 1;
  if countL == 10:
   countC = countC + 1;

print "total number of exact clones is",countC


#the problem is with the syntax
#I m trying to access the lines of both files and "i" is to keep the track of line number so that
# we can generate a new window as i gets incremented(window size i have taken 10),
#every time we check that if countL is equal to the window size then we increment 
# countC(exactclone)
#I googled but could not find anything related to this please try to fix it no
