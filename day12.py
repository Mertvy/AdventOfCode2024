from utils import get_input_lines


def region_area_perimeter(garden, visited, row, col):
    if visited[row][col]:
        return 0, 0
    visited[row][col] = True
    plant = garden[row][col]
    area, perimeter = 1, 4
    if row > 0 and garden[row - 1][col] == plant:
        a, p = region_area_perimeter(garden, visited, row - 1, col)
        area += a
        perimeter += p - 1
    if row < len(garden) - 1 and garden[row + 1][col] == plant:
        a, p = region_area_perimeter(garden, visited, row + 1, col)
        area += a
        perimeter += p - 1
    if col > 0 and garden[row][col - 1] == plant:
        a, p = region_area_perimeter(garden, visited, row, col - 1)
        area += a
        perimeter += p - 1
    if col < len(garden[row]) - 1 and garden[row][col + 1] == plant:
        a, p = region_area_perimeter(garden, visited, row, col + 1)
        area += a
        perimeter += p - 1
    return area, perimeter


def region_area_norms(garden, visited, norms, row, col):
    if visited[row][col]:
        return 0
    visited[row][col] = True
    plant = garden[row][col]
    area = 1
    if row > 0 and garden[row - 1][col] == plant:
        area += region_area_norms(garden, visited, norms, row - 1, col)
    else:
        norms[(-1, 0)][row].append(col)
    if row < len(garden) - 1 and garden[row + 1][col] == plant:
        area += region_area_norms(garden, visited, norms, row + 1, col)
    else:
        norms[(1, 0)][row].append(col)
    if col > 0 and garden[row][col - 1] == plant:
        area += region_area_norms(garden, visited, norms, row, col - 1)
    else:
        norms[(0, -1)][col].append(row)
    if col < len(garden[row]) - 1 and garden[row][col + 1] == plant:
        area += region_area_norms(garden, visited, norms, row, col + 1)
    else:
        norms[(0, 1)][col].append(row)
    return area


def sides_from_norms(norms):
    def non_contiguousness(l):
        if not l:
            return 0
        t = 1
        for i in range(1, len(l)):
            if l[i] != l[i - 1] + 1:
                t += 1
        return t
    total = 0
    for direction in norms:
        for index in norms[direction]:
            norms[direction][index].sort()
            total += non_contiguousness(norms[direction][index])
    return total


def part1(garden):
    visited = [[False for plant in row] for row in garden]
    total = 0
    for row in range(len(garden)):
        for col in range(len(garden[row])):
            area, perimeter = region_area_perimeter(garden, visited, row, col)
            total += area * perimeter
    return total


def part2(garden):
    visited = [[False for plant in row] for row in garden]
    total = 0
    for row in range(len(garden)):
        for col in range(len(garden[row])):
            norms = {
                (-1, 0): {r: [] for r in range(len(garden))},
                (1, 0): {r: [] for r in range(len(garden))},
                (0, -1): {c: [] for c in range(len(garden[row]))},
                (0, 1): {c: [] for c in range(len(garden[row]))}
            }
            area = region_area_norms(garden, visited, norms, row, col)
            total += area * sides_from_norms(norms)
    return total


input_garden = get_input_lines("inputs/day12.txt")
print(part1(input_garden))
print(part2(input_garden))
