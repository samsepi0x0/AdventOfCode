file = open('input.txt', 'r')
lines = file.readlines()

score = 0
for line in lines:
    line = int(line.strip())
    score += (line // 3) - 2

print(f"Part 1 :{score}")

score = 0

def f(fuel):
    global score
    val = ((fuel // 3) - 2)
    if val >= 0:
        score += val
        f(val)

for line in lines:
    fuel = int(line.strip())
    f(fuel)

print(f"Part 2: {score}")