import time

with open('input.txt', 'r') as f:
    puzzle_input = f.read()
    puzzle_lines = puzzle_input.split("\n")


def day3part1(lines):
    return lines


def day3part2(lines):
    return lines


start = time.perf_counter()
result = day3part1(puzzle_lines)
end = time.perf_counter()
print(f"Day 3 Part 1 result is: {result}, computed in: {end - start} seconds")

start = time.perf_counter()
result = day3part2(puzzle_lines)
end = time.perf_counter()
print(f"Day 3 Part 2 result is: {result}, computed in: {end - start} seconds")