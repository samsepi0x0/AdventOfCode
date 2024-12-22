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

totalChanges = {}
maxBuy = 0
for line in lines:
    num = int(line.strip())
    diff = []
    changes = {}
    for i in range(1, 2000):
        num2 = compute(num)
        a, b = num % 10, num2 % 10
        diff.append(b - a)
        if (len(diff) > 4):
            diff = diff[1:]
        if (len(diff) == 4):
            st = (diff[0], diff[1], diff[2], diff[3])
            if st not in changes.keys():
                changes[st] = b
        num = num2
    for key, val in changes.items():
        if key not in totalChanges.keys():
            totalChanges[key] = list()
        totalChanges[key].append(val)

for key, value in totalChanges.items():
    maxBuy = max(maxBuy, sum(value))

print(f"Part 2: {maxBuy}")