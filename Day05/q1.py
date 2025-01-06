# Advent of coding 2024 day 5

#Question 1

def check(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            key = (update[i], update[j])
            if key in cache and not cache[key]:
                return False
    return True

rules = []
updates = []
cache = {}
count = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if "|" in line:
            rules.append(line.split("|"))
        elif "," in line:
            updates.append(line.split(","))

for x,y in rules:
    cache[(x,y)] = True
    cache[(y,x)] = False

for update in updates:
    if check(update):
        count += int(update[len(update) // 2])

print(count)