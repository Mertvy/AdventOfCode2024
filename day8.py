from utils import get_input_lines
from math import gcd


def part1(antennas, anti_nodes):
    for frequency in antennas:
        for antenna1 in antennas[frequency]:
            x1, y1 = antenna1
            for antenna2 in antennas[frequency]:
                if antenna1 == antenna2:
                    continue
                x2, y2 = antenna2
                dx, dy = x2 - x1, y2 - y1
                anti_node1, anti_node2 = (x2 + dx, y2 + dy), (x1 - dx, y1 - dy)
                if 0 <= anti_node1[0] < len(anti_nodes[0]) and 0 <= anti_node1[1] < len(anti_nodes):
                    anti_nodes[anti_node1[0]][anti_node1[1]] = True
                if 0 <= anti_node2[0] < len(anti_nodes[0]) and 0 <= anti_node2[1] < len(anti_nodes):
                    anti_nodes[anti_node2[0]][anti_node2[1]] = True
    return sum(sum([1 if cell else 0 for cell in row]) for row in anti_nodes)


def part2(antennas, anti_nodes):
    for frequency in antennas:
        for antenna1 in antennas[frequency]:
            x1, y1 = antenna1
            for antenna2 in antennas[frequency]:
                if antenna1 == antenna2:
                    continue
                x2, y2 = antenna2
                dx, dy = (x2 - x1), (y2 - y1)
                gcf = gcd(x2 - x1, y2 - y1)
                if gcf > 0:
                    dx, dy = dx // gcf, dy // gcf
                cur_x, cur_y = x1, y1
                while 0 <= cur_x < len(anti_nodes[0]) and 0 <= cur_y < len(anti_nodes):
                    anti_nodes[cur_y][cur_x] = True
                    cur_x, cur_y = cur_x + dx, cur_y + dy
                cur_x, cur_y = x1, y1
                while 0 <= cur_x < len(anti_nodes[0]) and 0 <= cur_y < len(anti_nodes):
                    anti_nodes[cur_y][cur_x] = True
                    cur_x, cur_y = cur_x - dx, cur_y - dy
    return sum(sum([1 if cell else 0 for cell in row]) for row in anti_nodes)


input_grid = [list(line) for line in get_input_lines("inputs/day8.txt")]
antenna_dict = {}
for row in range(len(input_grid)):
    for col in range(len(input_grid[row])):
        if input_grid[row][col] == '.':
            continue
        if input_grid[row][col] not in antenna_dict:
            antenna_dict[input_grid[row][col]] = set()
        antenna_dict[input_grid[row][col]].add((col, row))
print(part1(antenna_dict, [[False for col in range(len(input_grid[row]))] for row in range(len(input_grid))]))
print(part2(antenna_dict, [[False for col in range(len(input_grid[row]))] for row in range(len(input_grid))]))
