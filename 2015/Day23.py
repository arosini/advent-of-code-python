from util.Util import timeit


def run(is_part_1):
    current_instruction = 0
    registers = {'a': (0 if is_part_1 else 1), 'b': 0}
    instructions = []
    with open("input/Day23.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == "": continue
            instructions.append(line.strip().replace(',', '').split())

    while current_instruction < len(instructions):
        instruction, *register = instructions[current_instruction]

        if instruction.startswith('j'):
            if instruction == 'jmp': current_instruction = eval(str(current_instruction) + str(register[0]))
            else:
                register, offset = register
                register_value = registers[register]

                if instruction == "jie" and register_value % 2 == 0:
                    current_instruction = eval(str(current_instruction) + offset)
                elif register_value == 1:
                    current_instruction = eval(str(current_instruction) + offset)
                else: current_instruction += 1

            continue

        register = register[0]
        register_value = registers[register]

        if instruction == 'hlf': registers[register] = register_value / 2
        elif instruction == 'tpl': registers[register] = register_value * 3
        elif instruction == 'inc': registers[register] = register_value + 1
        current_instruction += 1

    return registers['b']


@timeit
def part1():
    print('part1: ' + str(run(True)))


@timeit
def part2():
    print('part1: ' + str(run(False)))


part1()
print()
part2()

