def find_center(grid):
    for row in range(1, len(grid)):
        top = grid[:row][::-1]
        bottom = grid[row:]

        top = top[:len(bottom)]
        bottom = bottom[:len(top)]

        if (top == bottom):
            return True, row
    return False, -1

def rotate(grid):
    grid_transpose = [""] * len(grid[0])

    for line in grid:
        for ind, ch in enumerate(line):
            grid_transpose[ind] += ch
    return grid_transpose

def part1(grids):
    score = 0
    for grid in grids:

        found, center = find_center(grid)

        if (found):
            score = score + (100 * center)
            continue
        
        found, center = find_center(rotate(grid))
        if (found):
            score = score + (center)

    print(f"Part 1: {score}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    
    matrix = []
    grid = []
    for line in lines:
        if len(line.strip()) == 0:
            grid.append(matrix)
            matrix = []
        else:
            matrix.append(line.strip())
    grid.append(matrix)
    part1(grid)


main()
