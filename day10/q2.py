# Advant of Code 2024 Day 10

# Question 2

from collections import deque

trails = []

with open("input.txt", "r") as file:
    for line in file:
        trails.append(list(map(int, list(line.strip()))))

rows = len(trails)
cols = len(trails[0])
count = 0

def findTrailheads(sr, sc, grid):
    q = deque([(sr, sc)])
    # seen = {(sr, sc)}
    summits = 0
    while len(q) > 0:
        cr, cc = q.popleft()
        for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
            if 0 <= nr < rows and 0 <= nc < cols: 
                if grid[nr][nc] != grid[cr][cc] + 1: continue
                # if (nr, nc) in seen: continue
                # seen.add((nr, nc))
                if grid[nr][nc] == 9:
                    summits += 1
                else:
                    q.append((nr, nc))
    return summits

for r in range(len(trails)):
    for c in range(len(trails[0])):
        if trails[r][c] == 0:
            count += findTrailheads(r,c,trails)

print(count)
