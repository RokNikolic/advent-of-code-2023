import time


def day9part1(lines):
    return 0


def day9part2(lines):
    return 0


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = day9part1(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 9 Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = day9part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 9 Part 2 result is: {result}, computed in: {end - start :.3} seconds")