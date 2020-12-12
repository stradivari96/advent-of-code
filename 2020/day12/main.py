import math
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
    x, y = 0, 0
    wx, wy = 10, 1
    for i in instructions:
        a = i[0]
        v = int(i[1:])
        if a == "F":
            x += wx * v
            y += wy * v
        else:
            wx, wy = move_waypoint(wx, wy, a, v)
    return abs(x) + abs(y)


def move_waypoint(wx, wy, action, value):
    if action == "N":
        wy += value
    elif action == "S":
        wy -= value
    elif action == "E":
        wx += value
    elif action == "W":
        wx -= value
    elif action == "L":
        wx, wy = rotate(wx, wy, value)
    elif action == "R":
        wx, wy = rotate(wx, wy, -value)
    return wx, wy


def rotate(x, y, degrees):
    degrees = math.radians(degrees)
    nx = x * math.cos(degrees) - y * math.sin(degrees)
    ny = x * math.sin(degrees) + y * math.cos(degrees)
    return round(nx), round(ny)


if __name__ == "__main__":
    with open("data.txt") as f:
        instructions = f.read()
    instructions = instructions.split("\n")

    print(part_1(instructions))
    print(part_2(instructions))
