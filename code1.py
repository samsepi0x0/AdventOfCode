def main():
    file = open("input_1.txt", 'r')
    lines = file.readlines()

    calories = []
    temp_calories = 0
    for line in lines:
        if line == '\n':
            calories.append(temp_calories)
            temp_calories = 0
        else:
            temp_calories += int(line.strip())

    print("Total Elves: ", len(calories))
    print("Elf: ", calories.index(max(calories)) + 1, "\tCalories: ", max(calories))

    calories.sort()
    print("Calories by top 3 Elves: ", calories[-1] + calories[-2] + calories[-3])


if __name__ == '__main__':
    main()
