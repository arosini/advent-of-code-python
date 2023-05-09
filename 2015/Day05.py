from util.Util import timeit


@timeit
def part1():
    nice_string_count = 0
    with open("input/Day05.txt") as file:
        for line in file.readlines():
            vowel_count = 0
            twice_in_a_row = False
            naughty_substring = False
            last_char = None

            for c in line:
                if c in ["a", "e", "i", "o", "u"]: vowel_count += 1
                if last_char is not None:
                    if last_char is c: twice_in_a_row = True
                    if last_char + c in ["ab", "cd", "pq", "xy"]:
                        naughty_substring = True
                        break
                last_char = c

            if vowel_count >= 3 and twice_in_a_row and not naughty_substring:
                nice_string_count += 1
    print(nice_string_count)


@timeit
def part2():
    nice_string_count = 0
    with open("input/Day05.txt") as file:
        for line in file.readlines():
            pair_map = {}
            last_char = None
            last_last_char = None
            one_letter_between_repeat = False
            two_pair = False

            for idx, c in enumerate(line):
                if last_char is not None:
                    if not two_pair:
                        pair = last_char + c
                        pair_index_set = pair_map.setdefault(pair, set())
                        pair_index_set.add(idx - 1)
                        if max(pair_index_set) - min(pair_index_set) > 1: two_pair = True

                    if not one_letter_between_repeat:
                        if last_last_char == c: one_letter_between_repeat = True

                    if two_pair and one_letter_between_repeat:
                        nice_string_count += 1
                        break

                last_last_char = last_char
                last_char = c

    print(nice_string_count)


part1()
print()
part2()
