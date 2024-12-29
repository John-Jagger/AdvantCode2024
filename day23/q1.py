# Advant of Code 2024 Day 23

# Question 1

lans = []


with open("input.txt", "r") as file:
    for line in file:
        lans.append(line.strip().split("-"))


connections = {}
for x,y in lans:
    if x not in connections: connections[x] = set()
    if y not in connections: connections[y] = set()
    connections[x].add(y)
    connections[y].add(x)

sets = set()

for x in connections:
    for y in connections[x]:
        for z in connections[y]:
            if x != z and x in connections[z]:
                sets.add(tuple(sorted([x,y,z])))

count = 0 

print(len([s for s in sets if any(cn.startswith("t") for cn in s)]))