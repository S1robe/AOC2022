#!/bin/python
Cr = []
instruct = False
for i in open('in1.txt').readlines():
    if instruct:
        inst = i.replace("move ", "").replace("from ", "").replace(" to", "").rstrip().split(" ")
        # Part 1 for loop
        # for m in range(int(inst[0])):
        #     crane = Cr[int(inst[1])][0]  # take the first off
        #     Cr[int(inst[1])] = Cr[int(inst[1])][1:]  # cut the first off the stack
        #     Cr[int(inst[2])] = crane + Cr[int(inst[2])]  # put crane on top
        # Part 2
        crane = Cr[int(inst[1])][0:int(inst[0])]  # cut prefix
        Cr[int(inst[1])] = Cr[int(inst[1])][len(crane):]
        Cr[int(inst[2])] = crane + Cr[int(inst[2])]  # put crane on top
    elif len(i) != 1 and i[1] == '1':
        continue
    elif i[0] == '\n':
        print(Cr)
        instruct = True  # switch to handing instructions
        continue
    else:
        stacknum = 1
        while len(i) != 0:
            box = i[0:4][1].replace(' ', '').replace('\n', '')  # get the character from each box, each gets 4 chars
            i = i[4:]  # cut off the first 4 characters (consumed)
            if len(box) != 0:
                while len(Cr) <= stacknum:
                    Cr.append('')
                Cr[stacknum] += box  # add the character to the back of the list (building the stack downward
            stacknum += 1

for i in Cr[1:]:
    print(i[0], end="")

