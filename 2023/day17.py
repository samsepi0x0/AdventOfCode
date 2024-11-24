from heapq import heappush, heappop

def part1(grid):
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)] # heat, row, col, dirx, diry, steps

    while pq:
        heat, r, c, dirx, diry, steps = heappop(pq)

        if (r, c) == (len(grid)-1, len(grid[0])-1):
            print(f"Score: {heat}")
            break

        if ((r, c, dirx, diry, steps) in seen):
            continue
        seen.add((r, c, dirx, diry, steps))
        
        if steps < 3 and (dirx, diry) != (0, 0):
            x = r + dirx
            y = c + diry
            if (x >= 0 and x < len(grid)) and (y >= 0 and y < len(grid[0])):
                heappush(pq, (heat + grid[x][y], x, y, dirx, diry, steps+1))
        
        for ndirx, ndiry in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (ndirx, ndiry) == (dirx, diry) or (ndirx, ndiry) == (-dirx, -diry):
                continue
            x = r + ndirx
            y = c + ndiry
            if (x >= 0 and x < len(grid)) and (y >= 0 and y < len(grid[0])):
                heappush(pq, (heat + grid[x][y], x, y, ndirx, ndiry, 1))
        
def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    grid = []
    for line in lines:
        grid.append(list(map(int, line.strip())))

    part1(grid)

if __name__ == "__main__":
    main()