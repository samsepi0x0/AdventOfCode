def main():
    clock = 0
    x = 1
    beam = 0
    processing = False
    line = 0
    score = 0

    file = open('input_10.txt', 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip().split(" ")
        if line[0] == "noop":
            clock += 1
            if clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220:
                score += clock * x
        else:
            value = int(line[1])
            clock += 1

            if clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220:
                score += clock * x
            clock += 1
            if clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220:
                score += clock * x
            x += value

    print("Score: ", score)
    print("Pattern: ")
    part_2()

def part_2():
    file = open("input_10.txt", 'r')
    data = file.read()

    data_list = data.split("\n")

    x = 1
    cycles = 0
    totals = 0
    beam = 0
    process = False
    line = 0
    for i in range(240):
        if beam > 39:
            beam = 0
            print("")
        if beam <= x+1 and beam >= x-1:
            print("#", end='')
        else:
            print(" ", end='')
        if process == False:
            if data_list[line] == 'noop':
                cycles += 1
                beam += 1
                line += 1
            else:
                process = True
                cycles += 1
                beam += 1
        elif process == True:
            cycles += 1
            beam += 1
            x += int(data_list[line][4:])
            line += 1
            process = False

    print()


if __name__ == '__main__':
    main()