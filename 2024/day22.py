file = open("input.txt", "r")
lines = file.readlines()

def compute(n):
    ns = n * 64
    n ^= ns
    n %= 16777216
    ns = n // 32
    n ^= ns 
    n %= 16777216
    ns = n * 2048
    n ^= ns
    n %= 16777216
    return n

score = 0
for line in lines:
    num = int(line.strip())
    for i in range(2000):
        num = compute(num)
    score += num

print(f"Part 1: {score}")