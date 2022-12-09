def main():
    file = open('input_8.txt', 'r')
    lines = file.readlines()
    matrix = list()

    for line in lines:
        temp_line = list()
        line = line.strip()
        for i in line:
            temp_line.append(i)
        matrix.append(temp_line)

    visible_trees = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or i == len(matrix)-1:
                visible_trees += 1
            elif j == 0 or j == len(matrix)-1:
                visible_trees += 1
            else:
                # not a boundary tree
                # check from right:
                right = list()
                for k in range(0,j):
                    right.append(matrix[i][k])
                left = list()
                for k in range(j+1, len(matrix)):
                    left.append(matrix[i][k])
                
                #print(right, matrix[i][j], left)

                top = list()
                for k in range(i):
                    top.append(matrix[k][j])
                bottom = list()
                for k in range(i+1, len(matrix)):
                    bottom.append(matrix[k][j])
                
                #print(top, matrix[i][j], bottom)
                is_visible = visibility(right, matrix[i][j]) or visibility(left, matrix[i][j]) or visibility(bottom, matrix[i][j]) or visibility(top, matrix[i][j]) 

                if is_visible:
                    visible_trees += 1
    
    print("Score: ", visible_trees)
    print("New Score: ", second())

def second():
    lines = open("input_8.txt", 'r').readlines()
    lines = [line.rstrip() for line in lines]
    scores = [list(_scan_score(line)) for line in lines]
    for line, row in zip(lines, scores):
        for col_index, value in enumerate(_scan_score(line[::-1])):
            row[-1 - col_index] *= value
    for col_index, line in enumerate(zip(*lines)):
        line = "".join(line)
        for row_index, value in enumerate(_scan_score(line)):
            scores[row_index][col_index] *= value
        for row_index, value in enumerate(_scan_score(line[::-1])):
            scores[-1 - row_index][col_index] *= value
    return max(max(row) for row in scores)

def _scan_score(line):
    horizon = 0
    for index, height in enumerate(line):
        for horizon in range(index - 1, -1, -1):
            if line[horizon] >= height:
                break
        yield index - horizon
        
def visibility(neighbors, tree):
    for i in neighbors:
        if tree <= i:
            return False
    #print("Visible: ", tree)
    return True

if __name__ == '__main__':
    main()