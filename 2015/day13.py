from itertools import permutations

def main():
    part1()


def part1():
    file = open("input_13.txt", 'r')
    lines = file.readlines()

    people = set()
    scores = dict()

    for line in lines:
        line = line.strip().split(" ")
        personA = line[0]
        personB = line[-1][:-1]
        sign = line[2]
        score = int(line[3])
        if sign == "lose":
            score *= -1
        
        people.add(personA)
        people.add(personB)

        scores.setdefault(personA, dict())[personB] = score

    max_score = solve(scores, people)
    print("Part 1: ", max_score)

    people.add("myself")
    for i in people:
        scores.setdefault("myself", dict())[i] = 0
        scores[i]["myself"] = 0

    # print(scores)
    max_score = solve(scores, people)
    print("Part 2: ", max_score)

def solve(scores, people):
    max_score = 0
    # print(scores)
    for item in permutations(people):
        item = list(item)
        left = -1
        right = 1
        score = 0

        # print(item)
        for i in range(0, len(item)):
            score += (scores[item[i]][item[left]] + scores[item[i]][item[right]])
            # print(item[left], " ", scores[item[i]][item[left]], " <-- ", item[i], " --> ", scores[item[i]][item[right]], " ", item[right], "\t" , (scores[item[i]][item[left]] + scores[item[i]][item[right]]))
            left = left + 1
            right = right + 1
            if right == len(item)-1:
                right = -1            
        # print("\n")

        max_score = max(score, max_score)

    return max_score

if __name__ == "__main__":
    main()