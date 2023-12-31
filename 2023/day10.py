def part1():
    file = open("input10.txt")
    lines = file.readlines()

    map = list()

    for row, line in enumerate(lines):
        line = list(line.strip())
        map.append(line)
        if 'S' in line:
            start = (row, line.index('S'))


    legend = {
    "|": ((1, 0), (-1, 0)),
    "-": ((0, 1), (0, -1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((0, -1), (1, 0)),
    "F": ((0, 1), (1, 0)),
    }

    visited = [start]

    
    def addPoints(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def neighbors(curr, c):
        a = addPoints(curr, legend[c][0])
        b = addPoints(curr, legend[c][1])

        return (a, b)

    curr = ()

    for n in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        new_c = addPoints(start, n)
        if map[new_c[0]][new_c[1]] != ".":
            if start in neighbors(new_c, map[new_c[0]][new_c[1]]):
                curr = new_c
                break

    while True:
        last = visited[-1]
        visited.append(curr)
        a, b = neighbors(curr, map[curr[0]][curr[1]])

        if (a == start or b == start) and last != start:
            break
            
        if b == last:
            curr = a
        else:
            curr = b
    
    print("Steps: ", len(visited)//2)

    # field = [[0 for j in range(len(map[0]))] for i in range(len(map))] 
    # for i in range(0, len(map)):
    #     for j in range(0, len(map[0])):
    #         if (i, j) in visited:
    #             field[i][j] = 1
    
    # for i in range(len(map)):
    #     for j in range(len(map[0])):
    #         print(field[i][j], end='')
    #     print()

    visited.append(visited[0])

    area = 0

    for i in range(0, len(visited) - 1):
        x1, y1 = visited[i]
        x2, y2 = visited[i+1]

        area += (y2*x1 - x2*y1)
    
    print("Interior Points: ", abs(area)//2 + 1 - (len(visited)-1)//2)

def main():
    part1()

if __name__ == "__main__":
    main()