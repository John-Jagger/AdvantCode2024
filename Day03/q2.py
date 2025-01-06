# Advent of coding 2024 day 3

#Question 2

from operator import mul

corrupted = []
result = 0
do = True
numbers = "1234567890"

def decrypt(list, index):
    right = ""
    left = ""
    failed = False
    comma = False
    i = index
    while i < len(list):
        if(i == index and line[i+3] == "("):
            i = i+4
        elif(not comma):
            if(numbers.find(line[i]) != -1):
                left += line[i]
                i+=1
            elif(line[i] == ","):
                i+=1
                comma = True
            else:
                failed = True
                break
        elif(comma):
            if(numbers.find(line[i]) != -1):
                right += line[i]
                i+=1
            elif(line[i] == ")"):
                break
            else:
                failed = True
                break
    if(not failed):
        return mul(int(left), int(right))
    else:
        return -1
    
def doing(list, index):
    i = index
    while i < len(list):
        if(list[i+2] == "(" and list[i+3] == ")"):
            return True
        elif(list[i+2] == "n"):
            return False
    
with open('input.txt', 'r') as file:
    for line in file:
        corrupted.append(line)

for line in corrupted:
    run = True
    while(run):
        doIndex = line.find("do")
        index = line.find("mul")
        if(index != -1):
            if(doIndex != -1):
                if(index < doIndex):
                    output = decrypt(line, index)
                    if(output != -1 and do):
                        result += output
                    line = line[index+1:]
                else:
                    do = doing(line, doIndex)
                    line = line[doIndex+1:]
            elif(doIndex == -1):
                output = decrypt(line, index)
                if(output != -1 and do):
                    result += output
                line = line[index+1:]
        elif(index == -1):
            run = False

print(result)



