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
        return True
    flag = False
    for towel in towels:
        if pattern.startswith(towel):
            flag = flag or check(pattern[len(towel):])
    return flag

score = 0
for pattern in patterns:
    if check(pattern):
        score += 1

print(f"Part 1 : {score}")