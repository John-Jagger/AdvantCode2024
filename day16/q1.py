# Advant of Code 2024 Day 16

# Question 1

import heapq

grid = []

with open("input.txt", "r") as file:
    grid = [list(row.strip()) for row in file]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            sr = r
            sc = c
            break

pq = [(0, sr, sc, 0, 1)]
seen = {(sr, sc, 0, 1)}

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    seen.add((r, c, dr, dc))
    if grid[r][c] == "E":
        print(cost)
        break
    for ncost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == "#": continue
        if (nr, nc, ndr, ndc) in seen: continue
        heapq.heappush(pq, (ncost, nr, nc, ndr, ndc))
