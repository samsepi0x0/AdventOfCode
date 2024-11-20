import sys
sys.setrecursionlimit(10000)

def part1(grid):

    visited = set() 

    def f(dirn, r, c):
        if (dirn, r, c) in visited:
            return False
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])):
            return False
        visited.add((dirn, r, c))
        match dirn:
            case 'R':
                if grid[r][c] == '.':
                    return f(dirn, r, c+1)
                if grid[r][c] == '-':
                    return f(dirn, r, c+1)
                if grid[r][c] == '/':
                    return f('U', r-1, c)
                if grid[r][c] == '\\':
                    return f('D', r+1, c)
                if grid[r][c] == '|':
                    return f('U', r-1, c) or f('D', r+1, c)
            case 'D':
                match grid[r][c]:
                    case '.':
                        return f(dirn, r+1, c)
                    case '|':
                        return f(dirn, r+1, c)
                    case '/':
                        return f('L', r, c-1)
                    case '\\':
                        return f('R', r, c+1)
                    case '-':
                        return f('L', r, c-1) or f('R', r, c+1)
            case 'L':
                match grid[r][c]:
                    case '.':
                        return f(dirn, r, c-1)
                    case '-':
                        return f(dirn, r, c-1)
                    case '/':
                        return f('D', r+1, c)
                    case '\\':
                        return f('U', r-1, c)
                    case '|':
                        return f('D', r+1, c) or  f('U', r-1, c)
            case 'U':
                match grid[r][c]:
                    case '.':
                        return f(dirn, r-1, c)
                    case '|':
                        return f(dirn, r-1, c)
                    case '/':
                        return f('R', r, c+1)
                    case '\\':
                        return f('L', r, c-1)
                    case '-':
                        return f('R', r, c+1) or f('L', r, c-1)
    f('R', 0, 0)
    uniq_visited = set()
    for _, r, c in visited:
        uniq_visited.add((r, c))
    print(f"Part 1: {len(uniq_visited)}")


    maxCells = 0
    for i in range(0, len(grid)):
        visited = set()
        f('R', i, 0)
        uniq_visited = set()
        for _, r, c in visited:
            uniq_visited.add((r, c))
        maxCells = max(maxCells, len(uniq_visited))
        visited = set()
        uniq_visited = set()
        f('L', i, len(grid[0]) - 1)
        for _, r, c in visited:
            uniq_visited.add((r, c))
        maxCells = max(maxCells, len(uniq_visited))
        
    for i in range(0, len(grid[0])):
        visited = set()
        f('D', 0, i)
        uniq_visited = set()
        for _, r, c in visited:
            uniq_visited.add((r, c))
        maxCells = max(maxCells, len(uniq_visited))
        visited = set()
        uniq_visited = set()
        f('U', len(grid), i)
        for _, r, c in visited:
            uniq_visited.add((r, c))
        maxCells = max(maxCells, len(uniq_visited))
    
    print(f"Part 2: {maxCells}")

def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    grid = []
    for line in lines:
        grid.append(list(line.strip()))

    part1(grid)

if __name__ == "__main__":
    main()
