# Advant of Code 2024 Day 8

# Question 2

mp = []
antenna = ""
antinode = set()

def calcOffset(array, r1, c1, r2, c2, deltaR, deltaC):
    while True:
        key = (r1 - deltaR, c1 - deltaC)
        if 0 <= key[0] < len(array) and 0 <= key[1] < len(array[0]):
            antinode.add(key)
        elif not( 0 <= key[0] < len(array) and 0 <= key[1] < len(array[0])):
            break
        r1, c1 = key[0], key[1]

    while True:
        key = (r2 + deltaR, c2 + deltaC)
        if 0 <= key[0] < len(array) and 0 <= key[1] < len(array[0]):
            antinode.add(key)
        elif not( 0 <= key[0] < len(array) and 0 <= key[1] < len(array[0])):
            break
        r2, c2 = key[0], key[1]
    return

def calcAntinodes(array, character, sr, sc):
    output = 0
    for r in range(len(mp)):
        for c in range(len(mp[0])):
            if array[r][c] == character and (r,c) != (sr, sc):
                deltaR = r-sr
                deltaC = c-sc
                antinode.add((r,c))
                calcOffset(array, sr, sc, r, c, deltaR, deltaC)
    return

with open("input.txt", "r") as file:
    for line in file:
        mp.append(list(line.strip()))

for r in range(len(mp)):
    for c in range(len(mp[0])):
        if mp[r][c] != ".":
            antenna = mp[r][c]
            calcAntinodes(mp, antenna, r, c)

print(len(antinode))