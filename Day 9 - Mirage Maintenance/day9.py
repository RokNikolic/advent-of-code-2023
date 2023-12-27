import time


def predict_next_value(input_list):
    next_list = []
    for i in range(len(input_list) - 1):
        difference = input_list[i + 1] - input_list[i]
        next_list.append(difference)

    if all(value == 0 for value in next_list):
        return 0
    else:
        new_difference = next_list[-1] + predict_next_value(next_list)
        return new_difference


def predict_previous_value(input_list):
    next_list = []
    for i in range(len(input_list) - 1):
        difference = input_list[i + 1] - input_list[i]
        next_list.append(difference)

    if all(value == 0 for value in next_list):
        return 0
    else:
        new_difference = next_list[0] - predict_previous_value(next_list)
        return new_difference


def part1(lines):
    total_sum = 0
    for line in lines:
        list_of_line = [int(value) for value in line.split()]
        new_difference = predict_next_value(list_of_line)
        new_value = list_of_line[-1] + new_difference
        total_sum += new_value

    return total_sum


def part2(lines):
    total_sum = 0
    for line in lines:
        list_of_line = [int(value) for value in line.split()]
        new_difference = predict_previous_value(list_of_line)
        new_value = list_of_line[0] - new_difference
        total_sum += new_value

    return total_sum


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
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
