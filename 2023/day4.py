from tqdm import tqdm

def part1():
    file = open("input4.txt", "r")
    lines = file.readlines()
    sum = 0
    for line in lines:
        score = 0
        line = line.strip()
        line = line.split(": ")
        vals = line[1].split(" | ")
        winning = vals[0].split(" ")
        current = vals[1].split(" ")

        wins = [int(i) if i != '' else -1 for i in winning]
        curs = [int(i) if i != '' else -2 for i in current]

        for i in wins:
            if i in curs:
                if score == 0:
                    score = 1
                else: 
                    score *= 2
        print()
        sum += score
    
    print("Sum: ", sum)

def part2():
    file = open("input4.txt", "r")
    lines = file.readlines()
    card_count = dict()
    
    for i in range(1, len(lines) + 1):
        card_count[i] = 1
    
    index = 0
    for line in tqdm(lines):
        index += 1
        line = line.strip()
        for _ in range(0, card_count[index]):
            score = 0
            nums = line.split(": ")
            vals = nums[1].split(" | ")
            winning = vals[0].split(" ")
            current = vals[1].split(" ")

            wins = [int(i) if i != '' else -1 for i in winning]
            curs = [int(i) if i != '' else -2 for i in current]

            for i in wins:
                if i in curs:
                    score += 1
            for j in range(index+1, index + score+1):
                card_count[j] += 1
        
    print("Sum: ", sum(card_count.values()))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
