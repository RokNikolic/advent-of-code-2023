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


def part1_part2(lines, part):
    arrangements_sum = 0
    for line in lines:
        record, damaged_numbers = line.split(" ")
        damaged_list = tuple(map(int, damaged_numbers.split(",")))
        if part == 2:
            record = "?".join([record] * 5)
            damaged_list *= 5
        arrangements = count_arrangements(record, damaged_list)
        arrangements_sum += arrangements

    return arrangements_sum


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    state_dict = {}

    start = time.perf_counter()
    result = part1_part2(puzzle_lines, 1)
    end = time.perf_counter()
    print(f"Day 10 Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part1_part2(puzzle_lines, 2)
    end = time.perf_counter()
    print(f"Day 10 Part 2 result is: {result}, computed in: {end - start :.3} seconds")
