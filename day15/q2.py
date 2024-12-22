# Advant of Code 2024 Day 15

# Question 2

grid = []
moves = []
movement = {">": (0, 1), "<" : (0, -1), "^" : (-1, 0), "v" : (1, 0)}

with open("input.txt", "r") as file:
    top, bottom = file.read().split("\n\n")

    expansion = {"#" : "##", "." : "..", "O" : "[]", "@" : "@." }

    grid = [list("".join(expansion[char] for char in line)) for line in top.splitlines()]
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
    go = True
    for cr, cc in  targets:
        nr, nc = cr + direction[0], cc + direction[1]
        if (nr, nc) in targets: continue
        char = grid[nr][nc]
        if char == "#": 
            go = False
            break
            
        if char == "[":
            targets.append((nr,nc))
            targets.append((nr, nc + 1))
        
        if char == "]":
            targets.append((nr, nc))
            targets.append((nr, nc - 1))

    if not go: continue
    copy = [list(row) for row in grid]
    grid[r][c] = "."
    grid[r + direction[0]][c + direction[1]] = "@"
    for br, bc in set(targets[1:]):
        grid[br][bc] = "."
    for br, bc in set(targets[1:]):
        grid[br + direction[0]][bc + direction[1]] = copy[br][bc]
    r += direction[0]
    c += direction[1]


print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "["))