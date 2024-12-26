# Advant of Code 2024 Day 21

# Question 2

from collections import deque
from functools import cache
from itertools import product


def compute_seqs(keypad):
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
    return seqs

def solve(string, seqs):
    options = [seqs[(x,y)] for x,y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]

numeric_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

compute_num = compute_seqs(numeric_keypad)

dir_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

compute_dir = compute_seqs(dir_keypad)
dir_length = {key: len(value[0]) for key, value in compute_dir.items()}

total = 0

@cache
def compute_length(x,y,depth=25):
    if depth == 1:
        return dir_length[(x,y)]
    optimal = float("inf")
    for seq in compute_dir[(x,y)]:
        length = 0
        for i,j in zip("A" + seq, seq):
            length += compute_length(i,j,depth - 1)
        optimal = min(optimal, length)
    return optimal

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        inputs = solve(line, compute_num)
        optimal = float("inf")
        for seq in inputs:
            length = 0
            for x,y in zip("A" + seq, seq):
                length += compute_length(x,y)
            optimal = min(optimal, length)
        total += optimal * int(line[:-1])
print(total)

