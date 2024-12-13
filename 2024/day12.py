file = open("input.txt", "r")
lines = file.readlines()

grid = list()
gridcp = list()

for line in lines:
    grid.append(list(line.strip()))
    gridcp.append(list(line.strip()))

map = dict()

def solve(r, c, val, vis):
    if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != val):
        return
    vis.add((r, c))
    grid[r][c] = '#'
    solve(r-1, c, val, vis)
    solve(r, c-1, val, vis)
    solve(r, c+1, val, vis)
    solve(r+1, c, val, vis)

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if (grid[r][c] != '#'):
            vis = set()
            solve(r, c, col, vis)
            if col not in map.keys():
                map[col] = list()
            map[col].append(vis)

score = 0

for key in map.keys():
    for region in map[key]:
        area = len(region)
        perim_coord = list()
        for r, c in region:
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or gridcp[nr][nc] != key):
                    perim_coord.append((nr, nc))
        
        perimeter = len(perim_coord)
        score += (area * perimeter)

print(f"Part 1: {score}")