# Advent of coding 2024 day 1

#Question 2

leftList= []
rightList = []
output = 0

with open('input.txt', 'r') as file:
    for line in file:
        contents = line.split()
        leftList.append(int(contents[0]))
        rightList.append(int(contents[1]))

for i in range(len(leftList)):
    similarity = leftList[i] * rightList.count(leftList[i])
    output+=similarity

print(output)