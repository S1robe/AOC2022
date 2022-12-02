#!/bin/python

# 1 for Rock
# 2 for Paper
# 3 for Scicsors


# Score for round = Shape + Win/Draw/Lose

# first column = opponent play
# A = Rock
# B = Paper
# C = Scissors
# Second Column
# X = Rock
# Y = Paper
# Z = Scissors



A, B, C = 1, 2, 3
X, Y, Z = 1, 2, 3
score = 0
W = 6
D = 3
L = 0

for n in open('in.txt').readlines():
    if n[0] == 'C':  # if Sci
        if n[2] == 'Z':  # if Sci (Draw)
            score += D
            score += Z
        elif n[2] == 'Y': # Loss
            score += L
            score += Y
        else:
            score += W # Win
            score += X
    elif n[0] == 'B':  # if B PAper
        if n[2] == 'Z':  # if Sci ()
            score += W
            score += Z
        elif n[2] == 'Y':
            score += D
            score += Y
        else:
            score += L
            score += X
    else:  # if A
        if n[2] == 'Z':  # if Sci Rock
            score += L
            score += Z
        elif n[2] == 'Y':
            score += W
            score += Y
        else:
            score += D
            score += X
print(score)
