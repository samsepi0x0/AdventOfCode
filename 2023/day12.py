from functools import cache

def part1(lines):

    def f(seq, grp):
        if not grp:
            return '#' not in seq 
        slen = len(seq)
        glen = grp[0]

        if slen - sum(grp) - len(grp) + 1 < 0:
            return 0
        holes = any(seq[x] == '.' for x in range(glen))
        if (slen == glen):
            return 0 if holes else 1 
        use = not holes and (seq[glen] != '#')
        if (seq[0] == '#'):
            return f(seq[glen+1:].lstrip('.'), tuple(grp[1:])) if use else 0
        skip = f(seq[1:].lstrip('.'), grp)
        if not use:
            return skip
        return skip + f(seq[glen+1:].lstrip('.'), tuple(grp[1:]))

    score = 0
    for line in lines:
        seq, grp = line.split(' ')
        grp = [int(g) for g in grp.split(',')]
        score += f(seq, tuple(grp))
    
    print(f"Score: {score}")

def part2(lines):
    
    @cache
    def f(seq, grp):
        if not grp:
            return '#' not in seq 
        slen = len(seq)
        glen = grp[0]

        if slen - sum(grp) - len(grp) + 1 < 0:
            return 0
        holes = any(seq[x] == '.' for x in range(glen))
        if (slen == glen):
            return 0 if holes else 1 
        use = not holes and (seq[glen] != '#')
        if (seq[0] == '#'):
            return f(seq[glen+1:].lstrip('.'), tuple(grp[1:])) if use else 0
        skip = f(seq[1:].lstrip('.'), grp)
        if not use:
            return skip
        return skip + f(seq[glen+1:].lstrip('.'), tuple(grp[1:]))

    score = 0
    for line in lines:
        seq, grp = line.split(' ')
        seq = '?'.join([seq]*5).lstrip('.')
        grp = [int(g) for g in grp.split(',')] * 5
        score += f(seq, tuple(grp))
    
    print(f"Score: {score}")



def main():
    file = open('input.txt', 'r').readlines()
    lines = [line.strip() for line in file]
    part2(lines)

main()
