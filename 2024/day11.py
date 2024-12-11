from tqdm import tqdm

file = open("input.txt", "r")
line = file.readline().strip()

stones = list(map(int, line.split(" ")))


for blink in tqdm(range(25)):
    new_stone = list()
    for ind, stone in enumerate(stones):
        if (stone == 0):
            new_stone.append(1)
            continue
        string = str(stone)
        if (len(string) % 2 == 0):
            v = len(string) // 2
            new_stone.append(int(string[0:v]))
            new_stone.append(int(string[v:]))
        else:
            new_stone.append(stone * 2024)
    

    stones = new_stone
print(f"Part 1 : {len(stones)}")