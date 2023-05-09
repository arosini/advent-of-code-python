from util.Util import timeit

MFCSAM_OUTPUT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


MFCSAM_LOWER_THRESHOLD_PROPERTIES = {"cats", "trees"}
MFCSAM_HIGHER_THRESHOLD_PROPERTIES = {"pomeranians", "goldfish"}


def matches_mfcsam_output(item):
    property_name = item[0]
    property_value = item[1]
    mfcsam_output_value = MFCSAM_OUTPUT[property_name]

    if property_name in MFCSAM_LOWER_THRESHOLD_PROPERTIES: return property_value > mfcsam_output_value
    elif property_name in MFCSAM_HIGHER_THRESHOLD_PROPERTIES: return property_value < mfcsam_output_value
    else: return property_value == mfcsam_output_value


@timeit
def part1():
    with open("input/Day16.txt") as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            str_properties_list = line[line.index(":") + 1:].strip().split(", ")
            sue_properties = {k: int(v) for k, v in [i.split(': ') for i in str_properties_list]}
            if all(item in MFCSAM_OUTPUT.items() for item in sue_properties.items()):
                print(idx + 1)
                break


@timeit
def part2():
    with open("input/Day16.txt") as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            str_properties_list = line[line.index(":") + 1:].strip().split(", ")
            sue_properties = {k: int(v) for k, v in [i.split(': ') for i in str_properties_list]}
            if all(matches_mfcsam_output(item) for item in sue_properties.items()):
                print(idx + 1)
                break


part1()
print()
part2()

