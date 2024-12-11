def stone_multiplication(number, blinks, memo):
    if blinks == 0:
        return 1
    if (number, blinks) in memo:
        return memo[(number, blinks)]
    if number == 0:
        val = stone_multiplication(1, blinks - 1, memo)
    elif len(str(number)) % 2 == 0:
        num_str = str(number)
        num1, num2 = int(num_str[:len(num_str) // 2]), int(num_str[len(num_str) // 2:])
        val = stone_multiplication(num1, blinks - 1, memo) + stone_multiplication(num2, blinks - 1, memo)
    else:
        val = stone_multiplication(number * 2024, blinks - 1, memo)
    memo[(number, blinks)] = val
    return val


def part1(stones):
    memo = {}
    return sum([stone_multiplication(stone, 25, memo) for stone in stones])


def part2(stones):
    memo = {}
    return sum([stone_multiplication(stone, 75, memo) for stone in stones])


input_stones = [int(stone) for stone in open("inputs/day11.txt").read().split()]
print(part1(input_stones))
print(part2(input_stones))
