"""
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.

Your program breaks up the experiment into two parts:
    The first part generates a list of randomly selected 'heads' and 'tails' values
    The second part checks if there is a streak in it.

Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row.
"""

import random


numberOfStreaks = 0
head_tails = []
count_tail = 0
count_head = 0

for experimentNumber in range(10000):
    # Code that creates a list of 10000 'heads' or 'tails' values.
    if random.randint(0,1) == 0:
        head_tails.append("T")
        count_tail += 1
        count_head = 0
    else:
        head_tails.append("H")
        count_head += 1
        count_tail = 0
    
    if count_head == 6 or count_tail == 6:
        numberOfStreaks += 1

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
