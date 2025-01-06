# Advent of coding 2024 day 4

#Question 2

words = []

with open('input.txt', 'r') as file:
    for line in file:
        words.append(line.strip())

output = 0

for r in range(1, len(words) - 1):
    for c in range(1, len(words[0]) - 1):
        if words[r][c] != "A": continue
        corners = [words[r - 1][c - 1], words[r - 1][c + 1], words[r + 1][c + 1], words[r + 1][c - 1]] #we get the up left, up right, down right, down left
        if "".join(corners) in ["MMSS","MSSM","SSMM","SMMS"]:
            output+=1
                    
print(output)