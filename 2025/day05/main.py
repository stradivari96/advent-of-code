import typing
import functools
import math

class Range(typing.NamedTuple):
    low: int
    high: int

class Problem(typing.NamedTuple):
    ranges: list[Range]
    ingredients: list[int]

def main():
    with open("data.txt") as f:
        lines = f.read().split('\n\n')
    problem = Problem(
        ranges=[
            Range(low=int(line.split('-')[0]), high=int(line.split('-')[1]))
            for line in lines[0].splitlines()
        ],
        ingredients=[int(x) for x in lines[1].splitlines()],
    )
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    result = 0
    for ingredient in problem.ingredients:
        for r in problem.ranges:
            if r.low <= ingredient <= r.high:
                result += 1
                break
    return result


def part_2(problem: Problem):
    merged_ranges = []
    for r in sorted(problem.ranges, key=lambda x: x.low):
        if not merged_ranges or merged_ranges[-1].high < r.low:
            merged_ranges.append(r)
        else:
            merged_ranges[-1] = Range(
                low=merged_ranges[-1].low,
                high=max(merged_ranges[-1].high, r.high),
            )
    result = 0
    for range in merged_ranges:
        result += range.high - range.low + 1
    return result


if __name__ == "__main__":
    main()
