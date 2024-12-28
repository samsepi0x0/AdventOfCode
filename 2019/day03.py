file = open("input.txt", "r")
lines = file.readlines()

wire1 = lines[0].strip().split(",")
wire2 = lines[1].strip().split(",")

def manhattan(a, b):
    return abs(a) + abs(b)

def plot(wire, path, st):
    r, c = 0, 0
    steps = 0

    for command in wire:
        dirn = command[0]
        value = int(command[1:])
        for d in range(value):
            if dirn == 'R':
                c += 1
            elif dirn == 'L':
                c -= 1 
            elif dirn == 'U':
                r -= 1 
            elif dirn == 'D':
                r += 1 
            path.add((r, c))
            if (r, c) not in st.keys():
                st[(r, c)] = steps + 1
            steps += 1
    return path

path1, path2 = set(), set()
d1 = dict()
d2 = dict()
path1 = plot(wire1, path1, d1)
path2 = plot(wire2, path2, d2)

common = path1.intersection(path2)
distance = min([manhattan(r, c) for r, c in common])

print(f"Part 1 : {distance}")

minsteps = min([(d1[(r,c)] + d2[(r,c)]) for r,c in common])

print(f"Part 2 : {minsteps}")