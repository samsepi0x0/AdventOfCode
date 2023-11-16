def part1():
    file = open("input_14.txt", 'r')
    lines = file.readlines()
    reindeers = list()
    distance_covered = list()
    total_time = 2503

    for line in lines:
        line = line.strip().split(" ")
        reindeers.append(line[0])
        speed = int(line[3])
        flytime = int(line[6])
        resttime = int(line[-2])

        # print(line[0], "\t", speed, "\t", flytime, "\t", resttime)

        timer = 1
        distance = 0
        isFlying = True
        st = 1
        while(timer != total_time):
            if isFlying:
                distance += speed
                if st < flytime:
                    st += 1
                else:
                    isFlying = False
            else:
                for i in range(1, resttime):
                    timer += 1
                    if timer == total_time:
                        break
                st = 1
                isFlying = True
            if timer == total_time:
                break
            timer += 1
        distance_covered.append(distance)

    print("Part 1: ", max(distance_covered))

def part2():
    file = open("input_14.txt", 'r')
    lines = file.readlines()
    reindeers = list()
    speeds = list()
    fly_times = list()
    rest_times = list()

    total_time = 2503

    for line in lines:
        line = line.strip().split(" ")
        reindeers.append(line[0])
        speed = int(line[3])
        flytime = int(line[6])
        resttime = int(line[-2])

        speeds.append(speed)
        fly_times.append(flytime)
        rest_times.append(resttime)

    st = [0 for i in range(len(reindeers))]
    mint = [0 for i in range(len(reindeers))]

    sec = 0
    while (sec < total_time):
        for i in range(len(reindeers)):
            if (sec % (fly_times[i] + rest_times[i]) < fly_times[i]):
                st[i] += speeds[i]
        for i in range(len(reindeers)):
            max1 = max(st)
            if (st[i] == max1):
                mint[i] += 1
        sec += 1
    
    print("Part 2: ", max(mint))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()