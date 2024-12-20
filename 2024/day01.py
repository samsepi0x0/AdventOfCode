from collections import Counter

def part1(left, right):
    left.sort()
    right.sort()
    
    score = 0
    
    for x, y in zip(left, right):
        score += abs(x-y)

    print(f"Score: {score}")

def part2(left, right):
    d = Counter(right)
    score = 0

    for n in left:
        if n in d.keys():
            score += n*d[n]
    
    print(f"Part 2: {score}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    left, right = list(), list()

    for line in lines:
        x, y = line.strip().split("   ")
        left.append(int(x))
        right.append(int(y))

    part1(left, right)
    part2(left, right)
    
main()