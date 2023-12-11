import time

with open('input.txt', 'r') as f:
    puzzle_input = f.read()
    puzzle_lines = puzzle_input.split("\n")


def day7part1(lines):
    return 0


def day7part2(lines):
    return 0


start = time.perf_counter()
result = day7part1(puzzle_lines)
end = time.perf_counter()
print(f"Day 6 Part 1 result is: {result}, computed in: {end - start} seconds")

start = time.perf_counter()
result = day7part2(puzzle_lines)
end = time.perf_counter()
print(f"Day 6 Part 2 result is: {result}, computed in: {end - start} seconds")
