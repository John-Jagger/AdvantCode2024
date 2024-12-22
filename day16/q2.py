# Advant of Code 2024 Day 16

# Question 2 

import heapq
from collections import deque

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

pq = [(0, sr, sc, 0, 1, None, None, None, None)]
lowset_cost = {(sr, sc, 0, 1):0}
back_track = {}
best_cost = float("inf")
end_state = set()

while pq:
    cost, r, c, dr, dc, lr, lc, ldr, ldc = heapq.heappop(pq)
    if cost > lowset_cost.get((r, c, dr, dc), float("inf")): continue
    lowset_cost[(r, c, dr, dc)] = cost
    if grid[r][c] == "E":
        if cost > best_cost: break
        best_cost = cost
        end_state.add((r,c,dr,dc))
    if (r, c, dr, dc) not in back_track: back_track[(r, c, dr, dc)] = set()
    back_track[((r, c, dr, dc))].add((lr, lc, ldr, ldc))
    for ncost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == "#": continue
        if cost > lowset_cost.get((r, c, dr, dc), float("inf")): continue
        heapq.heappush(pq, (ncost, nr, nc, ndr, ndc, r, c, dr, dc))

states = deque(end_state)
seen = set(end_state)

while states:
    key = states.popleft()
    for last in back_track.get(key, []):
        if last in seen: continue
        seen.add(last)
        states.append(last)

print(len({(r,c) for r,c,_,_ in seen}) - 1)


