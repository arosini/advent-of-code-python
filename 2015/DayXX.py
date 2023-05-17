from util.Util import timeit


def run(is_part_1):
    with open("input/DayXX.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == "": continue

    return str(is_part_1)


@timeit
def part1():
    print('part1: ' + str(run(True)))


@timeit
def part2():
    print('part2: ' + str(run(False)))


part1()
print()
part2()