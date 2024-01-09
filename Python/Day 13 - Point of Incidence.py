import time


def find_mirror(array):
    last_found = []
    for i, line in enumerate(array):
        if line == last_found:
            real_reflection_flag = True
            for j in range(min(i, len(array) - i)):
                real_reflection_flag = array[i - (j + 1)] == array[i + j]
                print(array[i - (j + 1)], array[i + j])

            if real_reflection_flag:
                print(i)
                return i
        else:
            last_found = line
    else:
        return None


def part1(chunks):
    row_sum = 0
    column_sum = 0
    for chunk in chunks:
        array = chunk.split()
        transposed_array = [col for col in zip(*array)]

        if vertical_reflection := find_mirror(array):
            row_sum += vertical_reflection

        elif horizontal_reflection := find_mirror(transposed_array):
            column_sum += horizontal_reflection

    return column_sum + (row_sum * 100)


def part2(lines):
    return 0


if __name__ == "__main__":
    with open(r'../Input/day13.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_chunks = puzzle_input.split("\n\n")

    start = time.perf_counter()
    result = part1(puzzle_chunks)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_chunks)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
