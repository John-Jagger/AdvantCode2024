# Advant of Code 2024 Day 17

# Question 2

import re

program = list(map(int, re.findall(r"\d+",open("input.txt").read())))[3:]

def find(prog: list[int], ans: int) -> int | None:
	if len(prog) == 0:
		print(ans)
		return ans

	for b in range(8):
		a = (ans << 3) + b
		if a == 0: a = 8
		b = a % 8
		b = b ^ 3
		c = a >> b
		b = b ^ c
		b = b ^ 3
		if b % 8 == prog[-1]:
			find(prog[:-1], a)

	return None


find(program, 0)
