# Advant of Code 2024 Day 8

# Question 1

mp = []
antenna = ""
antinode = set()
count = 0

def calcOffset(array, offsetR, offsetC):
    key = (offsetR, offsetC)
    if 0 <= offsetR < len(array) and 0 <= offsetC < len(array[0]) and key not in antinode:
        antinode.add(key)
        return 1
    return 0

def calcAntinodes(array, character, sr, sc):
    output = 0
    for r in range(len(mp)):
        for c in range(len(mp[0])):
            if array[r][c] == character and (r,c) != (sr, sc):
                output += calcOffset(array, 2*sr-r, 2*sc-c) + calcOffset(array, 2*r-sr, 2*c-sc)
    return output

with open("input.txt", "r") as file:
    for line in file:
        mp.append(list(line.strip()))

for r in range(len(mp)):
    for c in range(len(mp[0])):
        if mp[r][c] != ".":
            antenna = mp[r][c]
            count += calcAntinodes(mp, antenna, r, c)

print(count)