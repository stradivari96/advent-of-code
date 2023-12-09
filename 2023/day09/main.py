from typing import NamedTuple


class Problem(NamedTuple):
    histories: list[list[int]]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(
        histories=[[int(n) for n in line.split(" ")] for line in lines]
    )
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    extrapolated = []
    for history in problem.histories:
        last_n = []
        cur = history.copy()
        while len(set(cur)) != 1:
            last_n.append(cur[-1])
            cur = [cur[i+1]-cur[i] for i in range(len(cur)-1)]
        diff = cur[0]
        while len(last_n) > 1:
            diff = last_n.pop() + diff
        extrapolated.append(last_n[0] + diff)
    return sum(extrapolated)


def part_2(problem: Problem):
    extrapolated = []
    for history in problem.histories:
        first_n = []
        cur = history.copy()
        while len(set(cur)) != 1:
            first_n.append(cur[0])
            cur = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        diff = cur[0]
        while len(first_n) > 1:
            diff = first_n.pop() - diff
        extrapolated.append(first_n[0] - diff)
    return sum(extrapolated)



if __name__ == "__main__":
    main()
