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

for i in range(m):
    for j in range(n):
        if (grid[i][j] == 0):
            seen = set()
            check(grid, i, j, i, j, 0, vis, seen)

score = 0

for val in vis.values():
    score += val

print("Score: ", score)