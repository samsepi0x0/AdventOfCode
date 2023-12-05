import tqdm

def part1():
    file = open("input5.txt", 'r')
    lines = file.readlines()

    seeds = [int(i) for i in (lines[0].strip().split(": ")[1].split(" "))]

    print("Seeds: ", seeds)
    i = 3

    swapped = [False for _ in range(len(seeds))]

    while (i < len(lines)):
        if lines[i] == "\n":
            print("Seeds: ", seeds)
            swapped = [False for _ in range(len(seeds))]
            i += 2
            continue
        # print(lines[i])

        line = lines[i].strip().split(" ")
        src = int(line[1])
        dst = int(line[0])
        step = int(line[2])

        src_spread = src + step
        dst_spread = dst + step

        for index in range(len(seeds)):
            if not swapped[index]:
                if seeds[index] >= src and seeds[index] <= src_spread:
                    tmp = seeds[index] - src
                    seeds[index] = dst + tmp
                    swapped[index] += 1
            else:
                continue
        i += 1


    print("Score: ", min(seeds))

def part2():
    input = open("input5.txt").read().strip()
    seeds, *blocks = input.split('\n\n')
    seeds = list(map(int, seeds.split(': ')[1].split()))

    seeds_ranges = []
    for i in range(0, len(seeds), 2):
        seeds_ranges.append((seeds[i], seeds[i] + seeds[i+1]))

    for block in blocks:
        mapping_ranges = []
        for line in block.split('\n')[1:]:
            mapping_ranges.append(list(map(int, line.split())))

        mapped_seed_ranges = []

        while seeds_ranges:
            seed_start, seed_end = seeds_ranges.pop()
            range_mapped = False

            for dst, src, sz in mapping_ranges:

                ovlp_start = max(seed_start, src)
                ovlp_end = min(seed_end, src+sz)

                if ovlp_start < ovlp_end:
                    mapped_seed_ranges.append((ovlp_start - src + dst, ovlp_end - src + dst))

                    if seed_start < ovlp_start:
                        seeds_ranges.append((seed_start, ovlp_start))
                    if ovlp_end < seed_end:
                        seeds_ranges.append((ovlp_end, seed_end))
                    range_mapped = True
                    break

            if not range_mapped:
                mapped_seed_ranges.append((seed_start, seed_end))

        seeds_ranges = mapped_seed_ranges

    print(min(seeds_ranges)[0])

def main():
    part2()


if __name__ == "__main__":
    main()