# Advant of Code 2024 Day 11

# Question 2

from functools import cache

stones = []

with open("input.txt", "r") as file:
    for line in file:
        stones = list(map(int, list(line.strip().split(" "))))


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    char = str(stone)
    length = len(char)
    if length % 2 == 0:
        return count(int(char[:(length // 2)]), steps - 1) + count(int(char[(length // 2):]), steps - 1)
    return count(stone * 2024, steps - 1)

print(sum(count(stone, 75) for stone in stones))