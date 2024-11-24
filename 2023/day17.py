from heapq import heappush, heappop

def part1(grid):
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)] # heat, row, col, dirx, diry, steps

    while pq:
        heat, r, c, dirx, diry, steps = heappop(pq)

        if (r, c) == (len(grid)-1, len(grid[0])-1) and steps >= 4: # "and steps >= 4" is for part 2
            print(f"Score: {heat}")
            break

        if ((r, c, dirx, diry, steps) in seen):
            continue
        seen.add((r, c, dirx, diry, steps))
        
        if steps < 10 and (dirx, diry) != (0, 0): # modified consecutive steps from 3 to 10
            x = r + dirx
            y = c + diry
            if (x >= 0 and x < len(grid)) and (y >= 0 and y < len(grid[0])):
                heappush(pq, (heat + grid[x][y], x, y, dirx, diry, steps+1))
        
        if (dirx, diry) == (0, 0) or steps >= 4: # part 2 condition of minimum consecutive steps.
            for ndirx, ndiry in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if (ndirx, ndiry) == (dirx, diry) or (ndirx, ndiry) == (-dirx, -diry):
                    continue
                x = r + ndirx
                y = c + ndiry
                if (x >= 0 and x < len(grid)) and (y >= 0 and y < len(grid[0])):
                    heappush(pq, (heat + grid[x][y], x, y, ndirx, ndiry, 1))
        
def main():
    file = open("input.txt.1", "r")
    lines = file.readlines()

    grid = []
    for line in lines:
        grid.append(list(map(int, line.strip())))

    part1(grid)

if __name__ == "__main__":
    main()