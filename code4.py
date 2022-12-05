def main():
    file = open('input_4.txt', 'r')
    lines = file.readlines()
    subsets = 0
    overlap = 0
    for line in lines:
        line = line.strip()
        elf1 = line.split(',')[0]
        elf2 = line.split(',')[1]

        elf1_start = int(elf1.split('-')[0])
        elf1_end = int(elf1.split('-')[1])

        elf2_start = int(elf2.split('-')[0])
        elf2_end = int(elf2.split('-')[1])

        elf1_subset = set([i for i in range(elf1_start, elf1_end+1)])
        elf2_subset = set([i for i in range(elf2_start, elf2_end+1)])

        if elf1_subset.issubset(elf2_subset) or elf2_subset.issubset(elf1_subset):
            subsets += 1

        for i in elf1_subset:
            if i in elf2_subset:
                overlap += 1
                break

    print("Score: ", subsets)
    print("New Score: ", overlap)

if __name__ == '__main__':
    main()