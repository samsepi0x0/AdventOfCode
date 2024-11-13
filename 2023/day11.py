def part1(grid):
    score = 0
    pairs = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (grid[i][j] == '#'):
            # found a hash, need to find distance to other galaxies.
                #print(f"Found galaxy at {i, j}")
                vertical = 0

                for x in range(j+1, len(grid[0])):
                    if (grid[i][x] == '#'):
                        #print(f"Found galaxy at {i, x}")
                        score += (x - j)
                
                for x in range(i+1, len(grid)):
                    vertical += 1
                    for y in range(0, len(grid[0])):
                        if (grid[x][y] == '#'):
                            pairs += 1
                            #print(f"Found galaxy from {i, j} to {x, y}")
                            #print(f"Vertical : {vertical} \tHorizontal: {abs(y-j)}")
                            score += vertical + abs(y - j)

    print(f"Pairs: {pairs}\nScore: {score}")

def main():
    lines = []
    with open('input1.txt', 'r') as f:
        for line in f:
            lines.append(list(line.strip()))
            if not ('#' in line):
                lines.append(list(line.strip()))
    result = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]
    linestp = []
    for i in range(len(result)):
        if not ('#' in result[i]):
            linestp.append(result[i])
        linestp.append(result[i])
    
    #for line in linestp:
    #    print(line)
    part1(linestp)    

if __name__ == '__main__':
    main()
