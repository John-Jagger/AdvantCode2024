# Advant of Code 2024 Day 23

# Question 2

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

def find_party(node, list):
    key = tuple(sorted(list))
    if key in sets: return
    sets.add(key)
    for neighbor in connections[node]:
        if neighbor in list: continue
        if not list <= connections[neighbor]: continue
        copy = set(list)
        copy.add(neighbor)
        find_party(neighbor, copy)



for x in connections:
    find_party(x, {x})

count = 0 

print(",".join(sorted(max(sets, key=len))))