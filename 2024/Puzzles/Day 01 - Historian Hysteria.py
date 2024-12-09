import time


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    left_list = []
    right_list = []
    for line in lines:
        first, second = line.split()
        left_list.append(int(first))
        right_list.append(int(second))

    left_list.sort()
    right_list.sort()
    differences = 0
    for first, second in zip(left_list, right_list):
        difference = abs(first - second)
        differences += difference

    return differences


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    left_list = []
    right_list = []
    for line in lines:
        first, second = line.split()
        left_list.append(int(first))
        right_list.append(int(second))

    right_list_tally = {}
    for number in right_list:
        if number in right_list_tally:
            right_list_tally[number] = right_list_tally[number] + 1
        else:
            right_list_tally[number] = 1

    similarity_score = 0
    for number in left_list:
        if number in right_list_tally:
            occurrences = right_list_tally[number]
            similarity_score += number * occurrences

    return similarity_score

if __name__ == "__main__":
    day = 1
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
