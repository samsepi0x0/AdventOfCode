file = open('input.txt', 'r')
lines = file.readlines()

variables = dict()
eq = dict()
eq_ind = 0

for index, line in enumerate(lines):
    line = line.strip()
    if (len(line) == 0):
        eq_ind = index + 1
        break
    line = line.split(": ")
    variables[line[0]] = int(line[1])

for index in range(eq_ind, len(lines)):
    left, right = lines[index].strip().split(" -> ")
    var1, op, var2 = left.split(" ")
    eq[right] = (var1, op, var2)

flag = True

while flag:
    flag = False

    for key, val in eq.items():
        if val[0] in variables.keys() and val[2] in variables.keys():
            operand1 = variables[val[0]]
            operand2 = variables[val[2]]

            if (val[1] == 'AND'):
                variables[key] = operand1 & operand2
            elif (val[1] == 'OR'):
                variables[key] = operand1 | operand2
            elif (val[1] == 'XOR'):
                variables[key] = operand1 ^ operand2
        else:
            flag = True

zs = []

for key in variables.keys():
    if key[0] == 'z':
        zs.append(key)

output = ""

for key in sorted(zs)[::-1]:
    output += str(variables[key])

print(f"Part 1 : {int(output, 2)}")