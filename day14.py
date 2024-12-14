from utils import get_input_lines
from numpy import var
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def update_second(x, y, vel, width, height):
    return (x + vel[0]) % width, (y + vel[1]) % height


def update(x, y, vel, width, height, seconds):
    for i in range(seconds):
        x, y = update_second(x, y, vel, width, height)
    return x, y


def part1(robot_data, width, height):
    quad1, quad2, quad3, quad4 = 0, 0, 0, 0
    for line in robot_data:
        x, y = [int(n) for n in line.split(' ')[0].split('=')[1].split(',')]
        vel = [int(n) for n in line.split(' ')[1].split('=')[1].split(',')]
        x, y = update(x, y, vel, width, height, 100)
        if x < width // 2 and y < height // 2:
            quad1 += 1
        elif x > width // 2 and y < height // 2:
            quad2 += 1
        elif x < width // 2 and y > height // 2:
            quad3 += 1
        elif x > width // 2 and y > height // 2:
            quad4 += 1
    return quad1 * quad2 * quad3 * quad4


def part2(robot_data, width, height):
    out = open("out.txt", 'a')
    robots = []
    for line in robot_data:
        x, y = [int(n) for n in line.split(' ')[0].split('=')[1].split(',')]
        vel = [int(n) for n in line.split(' ')[1].split('=')[1].split(',')]
        robots.append([(x, y), vel])
    for i in range(100001):
        print(i)
        if i % 10403 == 6620:
            out.write(f"Step {i}:\n")
            floor = [[' ' for i in range(width)] for j in range(height)]
            for robot in robots:
                (x, y), vel = robot[0], robot[1]
                floor[y][x] = '█'
                robot[0] = update_second(x, y, vel, width, height)
            for row in floor:
                out.write(''.join(row) + '\n')
        else:
            for robot in robots:
                (x, y), vel = robot[0], robot[1]
                robot[0] = update_second(x, y, vel, width, height)




def variances(robot_data, width, height):
    robots = []
    for line in robot_data:
        x, y = [int(n) for n in line.split(' ')[0].split('=')[1].split(',')]
        vel = [int(n) for n in line.split(' ')[1].split('=')[1].split(',')]
        robots.append([(x, y), vel])
    steps, varX, varY = [], [], []
    for i in range(100):
        xs, ys = [], []
        for robot in robots:
            (x, y), vel = robot[0], robot[1]
            robot[0] = update_second(x, y, vel, width, height)
            xs.append(x)
            ys.append(y)
        steps.append(i)
        varX.append(var(xs))
        varY.append(var(ys))
    plt.figure()
    plt.plot(steps, varX, label="varX")
    plt.plot(steps, varY, label="varY")
    plt.legend()
    plt.show()


input_lines = get_input_lines("inputs/day14.txt")
print(part1(input_lines, 101, 103))
# variances(input_lines, 101, 103)
part2(input_lines, 101, 103)
