from util.Util import timeit
from math import prod


def is_better_compartment(a, b):
    return a == get_better_compartment(a, b)


def get_better_compartment(a, b):
    if b is None: return a
    if a is None: return b
    if a == b: return a

    if len(a) < len(b): return a
    if len(b) < len(a): return b

    return min((a, b), key=prod)


# Returns true if a compartment can be made of the target weight from the given packages.
def find_any(compartment, packages, target_weight):
    if sum(compartment) == target_weight: return True

    for package in packages:
        compartment_copy = compartment.copy()
        compartment_copy.add(package)

        if sum(compartment_copy) > target_weight: continue

        packages_copy = packages.copy()
        packages_copy.remove(package)

        if find_any(compartment_copy, packages_copy, target_weight): return True

    return False


# Searches for the compartment with the lowest number of packages possible, preferring lower quantum entaglement
# to break ties.
def search(compartment, packages, target_weight):
    global best_compartment

    # If we found an answer, check if it's better than our best compartment. If it is, check that the remaining packages
    # can be divided evenly by weight. If both of those are true, this is the new best compartment.
    # Either way, return the best compartment.
    if sum(compartment) == target_weight:
        if is_better_compartment(compartment, best_compartment):
            if find_any(set(), packages, target_weight): best_compartment = compartment
        return best_compartment

    # Exit early if we have already seen this state.
    # NB: The input does not have duplicates, so we don't need to save the remaining packages. We could add that
    # to the state if we wanted to, though empirically that slows this down by about 4x.
    if frozenset(compartment) in seen_states: return best_compartment

    # Exit early if this configuration is already worse than our current best configuration.
    if not is_better_compartment(compartment, best_compartment):
        return best_compartment

    # Try adding each package to the compartment in a recursive fashion.
    for package in packages:
        # Copy the data structures so we don't mess with them when modifying them.
        compartment_copy = compartment.copy()
        compartment_copy.add(package)

        packages_copy = packages.copy()
        packages_copy.remove(package)

        # If the package puts us over the target weight, skip it.
        if sum(compartment_copy) > target_weight: continue

        #  Perform the search. THe best_compartment will get set by it.
        search(compartment_copy, packages_copy, target_weight)

        # Add the current state to known states so we can exit early if we get here again.
        seen_states.add(frozenset(compartment))

    return best_compartment


def run(is_part_1):
    global best_compartment
    global seen_states

    best_compartment = None
    seen_states = set()

    packages = list()
    with open("input/Day24.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == "": continue
            packages.append(int(line.strip()))

    total_weight = sum(packages)
    packages.reverse()

    compartment = search(set(), packages, total_weight / (3 if is_part_1 else 4))
    return prod(compartment)


best_compartment = None
seen_states = set()


@timeit
def part1():
    print('part1: ' + str(run(True)))


@timeit
def part2():
    print('part2: ' + str(run(False)))


part1()
print()
part2()
