import time


def num_of_differences(string1, string2):
    differences = 0
    for character1, character2 in zip(string1, string2):
        if character1 != character2:
            differences += 1
    return differences


def find_mirror(array, differences):
    for i in range(1, len(array)):
        before = array[:i][::-1]
        after = array[i:]
        zipped = zip(before, after)

        sum_of_differences = 0
        for first, second in zipped:
            sum_of_differences += num_of_differences(first, second)

        if sum_of_differences == differences:
            return i
    else:
        return None


def part1(puzzle_input):
    differences = 0  # <-- difference
    chunks = puzzle_input.split("\n\n")
    row_sum = 0
    column_sum = 0
    for chunk in chunks:
        array = chunk.split()
        transposed_array = list(zip(*array))

        if vertical_reflection := find_mirror(array, differences):
            row_sum += vertical_reflection

        elif horizontal_reflection := find_mirror(transposed_array, differences):
            column_sum += horizontal_reflection

    return column_sum + (row_sum * 100)


def part2(puzzle_input):
    differences = 1  # <-- difference
    chunks = puzzle_input.split("\n\n")
    row_sum = 0
    column_sum = 0
    for chunk in chunks:
        array = chunk.split()
        transposed_array = list(zip(*array))

        if vertical_reflection := find_mirror(array, differences):
            row_sum += vertical_reflection

        elif horizontal_reflection := find_mirror(transposed_array, differences):
            column_sum += horizontal_reflection

    return column_sum + (row_sum * 100)


if __name__ == "__main__":
    day = 13
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
