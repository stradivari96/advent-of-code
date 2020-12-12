from collections import Counter


def part_1(arr):
    result = 0
    for group in arr:
        questions = set()
        for person in group.split("\n"):
            questions.update(person)
        result += len(questions)
    return result


def part_2(arr):
    result = 0
    for group in arr:
        counter = Counter()
        people = group.split("\n")
        for person in people:
            counter.update(person)
        result += len([v for v in counter.values() if v == len(people)])
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        groups = f.read()
    groups = groups.split("\n\n")
    print(part_1(groups))
    print(part_2(groups))
