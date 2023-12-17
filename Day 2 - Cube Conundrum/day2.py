import time


def day2part1(lines, dict_of_limits):
    count = 0
    for line in lines:
        game, content = line.split(":")
        game_id = int(game.split(" ")[1])
        reveals = content.split(";")

        legal_game = True
        for reveal in reveals:
            cubes = reveal.split(",")
            for cube in cubes:
                num, color = cube.split(" ")[1:]
                if int(num) > dict_of_limits[color]:
                    legal_game = False

        if legal_game:
            count += game_id

    return count


def day2part2(lines):
    power = 0
    for line in lines:
        game, content = line.split(":")
        reveals = content.split(";")

        min_dict = {"red": 0, "green": 0, "blue": 0}
        for reveal in reveals:
            cubes = reveal.split(",")
            for cube in cubes:
                num, color = cube.split(" ")[1:]
                if (int_num := int(num)) > min_dict[color]:
                    min_dict[color] = int_num

        power += min_dict["red"] * min_dict["green"] * min_dict["blue"]

    return power


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = day2part1(puzzle_lines, {"red": 12, "green": 13, "blue": 14})
    end = time.perf_counter()
    print(f"Day 2 Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = day2part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Day 2 Part 2 result is: {result}, computed in: {end - start :.3} seconds")
