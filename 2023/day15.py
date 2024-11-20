def dhash(word):
    score = 0
    for index, ch in enumerate(word):
        val = ord(ch)
        score = score + val
        score = score * 17
        score = score % 256
    return score

def part1(line):
    score = 0
    for word in line:
        score += dhash(word)
    print(f"Part 1: {score}")

def part2(line):
    boxes = [{} for _ in range(256)]

    for word in line:
        if ('=' in word):
            values = word.split("=")
            label, val = values[0], values[1]
            ind = dhash(label)
            box = boxes[ind]
            box[label] = int(val)
        else:
            label = word.split('-')[0]
            ind = dhash(label)
            box = boxes[ind]
            box.pop(label, None)
    
    score = 0
    for id, box in enumerate(boxes):
        for index, lens in enumerate(box):
            score += (id + 1) * (index + 1) * box[lens]

    print(f"Part 2: {score}")

def main():
    file = open("input.txt", 'r')
    line = file.readlines()[0].strip().split(',')
    
    part1(line)
    part2(line)

if __name__ == "__main__":
    main()
