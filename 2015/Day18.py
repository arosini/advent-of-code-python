from util.Util import timeit


ON = "#"
OFF = "."


def print_lights(lights):
    for row in lights:
        for char in row:
            print(char, end="")
        print()
    print()


def calculate_next(y, x, lights, always_on):
    if (y, x) in always_on: return ON

    neighbors_on = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0: continue

            ny = y + dy
            nx = x + dx

            if (ny, nx) in always_on: neighbors_on += 1
            elif ny < 0 or ny >= len(lights): continue;
            elif nx < 0 or nx >= len(lights[y]): continue;
            elif lights[ny][nx] == ON: neighbors_on += 1

    if lights[y][x] == ON: return ON if neighbors_on in (2, 3) else OFF
    else: return ON if neighbors_on == 3 else OFF


def calculate_lights_on(grid_size, iterations, always_on):
    lights = [[OFF] * grid_size for _ in range(grid_size)]

    with open("input/Day18.txt") as file:
        lines = file.readlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                lights[y][x] = char

    # print_lights(lights)
    for _ in range(iterations):
        next_lights = [[OFF] * grid_size for _ in range(grid_size)]
        for y in range(grid_size):
            for x in range(grid_size):
                next_lights[y][x] = calculate_next(y, x, lights, always_on)
        lights = next_lights
        # print_lights(lights)

    lights_on = 0
    for y in range(grid_size):
        for x in range(grid_size):
            if lights[y][x] == ON: lights_on += 1
    print(lights_on)


@timeit
def part1():
    calculate_lights_on(100, 100, {})


@timeit
def part2():
    grid_size = 99
    calculate_lights_on(grid_size + 1, 100, {(0, 0), (0, grid_size), (grid_size, 0), (grid_size, grid_size)})


part1()
print()
part2()

