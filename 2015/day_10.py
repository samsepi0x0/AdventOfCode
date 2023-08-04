def main():
    part1("1113122113", 40)
    part1("1113122113", 50) # part 2

def part1(s, count):
    while count > 0:

        s = s + "."
        t_count = 1
        new_s = ""
        for i in range(0, len(s)-1):
            if (s[i] == s[i+1]):
                t_count += 1
            else:
                new_s += str(t_count) + str(s[i])
                t_count = 1
        s = new_s
        # print(s)


        # print("\n")
        count -= 1
    print("Solution: ", len(s))


if __name__ == '__main__':
    main()