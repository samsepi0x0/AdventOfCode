file = open("input.txt", "r")
lines = file.readlines()

M, N = 101, 103
robots = {}

for id, line in enumerate(lines):
    pos, vel = line.strip().split(" ")
    px, py = pos.split("=")[1].split(",")
    vx, vy = vel.split("=")[1].split(",")

    robots[id] = [(int(px), int(py)), (int(vx), int(vy))]


for robot, values in robots.items():
    pos, vel = values
    px, py = pos
    vx, vy = vel
    
    # print(px, py, vx, vy)
    
    Px = (px + vx*100) % M
    Py = (py + vy*100) % N

    robots[robot] = ((Px, Py), (vx, vy))
        
quads = [0, 0, 0, 0]
for robot, values in robots.items():
    pos, vel = values
    px, py = pos

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
