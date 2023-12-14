import sys
from typing import NamedTuple
from itertools import combinations


sys.setrecursionlimit(100_000_000)


class Problem(NamedTuple):
    image: list[str]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(image=lines)
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):

    image_expanded = expand(problem.image)
    galaxies_pos = []
    for i, line in enumerate(image_expanded):
        for j, c in enumerate(line):
            if c == "#":
                galaxies_pos.append((i, j))

    dists = []
    for (x1, y1), (x2, y2) in combinations(galaxies_pos, 2):
        dists.append(abs(x1-x2)+abs(y1-y2))
    return sum(dists)


def expand(image: list[str]) -> list[str]:
    empty_rows = [i for i, row in enumerate(image) if all(c == "." for c in row)]
    empty_cols = [j for j in range(len(image[0])) if all(row[j] == "." for row in image)]

    result = []
    for i, row in enumerate(image):
        new_row = []
        for j, c in enumerate(row):
            new_row.append(c)
            if j in empty_cols:
                new_row.append(".")
        result.append("".join(new_row))
        if i in empty_rows:
            result.append("".join(new_row))
    return result


def part_2(problem: Problem):
    galaxies_pos = []
    for i, line in enumerate(problem.image):
        for j, c in enumerate(line):
            if c == "#":
                galaxies_pos.append((i, j))

    dists = []
    empty_rows = [i for i, row in enumerate(problem.image) if all(c == "." for c in row)]
    empty_cols = [j for j in range(len(problem.image[0])) if all(row[j] == "." for row in problem.image)]
    for (x1, y1), (x2, y2) in combinations(galaxies_pos, 2):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        dist = (x2 - x1) + (y2 - y1)
        for row in empty_rows:
            if x1 <= row <= x2:
                dist += 999_999
        for col in empty_cols:
            if y1 <= col <= y2:
                dist += 999_999
        dists.append(dist)
    return sum(dists)


if __name__ == "__main__":
    main()
