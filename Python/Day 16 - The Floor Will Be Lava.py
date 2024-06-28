import time


def part1(puzzle_input):
    strings = puzzle_input.split("\n")


def part2(puzzle_input):
    strings = puzzle_input.split("\n")


if __name__ == "__main__":
    with open(r'../Input/day16.txt', 'r') as f:
        puzzle_read = f.read()

    start = time.perf_counter()
    result = part1(puzzle_read)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_read)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
