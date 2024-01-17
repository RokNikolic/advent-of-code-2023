import time


def move_stones(array):
    transposed_array = list(zip(*array))
    final_array = []
    for line in transposed_array:
        rolling_portions = "".join(line).split("#")
        sorted_portions = ["".join(sorted(portion, reverse=True)) for portion in rolling_portions]
        final_array.append("#".join(sorted_portions))

    return list(zip(*final_array))


def part1(lines):
    moved_stones_array = move_stones(lines)
    total_weight = 0
    for i, line in enumerate(moved_stones_array[::-1]):
        for position in line:
            if position == "O":
                total_weight += (i + 1)
    return total_weight


def part2(lines):
    return 0


if __name__ == "__main__":
    with open(r'../Input/day14.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = part1(puzzle_lines)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
