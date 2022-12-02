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


#------------ Alt Method (better imo)
# Not used but thought of after
outcomes1 = {"A X" : (4), #Draw # smaller enough # of outcomes to be enumerated
            "B Y" : (6), 
            "C Z" : (6), 
            "A Y" : (8),# Wins
            "B Z" :(9),
            "C X" :(7),
            "A Z":(3), # loss
            "B X":(1),
            "C Y":(2)}

outcomes2 = {"A X" : (3),  #loss to Rock      #small enough to be enumerated
            "B Y" : (5), #draw to paper
            "C Z" : (7), # win w/ scissors
            "A Y" : (4),
            "B Z" :(9),
            "C X" :(2),
            "A Z":(8),
            "B X":(1),
            "C Y":(6)}
score = 0
for r in open('in.txt').readlines(): score+= int(outcomes2[r.rstrip()])
