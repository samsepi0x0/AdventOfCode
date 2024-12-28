from copy import deepcopy

file = open('input.txt', 'r')
lines = file.readlines()

instructions = []
for line in lines:
    instructions += list(map(int, line.strip().split(",")))

def intcode(instructions):
    ind = 0

    while ind < len(instructions):
        if instructions[ind] == 1:
            index1, index2, index3 = instructions[ind+1], instructions[ind+2], instructions[ind+3]
            val1, val2 = instructions[index1], instructions[index2]
            instructions[index3] = val1 + val2
        elif instructions[ind] == 2:
            index1, index2, index3 = instructions[ind+1], instructions[ind+2], instructions[ind+3]
            val1, val2 = instructions[index1], instructions[index2]
            instructions[index3] = val1 * val2
        if instructions[ind] == 99:
            break
        ind += 4
    
    return instructions

instructions_copy = deepcopy(instructions)
instructions[1], instructions[2] = 12, 2
print(f"Part 1 : {intcode(deepcopy(instructions))[0]}")

for noun in range(0, 100):
    for verb in range(0, 100):
        instructions_copy = deepcopy(instructions)
        instructions_copy[1], instructions_copy[2] = noun, verb
        value = intcode(instructions_copy)[0]
        if (value == 19690720):
            print(f"Part 2 : {100*noun + verb}")
            break
    else:
        continue
    break
