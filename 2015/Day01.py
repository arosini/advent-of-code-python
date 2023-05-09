from util.Util import timeit


@timeit
def part1():
    floor = 0
    with open('input/Day01.txt') as file:
        for c in file.read():
            floor += 1 if c == '(' else -1
    print(floor)


@timeit
def part2():
    floor = 0
    with open('input/Day01.txt') as file:
        for idx, c in enumerate(file.read()):
            floor += 1 if c == '(' else -1
            if floor == -1:
                print(idx + 1)
                break


part1()
print()
part2()
