import time


def pad_matrix(array, symbol):
    padding = ""
    for i in range(len(array[0])):
        padding += symbol

    array = [padding] + array + [padding]

    for i in range(len(array)):
        array[i] = symbol + array[i] + symbol

    return array


def check_around(i, j, lines):
    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    found = []
    time_since_last = 100
    last_line = 0
    for y, x in positions:
        if lines[i+y][j+x].isnumeric():
            if time_since_last != 0 or i+y != last_line:
                found.append((i+y, j+x))
            last_line = i+y
            time_since_last = 0
        else:
            time_since_last += 1

    return found


def expand_number(found_num, lines):
    y, x = found_num
    right_x = x
    left_x = x
    while lines[y][right_x + 1].isnumeric():
        right_x += 1
    while lines[y][left_x - 1].isnumeric():
        left_x -= 1

    full_number = lines[y][left_x:right_x + 1]
    return int(full_number)


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    lines = pad_matrix(lines, ".")
    total_sum = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if not lines[i][j].isnumeric() and lines[i][j] != '.':
                list_of_found = check_around(i, j, lines)
                for found in list_of_found:
                    number = expand_number(found, lines)
                    total_sum += number

    return total_sum


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    lines = pad_matrix(lines, ".")
    total_sum = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] == '*':
                list_of_found = check_around(i, j, lines)
                if len(list_of_found) == 2:
                    gear_ratio = 1
                    for found in list_of_found:
                        number = expand_number(found, lines)
                        gear_ratio *= number

                    total_sum += gear_ratio

    return total_sum


if __name__ == '__main__':
    with open(r'../Input/day3.txt', 'r') as f:
        puzzle_read = f.read()

    start = time.perf_counter()
    result = part1(puzzle_read)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_read)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
