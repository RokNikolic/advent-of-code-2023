import time


def get_distance(point1, point2, empty_rows, empty_columns, expansion):
    y_expansion = 0
    for rows in empty_rows:
        if rows in range(point1[0], point2[0]) or rows in range(point2[0], point1[0]):
            y_expansion += 1

    x_expansion = 0
    for column in empty_columns:
        if column in range(point1[1], point2[1]) or column in range(point2[1], point1[1]):
            x_expansion += 1

    y_dist = abs(point1[0] - point2[0]) + y_expansion * (expansion - 1)
    x_dist = abs(point1[1] - point2[1]) + x_expansion * (expansion - 1)

    return y_dist + x_dist


def part1_part2(lines, expansion):
    index = 0
    galaxy_dict = {}
    empty_rows = set(range(len(lines)))
    empty_columns = set(range(len(lines[0])))

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                index += 1
                galaxy_dict[index] = (y, x)
                empty_rows.discard(y)
                empty_columns.discard(x)

    total_sum = 0
    for point1 in galaxy_dict.values():
        for point2 in galaxy_dict.values():
            manhattan_distance = get_distance(point1, point2, empty_rows, empty_columns, expansion)
            total_sum += manhattan_distance

    return int(total_sum / 2)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = part1_part2(puzzle_lines, 2)
    end = time.perf_counter()
    print(f"Day 11 Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part1_part2(puzzle_lines, 1_000_000)
    end = time.perf_counter()
    print(f"Day 11 Part 2 result is: {result}, computed in: {end - start :.3} seconds")
