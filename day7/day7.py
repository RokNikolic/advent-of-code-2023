import time

with open('input.txt', 'r') as f:
    puzzle_input = f.read()
    puzzle_lines = puzzle_input.split("\n")


def get_card_value(card):
    if card.isnumeric():
        return int(card)
    else:
        if card == "T": return 10
        elif card == "J": return 11
        elif card == "Q": return 12
        elif card == "K": return 13
        elif card == "A": return 14


def get_hand_strength(hand):
    hand_dict = {}
    card_ratings = []
    for card in hand:
        card_ratings.append(get_card_value(card))
        if card in hand_dict:
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1

    amounts_of_cards = sorted(hand_dict.values(), reverse=True)

    if amounts_of_cards[0] == 5:
        hand_strength = 6
    elif amounts_of_cards[0] == 4:
        hand_strength = 5
    elif amounts_of_cards[0] == 3 and amounts_of_cards[1] == 2:
        hand_strength = 4
    elif amounts_of_cards[0] == 3 and amounts_of_cards[1] == 1:
        hand_strength = 3
    elif amounts_of_cards[0] == 2 and amounts_of_cards[1] == 2:
        hand_strength = 2
    elif amounts_of_cards[0] == 2 and amounts_of_cards[1] == 1:
        hand_strength = 1
    else:
        hand_strength = 0

    return [hand_strength, card_ratings]


def resolve_same_hands(hand1, hand2):
    for i in range(len(hand1[1])):
        if hand1[1][i] > hand2[1][i]:
            return hand2, hand1
        elif hand1[1][i] < hand2[1][i]:
            return hand1, hand2
    return hand2, hand1


def day7part1(lines):
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append(get_hand_strength(hand) + [int(bid)])

    sorted_hands = sorted(hands)

    old_hand = (-1, [], 0)
    for i in range(len(sorted_hands)):
        if sorted_hands[i][0] == old_hand[0]:
            ordered = resolve_same_hands(old_hand, sorted_hands[i])
            sorted_hands[i] = ordered[1]
            sorted_hands[i-1] = ordered[0]
        old_hand = sorted_hands[i]

    final_hands = sorted(sorted_hands)
    total_sum = 0
    for i, final_hand in enumerate(final_hands):
        total_sum += final_hand[2] * (i + 1)

    return total_sum


def day7part2(lines):
    return 0


start = time.perf_counter()
result = day7part1(puzzle_lines)
end = time.perf_counter()
print(f"Day 7 Part 1 result is: {result}, computed in: {end - start} seconds")

start = time.perf_counter()
result = day7part2(puzzle_lines)
end = time.perf_counter()
print(f"Day 7 Part 2 result is: {result}, computed in: {end - start} seconds")
