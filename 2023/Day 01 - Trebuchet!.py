import time


def string_num_to_int(line):
    num_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit, name in enumerate(num_names):
        line = line.replace(name, f"{name}{digit}{name}")
    return line


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    count = 0
    for line in lines:
        num_list = [character for character in line if character.isnumeric()]
        joint_num = f"{num_list[0]}{num_list[-1]}"
        count += int(joint_num)

    return count


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    count = 0
    for line in lines:
        line = string_num_to_int(line)  # <-- difference
        num_list = [character for character in line if character.isnumeric()]
        joint_num = f"{num_list[0]}{num_list[-1]}"
        count += int(joint_num)

    return count


if __name__ == "__main__":
    day = 1
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
