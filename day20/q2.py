# Advant of Code 2024 Day 20

# Question 2

grid = []
with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])
count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            break
    else: continue
    break


distance = [[-1] * cols for _ in range(rows)]
distance[r][c] = 0

while grid[r][c] != "E":
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == "#": continue
            if distance[nr][nc] > -1: continue
            distance[nr][nc] = distance[r][c] + 1
            r = nr 
            c = nc

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#": continue
        for radius in range(2, 21):
            for dr in range(radius + 1):
                dc = radius - dr
                for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c -dc)}:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "#": continue
                        if distance[r][c] - distance[nr][nc] >= 100 + radius:
                            count += 1

print(count)
