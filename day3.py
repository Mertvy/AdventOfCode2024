from utils import getInputLines
import re


def part1(memory):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
    total = 0
    for match in matches:
        nums = [int(num) for num in match.split('(')[1][:-1].split(',')]
        total += nums[0] * nums[1]
    return total


def part2(memory):
    do_sections = re.split(r"don't\(\)[\s\S]*?(do\(\)|$)", memory)
    total = 0
    for do_section in do_sections:
        total += part1(do_section)
    return total


input_str = open("inputs/day3.txt", 'r').read()
print(part1(input_str))
print(part2(input_str))
