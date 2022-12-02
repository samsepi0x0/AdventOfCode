def chall_1():
    file = open('input_2.txt', 'r')
    lines = file.readlines()
    #'A': 'rock', 'B':'paper', 'C':'scissor'
    scheme2 = {'X': 1, 'Y': 2, 'Z':3}
    score = 0
    for line in lines:
        p1 = line[0]
        p2 = line.strip()[-1]
        
        if p1 == 'A':
            if p2 == 'X':
                # rock rock -> draw: 
                score += 3
            elif p2 == 'Y':
                # rock paper -> win:
                score += 6
            else:
                # rock scissor -> lose:
                score += 0
        if p1 == 'B':
            if p2 == 'X':
                # paper rock -> lose: 
                score += 0
            elif p2 == 'Y':
                # paper paper -> draw:
                score += 3
            else:
                # paper scissor -> win:
                score += 6
        if p1 == 'C':
            if p2 == 'X':
                # scissor rock -> win: 
                score += 6
            elif p2 == 'Y':
                # scissor paper -> lose:
                score += 0
            else:
                # scissor scissor -> draw:
                score += 3
        score += scheme2[p2]
    
    print("Score: ", score)

def chall_2():
    file = open("input_2.txt", 'r')
    lines = file.readlines()
    score = 0
    scheme_game = {'X': 0, 'Y': 3, 'Z': 6}

    for line in lines:
        p1 = line[0]
        state = line.strip()[-1]
        if p1 == 'A':
            if state == 'X':
                # rock and lose -> scissor
                score += 3
            if state == 'Y':
                # rock and draw -> rock
                score += 1
            if state == 'Z':
                # rock and win -> paper
                score += 2
        if p1 == 'B':
            if state == 'X':
                # paper and lose -> rock
                score += 1
            if state == 'Y':
                # paper and draw -> paper
                score += 2
            if state == 'Z':
                # paper and win -> scissor
                score += 3
        if p1 == 'C':
            if state == 'X':
                # scissor and lose -> paper
                score += 2
            if state == 'Y':
                # scissor and draw -> scissor
                score += 3
            if state == 'Z':
                # scissor and win -> rock
                score += 1
        score += scheme_game[state]
    
    print("New_Score: ", score)

if __name__ == '__main__':
    chall_1()
    chall_2()