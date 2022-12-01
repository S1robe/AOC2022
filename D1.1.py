#!/bin/python3
s,m,m2,m3 = 0,0,0,0
for n in open('in.txt').readlines():
   if len(n.strip()) == 0:
      if m < s:
        m3 = m2
        m2 = m
        m = s
      elif m2 < s:
        m3 = m2
        m2 = s
      elif m3 < s:
        m3 = s
        
      s = 0
      continue # new elf
   elif:
      s += int(n)
      
# print for 1
# print(m)
# print for 2
print(m + m2 +m3)
