from utils import get_input_lines
import re


def part1(memory):
    return sum(int(a) * int(b) for a, b in (match.split('(')[1][:-1].split(',')
                                            for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)))


def part2(memory):
    return sum(part1(do_section) for do_section in re.split(r"don't\(\)[\s\S]*?(do\(\)|$)", memory))


input_str = open("inputs/day3.txt", 'r').read()
print(part1(input_str))
print(part2(input_str))
