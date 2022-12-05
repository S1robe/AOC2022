#!/bin/python3

# The idea of this puzzle is to determine if the first pair can contain the second
# or if the second range contains the first,

s = 0
for pair in open('in1.txt'):
    pairs = pair.split(',') # split on comma
    r1 = pairs[0].split('-') # split at -
    r2 = pairs[1].split('-') 
    l1 = int(r1[0])
    h1 = int(r1[1])
    l2 = int(r2[0])
    h2 = int(r2[1])
    if(l1 <= l2 and h1 >= h2): # if first pair consumes second
        s+=1
    elif(l2 <= l1 and h2 >= h1): # if second pair convers first
        s+=1
    elif (h1 >= l2 and h1 <= h2) or (h2 >= l1 and h2 <= h1): # added for pt 2
        s+=1
print(s)

