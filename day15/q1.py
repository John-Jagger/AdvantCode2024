# Advant of Code 2024 Day 15

# Question 1

grid = []
moves = []
movement = {">": (0, 1), "<" : (0, -1), "^" : (-1, 0), "v" : (1, 0)}

with open("input.txt", "r") as file:
    top, bottom = file.read().split("\n\n")
    grid = [list(line) for line in top.splitlines()]
    moves = list(bottom.replace("\n", ""))

rows = len(grid)
cols = len(grid[0])
robot = (0,0)

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            robot = (r,c)
            break

r = robot[0]
c = robot[1]

for move in moves:
    direction = movement[move]
    targets = [(r,c)]
    cr, cc = r, c
    go = True
    while True:
        cr, cc = cr + direction[0], cc + direction[1]
        char = grid[cr][cc]
        if char == "#": 
            go = False
            break

        if char == ".":
            break
            
        if char == "O":
            targets.append((cr,cc))

    if not go: continue
    grid[r][c] = "."
    grid[r + direction[0]][c + direction[1]] = "@"
    for br, bc in targets[1:]:
        grid[br + direction[0]][bc + direction[1]] = "O"
    r += direction[0]
    c += direction[1]


print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "O"))