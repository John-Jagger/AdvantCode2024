# Advant of Code 2024 Day 12

# Question 2

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

def sides(region):
    edges = {}
    for r, c in region:
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if (nr, nc) in region: continue
            er = (r + nr) / 2
            ec = (c + nc) / 2
            edges[(er, ec)] = (er - r, ec - c)
    seen = set()
    side_count = 0
    for edge, direction in edges.items():
        if edge in seen: continue
        seen.add(edge)
        side_count += 1
        er, ec = edge
        if er % 1 == 0:
            for dr in [-1, 1]:
                cr = er + dr
                while edges.get((cr, ec)) == direction:
                    seen.add((cr, ec))
                    cr += dr
        else:
            for dc in [-1, 1]:
                cc = ec + dc
                while edges.get((er, cc)) == direction:
                    seen.add((er, cc))
                    cc += dc
    return side_count

print(sum(len(region) * sides(region) for region in regions))