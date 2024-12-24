# Advant of Code 2024 Day 17

# Question 2

import re

# program = list(map(int, re.findall(r"\d+", open("input.txt").read())[3:]))
text = "2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0"
program = [int(x) for x in text.split(",")]
assert program[-2:] == [3,0]

def find(input, ans):
    if input == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None

        def getCombo(operand):
            if 0 <= operand <= 3: return operand
            if operand == 4: return a
            if operand == 5: return b
            if operand == 6: return c
            else: exit(0)

        for pointer in range(0, len(program) - 2, 2): 
            ins = program[pointer]
            operand = program[pointer + 1]
            if ins == 0:
                assert operand == 3
            elif ins == 1:
                b = b ^ operand
            elif ins == 2:
                b = getCombo(operand) % 8
            elif ins == 3:
                raise AssertionError("Program has jump in unexpceted area") 
            elif ins == 4:
                b = b ^ c
            elif ins == 5:
                assert output is None, "Have too many outputs"
                output = getCombo(operand) % 8
            elif ins == 6:
                b = a >> getCombo(operand)
            elif ins == 7:
                c = a >> getCombo(operand)
            if output == input[-1]:
                sub = find(input[:-1], a)
                if sub is None: continue
                return sub 
print(find(program, 0))
