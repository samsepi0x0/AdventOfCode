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

def part2():
    file = open('input.txt.1', 'r')
    lines = file.readlines()

    paths = dict()

    for line in lines:
        line = line.strip()
        if (len(line) == 0):
            break
        name, val = line[:-1].split("{")
        vals = val.split(",")
        paths[name] = ([], vals.pop())
        for value in vals:
            comp, dst = value.split(":")
            key = comp[0]
            cmp = comp[1]
            n = int(comp[2:])
            paths[name][0].append((key, cmp, n, dst))
    
    def count(ranges, path = "in"):
        if path == 'R':
            return 0
        if path == 'A':
            prod = 1
            for i, j in ranges.values():
                prod *= (j - i + 1)
            return prod
        
        total = 0

        flow, default = paths[path]

        for key, cmp, n, dst in flow:
            lo, hi = ranges[key]
            if cmp == '<':
                true = (lo, n-1)
                false = (n, hi)
            else:
                true = (n+1, hi)
                false = (lo, n)
            if true[0] <= true[1]:
                cp = dict(ranges)
                cp[key] = true
                total += count(cp, dst)
            if false[0] <= false[1]:
                ranges = dict(ranges)
                ranges[key] = false
            else:
                break
        else:
            total += count(ranges, default)
        
        return total    


    score = count({key: (1, 4000) for key in "xmas"})
    print(score)

def main():
    file = open('input.txt', 'r')
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
    part2()

if __name__ == "__main__":
    main()