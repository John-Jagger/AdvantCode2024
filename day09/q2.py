# Advant of Code 2024 Day 9

# Question 2

input = ""
disk= []
copyDisk = []
files = set()
free = set()
fileNum = 0
count = 0

with open("input.txt", "r") as file:
    for line in file:
        input += line.strip()

for i, char in enumerate(input): #each pair represents the value and the length
    x = int(char)
    if i % 2 == 0:
        disk.append((fileNum, x))
        fileNum += 1
    else:
        disk.append((-1, x))

blanks = [ i for i, value in enumerate(disk) if value[0] == -1]

for chunk in reversed(disk):
    moved = False
    index = disk.index(chunk)
    for j in blanks:
        if moved or chunk in files or index < j: continue
        if chunk[0] == -1: break
        blank = disk[j]
        if chunk[1] <= blank[1]:
            extra = blank[1] - chunk[1]
            disk[j] = chunk
            disk[index] = (-1, blank[1] - extra)
            if index != len(disk)-1 and disk[index+1][0] == -1:
                disk[index] = (-1, disk[index][1] + disk[index+1][1])
                disk.pop(index+1)
            if index != 0 and disk[index-1][0] == -1:
                disk[index] = (-1, disk[index][1] + disk[index-1][1])
                disk.pop(index-1)
            if extra > 0: 
                disk.insert(j+1, (-1, extra))
            moved = True
    i+=1
    blanks = [ i for i, value in enumerate(disk) if value[0] == -1]
    files.add(chunk)

for file in disk:
    copyDisk += [file[0]] * file[1]

for i in range(len(copyDisk)):
    if copyDisk[i] == -1: continue
    count += i * copyDisk[i]


print(count)