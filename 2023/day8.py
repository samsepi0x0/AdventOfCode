import math

def main():
    file = open("input8.txt", "r")
    lines = file.readlines()

    dirs = lines[0].strip()

    network = dict()
    for line in lines[2:]:
        line = line.strip()
        p1 = line.split(" = ")
        src = p1[0]
        dst = [p1[1][1:4], p1[1][6:9]]
        network[src] = dst

    # Part 1 solution 
    
    current = "AAA"
    index = 0
    steps = 0
    while current != "ZZZ":
        direction = dirs[index % len(dirs)]
        if direction == "L":
            current = network[current][0]
        else:
            current = network[current][1]
        steps += 1
        index += 1
    print("Part 1: ", steps)

    # Part 2 solution

    current = list()
    dsts = list()
    for i in network.keys():
        if i[2] == 'A':
            current.append(i)
        if i[2] == 'Z':
            dsts.append(i)

    # print(current)
    # print(dsts)

    index = 0
    steps = list()

    for curr in current:
        step = 0
        index = 0
        while curr[2] != "Z":
            direction = dirs[index % len(dirs)]
            if direction == "L":
                curr = network[curr][0]
            else:
                curr = network[curr][1]
            step += 1
            index += 1
        steps.append(step)
    print("Part 2: ", LCM(steps))
    
def LCM(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm
        

if __name__ == "__main__":
    main()