from collections import deque

file = open("input.txt", "r")
lines = file.readlines()

grid = []

for line in lines:
    grid.append(list(line.strip()))

M, N = len(grid), len(grid[0])
sr, sc = 0, 0

for row, line in enumerate(grid):
    for col, ch in enumerate(line):
        if (ch == 'S'):
            sr, sc = row, col

dists = [[-1] * N for _ in range(M)]
dists[sr][sc] = 0

while grid[sr][sc] != 'E':
    for nr, nc in [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)]:
        if nr < 0 or nr >= M or nc < 0 or nc >= N:
            continue
        if grid[nr][nc] == '#':
            continue
        if dists[nr][nc] != -1:
            continue
        dists[nr][nc] = dists[sr][sc] + 1
        sr = nr
        sc = nc


score = 0
for r in range(M):
    for c in range(N):
        if (grid[r][c] == '#'):
            continue
        for nr, nc in [(r + 2, c), (r + 1, c + 1), (r, c + 2), (r - 1, c + 1)]:
            if nr < 0 or nr >= M or nc < 0 or nc >= N:
                continue
            if grid[nr][nc] == '#':
                continue
            if abs(dists[r][c] - dists[nr][nc]) >= 102:
                score += 1

print(f"Part 1 : {score}")

score = 0
for r in range(M):
    for c in range(N):
        if (grid[r][c] == '#'):
            continue
        for rad in range(2, 21):
            for dr in range(0, rad+1):
                dc = rad - dr
                for nr, nc in {(r + dr, c + dc), (r+dr, c-dc), (r-dr, c+dc), (r-dr, c-dc)}:
                    if nr < 0 or nr >= M or nc < 0 or nc >= N:
                        continue
                    if grid[nr][nc] == '#':
                        continue
                    if dists[r][c] - dists[nr][nc] >= 100+rad:
                        score += 1

print(f"Part 2 : {score}")