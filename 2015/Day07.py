from util.Util import timeit
from enum import Enum


class Gate(Enum):
    AND = "&"
    OR = "|"
    NOT = "^ 65535"
    LSHIFT = "<<"
    RSHIFT = ">>"


def calculate_instruction(wire, instructions):
    # Check if wire is actually a value. This happens for the second argument in the SHIFT operators.
    if wire.isnumeric():
        return_val = int(wire)
    # Check if instruction is just a numeric value.
    elif type(instructions[wire]) == int:
        return_val = int(instructions[wire])
    # Check if instruction points to another wire:
    elif " " not in instructions[wire]:
        return_val = calculate_instruction(instructions[wire], instructions)
    # Handle instruction with the NOT operator.
    elif instructions[wire].startswith(Gate.NOT.name):
        a = str(calculate_instruction(instructions[wire].split(" ")[1], instructions))
        return_val = eval(a + " " + Gate.NOT.value)
    # Handle instruction with all other operators.
    else:
        a, gate, b = instructions[wire].split(" ")
        return_val = eval(str(calculate_instruction(a, instructions))
                          + " " + Gate[gate].value + " "
                          + str(calculate_instruction(b, instructions)))

    instructions[wire] = return_val
    return return_val


@timeit
def part1():
    instructions = {}
    with open("input/Day07.txt") as file:
        lines = file.readlines()
        for line in lines:
            instruction, wire = line.split(" -> ")
            instructions[wire.strip("\n")] = instruction

    print(calculate_instruction("a", instructions))


@timeit
def part2():
    instructions = {}
    with open("input/Day07.txt") as file:
        lines = file.readlines()
        for line in lines:
            instruction, wire = line.split(" -> ")
            instructions[wire.strip("\n")] = instruction

    a_val = calculate_instruction("a", instructions.copy())
    instructions['b'] = a_val
    print(calculate_instruction("a", instructions.copy()))


part1()
print()
part2()

