#!/bin/python3

#So now we need to sift through three lines at a time and find the

# part 2
table = dict(zip([*range(97,123), *range(65, 91)], range(1,53)))
su = 0
n = open('in.txt').readlines()
i = 0
while i < len(n)-2:
  for l in n[i].rstrip():
      if(n[i+1].find(l) != -1 and n[i+2].find(l) != -1):
              su += table[ord(l)] # sum the equal ones
              break
  i += 3




print(su)
