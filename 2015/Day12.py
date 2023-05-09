from util.Util import timeit
import json


def count(json_or_value):
    input_type = type(json_or_value)

    if input_type == int: return json_or_value
    elif input_type == str: return 0
    elif input_type == bool: return 0
    elif input_type == dict: return sum(count(json_or_value[element]) for element in json_or_value)
    elif input_type == list: return sum(count(element) for element in json_or_value)
    else: assert False, f"Unhandled type {input_type}"


def count_ignore_red(json_or_value, parent_type):
    input_type = type(json_or_value)

    if input_type == int: return json_or_value
    elif input_type == str: return None if json_or_value == "red" and parent_type == dict else 0
    elif input_type == bool: return 0
    elif input_type == dict:
        dict_total = 0
        for element in json_or_value:
            element_total = count_ignore_red(json_or_value[element], input_type)
            if element_total is None: return 0
            dict_total += element_total
        return dict_total
    elif input_type == list: return sum(count_ignore_red(element, input_type) for element in json_or_value)
    else: assert False, f"Unhandled type {input_type}"


@timeit
def part1():
    total = 0
    with open("input/Day12.txt") as file:
        lines = file.readlines()
        for line in lines:
            total += count(json.loads(line))
        print(total)


@timeit
def part2():
    total = 0
    with open("input/Day12.txt") as file:
        lines = file.readlines()
        for line in lines:
            json_obj = json.loads(line)
            total += count_ignore_red(json_obj, type(json_obj))
        print(total)


part1()
print()
part2()

