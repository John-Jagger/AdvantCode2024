# Advant of Code 2024 Day 7

# Question 1

total = 0

def solve(target, values):
    if len(values) == 1: return target == values[0]
    if target % values[-1] == 0 and solve(target // values[-1], values[:-1]): return True
    if target > values[-1] and solve(target - values[-1], values[:-1]): return True
    return False

with open("input.txt", "r") as file:
    for line in file:
        target, values = line.strip().split(": ")
        target = int(target)
        values = [int(value) for value in values.split(" ")]
        if solve(target, values):
            total += target

print(total)        