# Advant of Code 2024 Day 24

# Question 1

known = {}
formulas = {}

with open("input.txt", "r") as file:
    for line in file:
        if line.isspace(): break
        line = line.strip().split(": ")
        known[line[0]] = int(line[1])

    for line in file:
        x, op, y, z = line.replace(" -> ", " ").split()
        formulas[z] = (op, x, y)

operations = {
    "OR" : lambda x,y: x | y,
    "AND" : lambda x,y: x & y,
    "XOR" : lambda x,y: x ^ y
}
    
def calc(wire):
    if wire in known: return known[wire]
    op,x,y = formulas[wire]
    known[wire] = operations[op](calc(x), calc(y))
    return known[wire]

z = []
i = 0
while True:
    key = "z" +str(i).rjust(2, "0")
    if key not in formulas: break
    z.append(calc(key))
    i+=1

print(int("".join(map(str, (z[::-1]))), 2))
    
