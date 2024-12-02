from utils import getInputLines


def check_level(level):
    increasing = True if level[1] - level[0] > 0 else False
    safe = True
    for i in range(len(level) - 1):
        difference = level[i + 1] - level[i]
        if not increasing:
            difference *= -1
        if not 1 <= difference <= 3:
            safe = False
            break
    return safe


def part1(data):
    safe_levels = 0
    for level in data:
        if check_level(level):
            safe_levels += 1

    return safe_levels


def part2(data):
    safe_levels = 0
    for level in data:
        possible_levels = [level[:i] + level[i + 1:] for i in range(len(level))]
        for trial_level in possible_levels:
            if check_level(trial_level):
                safe_levels += 1
                break

    return safe_levels


lines = getInputLines("inputs/day2.txt")
input_data = [[int(num) for num in line.split()] for line in lines]

print(part1(input_data))
print(part2(input_data))
