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

score2 = 0

for key in map.keys():
    for region in map[key]:
        area = len(region)
        edges = {}
        for r, c in region:
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in region:
                    continue
                er, ec = (r + nr) / 2, (c + nc) / 2
                edges[(er, ec)] = (er - r, ec - c)
        seen = set()
        count = 0

        for edge, dirn in edges.items():
            if edge in seen:
                continue
            seen.add(edge)
            count += 1
            er, ec = edge
            if (er%1 == 0):
                for dr in [-1, 1]:
                    cr = er + dr
                    while edges.get((cr, ec)) == dirn:
                        seen.add((cr, ec))
                        cr = cr + dr
            else:
                for dc in [-1, 1]:
                    cc = ec + dc
                    while edges.get((er, cc)) == dirn:
                        seen.add((er, cc))
                        cc = cc + dc
        score2 += (area * count)

print(f"Part 2 : {score2}")