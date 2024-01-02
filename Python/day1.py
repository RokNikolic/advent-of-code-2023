import time


def string_num_to_int(line):
    num_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit, name in enumerate(num_names):
        line = line.replace(name, f"{name}{digit}{name}")
    return line


def part1_part2(lines, part):
    count = 0
    for line in lines:
        if part == 2:
            line = string_num_to_int(line)
        num_list = [character for character in line if character.isnumeric()]
        joint_num = f"{num_list[0]}{num_list[-1]}"
        count += int(joint_num)

    return count


if __name__ == "__main__":
    with open(r'../input/day1.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = part1_part2(puzzle_lines, 1)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part1_part2(puzzle_lines, 2)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
