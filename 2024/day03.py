import re

def part1(lines):
    score = 0

    for line in lines:
        line = line.strip()
        matches = re.findall(r'mul\([0-9]+,[0-9]+\)', line)
        for match in matches:
            op, blob = match.split("(")
            x, y = list(map(int, blob[:-1].split(",")))
            score = score + (x*y)
    
    print(f"Part 1 : {score}")

def part2(lines):
    score = 0
    enable = True
    for line in lines:
        line = line.strip()
        matches = re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', line)

        for match in matches:
            if match == "do()":
                enable = True
            elif match == "don\'t()":
                enable = False
            
            if (enable) and match[0] == 'm':
                op, blob = match.split("(")
                x, y = list(map(int, blob[:-1].split(",")))
                score = score + (x*y)

    print(f"Part 2 : {score}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()