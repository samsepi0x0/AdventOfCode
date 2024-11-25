#shoelace and pick theorem - day 10
def part1(commands):
    N = 500
    x, y = 220, 190
    # N = 30
    # x, y = 15, 15
    grid = [['.' for i in range(1, N)] for i in range(1, N)]
    score = 0
    seen = list()
    boundary = 0
    for dirn, steps in commands:
        seen.append((x-220, y-190))
        for i in range(0, steps):
            grid[x][y] = '#'
            boundary += 1
            if dirn == 'R':
                y += 1
            elif dirn == 'L':
                y -= 1
            elif dirn == 'U':
                x -= 1
            else:
                x += 1 
    output(grid, N, "before.png")
    seen.append(seen[0])

    seen = seen[::-1]
    area = 0
    for i in range(0, len(seen)-1):
        x0, y0 = seen[i]
        x1, y1 = seen[i+1]
        area = area + (x0+x1)*(y1-y0)
    area = area // 2
    interior = area - (boundary // 2) + 1
    score = (boundary + interior)
    print(f"Part 1: {score}")

def output(arr, N, name='a.png'):
    from PIL import Image, ImageDraw
    cell_size = 5
    cell_border = 1

    # Create a blank canvas
    img = Image.new(
        "RGBA",
        (N * cell_size, N * cell_size),
        "black"
    )
    draw = ImageDraw.Draw(img)

    for i, row in enumerate(arr):
        for j, col in enumerate(row):

            # Walls
            if col == '.':
                fill = (40, 40, 40)

            # Empty cell
            else:
                fill = (237, 240, 252)

            # Draw cell
            draw.rectangle(
                ([(j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                fill=fill
            )

    img.save(name)

def main():
    file = open("input.txt.1", 'r')
    lines = file.readlines()

    commands = []
    for line in lines:
        dirn, steps = line.strip().split(" ")[:2]
        commands.append((dirn, int(steps)))
    
    part1(commands)

if __name__ == "__main__":
    main()