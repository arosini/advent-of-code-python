from util.Util import timeit


def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

@timeit
def part1():
    target = int(open("input/Day20.txt").read().strip())

    for x in range(int(target/50), target):
        if x % 10 != 0: continue
        if sum(factors(x)) * 10 > target:
            print(x)
            break

@timeit
def part2():
    target = int(open("input/Day20.txt").read().strip())

    houses = [0] * int(target / 11) + [0]

    for elf in range(1, len(houses)):
        houses_hit = 0
        for house in range(elf, len(houses), elf):
            houses[house] += elf * 11
            houses_hit += 1
            if houses_hit > 50: break

    for house, count in enumerate(houses):
        if count > target:
            print(house)
            break


part1()
print()
part2()

