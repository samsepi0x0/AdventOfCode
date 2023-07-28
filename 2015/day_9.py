from itertools import permutations
import sys

def main():
    part1()

def part1():
    cities = set()
    distance = dict()

    file = open("input_test.txt", 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip().split(" ")
        src = line[0]
        dst = line[2]
        value = int(line[4])

        cities.add(src)
        cities.add(dst)

        distance.setdefault(src, dict())[dst] = value
        distance.setdefault(dst, dict())[src] = value

    path_value_shortest = sys.maxsize
    path_value_longest = 0 # for part 2

    for items in permutations(cities):
        dist = sum(map(lambda x, y: distance[x][y], items[:-1], items[1:]))
        print(lambda x, y: distance[x][y], items[:-1], items[1:])
        path_value_shortest = min(path_value_shortest, dist)
        path_value_longest = max(path_value_longest, dist)

    print("Shortest Path: ", path_value_shortest)
    print("Longest Path: ", path_value_longest)

if __name__ == '__main__':
    main()