from enum import Enum
from util.Util import timeit


class Action(Enum):
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"


@timeit
def part1():
    grid_size = 1000
    lights = [[0] * grid_size for _ in range(grid_size)]

    with open("input/Day06.txt") as file:
        for line in file.readlines():
            for a in Action:
                if line.startswith(a.value):
                    action = a
                    line = line.removeprefix(a.value + ' ')
                    break

            start, stop = [tuple(map(int, s.split(","))) for s in line.split(" through ")]
            for x in range(start[0], stop[0] + 1):
                for y in range(start[1], stop[1] + 1):
                    match action:
                        case Action.TURN_ON:
                            lights[y][x] = 1
                        case Action.TURN_OFF:
                            lights[y][x] = 0
                        case Action.TOGGLE:
                            lights[y][x] = 1 - lights[y][x]
    total = 0
    for y in range(grid_size):
        for x in range(grid_size):
            total += lights[y][x]
    print(total)


@timeit
def part2():
    grid_size = 1000
    lights = [[0] * grid_size for _ in range(grid_size)]

    with open("input/Day06.txt") as file:
        for line in file.readlines():
            for a in Action:
                if line.startswith(a.value):
                    action = a
                    line = line.removeprefix(a.value + ' ')
                    break

            start, stop = [tuple(map(int, s.split(","))) for s in line.split(" through ")]
            for x in range(start[0], stop[0] + 1):
                for y in range(start[1], stop[1] + 1):
                    match action:
                        case Action.TURN_ON:
                            lights[y][x] += 1
                        case Action.TURN_OFF:
                            if lights[y][x] > 0: lights[y][x] -= 1
                        case Action.TOGGLE:
                            lights[y][x] += 2
    total = 0
    for y in range(grid_size):
        for x in range(grid_size):
            total += lights[y][x]
    print(total)


part1()
print()
part2()

