import time
import itertools
from math import lcm


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    lr_instructions = lines[0]
    ins_dict = {'L': 0, 'R': 1}

    nodes_dict = {}
    for line in lines[2:]:
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


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    lr_instructions = lines[0]
    ins_dict = {'L': 0, 'R': 1}

    nodes_dict = {}
    for line in lines[2:]:
        name, connections = line.split(" = ")
        formatted_conn = connections.translate({ord('('): None, ord(')'): None}).split(", ")
        nodes_dict[name] = formatted_conn

    start_nodes = [key for key in nodes_dict if key.endswith('A')]
    end_nodes = [key for key in nodes_dict if key.endswith('Z')]
    list_of_total_steps = []

    for start_node in start_nodes:
        current_node = start_node
        steps = 0
        for instruction in itertools.cycle(lr_instructions):
            steps += 1
            node = nodes_dict[current_node]
            current_node = node[ins_dict[instruction]]
            if current_node in end_nodes:
                list_of_total_steps.append(steps)
                break

    return lcm(*list_of_total_steps)


if __name__ == "__main__":
    day = 8
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
