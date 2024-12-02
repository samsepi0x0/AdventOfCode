def part1(lists):
    safe = 0

    for seq in lists:
        ascending = True
        prev = seq[0]
        for i in range(1, len(seq)):
            if (prev < seq[i] and seq[i]-prev >= 1 and seq[i]-prev <= 3):
                ascending = True
                prev = seq[i]
            else:
                ascending = False
                break
        
        if (ascending):
            safe += 1
        else:
            descending =  True
            prev = seq[0]
            for i in range(1, len(seq)):
                if (prev > seq[i] and prev - seq[i] >= 1 and prev - seq[i] <= 3):
                    prev = seq[i]
                else:
                    descending = False
                    break
            if (descending):
                safe += 1
    
    print(f"Part 1 : {safe}")


def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    lists = list()

    for line in lines:
        x = line.strip().split(" ")
        lists.append(list(map(int, x)))

    part1(lists)
    
main()