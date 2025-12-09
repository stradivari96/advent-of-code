import itertools
import typing

class Problem(typing.NamedTuple):
    tiles: list[tuple[int, int]]

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(tiles=[
        tuple(int(x) for x in line.split(','))
        for line in lines
    ])
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    largest_area = 0
    for (x1, y1), (x2, y2) in itertools.combinations(problem.tiles, 2):
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > largest_area:
            largest_area = area
    return largest_area


def part_2(problem: Problem):
    ...


if __name__ == "__main__":
    main()
