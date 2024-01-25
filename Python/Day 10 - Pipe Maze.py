import time


def is_pipe(symbol):
    pipe_dict = {'|': [(-1, 0), (1, 0)],
                 '-': [(0, -1), (0, 1)],
                 'L': [(-1, 0), (0, 1)],
                 'J': [(-1, 0), (0, -1)],
                 '7': [(0, -1), (1, 0)],
                 'F': [(1, 0), (0, 1)]}

    return symbol in pipe_dict


def find_pipe_directions(index, lines):
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


def find_start(lines):
    start_index = None
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                start_index = i, j

    positions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for y, x in positions:
        next_index = (start_index[0] + y, start_index[1] + x)
        symbol = lines[next_index[0]][next_index[1]]
        if is_pipe(symbol):
            possible_directions = find_pipe_directions((next_index[0], next_index[1]), lines)
            if start_index in possible_directions:
                return start_index, next_index


def follow_pipe(start_index, work_index, lines):
    pipe = [start_index]
    old_index = start_index
    steps = 1
    while start_index != work_index:
        steps += 1
        pipe.append(work_index)
        directions = find_pipe_directions(work_index, lines)
        next_index = [direction for direction in directions if direction != old_index][0]
        old_index = work_index
        work_index = next_index

    return steps, pipe


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    start_index, next_index = find_start(lines)
    steps, _ = follow_pipe(start_index, next_index, lines)
    return int(steps / 2)


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    start_index, next_index = find_start(lines)
    _, pipe = follow_pipe(start_index, next_index, lines)

    inside_tiles = 0
    inside_flag = False
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if (i, j) in pipe:
                if char in '|LJ':
                    inside_flag = not inside_flag
            else:
                inside_tiles += inside_flag

    return inside_tiles


if __name__ == "__main__":
    with open(r'../Input/day10.txt', 'r') as f:
        puzzle_read = f.read()

    start = time.perf_counter()
    result = part1(puzzle_read)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_read)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
