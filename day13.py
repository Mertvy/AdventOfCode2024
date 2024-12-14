from sympy import Matrix


def part1(machines, offset=0):
    total = 0
    for machine in machines:
        Ax, Ay = machine[0].split('+')[1:]
        Ax, Ay = int(Ax.split(',')[0]), int(Ay)
        Bx, By = machine[1].split('+')[1:]
        Bx, By = int(Bx.split(',')[0]), int(By)
        targetX, targetY = machine[2].split('=')[1:]
        targetX, targetY = int(targetX.split(',')[0]) + offset, int(targetY) + offset
        matrix = Matrix([[Ax, Bx, targetX], [Ay, By, targetY]]).rref()[0]
        if int(matrix.col(-1)[0]) != matrix.col(-1)[0] or int(matrix.col(-1)[1]) != matrix.col(-1)[1]:
            continue
        total += 3*matrix.row(0)[-1] + matrix.row(1)[-1]
    return total


def part2(machines):
    return part1(machines, offset=10000000000000)


input_machines = [s.split('\n') for s in open("inputs/day13.txt").read().split("\n\n")]
print(part1(input_machines))
print(part2(input_machines))
