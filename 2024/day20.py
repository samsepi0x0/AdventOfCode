from collections import deque
from tqdm import tqdm

file = open("input.txt", 'r')
lines = file.readlines()

grid = [list(line.strip()) for line in lines]

sr, sc = 0, 0
er, ec = 0, 0
for row, line in enumerate(grid):
    for col, ch in enumerate(line):
        if ch == 'S':
            sr, sc = row, col
        if ch == 'E':
            er, ec = row, col

def search(grid):
    global sr, sc, er, ec
    m, n = len(grid), len(grid[0])

    q = deque([(sr, sc, 0)])
    seen = {(sr, sc)}
    track = {(sr, sc): None}
    Cost = 0

    while (q):
        r, c, cost = q.popleft()
        if grid[r][c] == 'E':
            Cost = cost
            break
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr < 0 or nr >= m or nc < 0 or nc >= n):
                continue
            if (nr, nc) in seen:
                continue
            if grid[nr][nc] == '#':
                continue
            q.append((nr, nc, cost + 1))
            seen.add((nr, nc))
            track[(nr, nc)] = (r, c)

    path = set()

    while track[(er, ec)] != None:
        path.add(track[(er, ec)])
        er, ec = track[(er, ec)]
    
    return Cost, path 

initialCost, initialPath = search(grid)
print(f"Initial cost: {initialCost}")
walls = set()
costChange = dict()
score = 0

for cell in tqdm(initialPath):
    r, c = cell
    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if (nr, nc) in initialPath:
            continue
        if (nr, nc) in walls:
            continue
        if grid[nr][nc] != '#':
            continue
        walls.add((nr, nc))
        grid[nr][nc] = '.'
        new_cost, new_path = search(grid)
        grid[nr][nc] = '#'
        diff = initialCost - new_cost
        if not (diff in costChange.keys()):
            costChange[diff] = 0
        costChange[diff] += 1

for key in sorted(costChange.keys()):
    if key >= 100:
        score += costChange[key]

print(f"Part 1: {score}")
