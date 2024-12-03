from utils import getInputLines
import re


def part1(memory):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
    return sum(int(a) * int(b) for a, b in (match.split('(')[1][:-1].split(',') for match in matches))


def part2(memory):
    do_sections = re.split(r"don't\(\)[\s\S]*?(do\(\)|$)", memory)
    return sum(part1(do_section) for do_section in do_sections)


input_str = open("inputs/day3.txt", 'r').read()
print(part1(input_str))
print(part2(input_str))
