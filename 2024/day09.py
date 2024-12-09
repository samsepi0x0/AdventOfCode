def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    line = lines[0].strip()

    mem = []

    for i, ch in enumerate(line):
        char = "."
        if i % 2 == 0:
            char = i // 2
        for x in range(int(ch)):
            mem.append(char)

    while (mem.count(".")):
        ind = mem.index(".")
        val = mem.pop()
        mem[ind] = val

        while (mem[-1] == "."):
            mem.pop()
        
    score = 0
    for index, ch in enumerate(mem):
        if (ch != '.'):
            score += (index*int(ch))
    
    print(f"Part 1 : {score}")

    files = dict()
    spaces = dict()

    i, j, id = 0, 0, 0
    while (i < len(line)):
        f, space = i, i + 1

        if (f < len(line)):
            files[id] = (int(line[f]), j)
            j += int(line[f])
        if (space < len(line)):
            if (int(line[space]) > 0):
                spaces[j] = int(line[space])
            j += int(line[space])
        id += 1
        i += 2
        
        
    for key, value in reversed(files.items()):
        size = value[0]
        for pos, space in sorted(spaces.items()):
            if (pos >= value[1]):
                break
            if (space >= size):
                files[key] = (files[key][0], pos)
                if (space - size) > 0:
                    spaces[pos + size] = space - size
                spaces.pop(pos)
                break

    score = 0
    for key, value in files.items():
        n = value[0]
        pos = value[1]
        score += key * (n*pos + n*(n-1) // 2)
    
    print(f"Part 2 : {score}")

main()