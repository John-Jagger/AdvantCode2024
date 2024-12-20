# Advant of Code 2024 Day 14

# Question 1

import re
from math import prod


guards = []
coords = {(0,0) : 0, (0,1) : 0, (1,0) : 0, (1,1) : 0}
WIDTH = 101
HEIGHT = 103

with open("input.txt", "r") as file:
    for line in file:
        guards.append(tuple(map(int, (re.findall(r"-?\d+", line)))))

result = []

for px, py, vx, vy in guards:
    result.append(((px + vx * 100) % WIDTH, (py + vy * 100) % HEIGHT))

sx = WIDTH // 2
sy = HEIGHT // 2

for px, py in result:
    if px == sx or py == sy: continue
    coords[(px // (sx + 1), py // (sy + 1))] += 1

print(prod(coords.values()))