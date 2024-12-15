file = open("input.txt", "r")
lines = file.readlines()

M, N = 101, 103
# M, N = 11, 7
robots = {}

for id, line in enumerate(lines):
    pos, vel = line.strip().split(" ")
    px, py = pos.split("=")[1].split(",")
    vx, vy = vel.split("=")[1].split(",")

    robots[id] = [(int(px), int(py)), (int(vx), int(vy))]

def part1():
    quads = [0, 0, 0, 0]
    for robot, values in robots.items():
        pos, vel = values
        px, py = pos
        vx, vy = vel
        
        # print(px, py, vx, vy)
        
        px = (px + vx*100) % M
        py = (py + vy*100) % N

        if (px < M // 2 and py < N // 2):
            quads[0] += 1
        elif (px > M //2 and py < N // 2):
            quads[1] += 1
        elif (px < M // 2 and py > N // 2):
            quads[2] += 1
        elif (px > M // 2 and py > N // 2):
            quads[3] += 1

    score = 1
    for val in quads:
        score *= val

    print(f"Part 1: {score}")

def part2():
    minScore = float('inf')
    bestTime = None
    for time in range(M*N):
        quads = [0, 0, 0, 0]
        for robot, values in robots.items():
            pos, vel = values
            px, py = pos
            vx, vy = vel
            Px = (px + vx*time) % M
            Py = (py + vy*time) % N

            if (Px < M // 2 and Py < N // 2):
                quads[0] += 1
            elif (Px > M //2 and Py < N // 2):
                quads[1] += 1
            elif (Px < M // 2 and Py > N // 2):
                quads[2] += 1
            elif (Px > M // 2 and Py > N // 2):
                quads[3] += 1
        score = quads[0]*quads[1]*quads[2]*quads[3]
        if (score < minScore):
            minScore = score
            bestTime = time
    
    print(f"Part 2 : {bestTime}")

    for robot, values in robots.items():
        pos, vel = values
        px, py = pos
        vx, vy = vel

        # print(px, py, vx, vy)

        Px = (px + vx*bestTime) % M
        Py = (py + vy*bestTime) % N

        robots[robot] = ((Px, Py), (vx, vy))

    grid = [['-' for _ in range(M)] for i in range(N)]

    for robot, values in robots.items():
        pos, vel = values
        px, py = pos
        grid[py][px] = "#"

    from PIL import Image, ImageDraw
    cell_size = 10
    cell_border = 0

    # Create a blank canvas
    img = Image.new(
        "RGBA",
        (M * cell_size, N * cell_size),
        "black"
    )
    draw = ImageDraw.Draw(img)

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '#':
                fill = (255, 255, 255)
            else:
                fill = (0, 0, 0)
            draw.rectangle(
                ([(j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                fill=fill
            )
    img.save("Easter.png")

part1()
part2()