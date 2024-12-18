from collections import deque

file = open('input.txt', 'r')
lines = file.readlines()

N = 71
bytes = 1024
# N = 7
# bytes = 12

grid = [['.' for _ in range(N)] for _ in range(N)]

for i in range(bytes):
    line = lines[i].strip().split(",")
    x, y = int(line[0]), int(line[1])
    grid[y][x] = '#'

def solve(grid):
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}

    while q:
        r, c, cost = q.popleft()
        if (r, c) == (N-1, N-1):
            return cost   
        for nr, nc in [(r + 1, c), (r - 1, c),  (r, c + 1), (r, c - 1)]:
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if grid[nr][nc] == '#':
                continue
            if (nr, nc) in seen:
                continue 
            seen.add((nr, nc))
            q.append((nr, nc, cost+1))
    return -1

print(f"Part 1 : {solve(grid)}")

grid = [['.' for _ in range(N)] for _ in range(N)]

for i in range(len(lines)):
    line = lines[i].strip().split(",")
    x, y = int(line[0]), int(line[1])
    grid[y][x] = '#'
    if (solve(grid) == -1):
        print(f"Part 2 : {x},{y}")
        break