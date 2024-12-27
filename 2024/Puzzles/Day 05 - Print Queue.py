import time
from functools import cmp_to_key


def create_preceding_number_dict(orders):
    preceding_number_dict = {}
    for order in orders:
        before, after = list(map(int, order.split("|")))
        if after not in preceding_number_dict:
            preceding_number_dict[after] = {before}
        else:
            preceding_number_dict[after].add(before)
    return preceding_number_dict


def check_update_correctness(update, preceding_number_dictionary):
    for i, page_number in enumerate(update):
        if page_number not in preceding_number_dictionary:
            if i != 0:
                return False
        else:
            previous_needed_numbers = preceding_number_dictionary[page_number]
            previous_order_numbers = set(update[:i])
            if not previous_order_numbers.issubset(previous_needed_numbers):
                return False
    else:
        return True


def part1(puzzle_input):
    order_part, update_part = puzzle_input.split("\n\n")
    orders = order_part.split("\n")
    updates = update_part.split("\n")

    preceding_number_dict = create_preceding_number_dict(orders)

    overall_sum = 0
    for update in updates:
        update_numbers = list(map(int, update.split(",")))
        if check_update_correctness(update_numbers, preceding_number_dict):
            overall_sum += update_numbers[len(update_numbers) // 2]
    return overall_sum


def part2(puzzle_input):
    order_part, update_part = puzzle_input.split("\n\n")
    orders = order_part.split("\n")
    updates = update_part.split("\n")

    preceding_number_dict = create_preceding_number_dict(orders)

    comparison_dict = {}
    for order in orders:
        before, after = list(map(int, order.split("|")))
        comparison_dict[(before, after)] = -1
        comparison_dict[(after, before)] = 1

    overall_sum = 0
    for update in updates:
        update_numbers = list(map(int, update.split(",")))
        if not check_update_correctness(update_numbers, preceding_number_dict):
            update_numbers.sort(key=cmp_to_key(lambda num1, num2: comparison_dict[(num1, num2)]))
            overall_sum += update_numbers[len(update_numbers) // 2]
    return overall_sum


if __name__ == "__main__":
    day = 5
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
