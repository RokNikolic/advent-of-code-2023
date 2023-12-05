import time

with open('input.txt', 'r') as f:
    puzzle_input = f.readlines()


def day3part1(lines):
    pass


def day3part2(lines):
    pass


start = time.perf_counter()
result = day3part1(puzzle_input)
end = time.perf_counter()
print(f"Day 3 Part 1 result is: {result}, computed in: {end - start} seconds")

start = time.perf_counter()
result = day3part2(puzzle_input)
end = time.perf_counter()
print(f"Day 3 Part 2 result is: {result}, computed in: {end - start} seconds")