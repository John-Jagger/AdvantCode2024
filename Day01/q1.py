# Advent of coding 2024 day 1

#Question 1

leftList= []
rightList = []
output = 0

with open('input.txt', 'r') as file:
    for line in file:
        contents = line.split()
        leftList.append(int(contents[0]))
        rightList.append(int(contents[1]))

leftList.sort()
rightList.sort()

for i in range(len(leftList)):
    output += abs(leftList[i] - rightList[i])

print(output)