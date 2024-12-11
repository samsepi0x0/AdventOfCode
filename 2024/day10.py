file = open("input.txt", "r")
lines = file.readlines()

grid = []

for line in lines:
    line = line.strip()
    grid.append(list(map(int, list(line))))

m = len(grid)
n = len(grid[0])
ind = 1
vis = dict()
vis2 = dict()

def check(grid, st, en, i, j, val, vis, seen):
    seen.add((i,j))
    if (grid[i][j] == 9):
        if (st, en) not in vis.keys():
            vis[(st, en)] = 0
        vis[(st, en)] += 1
        return
    if (i-1 >= 0 and (i-1, j) not in seen and grid[i-1][j] == val+1):
            check(grid, st, en, i-1, j, val + 1, vis, seen)
    if (i+1 < len(grid) and (i+1, j) not in seen and grid[i+1][j] == val+1):
        check(grid, st, en, i+1, j, val + 1, vis, seen)
    if (j+1 < len(grid[0]) and (i, j+1) not in seen and grid[i][j+1] == val+1):
        check(grid, st, en, i, j+1, val + 1, vis, seen)
    if (j-1 >= 0 and (i, j-1) not in seen and grid[i][j-1] == val+1):
        check(grid, st, en, i, j-1, val + 1, vis, seen)    

def check2(grid, st, en, i, j, val, vis):
    if (grid[i][j] == 9):
        if (st, en) not in vis.keys():
            vis[(st, en)] = 0
        vis[(st, en)] += 1
        return
    if (i-1 >= 0 and grid[i-1][j] == val+1):
            check2(grid, st, en, i-1, j, val + 1, vis)
    if (i+1 < len(grid) and grid[i+1][j] == val+1):
        check2(grid, st, en, i+1, j, val + 1, vis)
    if (j+1 < len(grid[0]) and grid[i][j+1] == val+1):
        check2(grid, st, en, i, j+1, val + 1, vis)
    if (j-1 >= 0 and grid[i][j-1] == val+1):
        check2(grid, st, en, i, j-1, val + 1, vis)    

for i in range(m):
    for j in range(n):
        if (grid[i][j] == 0):
            seen = set()
            check(grid, i, j, i, j, 0, vis, seen)
            check2(grid, i, j, i, j, 0, vis2)

score = 0
score2 = 0

for val in vis.values():
    score += val

for val in vis2.values():
    score2 += val

print("Part 1 : ", score)
print("Part 2 : ", score2)