from util.Util import timeit


def look_and_say(seed, iterations):
    output = ""
    last_char = seed[0]
    char_count = 1

    for c in seed[1:]:
        if last_char is c: char_count += 1
        else:
            output += str(char_count) + last_char
            last_char = c
            char_count = 1

    output += str(char_count) + last_char
    return output if iterations == 1 else look_and_say(output, iterations - 1)


@timeit
def part1():
    print(len(look_and_say(open('input/Day10.txt').read().strip(), 40)))


@timeit
def part2():
    print(len(look_and_say(open('input/Day10.txt').read().strip(), 50)))


part1()
print()
part2()

