import time


def make_antenna_dict(matrix):
    antenna_dict = {}
    for y, row in enumerate(matrix):
        for x, antenna in enumerate(row):
            if antenna != ".":
                if antenna not in antenna_dict:
                    antenna_dict[antenna] = [(y, x)]
                else:
                    antenna_dict[antenna].append((y, x))
    return antenna_dict


def get_anti_nodes(point1, point2):
    y1, x1 = point1
    y2, x2 = point2
    dist_y, dist_x = (y1 - y2, x1 - x2)
    node1 = (y1 + dist_y, x1 + dist_x)
    node2 = (y2 - dist_y, x2 - dist_x)
    return node1, node2


def part1(puzzle_input):
    matrix = puzzle_input.split("\n")
    antenna_dict = make_antenna_dict(matrix)

    anti_node_set = set()
    for points in antenna_dict.values():
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                node1, node2 = get_anti_nodes(points[i], points[j])
                if 0 <= node1[0] < len(matrix) and 0 <= node1[1] < len(matrix[0]):
                    anti_node_set.add(node1)
                if 0 <= node2[0] < len(matrix) and 0 <= node2[1] < len(matrix[0]):
                    anti_node_set.add(node2)

    return len(anti_node_set)


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
