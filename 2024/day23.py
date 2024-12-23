file = open("input.txt", "r")
lines = file.readlines()

adj = dict()

for line in lines:
    line = line.strip().split("-")
    if (line[0] not in adj.keys()):
        adj[line[0]] = set()
    if (line[1] not in adj.keys()):
        adj[line[1]] = set()
    adj[line[0]].add(line[1])
    adj[line[1]].add(line[0])

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

sets = set()

def search(node, req):
    key = tuple(sorted(req))
    if key in sets:
        return
    sets.add(key)
    for neighbor in adj[node]:
        if neighbor in req:
            continue
        if not all(neighbor in adj[query] for query in req):
            continue
        copy = set(req)
        copy.add(neighbor)
        search(neighbor, copy)

for node in adj.keys():
    search(node, {node})

password = max(sets, key=len)

print(f"Part 2 : ", ",".join(sorted(list(password))))