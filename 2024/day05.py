def part1(mapping, updates):
    score = 0
    
    for update in updates:
        accepted = True
        n = len(update)

        for i in range(1, n):
            num = update[i]
            for j in range(0, i):
                if update[j] in mapping.keys() and num in mapping[update[j]]:
                    accepted = False
                    break
            if not accepted:
                break
        if accepted:
            score += update[n // 2]

    print(f"Part 1 : {score}")

def part2(mapping, updates):
    score = 0
    
    for update in updates:
        accepted = True
        n = len(update)

        for i in range(1, n):
            num = update[i]
            for j in range(0, i):
                if update[j] in mapping.keys() and num in mapping[update[j]]:
                    accepted = False
                    update[i], update[j] = update[j], update[i]

        if not accepted:
            score += update[n // 2]

    print(f"Part 2 : {score}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    mapping = dict()
    seq = 0

    for index, line in enumerate(lines):
        if (line.strip() == ''):
            seq = index
            break
        x, y = line.strip().split('|')
        if int(y) not in mapping.keys():
            mapping[int(y)] = list()
        mapping[int(y)].append(int(x))
    
    updates = []
    for index in range(seq+1, len(lines)):
        updates.append(list(map(int, lines[index].strip().split(","))))

    part1(mapping, updates)
    part2(mapping, updates)

if __name__ == "__main__":
    main()