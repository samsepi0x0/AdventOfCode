from tqdm import tqdm
from collections import defaultdict, Counter

file = open("input.txt", "r")
line = file.readline().strip()

all_stones = list(map(int, line.split(" ")))
stones = Counter(all_stones)

for _ in tqdm(range(75)):
    new_stones = defaultdict(int)
    for stone, n in stones.items():
        if (stone == 0):
            new_stones[1] += n 
            continue
        string = str(stone)
        if (len(string) % 2 == 0):
            v = len(string) // 2
            new_stones[int(string[:v])] += n 
            new_stones[int(string[v:])] += n
        else:
            new_stones[stone*2024] += n
    
    stones = new_stones

print(f"Part 1 : {sum(stones.values())}")

