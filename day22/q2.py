# Advant of Code 2024 Day 22

# Question 2

def monkey(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return(secret)


secret_nums = []

with open("input.txt", "r") as file:
    for line in file:
        secret_nums.append(int(line.strip()))

total = {}

for secret in secret_nums:
    buyer = [secret % 10]
    for i in range(2000):
        secret = monkey(secret)
        buyer.append(secret % 10)
    seen = set()
    for i in range(len(buyer) - 4):
        a,b,c,d,e= buyer[i:i+5]
        seq = (b-a, c-b, d-c, e-d)
        if seq in seen: continue
        seen.add(seq)
        if seq not in total: total[seq] = 0
        total[seq] += e
    
print(max(total.values()))