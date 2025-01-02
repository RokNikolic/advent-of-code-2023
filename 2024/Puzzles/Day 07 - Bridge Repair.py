import time


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    for line in lines:
        product_str, numbers_str = line.split(": ")
        product = int(product_str)
        numbers = list(map(int, numbers_str.split(" ")))
        print(product, numbers)
    return 0


def part2(puzzle_input):
    return 0


if __name__ == "__main__":
    day = 7
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
