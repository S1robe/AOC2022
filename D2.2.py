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
# X = Lose
# Y = Draw
# Z = Win

A, B, C = 1, 2, 3
score = 0
W = 6
D = 3
L = 0

# find the shape to pick

for n in open('in.txt').readlines():
    if n[0] == 'C':  # if Scissors
        if n[2] == 'Z':  # needs win
            score += A
            score += W  # won with rock
        elif n[2] == 'Y': # Draw
            score += C
            score += D # drew with Sci = Sci
        else: # Lose to Scisors
            score += B
            score += L
    elif n[0] == 'B':  # if B PAper
        if n[2] == 'Z':  # needs win
            score += C
            score += W  # won with rock
        elif n[2] == 'Y':  # Draw
            score += B
            score += D  # drew with Sci = Sci
        else:  # Lose to Paper
            score += A
            score += L
    else:  # if A
        if n[2] == 'Z':  # needs win
            score += B
            score += W  # won with paper
        elif n[2] == 'Y':  # Draw
            score += A
            score += D  # drew with Sci = Sci
        else:  # Lose to Scisors
            score += C
            score += L
print(score)
