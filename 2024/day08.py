def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    umap = dict()

    for r, line in enumerate(lines):
        line = line.strip()
        for c, ch in enumerate(line):
            if (ch != '.'):
                if ch not in umap.keys():
                    umap[ch] = list()
                umap[ch].append((r, c))

    vis = set()
    m = len(lines)
    n = len(lines[0].strip())

    for node in umap.keys():
        for x1, y1 in umap[node]:
            for x2, y2 in umap[node]:
                if (x1 == x2 and y1 == y2):
                    continue
                
                a1 = 2*x1 - x2
                b1 = 2*y1 - y2

                a2 = 2*x2 - x1
                b2 = 2*y2 - y1
                
                if (0 <= a1 < m and 0 <= b1 < n):
                    vis.add((a1, b1))
                if (0 <= a2 < m and 0 <= b2 < n):
                    vis.add((a2, b2))
    
    print(f"Part 1 : {len(vis)}")

    vis = set()
    
    for node in umap.keys():
        for x1, y1 in umap[node]:
            for x2, y2 in umap[node]:
                if (x1 == x2 and y1 == y2):
                    continue
                
                dx = x2 - x1
                dy = y2 - y1
                x, y = x1, y1
                while (0 <= x < m and 0 <= y < n):
                    vis.add((x, y))
                    x += dx
                    y += dy

    print(f"Part 2 : {len(vis)}")

main()