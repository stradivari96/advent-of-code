import re
from typing import List


def get_parents(rules: List[str], color: str) -> List[str]:
    colors = []
    for rule in rules:
        if not rule.startswith(color) and color in rule:
            colors.append(rule.split(" bags")[0])
    return colors


def part_1(rules: List[str]) -> int:
    colors = set()
    pending = ["shiny gold"]
    while pending:
        parents = get_parents(rules, pending.pop())
        pending.extend([p for p in parents if p not in colors])
        colors.update(parents)
    return len(colors)


def part_2(rules: List[str]) -> int:
    relations = {}
    parent_pattern = re.compile(r"^(\w+ \w+)")
    child_pattern = re.compile(r"(\d) (\w+ \w+) bag")
    for rule in rules:
        parent = parent_pattern.match(rule).group()
        children = child_pattern.findall(rule)
        relations[parent] = {bag: int(n) for n, bag in children}
    return count_bags(relations, "shiny gold")


def count_bags(relations, color):
    if not relations[color]:
        return 1
    result = 1 if color != "shiny gold" else 0
    for c, n in relations[color].items():
        result += n * count_bags(relations, c)
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        rules = f.read()
    rules = rules.split("\n")

    print(part_1(rules))
    print(part_2(rules))
