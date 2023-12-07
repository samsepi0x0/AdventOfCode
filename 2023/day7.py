from tqdm import tqdm

def part1():
    file = open("input7.txt", "r")
    lines = file.readlines()

    hands = [line.strip().split(" ")[0] for line in lines]
    bids = [int(line.strip().split(" ")[1]) for line in lines]
    sorting = []

    # print(hands)
    # print(bids)

    hand_bid_dict = {hands[i] : bids[i] for i in range(len(lines))}
    # print(hand_bid_dict)
    handScoring = dict()


    for i, hand in enumerate(hands):
        handScoring[hand] = get_hand_score(hand)
    
    handSorted = dict(sorted(handScoring.items(), key=lambda item: item[1]))

    # print(handSorted)
    sum = 0


    for i, hand in enumerate(tqdm(handSorted.keys())):
        if len(sorting) == 0:
            sorting.append(hand)
            continue
        
        cScore = handSorted[hand]
        # print(i, sorting)
        for j, phand in enumerate(sorting):
            pScore = handSorted[phand]

            if cScore < pScore:
                sorting.insert(j, hand)
            if cScore == pScore:
                # tie breaking
                tie_score = tie_breaker(hand, phand)
                if tie_score == 0:
                    sorting.insert(j, hand)
                    break
                else:
                    continue
        if hand not in sorting:
            sorting.append(hand)
    # print(sorting)
    for i in range(len(sorting)):
        sum = sum + (i+1) * (hand_bid_dict[sorting[i]])
    
    print("Sum: ", sum)

def part2():
    file = open("input7.txt", "r")
    lines = file.readlines()

    hands = [line.strip().split(" ")[0] for line in lines]
    bids = [int(line.strip().split(" ")[1]) for line in lines]
    sorting = []

    # print(hands)
    # print(bids)

    hand_bid_dict = {hands[i] : bids[i] for i in range(len(lines))}
    # print(hand_bid_dict)
    handScoring = dict()


    for i, hand in enumerate(hands):
        handScoring[hand] = get_hand_score2(hand)
    
    handSorted = dict(sorted(handScoring.items(), key=lambda item: item[1]))

    # print(handSorted)
    sum = 0


    for i, hand in enumerate(tqdm(handSorted.keys())):
        if len(sorting) == 0:
            sorting.append(hand)
            continue
        
        cScore = handSorted[hand]
        # print(i, sorting)
        for j, phand in enumerate(sorting):
            pScore = handSorted[phand]

            if cScore < pScore:
                sorting.insert(j, hand)
            if cScore == pScore:
                # tie breaking
                tie_score = tie_breaker2(hand, phand)
                if tie_score == 0:
                    sorting.insert(j, hand)
                    break
                else:
                    continue
        if hand not in sorting:
            sorting.append(hand)
    # print(sorting)
    for i in range(len(sorting)):
        sum = sum + (i+1) * (hand_bid_dict[sorting[i]])
    
    print("Sum: ", sum)


def tie_breaker2(handA, handB):
    knownChars = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    for i in range(0, 5):
        cA = handA[i]
        cB = handB[i]
        if cA == cB:
            continue
        return 1 if knownChars.index(cA) < knownChars.index(cB) else 0
    return -2
    

def get_hand_score2(hand):
    dict = {}
    for i in hand:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    max_key = max(zip(dict.values(), dict.keys()))[1]
    if max_key == 'J' and (not dict['J'] == 5):
        dict.pop('J')
        max_key = max(zip(dict.values(), dict.keys()))[1]

    if "J" in hand:
        hand_modified = list(hand)
        hand_modified = list(map(lambda x: x.replace('J', max_key), hand_modified))
        return get_hand_score("".join(hand_modified))
    else:
        return get_hand_score(hand)

def tie_breaker(handA, handB):
    knownChars = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    for i in range(0, 5):
        cA = handA[i]
        cB = handB[i]
        if cA == cB:
            continue
        return 1 if knownChars.index(cA) < knownChars.index(cB) else 0
    return -2


def get_hand_score(hand):
    if len(set(hand)) == 1:
        # five of a kind
        return 7
    elif len(set(hand)) == len(hand):
        # high card
        return 1 
    
    dict = {}
    for i in hand:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    scores = dict.values()
    if max(scores) == 4:
        # Four of a kind
        return 6
    if max(scores) == 3 and len(dict.keys()) == 2:
        # full house
        return 5
    if max(scores) == 3:
        # three of a kind
        return 4
    if max(scores) == 2 and len(dict.keys()) == 3:
        # two pair
        return 3
    if max(scores) == 2:
        # one pair
        return 2


if __name__ == "__main__":
    part1()
    part2()