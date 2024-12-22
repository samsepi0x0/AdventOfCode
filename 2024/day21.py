from collections import deque
from itertools import product

file = open("input.txt", "r")
lines = file.readlines()

def solve(string, grid):
    pos = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] is not None:
                pos[grid[r][c]] = (r, c)
    
    seq = {}
    for x in pos:
        for y in pos:
            if x == y:
                seq[(x, y)] = ["A"]
                continue
            possible = []
            q = deque([(pos[x], "")])
            optimal = float('inf')
            while q:
                (r, c), move = q.popleft()
                for nr, nc, nmove in [(r-1, c, "^"), (r+1, c, "v"), (r, c-1, "<"), (r, c+1, ">")]:
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    if grid[nr][nc] is None:
                        continue
                    if grid[nr][nc] == y:
                        if optimal < len(move) + 1:
                            break
                        optimal = len(move) + 1
                        possible.append(move+nmove+"A")
                    else:
                        q.append(((nr, nc), move+nmove))
                else:
                    continue
                break
            seq[(x, y)] = possible
    options = [seq[(x, y)] for x,y in zip("A"+string, string)]
    return ["".join(x) for x in product(*options)]


keypad = [["7","8","9"],["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
dirpad = [[None, "^", "A"], ["<", "v", ">"]]

score = 0

for line in lines:
    line = line.strip()
    level1 = solve(line, keypad)
    l2 = level1
    for _ in range(2):
        level2 = []
        for seq in level1:
            level2 += solve(seq, dirpad)
        minlen = min(map(len, level2))
        l2 = [seq for seq in level2 if len(seq) == minlen]
        level1 = l2
    length = len(l2[0])
    value = int(line[:-1], 10)
    score += (length * value)

print(f"Part 1 : {score}")