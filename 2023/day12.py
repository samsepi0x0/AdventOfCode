def part1(lines):
    score = 0
    for line in lines:
        pattern = list(line.split(' ')[0])
        values = "-".join(list(line.split(' ')[1].split(',')))
        print(values, pattern)
        a = 0    
        def f(pattern, ind):
            global a
            if (ind >= len(pattern)):
                p = "".join(pattern)
                p += "."
                count = 0
                string = ""
                for i in p:
                    if i == '#':
                        count += 1 
                    else:
                        if (count != 0):
                            string = string + str(count) + "-"
                        count = 0
                #print(p, string)
                if (string[:-1] == values):
                    return 1
                return 0
            x = 0
            if (pattern[ind] == '?'):
                pattern[ind] = '.'
                x = x + f(pattern, ind+1)
                pattern[ind] = '#'
                x = x + f(pattern, ind+1)
                pattern[ind] = '?'
            else:
                x = x + f(pattern, ind+1)
            return x
        score += f(pattern, 0)

    print(f"Score: {score}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    part1(lines)

main()
