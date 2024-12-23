import time


def find_guard(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] in "^ˇ><":
                return (y, x, matrix[y][x])
    return 0



def part1(puzzle_input):
    matrix = puzzle_input.split("\n")
    print(find_guard(matrix))
    return 0


def part2(puzzle_input):
    return 0


if __name__ == "__main__":
    day = 6
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
