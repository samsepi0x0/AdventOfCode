file = open("input.txt", "r")
lines = file.readlines()

adj = dict()

for line in lines:
    line = line.strip().split("-")
    if (line[0] not in adj.keys()):
        adj[line[0]] = []
    if (line[1] not in adj.keys()):
        adj[line[1]] = []
    adj[line[0]].append(line[1])
    adj[line[1]].append(line[0])

threepairs = set()

for node in adj.keys():
    for neighbor1 in adj[node]:
        for neighbor2 in adj[node]:
            if neighbor1 == neighbor2:
                continue
            if neighbor2 in adj[neighbor1]:
                st = sorted([node, neighbor1, neighbor2])
                threepairs.add((st[0], st[1], st[2]))

score = 0
for x, y, z in threepairs:
    if x[0] == 't' or y[0] == 't' or z[0] == 't':
        score += 1

print(f"Part 1 : {score}")