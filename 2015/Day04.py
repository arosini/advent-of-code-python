import hashlib
from util.Util import timeit


def find_has_with_leading_string(leading_string):
    with open("input/Day04.txt") as file: secret_key = file.read()
    x = 0
    hash_value = "0"

    while not hash_value.startswith(leading_string):
        x += 1
        hash_value = hashlib.md5((secret_key + str(x)).encode('utf-8')).hexdigest()
    print(x)


@timeit
def part1():
    find_has_with_leading_string("00000")


@timeit
def part2():
    find_has_with_leading_string("000000")


part1()
print()
part2()
