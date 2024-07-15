import time


def cycle(array):
    working_array = array
    for _ in range(4):
        moved_array = move_stones(working_array)
        working_array = [row[::-1] for row in moved_array]

    return working_array


def move_stones(array):
    transposed_array = list(map("".join, zip(*array)))
    final_array = []
    for line in transposed_array:
        rolling_portions = line.split("#")
        sorted_portions = ["".join(sorted(portion, reverse=True)) for portion in rolling_portions]
        final_array.append("#".join(sorted_portions))

    return final_array


def measure_weight(moved_stones):
    total_weight = 0
    for i, line in enumerate(moved_stones[::-1]):
        for position in line:
            if position == "O":
                total_weight += (i + 1)

    return total_weight


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    moved_stones_array = list(map("".join, zip(*move_stones(lines))))
    return measure_weight(moved_stones_array)


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    seen_list = [lines]
    i = 0
    while True:
        i += 1
        lines = cycle(lines)
        if lines in seen_list:
            break
        else:
            seen_list.append(lines)

    start_of_loop = seen_list.index(lines)
    end_of_loop = i

    final_array = seen_list[(1_000_000_000 - start_of_loop) % (end_of_loop - start_of_loop) + start_of_loop]

    return measure_weight(final_array)


if __name__ == "__main__":
    day = 14
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
