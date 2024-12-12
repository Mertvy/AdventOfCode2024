from utils import get_input_lines


def part1(left_list, right_list):
    left_list.sort()
    right_list.sort()

    distances = [abs(left_list[i] - right_list[i]) for i in range(len(left_list))]
    return sum(distances)


def part2(left_list, right_list):
    right_list_dict = {}
    for id in right_list:
        if id not in right_list_dict:
            right_list_dict[id] = 0
        right_list_dict[id] += id

    similarity_score = 0
    for id in left_list:
        if id in right_list_dict:
            similarity_score += right_list_dict[id]
    return similarity_score


input_lines = get_input_lines("inputs/day1.txt")
left_list = []
right_list = []
for line in input_lines:
    left_list.append(int(line.split()[0]))
    right_list.append(int(line.split()[1]))

print(part1(left_list, right_list))
print(part2(left_list, right_list))
