from collections import defaultdict
from functools import cache
from dataclasses import dataclass


@dataclass
class Problem:
    priorities: list[tuple[int, int]]
    updates: list[list[int]]


def main():
    with open("data.txt") as f:
        text = f.read().split("\n\n")
    priorities = []
    for line in text[0].splitlines():
        priorities.append(tuple(map(int, line.split("|"))))
    updates = []
    for line in text[1].splitlines():
        updates.append(list(map(int, line.split(","))))
    problem = Problem(priorities, updates)
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem) -> int:
    prerequisites = defaultdict(set)
    for priority in problem.priorities:
        prerequisites[priority[1]].add(priority[0])
    def update_ok(update: list[int]) -> bool:
        seen = set()
        for page in update:
            for prereq in prerequisites[page]:
                if prereq not in seen and prereq in update:
                    return False
            seen.add(page)
        return True
    result = 0
    for update in problem.updates:
        if update_ok(update):
            result += update[len(update) // 2]
    return result


def part_2(problem: Problem) -> int:
    prerequisites = defaultdict(set)
    for priority in problem.priorities:
        prerequisites[priority[1]].add(priority[0])
    def update_ok(update: list[int]) -> bool:
        seen = set()
        for page in update:
            for prereq in prerequisites[page]:
                if prereq not in seen and prereq in update:
                    return False
            seen.add(page)
        return True
    def reorder_update(update: list[int]) -> list[int]:
        # topological sort, only add pages that are present in the update
        result = []
        seen = set()
        def dfs(page: int) -> None:
            if page in seen:
                return
            seen.add(page)
            for prereq in prerequisites[page]:
                if prereq in update:
                    dfs(prereq)
            result.append(page)
        for page in update:
            dfs(page)
        return result

    result = 0
    for update in problem.updates:
        if not update_ok(update):
            result += reorder_update(update)[len(update) // 2]
    return result

if __name__ == "__main__":
    main()
