import numpy as np

def main():
    file = open("input_9.txt", 'r')
    lines = file.readlines()

    constant = 20

    head = (constant, 0)
    tail = (constant, 0)
    visited = [tail]
    rope = [np.array([0,0]) for _ in range(10)]
    tail_positions = set([tuple(rope[9])])


    for line in lines:
        line = line.strip().split(" ")
        dirn = line[0]
        counter = int(line[1])

        for i in range(counter):
            if dirn == 'R':
                head = move_r(head)
            if dirn == 'L':
                head = move_l(head)
            if dirn == 'U':
                head = move_u(head)
            if dirn == 'D':
                head = move_d(head)
            if not radar(head, tail):
                if indiag(head, tail):
                    tail = move_diagonal(head, tail)
                else:
                    if dirn == 'R':
                        tail = move_r(tail)
                    if dirn == 'L':
                        tail = move_l(tail)
                    if dirn == 'U':
                        tail = move_u(tail)
                    if dirn == 'D':
                        tail = move_d(tail)
                if tail not in visited:
                    visited.append(tail)

            """
                Part 2 reference: https://galaxyinferno.com/how-to-solve-advent-of-code-2022-day-9-with-python/
            """
            rope[0] = update_head(rope[0], dirn)
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i-1], rope[i])
            tail_positions.add(tuple(rope[9]))
            #print(dirn, head, tail, radar(head, tail))


    print("Score: ", len(set(visited)))
    print("New_Score: ", len(tail_positions))

def update_head(head, direction):
    if direction == 'R':
        head[1] += 1
    elif direction == 'L':
        head[1] -= 1
    elif direction == 'U':
        head[0] += 1
    elif direction == 'D':
        head[0] -= 1
    return head

def update_tail(head, tail):
    difference = head - tail
    change_for_tail={
        (2, 1):(1, 1),
        (1, 2):(1, 1),
        (2, 0):(1, 0),
        (2, -1):(1, -1),
        (1, -2):(1, -1),
        (0, -2):(0, -1),
        (-1, -2):(-1,-1),
        (-2, -1):(-1, -1),
        (-2, 0):(-1, 0),
        (-2, 1):(-1, 1),
        (-1, 2):(-1, 1),
        (0, 2):(0, 1),
        (2, 2):(1, 1),
        (-2, -2):(-1, -1),
        (-2, 2):(-1, 1),
        (2, -2):(1, -1)
      }
    new_tail_pos = tail + np.array(change_for_tail.get(tuple(difference), (0,0)))
    return new_tail_pos

def move_r(position):
    return (position[0], position[1]+1)

def move_u(position):
    return (position[0]-1, position[1])

def move_l(position):
    return (position[0], position[1]-1)

def move_d(position):
    return (position[0]+1, position[1])

def move_diagonal(head, tail):
    x, y = head[0], head[1]
    x1, y1 = tail[0], tail[1]

    if x1 == x-2:
        return (x-1, y)
    if y1 == y-2:
        return (x, y-1)
    if x1 == x+2:
        return (x+1, y)
    if y1 == y+2:
        return (x, y+1)

def indiag(head, tail):
    x, y = head[0], head[1]
    x1, y1 = tail[0], tail[1]

    if x1 == x-2 or x1 == x+2:
        return y1 == y-1 or y1 == y+1
    if x1 == x-1 or x1 == x+1:
        return y1 == y-2 or y1 == y+2

def radar(head, tail):
    x, y = head[0], head[1]
    x1, y1 = tail[0], tail[1]

    return (x1 == x or x1 == x+1 or x1 == x-1) and (y1 == y or y1 == y+1 or y1 == y-1)

if __name__ == '__main__':
    main()