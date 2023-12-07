import time

with open('input.txt', 'r') as f:
    puzzle_input = f.read()
    puzzle_lines = puzzle_input.split("\n")


def day4part1(lines):
    point_sum = 0
    for line in lines:
        _, numbers = line.split(":")
        our_nums, winning_nums = numbers.split("|")
        our_set = set(filter(None, our_nums.split(" ")))
        winning_set = set(filter(None, winning_nums.split(" ")))
        matches = len(our_set.intersection(winning_set))
        if matches != 0:
            points = pow(2, matches - 1)
        else:
            points = 0
        point_sum += points

    return point_sum


def day4part2(lines):
    return 0


start = time.perf_counter()
result = day4part1(puzzle_lines)
end = time.perf_counter()
print(f"Day 4 Part 1 result is: {result}, computed in: {end - start} seconds")

start = time.perf_counter()
result = day4part2(puzzle_lines)
end = time.perf_counter()
print(f"Day 4 Part 2 result is: {result}, computed in: {end - start} seconds")
