# Advant of Code 2024 Day 12

# Question 1

from collections import deque

regions = []
seen = set()
garden = []
total = 0

with open("input.txt", "r") as file:
    for line in file:
        garden.append(list(line.strip()))                

for r in range(len(garden)):
    for c in range(len(garden[0])):
        if (r,c) in seen: continue
        seen.add((r,c))
        flower = garden[r][c]
        key = (1,0)
        region = {(r, c)}
        q = deque([(r, c)])
        while len(q) > 0:
            cr, cc = q.popleft()
            for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if 0 <= nr < len(garden) and 0 <= nc < len(garden[0]):
                    if garden[nr][nc] != flower: continue
                    if (nr, nc) in region: continue
                    region.add((nr, nc))
                    q.append((nr, nc))
        seen |= region
        regions.append(region)

def perimeter(region):
    output = 0
    for cr, cc in region:
        output += 4
        for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
            if (nr, nc) in region:
                output -= 1
    return output

print(sum(len(region) * perimeter(region) for region in regions))