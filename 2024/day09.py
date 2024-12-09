def main():
    file = open("input.txt", "r")
    line = file.readline().strip()

    mem = []
    ind = 0

    for i, ch in enumerate(line):
        char = "."
        if i % 2 == 0:
            char = i // 2
        for x in range(int(ch)):
            mem.append(char)
        
    # print(mem)
    l = 0
    r = len(mem) - 1

    while (mem.count(".")):
        ind = mem.index(".")
        val = mem.pop()
        mem[ind] = val

        while (mem[-1] == "."):
            mem.pop()
        
        # print(mem)

    
    score = 0
    for index, ch in enumerate(mem):
        if (ch != '.'):
            score += (index*int(ch))
    
    print(f"Part 1 : {score}")

main()