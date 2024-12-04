import time


def hash_algorithm(string):
    current_value = 0
    for character in string:
        current_value += ord(character)
        current_value = (current_value * 17) % 256
    return current_value


def part1(puzzle_input):
    steps = puzzle_input.split(",")
    total_sum = sum(map(hash_algorithm, steps))
    return total_sum


def remove_lens_from_box(boxes, box_index, lens):
    working_box = boxes[box_index]
    if lens in working_box:
        del working_box[lens]


def add_lens_to_box(boxes, box_index, lens, focal_length):
    working_box = boxes[box_index]
    working_box[lens] = focal_length


def part2(puzzle_input):
    steps = puzzle_input.split(",")
    boxes = [{} for _ in range(256)]
    for step in steps:
        if "-" in step:
            lens_label = step.replace('-', '')
            box_index = hash_algorithm(lens_label)
            remove_lens_from_box(boxes, box_index, lens_label)
        elif "=" in step:
            lens_label, focal_length = step.split("=")
            box_index = hash_algorithm(lens_label)
            add_lens_to_box(boxes, box_index, lens_label, focal_length)

    total_sum = 0
    for i, box in enumerate(boxes):
        box_number = i + 1
        for j, focal_length in enumerate(box.values()):
            slot_number = j + 1
            total_sum += box_number * slot_number * int(focal_length)
    return total_sum


if __name__ == "__main__":
    day = 15
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
