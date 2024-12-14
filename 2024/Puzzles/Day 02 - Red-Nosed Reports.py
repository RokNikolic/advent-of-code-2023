import time


def check_safety(report):
    differences = []
    for x, y in zip(report, report[1:]):
        differences.append(y - x)

    # We can combine the sign and change amount check
    is_safe = all([1 <= dif <= 3 for dif in differences]) or all([-3 <= dif <= -1 for dif in differences])
    return is_safe


def check_without_one_element(report):
    for i in range(len(report)):
        report_without_i = report[:i] + report[i+1:]
        if check_safety(report_without_i):
            return True
    else:
        return False


def part1(puzzle_input):
    reports = puzzle_input.split("\n")
    safe_count = 0
    for report in reports:
        cleaned_report = list(map(int, report.split()))
        if check_safety(cleaned_report):
            safe_count += 1
    return safe_count


def part2(puzzle_input):
    reports = puzzle_input.split("\n")
    safe_count = 0
    for report in reports:
        cleaned_report = list(map(int, report.split()))
        if check_safety(cleaned_report):
            safe_count += 1
        elif check_without_one_element(cleaned_report):
                safe_count += 1
    return safe_count


if __name__ == "__main__":
    day = 2
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
