import sys
sys.setrecursionlimit(10000)

def part1(grid):
    score = 0
    x, y = -1, -1
    dirn = ""

    for row, line in enumerate(grid):
        for col, ch in enumerate(line):
            if (ch == '^'):
                x, y, dirn = row, col, 'N'
    
    vis = set()
    def solve(x, y, dirn, vis, mapping = {'N' : 'E', 'E':'S', 'S':'W', 'W':'N'}, values = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}):
        if ((x, y, dirn) in vis):
            return
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return

        vis.add((x, y, dirn))
        dx, dy = values[dirn]
        nx, ny = x + dx, y + dy

        if (nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0])):
            return
        
        if (grid[nx][ny] == '#'):
            solve(x, y, mapping[dirn], vis, mapping, values)
        else:
            solve(nx, ny, dirn, vis, mapping, values)
    

    solve(x, y, dirn, vis)
    cells = set()

    for x, y, _ in vis:
        cells.add((x, y))

    score = len(cells)
    print(f"Part 1 : {score}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    grid = list() 
    for line in lines:
        grid.append(list(line.strip()))

    part1(grid)

if __name__ == "__main__":
    main()