import typing
from functools import lru_cache


class Problem(typing.NamedTuple):
    grid: list[str]

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(grid=[list(line) for line in lines])
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    split = 0
    for i, row in enumerate(problem.grid):
        for j, cell in enumerate(row):
            if problem.grid[i-1][j] not in '|S':
                continue
            if cell == '.':
                row[j] = '|'
            elif cell == '^':
                row[j-1] = '|'
                row[j+1] = '|'
                split += 1
    return split


def part_2(problem: Problem):
    @lru_cache(maxsize=None)
    def solve(r, c):
        if c < 0 or c >= len(problem.grid[0]):
            return 0
        if r == len(problem.grid) - 1:
            return 1
        char = problem.grid[r][c]
        if char == '^':
            return solve(r + 1, c - 1) + solve(r + 1, c + 1)
        else:
            return solve(r + 1, c)
    for i, row in enumerate(problem.grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return solve(i, j)


if __name__ == "__main__":
    main()
