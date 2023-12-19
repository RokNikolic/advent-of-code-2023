import time


def expand_universe(matrix):
    empty_rows = []
    for i, line in enumerate(matrix):
        if all(value == '.' for value in line):
            empty_rows.append((i, line))
    for i, (row, line) in enumerate(empty_rows):
        matrix.insert(row + i, line)

    trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    empty_columns = []
    for j, line in enumerate(trans_matrix):
        if all(value == '.' for value in line):
            empty_columns.append((j, line))
    for j, (columns, line) in enumerate(empty_columns):
        trans_matrix.insert(columns + j, line)

    return [[trans_matrix[j][i] for j in range(len(trans_matrix))] for i in range(len(trans_matrix[0]))]


def part1(lines):
    expanded_lines = expand_universe(lines)

    index = 0
    galaxy_dict = {}
    for i, line in enumerate(expanded_lines):
        for j, char in enumerate(line):
            if char == "#":
                index += 1
                galaxy_dict[index] = (i, j)

    total_sum = 0
    for current_name, (y1, x1) in galaxy_dict.items():
        for other_name, (y_other, x_other) in galaxy_dict.items():
            manhattan_distance = abs(y1 - y_other) + abs(x1 - x_other)
            total_sum += manhattan_distance

    return int(total_sum / 2)


def part2(lines):
    return 0


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = part1(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 11 Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 11 Part 2 result is: {result}, computed in: {end - start :.3} seconds")
