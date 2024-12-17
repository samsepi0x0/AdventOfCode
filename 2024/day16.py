import heapq
from collections import deque

file = open('input.txt', 'r')
lines = file.readlines()

grid = [list(line.strip()) for line in lines]

m, n = len(grid), len(grid[0])
sx, sy = 0, 0

for row, line in enumerate(grid):
    for col, val in enumerate(line):
        if (val == 'S'):
            sx, sy = row, col

pq = [(0, sx, sy, 0, 1)]
seen = {(sx,  sy, 0, 1)}

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    seen.add((r, c, dr, dc))
    if (grid[r][c] == 'E'):
        print(f"Part 1 : {cost}")
        break
    for ncost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == '#':
            continue
        if (nr, nc, ndr, ndc) in seen:
            continue
        heapq.heappush(pq, (ncost, nr, nc, ndr, ndc))


pq = [(0, sx, sy, 0, 1)]
lcost = {(sx, sy, 0, 1) : 0}
backtrack = {}
bestcost = float("inf")
end = set()

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    if cost > lcost.get((r, c, dr, dc), float("inf")):
        continue
    if (grid[r][c] == 'E'):
        if cost > bestcost:
            break
        bestcost = cost
        end.add((r, c, dr, dc))
    for ncost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == '#':
            continue
        lowest = lcost.get((nr, nc, ndr, ndc), float("inf"))
        if ncost > lowest:
            continue
        if ncost < lowest:
            backtrack[(nr, nc, ndr, ndc)] = set()
            lcost[(nr, nc, ndr, ndc)] = ncost
        backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
        heapq.heappush(pq, (ncost, nr, nc, ndr, ndc))

states = deque(end)
seen = set(end)

while states:
    key = states.popleft()
    for last in backtrack.get(key, []):
        if last in seen:
            continue
        seen.add(last)
        states.append(last)

new_seen = {(r, c) for r, c, _, _ in seen}

print(f"Part 2: {len(new_seen)}")