# Advent of coding 2024 day 5

#Question 2

import functools 

def check(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            key = (array[i], array[j])
            if key in cache and cache[key] == 1:
                return False
    return True

def cmp(x, y):
    return cache.get((x,y), 0)


rules = []
updates =[]
cache = {}
count = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            rules.append(list(map(int, line.split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

for x,y in rules:
    cache[(x,y)] = -1
    cache[(y,x)] = 1

for update in updates:
    if check(update): continue
    update.sort(key=functools.cmp_to_key(cmp))
    count += update[len(update) // 2]

print(count)