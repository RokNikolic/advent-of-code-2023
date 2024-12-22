import time


def check_update_correctness(update_list, order_dictionary):
    for i, page_number in enumerate(update_list):
        if page_number not in order_dictionary:
            if i != 0:
                return False
        else:
            previous_needed_numbers = order_dictionary[page_number]
            previous_order_numbers = set(update_list[:i])
            if not previous_order_numbers.issubset(previous_needed_numbers):
                return False
    else:
        return True


def part1(puzzle_input):
    order_part, update_part = puzzle_input.split("\n\n")
    orders = order_part.split("\n")
    updates = update_part.split("\n")

    order_dict = {}
    for order in orders:
        before, after = list(map(int, order.split("|")))
        if after not in order_dict:
            order_dict[after] = {before}
        else:
            order_dict[after].add(before)

    overall_sum = 0
    for update in updates:
        page_numbers = list(map(int, update.split(",")))
        if check_update_correctness(page_numbers, order_dict):
            middle_index = len(page_numbers) // 2
            overall_sum += page_numbers[middle_index]
    
    return overall_sum


def part2(puzzle_input):

    return 0


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
