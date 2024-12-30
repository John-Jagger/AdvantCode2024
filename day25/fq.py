# Advant of Code 2024 Day 25

# Final Question

keys = {}
locks = {}
chunks = []

with open("input.txt", "r") as file:
    for block in file.read().split("\n\n"):
        block = block.split("\n")
        if block[0] == "#####":
            locks[tuple(block)] = []
        elif block[0] == ".....":
            keys[tuple(block)] = []
        else:
            print(block)

def decrypt(grid):
    level = {
        0 : -1,
        1 : -1,
        2 : -1,
        3 : -1,
        4 : -1
    }
    values = []
    for r in range(7):
        for c in range(5):
            if grid[r][c] == ".": continue
            level[c] += 1
    for key, value in level.items():
        values.append(value)
    return values

for item in locks.keys():
    locks[item] = decrypt(item)

for item in keys.keys():
    keys[item] = decrypt(item)

count = 0

for lock in locks.keys():
    lockLevel = locks[lock]
    for key in keys.keys():
        keyLevel = keys[key]
        for i in range(5):
            if keyLevel[i] + lockLevel[i] >= 6: break
        else: count += 1

print(count)