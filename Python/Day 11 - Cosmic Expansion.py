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


def part1(puzzle_input):
    expansion = 2  # <-- difference
    lines = puzzle_input.split("\n")
    index = 0
    galaxy_points = []
    empty_rows = set(range(len(lines)))
    empty_columns = set(range(len(lines[0])))

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                index += 1
                galaxy_points.append((y, x))
                empty_rows.discard(y)
                empty_columns.discard(x)

    total_sum = 0
    for i, point1 in enumerate(galaxy_points):
        for point2 in galaxy_points[:i]:
            manhattan_distance = get_distance(point1, point2, empty_rows, empty_columns, expansion)
            total_sum += manhattan_distance

    return total_sum


def part2(puzzle_input):
    expansion = 1_000_000  # <-- difference
    lines = puzzle_input.split("\n")
    index = 0
    galaxy_points = []
    empty_rows = set(range(len(lines)))
    empty_columns = set(range(len(lines[0])))

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                index += 1
                galaxy_points.append((y, x))
                empty_rows.discard(y)
                empty_columns.discard(x)

    total_sum = 0
    for i, point1 in enumerate(galaxy_points):
        for point2 in galaxy_points[:i]:
            manhattan_distance = get_distance(point1, point2, empty_rows, empty_columns, expansion)
            total_sum += manhattan_distance

    return total_sum


if __name__ == "__main__":
    day = 11
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
