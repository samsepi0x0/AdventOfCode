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

def rotate(board):
    return [list(elem) for elem in zip(*board[::-1])]

def part1(board):
    titledboard = settleNorth(board)

    score = load(titledboard)

    print(f"Part 1: {score}")

def part2(board):
    s = "$".join(["-".join(w) for w in board]) # since list are not hashable objects and implementing a tuple now would be too much work
    seen = {s}
    seen_list = [s]

    for cycle in range(1000000000):
        for i in range(0, 4):
            new_board = settleNorth(board)
            board = rotate(new_board)

        s = "$".join(["-".join(w) for w in board])

        if (s in seen):

            break
        
        seen.add(s)
        seen_list.append(s)

    firstIndex = seen_list.index(s)
    x = seen_list[(1000000000 - firstIndex) % (cycle + 1 - firstIndex) + firstIndex]
    board = [a.split('-') for a in x.split('$')]

    score = load(board)
    print(f"Part 2 {cycle + 1}: {score}")

def printf(board):
    for line in board:
        print("".join(line))
    print()

def main():
    lines = open("input.txt.1", 'r').readlines()
    
    matrix = []
    for line in lines:
        matrix.append(list(line.strip()))
    
    part1(matrix)
    part2(matrix)

if __name__ == "__main__":
    main()