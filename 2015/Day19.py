from util.Util import timeit
import re

@timeit
def part1():
    transformations = {}
    medicine_molecule = None

    with open("input/Day19.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == "": continue
            split_line = line.strip().split(" => ")
            if len(split_line) == 1: medicine_molecule = split_line[0]
            else: transformations.setdefault(split_line[0], set()).add(split_line[1])

    resulting_molecules = set()
    for idx, element in enumerate(medicine_molecule):
        for transformation in transformations.get(element, set()):
            resulting_molecules.add(medicine_molecule[:idx] + transformation + medicine_molecule[idx + 1:])

        if idx < len(medicine_molecule) - 1:
            element_2 = element + medicine_molecule[idx + 1]
            for transformation in transformations.get(element_2, set()):
                resulting_molecules.add(medicine_molecule[:idx] + transformation + medicine_molecule[idx + 2:])

    print(len(resulting_molecules))


@timeit
def part2():
    # This solution reverses both the input and transformation strings. It goes "backward" from the medicine molecule
    # to the starting molecule ('e'). This doesn't work for the general case but does work for how the inputs for this
    # puzzle were generated. See https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/.
    transformations = {}
    medicine_molecule = None
    target = 'e'

    with open("input/Day19.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == "": continue
            split_line = line.strip().split(" => ")

            if len(split_line) == 1: medicine_molecule = split_line[0][::-1]
            else: transformations[split_line[1][::-1]] = split_line[0][::-1]

    # Greedily replace the string with matching values from left to right (it was reversed).
    count = 0
    while medicine_molecule != target:
        medicine_molecule = re.sub('|'.join(transformations.keys()), lambda x: transformations[x.group()],
                                   medicine_molecule, 1)
        count += 1
    print(count)


part1()
print()
part2()


# Unfortunately BFS does not work, too many branches, not enough opportunity to prune.
# Good example of why understanding the input data is important.
@timeit
def part2_bfs_failed():
    transformations = {}
    medicine_molecule = None
    starting_molecule = 'e'

    with open("input/Day19.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == "": continue
            split_line = line.strip().split(" => ")
            if len(split_line) == 1:
                medicine_molecule = split_line[0]
            else:
                transformations.setdefault(split_line[0], set()).add(split_line[1])

    queue = [(starting_molecule, 0)]
    visited = set()
    nt_target_pairs = find_nt_pairs(medicine_molecule, transformations)
    depths = set()

    while True:
        molecule, depth = queue.pop(0)

        if molecule in visited: continue
        visited.add(molecule)

        if depth not in depths:
            depths.add(depth)
            print("Reached depth " + str(depth))

        # Check if the non-transformable pairs can ever match the non-transformable pairs of the target.
        if not compatible_nt_pairs(find_nt_pairs(molecule, transformations), nt_target_pairs): continue

        for idx, element in enumerate(molecule):
            # Pair of element transformations.
            if idx < len(molecule) - 1:
                element_pair = element + molecule[idx + 1]

                for transformation in transformations.get(element_pair, set()):
                    resulting_molecule = molecule[:idx] + transformation + molecule[idx + 2:]
                    if resulting_molecule == medicine_molecule:
                        print(depth + 1)
                        return
                    queue.append((resulting_molecule, depth + 1))

            # Single element transformations.
            for transformation in transformations.get(element, set()):
                resulting_molecule = molecule[:idx] + transformation + molecule[idx + 1:]
                if resulting_molecule == medicine_molecule:
                    print(depth + 1)
                    return
                queue.append((resulting_molecule, depth + 1))


def find_nt_pairs(medicine_molecule, transformations):
    nt_pairs = list()

    idx = 0
    for element in medicine_molecule:
        if idx > len(medicine_molecule) - 2: break

        element_pair = element + medicine_molecule[idx + 1]
        if all(key not in transformations.keys() for key in (element, element_pair[1], element_pair)):
            nt_pairs.append(element_pair)
            idx += 1

        idx += 1

    return nt_pairs


def compatible_nt_pairs(nt_pairs, nt_target_pairs):
    target_idx = 0

    for nt_pair in nt_pairs:
        found = False
        for i in range(target_idx, len(nt_target_pairs)):
            if nt_target_pairs[i] == nt_pair:
                found = True
                target_idx = i + 1
                break

        if not found: return False

    return True


# This DFS also failed due to not terminating.
def reverse_dfs(current, target, transformations, transform_count, visited):
    if current == target: return transform_count
    if current in visited: return None
    visited.add(current)

    for transformation in transformations:
        if transformation[1] not in current: continue
        next_molecule = current.replace(transformation[1], transformation[0], 1)
        next_transform_count = reverse_dfs(next_molecule, target, transformations,  transform_count + 1, visited)
        if next_transform_count is not None: return next_transform_count

    return None
