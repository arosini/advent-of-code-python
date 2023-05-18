from util.Util import timeit
import re


@timeit
def part1():
    target_row, target_col = (int(n) - 1 for n in re.findall(r'\d+', open("input/Day25.txt").read().strip()))
    codes = list()
    codes.append(list())
    codes[0].append(20151125)

    q = [(1, 0), (0, 1)]
    y, x = 0, 0
    previous_val = codes[0][0]

    while len(codes) <= target_row or len(codes[target_row]) <= target_col or codes[target_row][target_col] == -1:
        next_code = q.pop(0)
        next_val = (previous_val * 252533) % 33554393

        while len(codes) <= next_code[0]: codes.append(list())

        codes[next_code[0]].append(next_val)
        previous_val = next_val

        if next_code[1] == 0:
            next_y = next_code[0] + 1
            next_x = 0
            while next_y >= 0:
                q.append((next_y, next_x))
                next_y -= 1
                next_x += 1

    print("part1: " + str(codes[target_row][target_col]))


part1()
