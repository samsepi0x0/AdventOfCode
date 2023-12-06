def part1():
    file = open("input6.txt", "r")
    lines = file.readlines()
    times = []
    sum = 1
    for i in (lines[0].strip().split(": ")[1].split(" ")):
        if not i == '':
            times.append(int(i))
    distances = []
    for i in (lines[1].strip().split(": ")[1].split(" ")):
        if not i == '':
            distances.append(int(i))

    for i in range(0, len(times)):
        start = 1
        end = times[i]
        max_dist = distances[i]

        for j in range(1, times[i]):
            dist = j * (end-j)
            if dist > max_dist:
                start = j
                break
        
        for j in range(times[i] - 1, 1, -1):
            dist = j * (end - j)
            if dist > max_dist:
                end = j
                break

        count = end - start + 1
        sum *= count
    print("Sum: ", sum)

def part2():
    file = open("input6.txt", "r")
    lines = file.readlines()
    times = [""]
    sum = 1
    for i in (lines[0].strip().split(": ")[1].split(" ")):
        if not i == '':
            times[0] += i
    times[0] = int(times[0])
    distances = [""]
    for i in (lines[1].strip().split(": ")[1].split(" ")):
        if not i == '':
            distances[0] += i
    distances[0] = int(distances[0])
    for i in range(0, len(times)):
        start = 1
        end = times[i]
        max_dist = distances[i]

        for j in range(1, times[i]):
            dist = j * (end-j)
            if dist > max_dist:
                start = j
                break
        
        for j in range(times[i] - 1, 1, -1):
            dist = j * (end - j)
            if dist > max_dist:
                end = j
                break

        count = end - start + 1
        sum *= count
    print("Sum: ", sum)

if __name__ == "__main__":
    part1()
    part2()