from enum import Enum, auto


class Options(Enum):
    paper = auto()
    rock = auto()
    scissors = auto()


to_enum = {
    "A": Options.rock,
    "B": Options.paper,
    "C": Options.scissors,
    "X": Options.rock,
    "Y": Options.paper,
    "Z": Options.scissors,
}

to_outcome_points = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


def calculate(a: Options, b: Options):
    shape_points = {
        Options.rock: 1,
        Options.paper: 2,
        Options.scissors: 3,
    }
    outcome = 0
    if a == b:
        outcome = 3
    elif b == Options.rock:
        outcome = 6 if a == Options.scissors else 0
    elif b == Options.scissors:
        outcome = 6 if a == Options.paper else 0
    elif b == Options.paper:
        outcome = 6 if a == Options.rock else 0
    return shape_points[b], outcome


def part_1(arr):
    total = 0
    for a, b in arr:
        a, b = to_enum[a], to_enum[b]
        total += sum(calculate(a, b))
    return total


def part_2(arr):
    total = 0
    for a, b in arr:
        a, b = to_enum[a], to_outcome_points[b]
        for option in [Options.rock, Options.paper, Options.scissors]:
            shape_p, outcome = calculate(a, option)
            if outcome == b:
                total += shape_p + outcome
                break
    return total


if __name__ == "__main__":
    with open("data.txt") as f:
        numbers = f.read()
    lines = numbers.split("\n")
    lines = [line.split() for line in lines]

    print(part_1(lines))
    print(part_2(lines))
