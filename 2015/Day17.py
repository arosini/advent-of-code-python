from util.Util import timeit


def find_combinations(current_containers, remaining_containers, total_liters, seen_states, solutions):
    state = frozenset(current_containers.keys()), frozenset(remaining_containers.keys())
    if state in seen_states: return
    seen_states.add(state)

    current_capacity = sum(current_containers.values())
    if current_capacity == total_liters: solutions.add(frozenset(current_containers.keys()))
    if current_capacity > total_liters: return

    for container_idx in remaining_containers:
        next_current_containers = current_containers.copy()
        next_current_containers[container_idx] = remaining_containers[container_idx]

        next_remaining_containers = remaining_containers.copy()
        next_remaining_containers.pop(container_idx)

        find_combinations(next_current_containers, next_remaining_containers, total_liters, seen_states, solutions)


@timeit
def part1():
    container_sizes = {}

    with open("input/Day17.txt") as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            container_sizes[idx] = int(line.strip())

    solutions = set()
    find_combinations({}, container_sizes.copy(), 150, set(), solutions)
    print(len(solutions))


@timeit
def part2():
    container_sizes = {}
    with open("input/Day17.txt") as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            container_sizes[idx] = int(line.strip())

    solutions = set()
    find_combinations({}, container_sizes.copy(), 150, set(), solutions)
    print(sum(1 for s in solutions if len(s) == min(len(s) for s in solutions)))


part1()
print()
part2()

