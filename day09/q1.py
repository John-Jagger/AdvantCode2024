# Advant of Code 2024 Day 9

# Question 1

input = ""
disk= []
fileNum = 0
count = 0

with open("input.txt", "r") as file:
    for line in file:
        input += line.strip()

for i, char in enumerate(input):
    x = int(char)
    if i % 2 == 0:
        disk += [fileNum] * x
        fileNum += 1
    else:
        disk += [-1] * x

blanks = [ i for i, value in enumerate(disk) if value == -1]

for i in blanks:
    while disk[-1] == -1: disk.pop()
    if len(disk) <= i: break
    disk[i] = disk.pop()

for i in range(len(disk)):
    count += i * disk[i]

print(count)