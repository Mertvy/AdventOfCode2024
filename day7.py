from utils import get_input_lines


def cint(n):
    if n == '':
        return 0
    return int(n)


def is_solvable(value, operands, index, concatenation):
    if index == 0:
        if operands[0] == value:
            return True
        return False
    if value >= operands[index] and is_solvable(value - operands[index], operands, index - 1, concatenation):
        return True
    if value % operands[index] == 0 and is_solvable(value // operands[index], operands, index - 1, concatenation):
        return True
    if concatenation and str(value)[-len(str(operands[index])):] == str(operands[index]) \
        and is_solvable(cint(str(value)[:-len(str(operands[index]))]), operands, index - 1, concatenation):
        return True
    return False


def part1(equations):
    return sum([equation[0] for equation in equations if is_solvable(equation[0], equation[1], len(equation[1]) - 1, False)])


def part2(equations):
    return sum([equation[0] for equation in equations if is_solvable(equation[0], equation[1], len(equation[1]) - 1, True)])


input_lines = get_input_lines("inputs/day7.txt")
equations = []
for line in input_lines:
    value, operands = line.split(': ')
    equations.append((int(value), [int(operand) for operand in operands.split()]))

print(part1(equations))
print(part2(equations))
