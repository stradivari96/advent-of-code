from collections import defaultdict
from typing import NamedTuple


class Problem(NamedTuple):
    time: list[int]
    distance: list[int]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(
        time=_parse_ints(lines[0]),
        distance=_parse_ints(lines[1])
    )
    print(part_1(problem))
    print(part_2(problem))


def _parse_ints(line: str):
    line = line.split(":")[1]
    result = []
    i = 0
    n = ""
    while i < len(line):
        if line[i].isdigit():
            n += line[i]
        elif n:
            result.append(int(n))
            n = ""
        i += 1
    if n:
        result.append(int(n))
    return result


def part_1(problem: Problem):
    list_ways = []
    for time, distance in zip(problem.time, problem.distance):
        ways = 0
        for i in range(1, time):
            if i * (time-i) > distance:
                ways += 1
        list_ways.append(ways)
    result = 1
    for w in list_ways:
        result *= w
    return result


def part_2(problem: Problem):
    time = int("".join(str(t) for t in problem.time))
    distance = int("".join(str(d) for d in problem.distance))
    ways = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            ways += 1
        elif ways > 0:
            break
    return ways


if __name__ == "__main__":
    main()
