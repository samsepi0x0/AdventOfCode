def main():
    file = open("input_5.txt", 'r')
    lines = file.readlines()

    stacks = [[], [], [], [], [], [], [], [], []]
    

    index = 0
    for line in lines:
        if index < 9:
            stacks[index] = lines[index].strip().split(' ')
            index += 1
        else:
            line = line.strip()
            temp_line = line.split(' ')
            crates = int(temp_line[temp_line.index('move')+1])
            from_ = int(temp_line[temp_line.index('from')+1])
            to = int(temp_line[temp_line.index('to')+1])
            #for i in range(crates):
            #    crate = stacks[from_ - 1].pop()
            #    stacks[to-1].append(crate)
            temp_stack = []
            for i in range(crates):
                crate = stacks[from_ - 1].pop()
                temp_stack.append(crate)
            stacks[to-1] = stacks[to-1] + temp_stack[::-1]
    for i in stacks:
        print(i[-1], end='')
    print()



if __name__ == '__main__':
    main()