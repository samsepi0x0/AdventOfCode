file = open('input2.txt', 'r')
lines = file.readlines()

keys = []
locks = []

grid = []

for line in lines:
    line = line.strip()
    if len(line) == 0:
        if (grid[0] == "#####"):
            locks.append(grid)
        else:
            keys.append(grid)
        grid = []
    else:
        grid.append(line)

lock_array = []

for lock in locks:
    L = [0]* len(lock[0])
    for row in range(1, len(lock)):
        for col in range(0, len(lock[0])):
            if lock[row][col] == '#':
                L[col] += 1
    lock_array.append(L)

key_array = []

for key in keys:
    L = [0] * len(key[0])
    for row in range(0, len(key)-1):
        for col in range(0, len(key[0])):
            if key[row][col] == '#':
                L[col] += 1
    key_array.append(L)

possible = 0
for lock in lock_array:
    for key in key_array:
        X = []
        flag = True
        for x, y in zip(lock, key):
            X.append(x+y)
            if (X[-1] > 5):
                flag = False
                break
        if flag:
            possible += 1

print(f"Part 1 : {possible}")