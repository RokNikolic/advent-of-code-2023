import time


def is_pipe(symbol):
    pipe_dict = {'|': [(-1, 0), (1, 0)],
                 '-': [(0, -1), (0, 1)],
                 'L': [(-1, 0), (0, 1)],
                 'J': [(-1, 0), (0, -1)],
                 '7': [(0, -1), (1, 0)],
                 'F': [(1, 0), (0, 1)]}

    return symbol in pipe_dict


def check_pipe_dict(index, lines):
    pipe_dict = {'|': [(-1, 0), (1, 0)],
                 '-': [(0, -1), (0, 1)],
                 'L': [(-1, 0), (0, 1)],
                 'J': [(-1, 0), (0, -1)],
                 '7': [(0, -1), (1, 0)],
                 'F': [(1, 0), (0, 1)]}

    y, x = index
    abs_directions = pipe_dict[lines[y][x]]
    relative_directions = []
    for y_abs, x_abs in abs_directions:
        relative_directions.append((y + y_abs, x + x_abs))

    return relative_directions


def replace_s(lines):
    positions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    start_index = None
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] == 'S':
                start_index = j, i

    found = []
    for y, x in positions:
        next_y = start_index[0] + y
        next_x = start_index[1] + x
        symbol = lines[next_y][next_x]
        if is_pipe(symbol):
            possible_directions = check_pipe_dict((next_index := (next_y, next_x)), lines)
            if start_index in possible_directions:
                found.append(next_index)

    print(found)


def follow_pipe(start_index, lines):
    start_directions = check_pipe_dict(start_index, lines)
    work_index = start_directions[0]
    old_index = start_index
    steps = 1
    while start_index != work_index:
        steps += 1
        directions = check_pipe_dict(work_index, lines)
        next_index = [direction for direction in directions if direction != old_index][0]
        old_index = work_index
        work_index = next_index

    return steps


def day10part1(lines):
    start_index = (2, 0)
    start_index, new_lines = replace_s(lines)

    steps = follow_pipe(start_index, new_lines)
    return steps / 2


def day10part2(lines):
    return 0


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = day10part1(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 10 Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = day10part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 10 Part 2 result is: {result}, computed in: {end - start :.3} seconds")
