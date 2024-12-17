from z3 import *

file = open('input.txt', "r")
lines = file.readlines()

A = int(lines[0].split(": ")[1])
B = int(lines[1].split(": ")[1])
C = int(lines[2].split(": ")[1])

instructions = list(map(int, lines[4].split(": ")[1].split(",")))

def solve(A, B, C):
    ip = 0
    output = ""

    while (ip < len(instructions)):
        combo = {0: 0, 1: 1, 2:2, 3:3, 4:A, 5:B, 6:C, 7:None}
        instruction = instructions[ip]
        jmp = False

        if instruction == 0:
            numerator = A
            denominator = combo[instructions[ip + 1]]
            A = numerator // (2 ** denominator)
        elif instruction == 1:
            op1 = B
            op2 = instructions[ip + 1]
            B = op1 ^ op2
        elif instruction == 2:
            op1 = combo[instructions[ip + 1]]
            B = op1 % 8
        elif instruction == 3:
            if (A != 0):
                ip = instructions[ip + 1]
                jmp = True
        elif instruction == 4:
            op1 = B
            op2 = C 
            B = op1 ^ op2
        elif instruction == 5:
            op = combo[instructions[ip+1]]
            output += str(op % 8) + ","
        elif instruction == 6:
            numerator = A
            denominator = combo[instructions[ip + 1]]
            B = numerator // (2 ** denominator)
        elif instruction == 7:
            numerator = A
            denominator = combo[instructions[ip + 1]]
            C = numerator // (2 ** denominator)

        if (not jmp):
            ip += 2
    return output[:-1]

print(f"Part 1 : {solve(A, B, C)}")

target = instructions[::-1]
def find_a(a = 0, ind = 0):
    if ind == len(target):
        return a 
    for i in range(8):
        output = solve((a*8 + i), B, C)
        if output and output[0] == str(target[ind]):
            if (res := find_a((a*8+i), ind+1)):
                return res
    return 0
    
val = find_a()
print(f"Part 2: {val}")