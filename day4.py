from utils import getInputLines
from itertools import product


def check_xmas(grid, position):
    x, y = position
    if grid[y][x] != 'X':
        return 0
    total = 0
    for direction in product((-1, 0, 1), (-1, 0, 1)):
        x, y = position
        for i in range(len("XMAS")):
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
                break
            if grid[y][x] != "XMAS"[i]:
                break
            x += direction[0]
            y += direction[1]
        else:
            total += 1
    return total


def check_crossmas(grid, position):
    x, y = position
    if grid[y][x] != 'A':
        return 0
    diag1 = grid[y - 1][x - 1] + grid[y][x] + grid[y + 1][x + 1]
    diag2 = grid[y - 1][x + 1] + grid[y][x] + grid[y + 1][x - 1]
    if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
        return 1
    return 0


def part1(word_search):
    return sum(check_xmas(word_search, (x, y)) for y in range(len(word_search)) for x in range(len(word_search[y])))


def part2(word_search):
    return sum(check_crossmas(word_search, (x, y)) for y in range(1, len(word_search) - 1) for x in range(1, len(word_search[y]) - 1))


input_word_search = getInputLines("inputs/day4.txt")
print(part1(input_word_search))
print(part2(input_word_search))
