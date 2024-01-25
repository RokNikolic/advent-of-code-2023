import time


def get_distance(speed, remaining_time):
    return speed * remaining_time


def part1(puzzle_input):
    lines = puzzle_input.split("\n")

    times = map(int, lines[0].split()[1:])
    distances = map(int, lines[1].split()[1:])
    total_sum = 1
    for total_time, max_distance in zip(times, distances):
        winning_times = []
        for held_time in range(total_time + 1):
            if held_time * (total_time - held_time) > max_distance:
                winning_times.append(held_time)

        amount_of_wins = len(winning_times)
        total_sum *= amount_of_wins

    return total_sum


def part2(puzzle_input):
    lines = puzzle_input.split("\n")

    time_of_race = int(lines[0].split(":")[1].replace(" ", ""))
    distance_of_race = int(lines[1].split(":")[1].replace(" ", ""))
    winning_times = 0
    for held_time in range(time_of_race + 1):
        if held_time * (time_of_race - held_time) > distance_of_race:
            winning_times += 1

    return winning_times


if __name__ == "__main__":
    with open(r'../Input/day6.txt', 'r') as f:
        puzzle_read = f.read()

    start = time.perf_counter()
    result = part1(puzzle_read)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_read)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
