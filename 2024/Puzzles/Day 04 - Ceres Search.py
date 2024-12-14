import time


def pad_matrix(array, symbol):
    padding = ""
    for i in range(len(array[0])):
        padding += symbol

    array = [padding] + array + [padding]

    for i in range(len(array)):
        array[i] = symbol + array[i] + symbol

    return array


def check_location(matrix, y, x):
    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    needed_letters = ["M", "A", "S"]
    xmas_count = 0
    for p_y, p_x in positions:
        for i, letter in enumerate(needed_letters):
            i += 1
            if matrix[y + (p_y * i)][x + (p_x * i)] != letter:
                break
        else:
            xmas_count += 1
    return xmas_count


def part1(puzzle_input):
    matrix = puzzle_input.split("\n")
    padded_matrix = pad_matrix(matrix, ".")
    overall_count = 0
    for y in range(len(padded_matrix)):
        for x in range(len(padded_matrix[0])):
            if padded_matrix[y][x] == "X":
                count = check_location(padded_matrix, y, x)
                overall_count += count

    return overall_count


def part2(puzzle_input):
    return 0


if __name__ == "__main__":
    day = 4
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
