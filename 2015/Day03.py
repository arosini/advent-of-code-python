from util.Util import timeit


class Direction:
    NORTH = (0, 1)
    SOUTH = (0, -1)
    EAST = (1, 0)
    WEST = (-1, 0)


def find_direction_for_char(c):
    match c:
        case '^':
            return Direction.NORTH
        case 'v':
            return Direction.SOUTH
        case '>':
            return Direction.EAST
        case '<':
            return Direction.WEST


@timeit
def part1():
    location = (0, 0)
    visited_coordinates = set()

    with open('input/Day03.txt') as file:
        for c in file.read():
            direction = find_direction_for_char(c)
            location = ((location[0] + direction[0]),  (location[1] + direction[1]))
            visited_coordinates.add(location)
    print(len(visited_coordinates))


@timeit
def part2():
    location, robo_location = (0, 0), (0, 0)
    visited_coordinates = set()

    with open('input/Day03.txt') as file:
        for idx, c in enumerate(file.read()):
            is_for_robo = idx % 2 == 0
            direction = find_direction_for_char(c)

            if is_for_robo:
                robo_location = ((robo_location[0] + direction[0]),  (robo_location[1] + direction[1]))
                visited_coordinates.add(robo_location)
            else:
                location = ((location[0] + direction[0]), (location[1] + direction[1]))
                visited_coordinates.add(location)

    print(len(visited_coordinates))


part1()
print()
part2()
