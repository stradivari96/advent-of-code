import sys
from typing import NamedTuple

from matplotlib.path import Path


sys.setrecursionlimit(100_000_000)


class Problem(NamedTuple):
    tiles: list[str]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(tiles=lines)
    loop = part_1(problem)
    print(part_2(problem, loop))


def part_1(problem: Problem):
    tiles = problem.tiles
    start = find_start(tiles)
    nrows = len(tiles)
    ncols = len(tiles[0])
    seen = []
    def dfs(i, j):
        for x, y in neighbours(i, j, tiles):
            newi, newj = i+x, j+y
            if newi < 0 or newi >= nrows:
                continue
            if newj < 0 or newj >= ncols:
                continue
            if tiles[newi][newj] == "S" and len(seen) > 1:
                seen.append((i, j))
                return 1
            if (newi, newj) in seen:
                continue
            if x == 1 and tiles[newi][newj] not in "|LJ":
                continue
            if x == -1 and tiles[newi][newj] not in "|7F":
                continue
            if y == 1 and tiles[newi][newj] not in "-J7":
                continue
            if y == -1 and tiles[newi][newj] not in "-LF":
                continue
            seen.append((i, j))
            return 1 + dfs(newi, newj)
        raise Exception(f"Error {i} {j}")
    print(dfs(start[0], start[1]) // 2)
    return seen


def neighbours(i, j, tiles):
    if tiles[i][j] == "S":
        return [(0, 1), (1, 0), (-1, 0), (0, -1)]
    if tiles[i][j] == "|":
        return [(-1, 0), (1, 0)]
    if tiles[i][j] == "-":
        return [(0, 1), (0, -1)]
    if tiles[i][j] == "L":
        return [(-1, 0), (0, 1)]
    if tiles[i][j] == "7":
        return [(1, 0), (0, -1)]
    if tiles[i][j] == "J":
        return [(0, -1), (-1, 0)]
    if tiles[i][j] == "F":
        return [(1, 0), (0, 1)]

def find_start(tiles: list[str]):
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            if tiles[i][j] == "S":
                return i, j


def part_2(problem: Problem, loop: set[tuple]):
    tiles = problem.tiles
    interior = set()

    p = Path(loop)

    # maybe something like cross odd times == interior else exterior
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            if (i, j) not in loop and p.contains_point((i, j)):
                interior.add((i, j))

    return len(interior)


if __name__ == "__main__":
    main()
