# Advant of Code 2024 Day 13

# Question 1 + 2

import re

total = 0

with open("input.txt", "r") as file:
    for block in file.read().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, (re.findall(r"\d+", block)))
        px, py = px + 10000000000000, py + 10000000000000 # used for question 2 not needed for question 1
        xMoves = ((px * by) - (py * bx)) / ((ax * by) - (ay * bx))
        yMoves = (px - (ax * xMoves)) / (bx)
        if xMoves % 1 == yMoves % 1 == 0:
            total += ((xMoves * 3) + yMoves)

print(int(total))