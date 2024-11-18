def settleNorth(board):
    for row in range(1, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == 'O':
                displaced = False
                for x in range(row-1, -1, -1):
                    if (board[x][col] == '.'):
                        displaced = True
                    if (board[x][col] == '#' or board[x][col] == 'O'):
                        x = x + 1
                        break
                if (displaced):
                    board[x][col] = 'O'
                    board[row][col] = '.'

    return board

def load(board):
    res = 0
    N = len(board)
    for row in range(0, len(board)):
        res = res + (board[row].count('O') * N)
        N -= 1
    
    return res

def part1(board):
    titledboard = settleNorth(board)

    score = load(titledboard)

    print(f"Part 1: {score}")

def main():
    lines = open("input.txt", 'r').readlines()
    
    matrix = []
    for line in lines:
        matrix.append(list(line.strip()))
    
    part1(matrix)

if __name__ == "__main__":
    main()