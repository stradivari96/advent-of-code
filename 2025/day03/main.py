import typing
import functools
import math

class Batteries(typing.NamedTuple):
    joltage: list[int]


class Problem(typing.NamedTuple):
    batteries: list[Batteries]

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(
        batteries=[
            Batteries(joltage=[int(x) for x in line])
            for line in lines
        ]
    )
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    result = 0
    for b in problem.batteries:
        max_joltage = 0
        for i in range(len(b.joltage)):
            for j in range(i + 1, len(b.joltage)):
                max_joltage = max(max_joltage, b.joltage[i]*10 + b.joltage[j])
        result += max_joltage
    return result


def part_2(problem: Problem):
    total = 0
    for b in problem.batteries:
        result = dp(tuple(b.joltage), 12)
        total += result
    return total


@functools.lru_cache(maxsize=None)
def dp(joltages: tuple[int], available: int):
    if available == 0 or not joltages:
        return -math.inf
    if available == 1:
        return max(joltages)
    return max(
        joltages[i]*10**(available - 1) + dp(joltages[i+1:], available - 1)
        for i in range(len(joltages))
    )


if __name__ == "__main__":
    main()
