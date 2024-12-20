# Advant of Code 2024 Day 14

# Question 2

import re
from math import prod

guards = []
coords = {(0,0) : 0, (0,1) : 0, (1,0) : 0, (1,1) : 0}
WIDTH = 101
HEIGHT = 103

with open("input.txt", "r") as file:
    for line in file:
        guards.append(tuple(map(int, (re.findall(r"-?\d+", line)))))

min_safe = float("inf")
best_iteration = None

for second in range(WIDTH * HEIGHT):
    result = []
    for px, py, vx, vy in guards:
        result.append(((px + vx * second) % WIDTH, (py + vy * second) % HEIGHT))

    tl = bl = tr = br = 0

    VM = WIDTH // 2
    HM = HEIGHT // 2

    for px, py in result:
        if  px == HM or py == VM: continue
        if px  < HM:
            if py < VM:
                tl += 1 
            else: 
                bl += 1
        else:
            if py <  VM:
                tr += 1
            else:
                br += 1
    sf =  tl * bl  * tr * br

    if sf < min_safe:
        min_safe = sf
        best_iteration = second
print(min_safe, best_iteration)