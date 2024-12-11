from functools import cache


@cache
def stone_multiplication(number, blinks):
    if blinks == 0:
        return 1
    if number == 0:
        return stone_multiplication(1, blinks - 1)
    elif len(str(number)) % 2 == 0:
        num_str = str(number)
        num1, num2 = int(num_str[:len(num_str) // 2]), int(num_str[len(num_str) // 2:])
        return stone_multiplication(num1, blinks - 1) + stone_multiplication(num2, blinks - 1)
    else:
        return stone_multiplication(number * 2024, blinks - 1)


def part1(stones):
    return sum([stone_multiplication(stone, 25) for stone in stones])


def part2(stones):
    return sum([stone_multiplication(stone, 75) for stone in stones])


input_stones = [int(stone) for stone in open("inputs/day11.txt").read().split()]
print(part1(input_stones))
print(part2(input_stones))
