import time
import re


def extract_mul_commands(memory):
    regex = r'mul\([0-9]+,[0-9]+\)'
    return re.findall(regex, memory)


def resolve_mul(command):
    command = command.replace("mul(", "")
    command = command.replace(")", "")
    one, two = list(map(int, command.split(",")))
    return one * two


def part1(puzzle_input):
    commands = extract_mul_commands(puzzle_input)
    sum_of_all = sum([resolve_mul(command) for command in commands])
    return sum_of_all


def part2(puzzle_input):

    return 0


if __name__ == "__main__":
    day = 3
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
