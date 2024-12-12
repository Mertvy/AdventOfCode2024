from utils import get_input_lines


def trail_DFS(t_map, x, y, visit=False, visited=None):
    if visit:
        visited[y][x] = True
    height = t_map[y][x]
    if height == 9:
        return 1
    score = 0
    if y > 0 and t_map[y - 1][x] == height + 1 and (not visit or not visited[y - 1][x]):
        score += trail_DFS(t_map, x, y - 1, visit=visit, visited=visited)
    if x > 0 and t_map[y][x - 1] == height + 1 and (not visit or not visited[y][x - 1]):
        score += trail_DFS(t_map, x - 1, y, visit=visit, visited=visited)
    if y < len(t_map) - 1 and t_map[y + 1][x] == height + 1 and (not visit or not visited[y + 1][x]):
        score += trail_DFS(t_map, x, y + 1, visit=visit, visited=visited)
    if x < len(t_map[y]) - 1 and t_map[y][x + 1] == height + 1 and (not visit or not visited[y][x + 1]):
        score += trail_DFS(t_map, x + 1, y, visit=visit, visited=visited)
    return score


def part1(t_map):
    total = 0
    for y in range(len(t_map)):
        for x in range(len(t_map[0])):
            if t_map[y][x] == 0:
                visited = [[False for x in row] for row in t_map]
                total += trail_DFS(t_map, x, y, visit=True, visited=visited)
    return total


def part2(t_map):
    total = 0
    for y in range(len(t_map)):
        for x in range(len(t_map[0])):
            if t_map[y][x] == 0:
                total += trail_DFS(t_map, x, y)
    return total


topographic_map = [[int(c) for c in line] for line in get_input_lines("inputs/day10.txt")]
print(part1(topographic_map))
print(part2(topographic_map))
