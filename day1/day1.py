import time

with open('input.txt', 'r') as f:
    puzzle_input = f.readlines()


def day1(lines):
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


start = time.perf_counter()
result = day1(puzzle_input)
end = time.perf_counter()
print(f"The result is: {result}, computed in: {end - start} seconds")
