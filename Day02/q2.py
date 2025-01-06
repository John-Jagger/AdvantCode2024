# Advent of coding 2024 day 2

#Question 2



import numpy as np

def isSafe(report):
    diff = np.diff(report)
    return np.all((diff >= 1) & (diff <= 3)) or np.all((diff <= -1) & (diff >= -3))

def testModifications(report):
    # Try removing each element one by one and check if any result in a safe report
    for i in range(len(report)):
        test = report[:i] + report[i+1:]
        if isSafe(test):
            return True  # If any modification is safe, return True
    return False  # If no modification is safe, return False

safeReports = 0
reports = []

with open('input.txt', 'r') as file:
    for line in file:
        content = list(map(int, line.split()))
        reports.append(content)

for report in reports:
    diff = np.diff(report)
    isNeg = np.signbit(diff[0])
    safe = True

    for i in range(len(diff)):
        value = abs(diff[i])
        if 1 <= value <= 3 and isNeg == np.signbit(diff[i]):
            continue
        else:
            if not testModifications(report):
                safe = False
                break
            else:
                safe = True
                break

    if safe:
        safeReports += 1

print(f"Number of safe reports: {safeReports}")
