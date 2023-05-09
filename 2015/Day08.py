from util.Util import timeit


def count_characters(line):
    characters_of_code = 0
    characters_in_memory = 0
    characters_to_skip = 0

    for idx, c in enumerate(line):
        # If we already counted this escaped character, continue.
        if characters_to_skip > 0:
            characters_to_skip -= 1
            continue

        # If we are at the ending or closing quote, it is only a character in code.
        if idx == 0 or idx == len(line) - 1:
            characters_of_code += 1
        # Encountering an escape sequence.
        elif c == "\\":
            # A hex escape.
            if line[idx + 1] == 'x':
                characters_of_code += 4
                characters_in_memory += 1
                characters_to_skip = 3
            # A single character escape. We want to skip the next character to handle escaping \ itself.
            else:
                characters_of_code += 2
                characters_in_memory += 1
                characters_to_skip = 1
        # A regular old unescaped character.
        else:
            characters_of_code += 1
            characters_in_memory += 1

    return characters_of_code, characters_in_memory

@timeit
def part1():
    characters_of_code = 0
    characters_in_memory = 0

    with open("input/Day08.txt") as file:
        lines = file.readlines()
        for line in lines:
            counts = count_characters(line.strip())
            characters_of_code += counts[0]
            characters_in_memory += counts[1]

    print(characters_of_code - characters_in_memory)


@timeit
def part2():
    characters_of_code = 0
    encoded_characters_of_code = 0

    with open("input/Day08.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            encoded_line = "\"\\\"" + line.replace("\\", "\\\\")[1:-1].replace('"', "\\\"") + "\\\"\""

            characters_of_code += count_characters(line)[0]
            encoded_characters_of_code += count_characters(encoded_line)[0]

    print(encoded_characters_of_code - characters_of_code)


part1()
print()
part2()

