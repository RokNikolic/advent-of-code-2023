import time


def create_range(mapping):
    dest, start_of_range, length = map(int, mapping.split())
    end_of_range = start_of_range + length
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
    seed_map, *line_maps = lines
    seed_list = list(map(int, seed_map.split()[1:]))

    almanac = []
    for line in line_maps:
        _, *maps = line.split("\n")
        ranges = [create_range(mapping) for mapping in maps]
        almanac.append(ranges)

    location_list = [apply_maps(seed, almanac) for seed in seed_list]
    return min(location_list)


def part2(lines):
    seed_map, *line_maps = lines
    seed_list = list(map(int, seed_map.split()[1:]))

    seed_pairs = []
    for i in range(0, len(seed_list), 2):
        seed_pairs.append((seed_list[i], seed_list[i] + seed_list[i + 1]))

    for line in line_maps:
        _, *maps = line.split("\n")
        ranges = [create_range(mapping) for mapping in maps]

        locations = []
        while seed_pairs:
            seed_start, seed_end = seed_pairs.pop()
            for start_interval, end_interval, offset in ranges:
                overlap_start = max(seed_start, start_interval)
                overlap_end = min(seed_end, end_interval)
                if overlap_start < overlap_end:
                    locations.append((overlap_start + offset, overlap_end + offset))
                    if overlap_start > seed_start:
                        seed_pairs.append((seed_start, overlap_start))
                    if seed_end > overlap_end:
                        seed_pairs.append((overlap_end, seed_end))
                    break
            else:
                locations.append((seed_start, seed_end))

        seed_pairs = locations

    return min(seed_pairs)[0]


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
