from util.Util import timeit


@timeit
def part1():
    total = 0
    with open('input/Day02.txt') as file:
        for line in file:
            line.replace('\n', '')
            dimensions = [int(n) for n in line.split('x')]
            l, w, h = dimensions
            total += 2*l*w + 2*w*h + 2*h*l

            dimensions.sort()
            total += dimensions[0] * dimensions[1]
    print(total)


@timeit
def part2():
    total = 0
    with open('input/Day02.txt') as file:
        for line in file:
            line.replace('\n', '')
            dimensions = [int(n) for n in line.split('x')]
            l, w, h = dimensions
            total += l*w*h

            dimensions.sort()
            total += (dimensions[0] * 2) + (dimensions[1] * 2)
    print(total)


part1()
print()
part2()
