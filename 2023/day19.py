from collections import OrderedDict

def part1(paths, values):
    accepted = list()

    for value in values:
        src = 'in'
        while (True):
            if (src == 'R'):
                break
            if (src == 'A'):
                accepted.append(value)
                break
            path = paths[src]
            def_dst = path["default"]
            src = def_dst
            for val in path.keys():
                if (val == "default"):
                    continue
                ch = val[0]
                symbol, score, dst = path[val] 
                if (symbol == '<'):
                    if (value[ch] < score):
                        src = dst
                        break
                if (symbol == '>'):
                    if (value[ch] > score):
                        src = dst
                        break
    
    score = 0
    for vals in accepted:
        score += sum(vals.values())

    print(f"Part 1: {score}")

def main():
    file = open('input.txt.1', 'r')
    lines = file.readlines()

    paths = OrderedDict()
    st = 0
    for index, line in enumerate(lines):
        line = line.strip()

        if (len(line) == 0):
            st = index + 1
            break
        
        label, values = line[:-1].split("{")
        path = OrderedDict()
        i = 0
        for x in values.split(","):
            if '<' in x:
                letter = x[0]
                comp, dest = x[2:].split(":")
                path[letter + str(i)] = ('<', int(comp), dest)
            if '>' in x:
                letter = x[0]
                comp, dest = x[2:].split(":")
                path[letter + str(i)] = ('>', int(comp), dest)
            else:
                path["default"] = x
            i += 1
        paths[label] = path
    

    values = list()
    for i in range(st, len(lines)):
        value = dict()
        line = lines[i].strip()[1:-1].split(",")

        for part in line:
            x = part.split('=')
            value[x[0]] = int(x[1])
        values.append(value)

    part1(paths, values)

if __name__ == "__main__":
    main()