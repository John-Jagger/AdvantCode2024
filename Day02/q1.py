# Advent of coding 2024 day 2

#Question 1

import numpy as np

safe = 0
reports = []

with open('input.txt', 'r') as file:
    for line in file:
        content = list(map(int, line.split()))
        reports.append(np.diff(content))

for report in reports:
    isNeg = True
    isSafe = True
    for i in range(len(report)):
        value = abs(report[i])
        if(i == 0):
            isNeg = np.signbit(report[i])
        if(value >= 1 and value <= 3 and isNeg == np.signbit(report[i])):
            continue
        else:
            isSafe = False
            break
    if(isSafe):
        safe += 1

print(safe)
        


