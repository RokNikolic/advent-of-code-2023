import time
import itertools

with open('input.txt', 'r') as f:
    puzzle_input = f.read()
    puzzle_lines = puzzle_input.split("\n")


def day8part1(lines):
    lr_instructions = lines.pop(0)
    ins_dict = {'L': 0, 'R': 1}
    del lines[0]

    nodes_dict = {}
    for line in lines:
        name, connections = line.split(" = ")
        formatted_conn = connections.translate({ord('('): None, ord(')'): None}).split(", ")
        nodes_dict[name] = formatted_conn

    current_node = 'AAA'
    end_node = 'ZZZ'
    steps = 0
    for instruction in itertools.cycle(lr_instructions):
        steps += 1
        node = nodes_dict[current_node]
        current_node = node[ins_dict[instruction]]
        if current_node == end_node:
            break

    return steps


def day8part2(lines):
    return 0


start = time.perf_counter()
result = day8part1(puzzle_lines)
end = time.perf_counter()
print(f"Day 8 Part 1 result is: {result}, computed in: {end - start} seconds")

start = time.perf_counter()
result = day8part2(puzzle_lines)
end = time.perf_counter()
print(f"Day 8 Part 2 result is: {result}, computed in: {end - start} seconds")
