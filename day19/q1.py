# Advant of Code 2024 Day 19

# Question 1

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
    if design == "": return True
    for i in range(maxlen):
        if design[:i] in patterns and find(design[i:]):
            return True
    return False
        
print( sum( find(design) for design in designs ) )
