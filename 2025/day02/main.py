import typing


class Range(typing.NamedTuple):
    low: int
    high: int


class Problem(typing.NamedTuple):
    ranges: list[Range]

def main():
    with open("data.txt") as f:
        lines = f.read().split(',')
    problem = Problem(
        ranges=[
            Range(low=int(line.split('-')[0]), high=int(line.split('-')[1]))
            for line in lines
        ]
    )
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    result = set()
    for r in problem.ranges:
        for i in range(r.low, r.high + 1):
            i = str(i)
            if len(i) % 2 != 0:
                continue
            if i[:len(i)//2] == i[len(i)//2:]:
                result.add(int(i))
    return sum(result)


def part_2(problem: Problem):
    result = set()
    for r in problem.ranges:
        for i in range(r.low, r.high + 1):
            i = str(i)
            # made of any sequence of digits repeated at least twice
            for l in range(1, len(i)//2 + 1):
                if len(i) % l != 0:
                    continue
                if all(i[j:j+l] == i[0:l] for j in range(0, len(i), l)):
                    result.add(int(i))
                    break
    return sum(result)


if __name__ == "__main__":
    main()
