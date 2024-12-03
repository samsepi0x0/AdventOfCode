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

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    part1(lines)

if __name__ == "__main__":
    main()