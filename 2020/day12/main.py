from enum import Enum
from typing import List


class Direction(Enum):
    E = 0
    N = 90
    W = 180
    S = 270


def change_direction(direction, i):
    d = i[0]
    v = int(i[1:])
    if d == "L":
        return Direction((direction.value + v) % 360)
    return Direction((direction.value - v) % 360)


def move(x, y, i):
    d = i[0]
    v = int(i[1:])
    if d == "N":
        y += v
    elif d == "S":
        y -= v
    elif d == "E":
        x += v
    elif d == "W":
        x -= v
    return x, y


def part_1(instructions: List[str]):
    x, y = 0, 0
    direction = Direction.E
    for i in instructions:
        if i[0] in ("L", "R"):
            direction = change_direction(direction, i)
        else:
            if i[0] == "F":
                i = f"{direction.name}{i[1:]}"
            x, y = move(x, y, i)
    return abs(x) + abs(y)


def part_2(instructions: List[str]):
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        instructions = f.read()
    instructions = instructions.split("\n")

    print(part_1(instructions))
    print(part_2(instructions))
