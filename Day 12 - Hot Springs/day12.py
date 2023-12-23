import time


def part1(lines):
    for line in lines:
        springs, arrangements = line.split(" ")
        arrangements_list = map(int, arrangements.split(","))
        print(list(arrangements_list))


def part2(lines):
    return 0


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = part1(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 10 Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 10 Part 2 result is: {result}, computed in: {end - start :.3} seconds")
