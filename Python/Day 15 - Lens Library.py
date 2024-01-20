import time


def process_string(string):
    current_value = 0
    for character in string:
        current_value += ord(character)
        current_value = (current_value * 17) % 256
    return current_value


def part1(strings):
    total_sum = 0
    for string in strings:
        total_sum += process_string(string)
    return total_sum


def part2(lines):
    return 0


if __name__ == "__main__":
    with open(r'../Input/day15.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_strings = puzzle_input.split(",")

    start = time.perf_counter()
    result = part1(puzzle_strings)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_strings)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
