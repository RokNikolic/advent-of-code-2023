import time


def part1(lines):
    point_sum = 0
    for line in lines:
        _, numbers = line.split(":")
        winning_nums, our_nums = numbers.split("|")
        winning_set = set(winning_nums.split())
        our_set = set(our_nums.split())
        matches = len(winning_set.intersection(our_set))
        points = int(pow(2, matches - 1))
        point_sum += points

    return point_sum


def part2(lines):
    card_list = []
    for line in lines:
        _, numbers = line.split(":")
        winning_nums, our_nums = numbers.split("|")
        winning_set = set(winning_nums.split())
        our_set = set(our_nums.split())
        matches = len(winning_set.intersection(our_set))
        card_list.append([int(matches), 1])

    score = 0
    for card_id, (matches, amount_of_cards) in enumerate(card_list):
        score += amount_of_cards
        for new_card_id in range(card_id + 1, card_id + 1 + matches):
            card_list[new_card_id][1] += amount_of_cards

    return score


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = part1(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 4 Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 4 Part 2 result is: {result}, computed in: {end - start :.3} seconds")
