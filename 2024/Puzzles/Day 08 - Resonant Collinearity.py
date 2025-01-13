import math
import time


def part1(puzzle_input):
    matrix = puzzle_input.split("\n")
    antenna_dict = {}
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] != ".":
                antenna = matrix[y][x]
                if antenna not in antenna_dict:
                    antenna_dict[antenna] = [(y, x)]
                else:
                    antenna_dict[antenna].append((y, x))

    node_set = set()
    for points in antenna_dict.values():
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                y1, x1 = points[i]
                y2, x2 = points[j]
                vector = (x2 - x1,y2 - y1)
                distance = math.dist(points[i], points[j])
                normalized_vector = (vector[0] / distance, vector[1] / distance)

                offset1_y, offset1_x = (normalized_vector[0] * -distance, normalized_vector[1] * -distance)
                offset2_y, offset2_x = (normalized_vector[0] * 2 * distance, normalized_vector[1] * 2 * distance)
                node1 = (y1 + offset1_y, x1 + offset1_x)
                node2 = (y1 + offset2_y, x1 + offset2_x)
                if node1[0] >= 0 and node1[1] >= 0:
                    node_set.add(node1)
                if node2[0] >= 0 and node2[1] >= 0:
                    node_set.add(node2)
    print(node_set)
    return len(node_set)


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    return 0


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
