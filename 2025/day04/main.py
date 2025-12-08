import typing
import functools
import math


class Problem(typing.NamedTuple):
    grid: dict[tuple[int, int], str]
    rows: int
    cols: int

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(
        grid={
            (i, j): lines[i][j]
            for i in range(len(lines))
            for j in range(len(lines[0]))
        },
        rows=len(lines),
        cols=len(lines[0])
    )
    print(part_1(problem)[0])
    print(part_2(problem))


def part_1(problem: Problem):
    result = 0
    positions = set()
    for i in range(problem.rows):
        for j in range(problem.cols):
            if problem.grid[i, j] == '.':
                continue
            neighbors = [
                (i-1, j), (i+1, j),
                (i, j-1), (i, j+1),
                (i-1, j-1), (i-1, j+1),
                (i+1, j-1), (i+1, j+1),
            ]
            adjacent_rolls = sum(
                1 for ni, nj in neighbors
                if problem.grid.get((ni, nj)) == '@'
            )
            if adjacent_rolls < 4:
                result += 1
                positions.add((i, j))
    return result, positions


def part_2(problem: Problem):
    result = 0
    while True:
        removed, positions = part_1(problem)
        if removed == 0:
            break
        result += removed
        for pos in positions:
            problem.grid[pos] = '.'
    return result


if __name__ == "__main__":
    main()
