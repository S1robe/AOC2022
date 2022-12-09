#!bin/python3
cc = 14 # 4
for c in open('in1.txt').readlines():
    match = False
    marker = 14 # 4
    while not match:
        mark = set(c[0:14])  # first possible substring replace 4 with 14 to get part 2
        if len(mark) == 14: # 4
            match = True
            break
        c = c[1:]  # cut off first digit
        marker += 1
        cc += 1
print(cc)


