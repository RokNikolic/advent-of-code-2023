import time


def process_string(string):
    current_value = 0
    for character in string:
        current_value += ord(character)
        current_value = (current_value * 17) % 256
    return current_value


def part1(puzzle_input):
    strings = puzzle_input.split(",")
    total_sum = sum(map(process_string, strings))
    return total_sum


def part2(puzzle_input):
    strings = puzzle_input.split(",")
    return 0


if __name__ == "__main__":
    with open(r'../Input/day15.txt', 'r') as f:
        puzzle_read = f.read()

    start = time.perf_counter()
    result = part1(puzzle_read)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_read)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
