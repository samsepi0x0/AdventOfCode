file = open('input.txt', 'r')
lines = file.readlines()

def part1():
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

def part2():\

    from copy import deepcopy

    grid = []
    row, col = 0, 0
    inst = 0

    for ind, line in enumerate(lines):
        line = line.strip()
        if (len(line) == 0):
            inst = ind
            break
        l = []
        for ch in line:
            if (ch == '#'):
                l.append('#')
                l.append('#')
            elif (ch == 'O'):
                l.append('[')
                l.append(']')
            elif (ch == '.'):
                l.append('.')
                l.append('.')
            else:
                l.append('@')
                l.append('.')
        
        if '@' in l:
            row = ind
            col = l.index('@')
        grid.append(l)
    

    m, n = len(grid), len(grid[0])

    instructions = ""
    for ind in lines[inst:]:
        instructions += ind.strip()

    for val in instructions:
        dr = {"^": -1, "v": 1}.get(val, 0)
        dc = {"<": -1, ">": 1}.get(val, 0)
        target = [(row, col)]
        cr = row
        cc = col
        go = True

        for cr, cc in target:
            nr = cr + dr
            nc = cc + dc
            if (nr, nc) in target:
                continue
            char = grid[nr][nc]
            if (char == '#'):
                go = False
                break
            if (char == '['):
                target.append((nr, nc))
                target.append((nr, nc+1))
            if (char  == ']'):
                target.append((nr, nc))
                target.append((nr, nc-1))
            
        if not go:
            continue
        cp = deepcopy(grid)
        grid[row][col] = '.'
        grid[row+dr][col+dc] = '@'
        for br, bc in target[1:]:
            grid[br][bc] = '.'
        for br, bc in target[1:]:
            grid[br+dr][bc+dc] = cp[br][bc]
        
        row += dr
        col += dc
    
    print("Part 2: ", sum(100*r + c for r in range(m) for c in range(n) if grid[r][c] == '['))

        
part1()
part2()