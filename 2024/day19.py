from functools import lru_cache

file = open('input.txt', 'r')
lines = file.readlines()

towels = lines[0].strip().split(", ")

patterns = []

for line in lines[2:]:
    patterns.append(line.strip())

@lru_cache
def check(pattern):
    if (pattern == ""):
        return 1
    flag = 0
    for towel in towels:
        if pattern.startswith(towel):
            flag += check(pattern[len(towel):])
    return flag

score = 0
score2 = 0
for pattern in patterns:
    val = check(pattern)
    score2 += val
    if (val > 0):
        score += 1

print(f"Part 1 : {score}")
print(f"Part 2 : {score2}")