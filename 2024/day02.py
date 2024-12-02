def part1(lists):
    safe = 0

    for seq in lists:
        ascending = all((seq[i] < seq[i+1] and seq[i+1]-seq[i] >= 1 and seq[i+1]-seq[i] <= 3) for i in range(len(seq) - 1))
        
        if (ascending):
            safe += 1
        else:
            descending = all((seq[i] > seq[i+1] and seq[i]-seq[i+1] >= 1 and seq[i]-seq[i+1] <= 3) for i in range(len(seq) - 1))
            if (descending):
                safe += 1
        
    print(f"Part 1 : {safe}")

def part2(lists):
    safe = 0
    
    for seq in lists:
        good = False
        for j in range(len(seq)):
            s = seq[:j] + seq[j+1:]
            ascending = all((s[i] < s[i+1] and s[i+1]-s[i] >= 1 and s[i+1]-s[i] <= 3) for i in range(len(s) - 1))
            descending = all((s[i] > s[i+1] and s[i]-s[i+1] >= 1 and s[i]-s[i+1] <= 3) for i in range(len(s) - 1))
            if (ascending or descending):
                good = True
        if (good):
            safe += 1
            
    print(f"Part 2 : {safe}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    lists = list()

    for line in lines:
        x = line.strip().split(" ")
        lists.append(list(map(int, x)))

    part1(lists)
    part2(lists)
    
main()