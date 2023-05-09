from util.Util import timeit


def find_shortest_distance(route, remaining_cities, destinations):
    if len(remaining_cities) == 0:
        return 0

    current_city = None if len(route) == 0 else route[-1]
    shortest_distance = float('inf')

    for next_city in remaining_cities:
        if current_city is None: distance_to_next_city = 0
        else: distance_to_next_city = destinations.get(current_city, {}).get(next_city, None)

        if distance_to_next_city is None: continue

        next_route = route + [next_city]
        next_remaining_cities = remaining_cities.copy()
        next_remaining_cities.remove(next_city)

        distance = distance_to_next_city + find_shortest_distance(next_route, next_remaining_cities, destinations)

        if distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance


def find_longest_distance(route, remaining_cities, destinations):
    if len(remaining_cities) == 0:
        return 0

    current_city = None if len(route) == 0 else route[-1]
    longest_distance = 0

    for next_city in remaining_cities:
        if current_city is None: distance_to_next_city = 0
        else: distance_to_next_city = destinations.get(current_city, {}).get(next_city, None)

        if distance_to_next_city is None: continue

        next_route = route + [next_city]
        next_remaining_cities = remaining_cities.copy()
        next_remaining_cities.remove(next_city)

        distance = distance_to_next_city + find_longest_distance(next_route, next_remaining_cities, destinations)

        if distance > longest_distance:
            longest_distance = distance

    return longest_distance


@timeit
def part1():
    all_cities = set()
    destinations = dict()

    with open("input/Day09.txt") as file:
        lines = file.readlines()
        for line in lines:
            cities, distance = line.strip().split(" = ")
            a, b = cities.split(" to ")
            all_cities.add(a)
            all_cities.add(b)
            destinations.setdefault(a, {})[b] = int(distance)
            destinations.setdefault(b, {})[a] = int(distance)

    print(find_shortest_distance(list(), all_cities.copy(), destinations))


@timeit
def part2():
    all_cities = set()
    destinations = dict()

    with open("input/Day09.txt") as file:
        lines = file.readlines()
        for line in lines:
            cities, distance = line.strip().split(" = ")
            a, b = cities.split(" to ")
            all_cities.add(a)
            all_cities.add(b)
            destinations.setdefault(a, {})[b] = int(distance)
            destinations.setdefault(b, {})[a] = int(distance)

    print(find_longest_distance(list(), all_cities.copy(), destinations))


part1()
print()
part2()

