import time
import re


def extract_mul_commands(memory):
    regex = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
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
    dos = puzzle_input.split("do()")
    sum_of_all = 0
    for do in dos:
        allowed_memory = do.split("don't()")[0]
        commands = extract_mul_commands(allowed_memory)
        sum_of_allowed = sum([resolve_mul(command) for command in commands])
        sum_of_all += sum_of_allowed

    return sum_of_all


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
