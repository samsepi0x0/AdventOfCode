def main():
    file = open('input_3.txt', 'r')
    lines = file.readlines()
    score = 0
    scheme = dict()
    for i in range(0, 26):
        scheme[chr(65+i)] = 27 + i
        scheme[chr(97+i)] = i + 1
    for line in lines:
        line = line.strip()
        first = line[:len(line)//2]
        second = line[len(line)//2:]
        for i in first:
            if i in second:
                score += scheme[i]
                break
    print("Score: ", score)

    score = 0
    for index in range(0, len(lines), 3):
        sack0 = lines[index].strip()
        sack1 = lines[index + 1].strip()
        sack2 = lines[index + 2].strip()

        for i in sack0:
            if i in sack1 and i in sack2:
                score += scheme[i]
                break

    print("New_score: ", score)

if __name__ == '__main__':
    main()