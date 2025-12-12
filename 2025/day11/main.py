import typing
from functools import cache


class Problem(typing.NamedTuple):
    graph: dict[str, list[str]]

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    graph = {}
    for line in lines:
        label, other = line.split(': ')
        other = other.split(' ')
        graph[label] = other
    problem = Problem(graph=graph)
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    @cache
    def dfs(device):
        if 'out' in problem.graph[device]:
            return 1
        return sum(dfs(d) for d in problem.graph[device])
    return dfs('you')


def part_2(problem: Problem):
    @cache
    def dfs(device, dst):
        if device not in problem.graph:
            return 0
        if dst in problem.graph[device]:
            return 1
        return sum(dfs(d, dst) for d in problem.graph[device])
    a = dfs('svr', 'fft') * dfs('fft', 'dac') * dfs('dac', 'out')
    b = dfs('svr', 'dac') * dfs('dac', 'fft') * dfs('fft', 'out')
    return a+b


if __name__ == "__main__":
    main()
