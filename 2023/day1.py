def main():
    sum = 0
    with open("input1.txt", "r") as f:
        for line in f:
            nums = parseLine(line)
            number = nums[0] * 10 + nums[-1]
            sum += number
    print(sum)

look = {"one"  : 1, "two"  : 2, "three": 3, "four" : 4, "five" : 5, "six"  : 6, "seven": 7, "eight": 8, "nine" : 9,}

def parseLine(line :str) -> [int]:
    result = []
    for i, char in enumerate(line):
        if char.isnumeric():
            result.append(int(char))
        else:
            for word, value in look.items():
                if line[i:].startswith(word):
                    result.append(value)
                
    return result

if __name__ == "__main__":
    main()
