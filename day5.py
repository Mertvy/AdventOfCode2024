from utils import get_input_lines


def slide(arr, old_index, new_index):
    cur_index = old_index
    while cur_index != new_index:
        tmp = arr[cur_index - 1]
        arr[cur_index - 1] = arr[cur_index]
        arr[cur_index] = tmp
        cur_index -= 1


def part1(page_orderings, production_queues):
    total = 0
    for queue in production_queues:
        printed_pages = set()
        for page in queue:
            after = page_orderings.get(page) if page in page_orderings else set()
            if len(after.intersection(printed_pages)) != 0:
                break
            printed_pages.add(page)
        else:
            total += queue[len(queue)//2]
    return total


def part2(page_orderings, production_queues):
    total = 0
    for queue in production_queues:
        incorrect_order = False
        printed_pages = set()
        for i, page in enumerate(queue):
            after = page_orderings.get(page) if page in page_orderings else set()
            wrong_indices = []
            for p in after:
                if p in printed_pages:
                    wrong_indices.append(queue.index(p))
            if len(wrong_indices) > 0:
                slide(queue, i, min(wrong_indices))
                incorrect_order = True
            printed_pages.add(page)
        if incorrect_order:
            total += queue[len(queue) // 2]
    return total


instructions = get_input_lines("inputs/day5.txt")
break_line = instructions.index("")
page_ordering_rules, input_production_queues = instructions[:break_line], instructions[break_line + 1:]
input_production_queues = [[int(page) for page in queue.split(',')] for queue in input_production_queues]
input_page_orderings = {}
for rule in page_ordering_rules:
    b, a = [int(page) for page in rule.split('|')]
    if b not in input_page_orderings:
        input_page_orderings[b] = set()
    input_page_orderings[b].add(a)

print(part1(input_page_orderings, input_production_queues))
print(part2(input_page_orderings, input_production_queues))
