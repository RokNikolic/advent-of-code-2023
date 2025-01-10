import time


def determine_cal(product, numbers):
    last_number = numbers[-1]
    the_rest_of_nums = numbers[:-1]
    if len(numbers) == 1:
        return product == last_number
    if product % last_number == 0 and determine_cal(product // last_number, the_rest_of_nums):
        return True
    if product > last_number and determine_cal(product - last_number, the_rest_of_nums):
        return True
    else:
        return False


def determine_cal_cot(product, numbers):
    last_number = numbers[-1]
    the_rest_of_nums = numbers[:-1]
    if len(numbers) == 1:
        return product == last_number
    if product % last_number == 0 and determine_cal_cot(product // last_number, the_rest_of_nums):
        return True
    if product > last_number and determine_cal_cot(product - last_number, the_rest_of_nums):
        return True
    p = str(product)
    l_n= str(last_number)
    if len(p) > len(l_n) and p.endswith(l_n) and determine_cal_cot(int(p[:-len(l_n)]), the_rest_of_nums):
        return True
    else:
        return False


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    overall_sum = 0
    for line in lines:
        product_str, numbers_str = line.split(": ")
        product = int(product_str)
        numbers = [int(num) for num in numbers_str.split()]
        if determine_cal(product, numbers):
            overall_sum += product
    return overall_sum


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    overall_sum = 0
    for line in lines:
        product_str, numbers_str = line.split(": ")
        product = int(product_str)
        numbers = [int(num) for num in numbers_str.split()]
        if determine_cal_cot(product, numbers):
            overall_sum += product
    return overall_sum


if __name__ == "__main__":
    day = 7
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
