def part1():
    file = open("input_8.txt", 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        line = line.strip()
        count += (len(line) - len(eval(line)))
    print("Part 1: ", count)

def part2():
    """
        To find difference b/w length of string and length of string if characters are encoded, thus, total number of encoded characters + 2 for the double quotes at the start of the string.
    """
    file = open("input_8.txt", 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        line = line.strip()
        count += (2 + line.count('\\') + line.count('"'))
    print("Part 2: ", count)


def main():
    part1()
    part2()

if __name__ == '__main__':
    main()