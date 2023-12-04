import time

with open('input.txt', 'r') as f:
    puzzle_input = f.readlines()


def day2(lines, dict_of_limits):
    count = 0
    for line in lines:
        line = line.strip()
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


start = time.perf_counter()
result = day2(puzzle_input, {"red": 12, "green": 13, "blue": 14})
end = time.perf_counter()
print(f"The result is: {result}, computed in: {end - start} seconds")
