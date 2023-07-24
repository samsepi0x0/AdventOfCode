def main():
    file = open("input_7.txt", 'r')
    lines = file.readlines()
    map = dict()
    solved = dict()
    for line in lines:
        line = line.strip()
        asci = ord(line[0])
        temp = line.split(" ")
        if asci >= 48 and asci <= 57 and len(temp) == 3:
            map[temp[-1]] = int(temp[0])
            solved[line[line.rfind(" "):][1:]] = map[line[line.rfind(" "):][1:]]
        else:
            line = line.replace("AND", "&")
            line = line.replace("OR", "|")
            line = line.replace("LSHIFT", "<<")
            line = line.replace("RSHIFT", ">>")
            line = line.replace("NOT", "~")
            map[line[line.rfind(" "):][1:]] = line[0:line.rfind(" ")-3]
    keys = list(map.keys())
    count = 0
    # print(solved)
    # print(map, "\n")
    # print(keys)
    constants = list(solved.keys())
    allsolved = 0
    # Uncomment line below for part B
    # solved['b'] = 46065
    ###############################################################
    outer = 100
    while outer >= 0:
        countdown = 500
        while countdown >= 0:
            if(count == len(map)):
                count = 0
                allsolved = 0
            # print(keys[count], end=' = ')
            if(allsolved == len(map)):
                break
            equ = str(map[keys[count]])
            if equ.isdigit():
                count += 1
                allsolved += 1
            else:
                equation = equ.split(" ")
                for i in equation:
                    if i in solved.keys():
                        equation[equation.index(i)] = str(solved[i])
                # print(" ".join(equation), solved)
                try:
                    solved[keys[count]] = eval(" ".join(equation)) % 65536
                    allsolved += 1
                    count += 1
                except:
                    count += 1
            countdown -= 1
        outer -= 1
    ###############################################################
    
    print("a: ", solved['a'])
    # print(map)


    
    
if __name__ == '__main__':
    main()  