# Advant of Code 2024 Day 11

# Question 1

stones = []

with open("input.txt", "r") as file:
    for line in file:
        stones = list(map(int, list(line.strip().split(" "))))

def reorder(array):
    output = []
    for stone in array:
        char = str(stone)
        length = len(char)
        if stone == 0: 
            output.append(1)
        elif length % 2 == 0:
            output.append(int(char[:-(int(length/2))]))
            output.append(int(char[-(int(length/2)):]))
        else: output.append(stone * 2024)
    return output


for i in range(25):
    stones = reorder(stones)
print(len(stones))