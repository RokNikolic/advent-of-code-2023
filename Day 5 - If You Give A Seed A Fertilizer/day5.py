import time


def create_range(mapping):
    dest, start_of_range, length = map(int, mapping.split())
    end_of_range = start_of_range + length - 1
    offset = dest - start_of_range
    return [start_of_range, end_of_range, offset]


def apply_maps(seed, map_list):
    for maps in map_list:
        for map_range in maps:
            if seed in range(map_range[0], map_range[1] + 1):
                seed += map_range[2]
                break

    return seed


def part1(lines):
    seed_map = lines.pop(0)
    seed_list = list(map(int, seed_map.split()[1:]))

    map_list = []
    for line in lines:
        _, *maps = line.split("\n")
        map_list.append([create_range(mapping) for mapping in maps])

    location_list = [apply_maps(seed, map_list) for seed in seed_list]
    return min(location_list)


def part2(lines):
    return 0


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n\n")

    start = time.perf_counter()
    result = part1(puzzle_lines)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
