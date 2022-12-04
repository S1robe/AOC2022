#!/bin/python3

# The main idea of this one is to divide each line in two and then find the first matching character
# No sorting is required but might be for part 2

# part 1
table = dict(zip([*range(97,123), *range(65, 91)], range(1,53)))
su = 0
for n in open('in.txt').readlines():
    f = n[0:(len(n)//2)] # first half
    s = n[(len(n)//2):]    # second half
    for l in f:
        if(s.find(l) != -1): # find me the letter from f in s
            su += table[ord(l)] # sum the equal ones
            break
print(su)
