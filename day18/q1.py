# Advant of Code 2024 Day 18

# Question 1

from collections import deque


bytes = []

with open("input.txt", "r") as file:
    for line in file:
        line = list(line.strip().split(","))
        bytes.append((int(line[0]), int(line[1])))

size = 70
bytes = bytes[:1024]


q = deque([(0,0,0)])
seen = {(0,0)}
while q:
    r,c,d = q.popleft()
    for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if nr < 0 or nc < 0 or nr > size or nc > size: continue
        if (nr, nc) in bytes: continue
        if (nr, nc) in seen: continue
        if nr == size and nc == size:
            print(d + 1)
            exit(0)
        seen.add((nr,nc))
        q.append((nr,nc,d+1))