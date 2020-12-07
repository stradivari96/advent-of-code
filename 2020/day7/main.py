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
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        rules = f.read()
    rules = rules.split("\n")

    print(part_1(rules))
    print(part_2(rules))
