def part1(grid, rows, cols):

    score = 0
    pairs = 0
    n = 1000000

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (grid[i][j] == '#'):
                vertical, horizontal = 0, 0
                for x in range(j+1, len(grid[0])):
                    if x in cols:
                        horizontal += n 
                    else:
                        horizontal += 1 
                    if (grid[i][x] == '#'):
                        pairs += 1 
                        score = score + horizontal
                        #print(f"Found source at {i, j} to destination at {i, x} with distance: 0i + {horizontal}j = {horizontal}")

                for x in range(i+1, len(grid)):
                    if x in rows:
                        vertical += n 
                    else:
                        vertical += 1 
                    for y in range(0, len(grid[0])):
                        if (grid[x][y] == '#'):
                            pairs += 1
                            horizontal = 0
                            start = min(y, j)
                            end = max(y, j)
                            for a in range(start, end):
                                if a in cols:
                                    horizontal += n 
                                else:
                                    horizontal += 1 
                            score += horizontal + vertical
                            #print(f"Found source at {i, j} to destination at {x, y} with distance: {vertical}i + {horizontal}j = {vertical + horizontal}")


    print(f"Pairs: {pairs}\nScore: {score}")

def main():
    lines = []
    rows = []
    cols = []
    r = 0
    with open('input1.txt', 'r') as f:
        for line in f:
            lines.append(list(line.strip()))
            if not ('#' in line):
                rows.append(r)
            r += 1 

    result = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]
    
    for i in range(len(result)):
        if not ('#' in result[i]):
            cols.append(i)
    
    #for line in lines:
        #print(line)
    
    #print(rows)
    #print(cols)

    part1(lines, rows, cols)    

if __name__ == '__main__':
    main()
