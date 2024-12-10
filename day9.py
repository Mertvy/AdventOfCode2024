from collections import deque


def generate_filesystem(disk_map):
    file_system = []
    for i in range(0, len(disk_map), 2):
        file_system += [i // 2] * disk_map[i]
        if i + 1 < len(disk_map):
            file_system += ['.'] * disk_map[i + 1]
    return file_system

def part1(file_system):
    p1, p2, total = 0, len(file_system) - 1, 0
    while p1 <= p2:
        if file_system[p1] != '.':
            total += file_system[p1] * p1
        else:
            total += file_system[p2] * p1
            p2 -= 1
            while file_system[p2] == '.':
                p2 -= 1
        p1 += 1
    return total


def part2(file_system):
    moved_IDs = set()
    p = len(file_system) - 1
    while file_system[p] == '.':
        p -= 1
    while p > 0:
        cur_ID = file_system[p]
        file_size = 0
        moved_IDs.add(cur_ID)
        while file_system[p] == cur_ID:
            file_size += 1
            p -= 1
        j = 0
        for i in range(p + 1):
            i = max(i, j)
            if file_system[i] == '.':
                j = i
                free_space = 0
                while file_system[j] == '.' and free_space < file_size:
                    free_space += 1
                    j += 1
                if free_space < file_size:
                    continue
                for n in range(file_size):
                    file_system[i + n] = cur_ID
                    file_system[p + n + 1] = '.'
                break
        while p >= 0 and (file_system[p] == '.' or file_system[p] in moved_IDs):
            p -= 1
    return sum([i * file_system[i] if file_system[i] != '.' else 0 for i in range(len(file_system))])


input_file_system = generate_filesystem([int(i) for i in open("inputs/day9.txt").read()])
print(part1(input_file_system))
print(part2(input_file_system))
