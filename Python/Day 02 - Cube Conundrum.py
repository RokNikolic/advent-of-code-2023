import time


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    dict_of_limits = {"red": 12, "green": 13, "blue": 14}
    count = 0
    for game_id, line in enumerate(lines):
        _, content = line.split(":")
        reveals = content.split(";")

        legal_game = True
        for reveal in reveals:
            cubes = reveal.split(",")
            for cube in cubes:
                num, color = cube.split(" ")[1:]
                if int(num) > dict_of_limits[color]:
                    legal_game = False

        if legal_game:
            count += (game_id + 1)

    return count


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    power = 0
    for line in lines:
        _, content = line.split(":")
        reveals = content.split(";")

        min_dict = {"red": 0, "green": 0, "blue": 0}
        for reveal in reveals:
            cubes = reveal.split(",")
            for cube in cubes:
                num, color = cube.split(" ")[1:]
                min_dict[color] = max(min_dict[color], int(num))

        power += min_dict["red"] * min_dict["green"] * min_dict["blue"]

    return power


if __name__ == "__main__":
    with open(r'../Input/day2.txt', 'r') as f:
        puzzle_read = f.read()

    start = time.perf_counter()
    result = part1(puzzle_read)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_read)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
