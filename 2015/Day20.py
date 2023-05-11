from util.Util import timeit


def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result


# I originally tried with algo 2 outlined in https://www.reddit.com/r/adventofcode/comments/3xjpp2/comment/cy59zd9/.
# However, the numbers are big enough that n squared easy operations becomes problematic.
# This solution sums the factors of a given number (since only those elves will visit that house), and multiplies by 10.
# It also assumes the answer will be divisible by 10 (maybe only a good assumption for my input), and also only starts
# checking numbers greater than 50 times the target. This is because while I was figuring this out, I noticed
# most houses had sums of ~20 or ~30 times their house number. The largest I saw was ~40 times.
@timeit
def part1():
    target = int(open("input/Day20.txt").read().strip())

    for x in range(int(target/50), target):
        if x % 10 != 0: continue
        if sum(factors(x)) * 10 > target:
            print(x)
            break


# My first solution completely breaks down with the requirements for part two, so instead I implemented the
# "calculate the total for every house" solution, which seems naive at first, but actually works well here.
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

