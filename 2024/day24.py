from copy import deepcopy
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

def solve(variables, eq):
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

    return output

file = open("input.txt", 'r')

index = 0
for i, line in enumerate(lines):
    line = line.strip()
    if (len(line) == 0):
        index = i
        break

formula = {}

for i in range(index+1, len(lines)):
    x, op, y, z = lines[i].strip().replace(" -> ", " ").split()
    formula[z] = (op, x, y)

def make_wire(char, num):
    return char + str(num).rjust(2, "0")

def v(wire, depth = 0):
    if wire not in formula.keys():
        return "  "*depth + wire
    op, x, y = formula[wire]
    return "  "*depth + op + " (" + wire + ")\n" + v(x, depth+1) + "\n" + v(y, depth+1)

def verify(wire, num):
    # print("verify", wire, num)
    if wire not in formula:
        return False
    op, x, y = formula[wire]
    if op != 'XOR':
        return False
    if num == 0:
        return sorted([x, y]) == ["x00", "y00"]
    return verify_imm(x, num) and verify_carry(y, num) or verify_imm(y, num) and verify_carry(x, num)

def verify_imm(wire, num):
    # print("verify_xor", wire, num)
    if wire not in formula:
        return False
    op, x, y = formula[wire]
    if op != "XOR":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry(wire, num):
    # print("verify_carry", wire, num)
    if wire not in formula:
        return False
    op, x, y = formula[wire]
    if num == 1:
        if op != "AND":
            return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR":
        return False
    return verify_direct(x, num-1) and verify_recarry(y, num-1) or verify_direct(y, num-1) and verify_recarry(x, num-1)

def verify_direct(wire, num):
    # print("verify_direct", wire, num)
    if wire not in formula:
        return False
    op, x, y = formula[wire]
    if op != "AND":
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    # print("verify_recarry", wire, num)
    if wire not in formula:
        return False
    op, x, y = formula[wire]
    if op != "AND":
        return False
    return verify_imm(x, num) and verify_carry(y, num) or verify_imm(y, num) and verify_carry(x, num)

def ver(num):
    return verify(make_wire("z", num), num)

def progress():
    i = 0

    while(True):
        if not ver(i):
            break
        i += 1
    return i

swaps = []
for _ in range(4):
    baseline = progress()
    for x in formula:
        for y in formula:
            if x == y:
                continue
            formula[x], formula[y] = formula[y], formula[x]
            if (progress() > baseline):
                break
            formula[x], formula[y] = formula[y], formula[x]
        else:
            continue
        break
    swaps += [x, y]

print(",".join(sorted(swaps)))