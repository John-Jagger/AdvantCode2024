# Advant of Code 2024 Day 7

# Question 2

total = 0

def solve(target, values):
    if len(values) == 1: return target == values[0]
    # ex: 3267 | 81 40 27, we take 27 and make sure it is a factor of 3267 (which it is) then we divide 3267 by 27
    #   getting 121, we then send 
    #   121 as the target and 
    #   81 40 as the values (repeat)
    if target % values[-1] == 0 and solve(target // values[-1], values[:-1]): return True
    # ex: 3267 | 81 40 27, we take 27 and make sure it is a less than 3267 (which it is) then we subtract 27 from 3267
    #   getting 3240, we then send
    #   3240 as the target and
    #   81 40 as the vlaues (repeat)
    if target > values[-1] and solve(target - values[-1], values[:-1]): return True
    s_target = str(target)
    s_lastValue = str(values[-1])
    if len(s_target) > len(s_lastValue) and s_target.endswith(s_lastValue) and solve(int(s_target[:-len(s_lastValue)]), values[:-1]):return True
    # ex: 178 | 17 8, we check id 8 is less than 178 and if 8 is in 178 if so we remve 8 from 178
    #   getting 17 as the targte and value
    str(values)
    return False

with open("input.txt", "r") as file:
    for line in file:
        target, values = line.strip().split(": ")
        target = int(target)
        values = [int(value) for value in values.split(" ")]
        if solve(target, values):
            total += target

print(total)        