from util.Util import timeit


class Reinder:
    def __init__(self, name, speed, run_time, rest_time):
        self.name = name
        self.speed = speed
        self.run_time = run_time
        self.rest_time = rest_time
        self.run_time_remaining = run_time
        self.rest_time_remaining = 0
        self.distance = 0

    def advance_one_second(self):
        if self.run_time_remaining > 0:
            self.run_time_remaining -= 1
            self.distance += self.speed
            if self.run_time_remaining == 0: self.rest_time_remaining = self.rest_time
        elif self.rest_time_remaining > 0:
            self.rest_time_remaining -= 1
            if self.rest_time_remaining == 0: self.run_time_remaining = self.run_time
        else: assert False

    def __str__(self):
        return f"{self.name}: {self.distance}"

    def __repr__(self):
        return str(self)


@timeit
def part1():
    all_reindeer = list()
    with open("input/Day14.txt") as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.strip().split()
            all_reindeer.append(Reinder(tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[13])))

    for second in range(2503):
        for reindeer in all_reindeer: reindeer.advance_one_second()

    print(max(reindeer.distance for reindeer in all_reindeer))


@timeit
def part2():
    all_reindeer = {}
    with open("input/Day14.txt") as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.strip().split()
            all_reindeer[Reinder(tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[13]))] = 0

    for second in range(2503):
        for reindeer in all_reindeer: reindeer.advance_one_second()
        all_reindeer[max(all_reindeer, key=lambda r: r.distance)] += 1

    print(all_reindeer[max(all_reindeer, key=all_reindeer.get)])


part1()
print()
part2()

