file = open('input.txt', 'r')
lines = file.readlines()

grid = []
row, col = 0, 0
inst = 0

for ind, line in enumerate(lines):
    line = list(line.strip())
    if (len(line) == 0):
        inst = ind+1
        break
    grid.append(line)
    if ('@' in line):
        row = ind
        col = line.index('@')

m, n = len(grid), len(grid[0])

instructions = ""
for ind in lines[inst:]:
    instructions += ind.strip()

for val in instructions:
    if val == '>':
        nr, nc = row, col + 1
        if (grid[nr][nc] == '#'):
            continue
        if (grid[nr][nc] == 'O'):
            while(grid[nr][nc] == 'O'):
                nc += 1
            if (grid[nr][nc] == '#'):
                continue
            else:
                for c in range(nc, col-1, -1):
                    grid[nr][c] = grid[nr][c-1]
                grid[row][col] = '.'
                col = col + 1
        else:
            grid[row][col+1], grid[row][col] = grid[row][col], grid[row][col+1]
            col += 1
    elif val == '<':
        nr, nc = row, col-1
        if (grid[nr][nc] == '#'):
            continue
        if (grid[nr][nc] == 'O'):
            while(grid[nr][nc] == 'O'):
                nc -= 1
            if (grid[nr][nc] == '#'):
                continue
            else:
                for c in range(nc, col):
                    grid[nr][c] = grid[nr][c+1]
                grid[row][col] = '.'
                col = col - 1
        else:
            grid[row][col-1], grid[row][col] = grid[row][col], grid[row][col-1]
            col -= 1
    elif val == 'v':
        nr, nc = row + 1, col
        if (grid[nr][nc] == '#'):
            continue
        if (grid[nr][nc] == 'O'):
            while(grid[nr][nc] == 'O'):
                nr += 1
            if (grid[nr][nc] == '#'):
                continue
            else:
                for r in range(nr, row, -1):
                    grid[r][nc] = grid[r-1][nc]
                grid[row][col] = '.'
                row = row + 1
        else:
            grid[row+1][col], grid[row][col] = grid[row][col], grid[row+1][col]
            row += 1
    elif val == '^':
        nr, nc = row - 1, col
        if (grid[nr][nc] == '#'):
            continue
        if (grid[nr][nc] == 'O'):
            while(grid[nr][nc] == 'O'):
                nr -= 1
            if (grid[nr][nc] == '#'):
                continue
            else:
                for r in range(nr, row+1):
                    grid[r][nc] = grid[r+1][nc]
                grid[row][col] = '.'
                row = row - 1
        else:
            grid[row-1][col], grid[row][col] = grid[row][col], grid[row-1][col]
            row -= 1 


score = 0
for row, line in enumerate(grid):
    for col, val in enumerate(line):
        if (val == 'O'):
            score += (100 * row) + col

print(f"Part 1 : {score}")