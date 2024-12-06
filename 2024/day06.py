import sys
sys.setrecursionlimit(10000)

def part2(grid):
    x, y = -1, -1
    dirn = ""

    for row, line in enumerate(grid):
        for col, ch in enumerate(line):
            if (ch == '^'):
                x, y, dirn = row, col, 'N'
    
    def solve(x, y, dirn, obstacle = None, mapping = {'N' : 'E', 'E':'S', 'S':'W', 'W':'N'}, values = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}):
        visited = set()
        path = set()

        path.add((x, y, dirn))

        while (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            visited.add((x, y))
            dx, dy = values[dirn]
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) and (grid[nx][ny] == '#' or (obstacle and (nx, ny) == obstacle)):
                dirn = mapping[dirn]
            else:
                x, y = nx, ny
            
            if (x, y, dirn) in path:
                return True, visited
            path.add((x, y, dirn))
        return False, visited

    _, vis = solve(x, y, dirn)
    print(f"Part 1 : {len(vis)}")
    obstaclePos = 0

    for possible in vis:
        if not (vis == (x, y)):
            valid, _ = solve(x, y, dirn, obstacle=possible)
            if valid:
                obstaclePos += 1
    
    print(f"Part 2 : {obstaclePos}")


def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    grid = list() 
    for line in lines:
        grid.append(list(line.strip()))

    part2(grid)

if __name__ == "__main__":
    main()