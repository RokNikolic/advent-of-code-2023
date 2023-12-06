import time

with open('input.txt', 'r') as f:
    puzzle_input = f.readlines()


def day1part1(lines):
    count = 0
    for line in lines:
        exploded = [*line]
        num_list = []
        for character in exploded:
            if character.isnumeric():
                num_list.append(character)

        first_num = num_list[0]
        last_num = num_list[-1]
        joint_num = f"{first_num}{last_num}"
        count += int(joint_num)

    return count


def string_num_to_int(line):
    num_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit, name in enumerate(num_names):
        line = line.replace(name, f"{name}{digit}{name}")
    return line


def day1part2(lines):
    count = 0
    for line in lines:
        line = string_num_to_int(line)
        exploded = [*line]
        num_list = []
        for character in exploded:
            if character.isnumeric():
                num_list.append(character)

        first_num = num_list[0]
        last_num = num_list[-1]
        joint_num = f"{first_num}{last_num}"
        count += int(joint_num)

    return count


start = time.perf_counter()
result = day1part1(puzzle_input)
end = time.perf_counter()
print(f"Day 1 Part 1 result is: {result}, computed in: {end - start} seconds")

start = time.perf_counter()
result = day1part2(puzzle_input)
end = time.perf_counter()
print(f"Day 1 Part 2 result is: {result}, computed in: {end - start} seconds")

# :)
