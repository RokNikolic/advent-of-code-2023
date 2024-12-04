# Code inspired by https://github.com/hyper-neutrino
import time


def count_arrangements(record, damaged_list):
    if record == "":
        if damaged_list == ():
            return 1
        else:
            return 0

    if damaged_list == ():
        if "#" in record:
            return 0
        else:
            return 1

    if (record, damaged_list) in state_dict:
        return state_dict[(record, damaged_list)]

    count = 0
    symbol = record[0]
    block = damaged_list[0]
    if symbol in ".?":
        count += count_arrangements(record[1:], damaged_list)

    if symbol in "#?":
        if block <= len(record) and "." not in record[:block] and (block == len(record) or record[block] != "#"):
            count += count_arrangements(record[block + 1:], damaged_list[1:])

    state_dict[(record, damaged_list)] = count
    return count


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    arrangements_sum = 0
    for line in lines:
        record, damaged_numbers = line.split(" ")
        damaged_list = tuple(map(int, damaged_numbers.split(",")))
        arrangements = count_arrangements(record, damaged_list)
        arrangements_sum += arrangements

    return arrangements_sum


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    arrangements_sum = 0
    for line in lines:
        record, damaged_numbers = line.split(" ")
        damaged_list = tuple(map(int, damaged_numbers.split(",")))
        record = "?".join([record] * 5)  # <-- difference
        damaged_list *= 5  # <-- difference
        arrangements = count_arrangements(record, damaged_list)
        arrangements_sum += arrangements

    return arrangements_sum


if __name__ == "__main__":
    day = 12
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    state_dict = {}  # Sadly has to be here with this implementation

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
