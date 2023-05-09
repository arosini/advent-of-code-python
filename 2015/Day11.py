from util.Util import timeit


def is_valid_password(password):
    if any(char in "iol" for char in password): return False

    pair_index_set = set()
    last_char, last_last_char = None, None
    seq_of_3, two_pair = False, False

    for idx, c in enumerate(password):
        if last_char is not None:
            if not two_pair and last_char is c:
                pair_index_set.add(idx - 1)
                if max(pair_index_set) - min(pair_index_set) > 1: two_pair = True

            if not seq_of_3 and last_last_char is not None:
                if last_char == chr(ord(c) - 1) and last_last_char == chr(ord(c) - 2): seq_of_3 = True

            if two_pair and seq_of_3: break

        last_last_char = last_char
        last_char = c

    return two_pair and seq_of_3


def increment_password(password):
    idx_to_increment = len(password) - 1

    while idx_to_increment >= 0:
        char_to_increment = password[idx_to_increment]
        if char_to_increment == 'z':
            password = swap_character(password, idx_to_increment, 'a')
            idx_to_increment -= 1
        else:
            password = swap_character(password, idx_to_increment, chr(ord(char_to_increment) + 1))
            break

    return password


def swap_character(string, idx, char):
    return string[:idx] + char + string[idx + 1:]


@timeit
def part1():
    password = open('input/Day11.txt').read().strip()
    while not is_valid_password(password):
        password = increment_password(password)
    print(password)


@timeit
def part2():
    password = open('input/Day11.txt').read().strip()
    while not is_valid_password(password):
        password = increment_password(password)

    password = increment_password(password)
    while not is_valid_password(password):
        password = increment_password(password)
    print(password)


part1()
print()
part2()

