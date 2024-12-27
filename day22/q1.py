# Advant of Code 2024 Day 22

# Question 1

secret_nums = []
total = 0

with open("input.txt", "r") as file:
    for line in file:
        secret_nums.append(int(line.strip()))

print(secret_nums)

for secret in secret_nums:
    for i in range(2000):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216

    total += secret

print(total)
