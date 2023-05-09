from util.Util import timeit


def calculate_max_happiness(seated_guests, to_seat, happiness_map):
    happiness = 0

    if len(to_seat) == 0:
        for idx, guest in enumerate(seated_guests):
            happiness += happiness_map[guest][seated_guests[idx - 1]]
            happiness += happiness_map[guest][seated_guests[(idx + 1) % len(seated_guests)]]
        return happiness

    for guest in to_seat:
        next_seated_guest = seated_guests + [guest]
        next_to_seat = to_seat.copy()
        next_to_seat.discard(guest)

        potential_happiness = calculate_max_happiness(next_seated_guest, next_to_seat, happiness_map)
        if potential_happiness > happiness: happiness = potential_happiness

    return happiness


@timeit
def part1():
    happiness_map = {}
    with open("input/Day13.txt") as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.strip()[:-1].split()
            a, b, multiplier = tokens[0], tokens[-1], 1 if tokens[2] == "gain" else -1
            happiness_map.setdefault(a, {})[b] = int(tokens[3]) * multiplier

    print(calculate_max_happiness(list(), set(happiness_map.keys()), happiness_map))


@timeit
def part2():
    happiness_map = {}
    with open("input/Day13.txt") as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.strip()[:-1].split()
            a, b, multiplier = tokens[0], tokens[-1], 1 if tokens[2] == "gain" else -1
            happiness_map.setdefault(a, {})[b] = int(tokens[3]) * multiplier

    me = 'Adam'
    for guest in set(happiness_map.keys()):
        happiness_map.setdefault(me, {})[guest] = 0
        happiness_map[guest][me] = 0

    print(calculate_max_happiness(list(), set(happiness_map.keys()), happiness_map))


part1()
print()
part2()

