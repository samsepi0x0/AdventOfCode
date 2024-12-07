from tqdm import tqdm
def part1(commands):
    score = 0

    def check(out, inp, ind):
        if (ind == len(inp) - 1):
            return  [inp[ind]]
        
        res = []
        
        for i in check(out, inp, ind+1):
            a = inp[ind]+ " + " + i
            b = inp[ind] + " * " + i
            # c = inp[ind] + i # for part 2
            res.append(a)
            res.append(b)
            # res.append(c) # for part 2

        return res        
        

    for out, inp in tqdm(commands):
        res = check(out, inp, 0)
        possible = False
        for val in res:
            val = val.split()
            
            while (len(val) > 1):
                op1 = val[0]
                oper = val[1]
                op2 = val[2]

                del[val[0]]
                del[val[0]]
                del[val[0]]

                if (oper == "||"):
                    val.insert(0, op1+op2)
                else:
                    val.insert(0, str(eval(op1+oper+op2)))

            if (int(val[0]) == out):
                possible = True
                break
        
        if (possible):
            score += out
    print(f"Part 1: {score}")

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    commands = []

    for line in lines:
        value, blob = line.strip().split(": ")
        values = blob.split(" ")

        commands.append([int(value), values])

    part1(commands)

if __name__ == "__main__":
    main()