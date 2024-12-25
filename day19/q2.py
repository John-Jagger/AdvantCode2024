# Advant of Code 2024 Day 19

# Question 2

from functools import cache

patterns = []
designs = []

with open("input.txt", "r") as file:
    switched = False
    for line in file:
        line = line.strip() 
        if not line: 
            switched = True
            continue
        if not switched:
            patterns = line.split(", ")
        else:
            designs.append(line)

maxlen = max(map(len, patterns))

@cache
def find(design):
    if design == "": return 1
    count = 0
    for i in range(min(len(design), maxlen) + 1): #either do up to len of the design of the maxlen of the pattenrs depending on which is shorter
        if design[:i] in patterns:
            count += find(design[i:])
    return count
        
print( sum( find(design) for design in designs ) )
