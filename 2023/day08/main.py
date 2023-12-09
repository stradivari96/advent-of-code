from typing import NamedTuple
import math
from concurrent.futures import ProcessPoolExecutor


class Problem(NamedTuple):
    steps: str
    nodes: dict[str, list[str]]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(lines[0], {})
    for line in lines[2:]:
        node, children = line.split(" = ")
        children = children.replace("(", "").replace(")", "")
        problem.nodes[node] = children.split(", ")
    #print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    cur = "AAA"
    steps = 0
    iterator = iter(infinite_iterator(problem.steps))
    while cur != "ZZZ":
        steps += 1
        step = next(iterator)
        if step == "L":
            cur = problem.nodes[cur][0]
        else:
            cur = problem.nodes[cur][1]
    return steps


def infinite_iterator(l):
    while True:
        for element in l:
            yield element



BATCH_SIZE = 100_000_000


def part_2(problem: Problem):
    starting = []
    for node in problem.nodes:
        if node[-1] == "A":
            starting.append(node)

    steps = []
    for node in starting:
        step = 0
        iterator = iter(infinite_iterator(problem.steps))
        while node[-1] != "Z":
            step += 1
            node = problem.nodes[node][0 if next(iterator) == "L" else 1]
        steps.append(step)
    # why can't it be another node that endswith Z the first that they all meet?
    return math.lcm(*steps)

    # FAILED BRUTE FORCE
    # nodes = starting.copy()
    # for i in range(0, 100_000_000_000_000, BATCH_SIZE):
    #     args = [(problem, nodes[j], i) for j in range(len(starting))]
    #     with ProcessPoolExecutor(max_workers=len(starting)) as executor:
    #         values = executor.map(process_batch, args)
    #     values = list(values)
    #     solution = values[0][1]
    #     for j, (value, z_ending) in enumerate(values):
    #         nodes[j] = value
    #         solution = solution.intersection(z_ending)
    #     if solution:
    #         return min(solution) + 1
    #     print(i)


def process_batch(arg):
    problem, node, start = arg
    z_ending = set()
    for i in range(start, start+BATCH_SIZE):
        step = 0 if problem.steps[i % len(problem.steps)] == "L" else 1
        node = problem.nodes[node][step]
        if node[-1] == "Z":
            z_ending.add(i)
    return node, z_ending


if __name__ == "__main__":
    main()
