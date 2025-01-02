import time


def find_guard(matrix):
    directions = {"^":(-1, 0), ">":(1, 0), "ˇ":(0, 1), "<":(0, -1)}
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] in "^ˇ><":
                return (y, x), directions[matrix[y][x]]


def rotate_right(position):
    direction_change = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    return direction_change[position]


def part1(puzzle_input):
    matrix = puzzle_input.split("\n")
    current_position, current_direction = find_guard(matrix)

    visited_positions = [current_position]
    while current_position[0] + 1 < len(matrix[0]) and current_position[1] + 1 < len(matrix[1]):
        new_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
        if matrix[new_position[0]][new_position[1]] == "#":
            current_direction = rotate_right(current_direction)
        else:
            current_position = new_position
            visited_positions.append(new_position)

    return len(set(visited_positions))


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
