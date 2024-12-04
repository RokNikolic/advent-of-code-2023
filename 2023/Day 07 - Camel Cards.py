import time


def get_card_value(card, part):
    if card.isnumeric():
        return int(card)
    else:
        if card == "T":
            return 10
        elif card == "J":
            if part == 1:
                return 11
            elif part == 2:
                return 1
        elif card == "Q":
            return 12
        elif card == "K":
            return 13
        elif card == "A":
            return 14


def determine_hand_type(amounts_of_cards):
    if amounts_of_cards[0] == 5:
        return 6
    elif amounts_of_cards[0] == 4:
        return 5
    elif amounts_of_cards[0] == 3 and amounts_of_cards[1] == 2:
        return 4
    elif amounts_of_cards[0] == 3 and amounts_of_cards[1] == 1:
        return 3
    elif amounts_of_cards[0] == 2 and amounts_of_cards[1] == 2:
        return 2
    elif amounts_of_cards[0] == 2 and amounts_of_cards[1] == 1:
        return 1
    else:
        return 0


def get_hand_strength(hand, part):
    hand_dict = {}
    card_ratings = []
    for card in hand:
        card_ratings.append(get_card_value(card, part))
        if card in hand_dict:
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1

    if part == 2 and "J" in hand_dict and hand_dict["J"] != 5:
        amount_of_jokers = hand_dict.pop("J")
        amounts_of_cards = sorted(hand_dict.values(), reverse=True)
        amounts_of_cards[0] += amount_of_jokers
    else:
        amounts_of_cards = sorted(hand_dict.values(), reverse=True)

    hand_strength = determine_hand_type(amounts_of_cards)

    return [hand_strength, card_ratings]


def resolve_same_hands(hand1, hand2):
    for i in range(len(hand1[1])):
        if hand1[1][i] > hand2[1][i]:
            return hand2, hand1
        elif hand1[1][i] < hand2[1][i]:
            return hand1, hand2
    return hand2, hand1


def get_final_hands(hands):
    sorted_hands = sorted(hands)

    old_hand = (-1, [], 0)
    for i in range(len(sorted_hands)):
        if sorted_hands[i][0] == old_hand[0]:
            ordered = resolve_same_hands(old_hand, sorted_hands[i])
            sorted_hands[i] = ordered[1]
            sorted_hands[i - 1] = ordered[0]
        old_hand = sorted_hands[i]

    final_hands = sorted(sorted_hands)
    return final_hands


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append(get_hand_strength(hand, 1) + [int(bid)])

    final_hands = get_final_hands(hands)
    total_sum = 0
    for i, final_hand in enumerate(final_hands):
        total_sum += final_hand[2] * (i + 1)

    return total_sum


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append(get_hand_strength(hand, 2) + [int(bid)])

    final_hands = get_final_hands(hands)
    total_sum = 0
    for i, final_hand in enumerate(final_hands):
        total_sum += final_hand[2] * (i + 1)

    return total_sum


if __name__ == '__main__':
    day = 7
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
