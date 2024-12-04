def part1(lines):
    score = 0
    m = len(lines)
    n = len(lines[0])
    key = "XMAS"
    rkey = key[::-1]

    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if (ch == 'X'):
                right = ""
                for i in range(0, 4):
                    if (col+i >= n):
                        break
                    right += lines[row][col+i]
                
                if (right == key or right == rkey):
                    score += 1
                    
                left = ""
                for i in range(0, 4):
                    if (col-i < 0):
                        break
                    left += lines[row][col-i]
                
                if (left == key or left == rkey):
                    score += 1
                    
                up = ""
                for i in range(0, 4):
                    if (row - i < 0):
                        break
                    up += lines[row-i][col]

                if (up == key or up == rkey):
                    score += 1
                    
                down = ""
                for i in range(0, 4):
                    if (row + i >= m):
                        break
                    down += lines[row + i][col]

                if (down == key or down == rkey):
                    score += 1
                    
                rudiag = ""
                for i in range(0,4):
                    if (row + i >= m or col -i < 0):
                        break
                    rudiag += lines[row+i][col-i]

                if (rudiag == key or rudiag == rkey):
                    score += 1
                    
                rddiag = ""
                for i in range(0, 4):
                    if (row + i >= m or col + i >= n):
                        break
                    rddiag += lines[row+i][col+i]

                if (rddiag == key or rddiag == rkey):
                    score += 1
                    
                ludiag = ""
                for i in range(0, 4):
                    if (row - i < 0 or col - i < 0):
                        break
                    ludiag += lines[row-i][col-i]

                if (ludiag == key or ludiag == rkey):
                    score += 1
                    
                lddiag = ""
                for i in range(0, 4):
                    if (row - i < 0 or col +i >= n):
                        break
                    lddiag += lines[row-i][col+i]

                if (lddiag == key or lddiag == rkey):
                    score += 1

    print(f"Part 1: {score}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    grid = list()

    for line in lines:
        grid.append(line.strip())

    part1(grid)

if __name__ == "__main__":
    main()