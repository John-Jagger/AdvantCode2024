# Advant of Code 2024 Day 21

# Question 1

from collections import deque
from itertools import product


def solve(string, keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r,c)
    seqs = {}
    for i in pos:
        for j in pos:
            if i == j: 
                seqs[(i,j)] = ["A"]
                continue
            else:
                possibilities = []
                q = deque([(pos[i], "")])
                maxlen = float("inf")
                while q:
                    (cr, cc),  moves = q.popleft()
                    for nr, nc, nm in [(cr + 1, cc, "v"), (cr - 1, cc, "^"), (cr, cc + 1, ">"), (cr, cc - 1, "<")]:
                        if 0 <= nr < len(keypad) and 0 <= nc < len(keypad[0]):
                            if keypad[nr][nc] is None: continue
                            if keypad[nr][nc] == j:
                                if maxlen < len(moves) + 1: break
                                maxlen = len(moves) + 1
                                possibilities.append(moves + nm + "A")
                            else:
                                q.append(((nr, nc), moves + nm))
                    else:
                        continue
                    break

                seqs[(i,j)] = possibilities
    options = [seqs[(x,y)] for x,y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]

numeric_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

dir_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

total = 0 

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        robot1 = solve(line, numeric_keypad)
        next = robot1
        for _ in range(2):
            possible_next = []
            for seq in next:
                possible_next += solve(seq, dir_keypad)
            minlen = min(map(len, possible_next))
            next = [seq for seq in possible_next if len(seq) == minlen]
        length = len(next[0])
        complexity = length * int(line[:-1])
        total += complexity

print(total)