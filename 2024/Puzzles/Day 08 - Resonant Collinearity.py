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


def get_2_anti_nodes(point1, point2, borders):
    y1, x1 = point1
    y2, x2 = point2
    dist_y, dist_x = (y2 - y1, x2 - x1)
    height, width = borders
    nodes = []
    node1 = (y1 - dist_y, x1 - dist_x)
    if 0 <= node1[0] < height and 0 <= node1[1] < width:
        nodes.append(node1)
    node2 = (y2 + dist_y, x2 + dist_x)
    if 0 <= node2[0] < height and 0 <= node2[1] < width:
        nodes.append(node2)
    return nodes


def get_all_anti_nodes(point1, point2, borders):
    y1, x1 = point1
    y2, x2 = point2
    dist_y, dist_x = (y1 - y2, x1 - x2)
    height, width = borders
    nodes = []
    for i in range(1, 1000):
        node1 = (y1 - dist_y * i, x1 - dist_x * i)
        if 0 <= node1[0] < height and 0 <= node1[1] < width:
            nodes.append(node1)
        else:
            break
    for i in range(1, 1000):
        node2 = (y2 + dist_y * i, x2 + dist_x * i)
        if 0 <= node2[0] < height and 0 <= node2[1] < width:
            nodes.append(node2)
        else:
            break
    return nodes


def part1(puzzle_input):
    matrix = puzzle_input.split("\n")
    antenna_dict = make_antenna_dict(matrix)

    anti_nodes = []
    for points in antenna_dict.values():
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                nodes = get_2_anti_nodes(points[i], points[j], (len(matrix), len(matrix[0])))
                anti_nodes.extend(nodes)
    return len(set(anti_nodes))


def part2(puzzle_input):
    matrix = puzzle_input.split("\n")
    antenna_dict = make_antenna_dict(matrix)

    anti_nodes = []
    for points in antenna_dict.values():
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                nodes = get_all_anti_nodes(points[i], points[j], (len(matrix), len(matrix[0])))
                anti_nodes.extend(nodes)
    return len(set(anti_nodes))


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
