# Advant of Code 2024 Day 17

# Question 1

rA = 108107566389757
rB = 0
rC = 0

text = "2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0"
program = [int(x) for x in text.split(",")]
pointer = 0
output = []

def getCombo(operand):
    if 0 <= operand <= 3: return operand
    if operand == 4: return rA
    if operand == 5: return rB
    if operand == 6: return rC
    else: exit(0)

while pointer < len(program):
    inst = program[pointer]
    operand = program[pointer + 1]
    if inst == 0:
        rA = rA >> getCombo(operand)
    elif inst == 1:
        rB = rB ^ operand
    elif inst == 2:
        rB = getCombo(operand) % 8
    elif inst == 3:
        if rA != 0:
            pointer = operand
            continue
    elif inst == 4:
        rB = rB ^ rC
    elif inst == 5:
        output.append(getCombo(operand) % 8)
    elif inst == 6:
        rB = rA >> getCombo(operand)
    elif inst == 7:
        rC = rA >> getCombo(operand)
    pointer += 2

print(*output, sep=",")

