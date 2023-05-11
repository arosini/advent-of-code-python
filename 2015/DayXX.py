from util.Util import timeit


@timeit
def part1():
    with open("input/DayXX.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == "": continue


@timeit
def part2():
    print('part2')


part1()
print()
part2()

