def part_1(data):
    horizontal = 0
    depth = 0
    for x, y in data:
        if x == "forward":
            horizontal += y
        elif x == "down":
            depth += y
        elif x == "up":
            depth -= y
    return horizontal, depth


def part_2(data):
    aim = 0
    horizontal = 0
    depth = 0
    for x, y in data:
        if x == "forward":
            horizontal += y
            depth += aim * y
        elif x == "down":
            aim += y
        elif x == "up":
            aim -= y
    return horizontal, depth


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()
    data = [i.strip().split(" ") for i in data]
    data = [(x, int(y)) for x, y in data]
    horizontal, depth = part_1(data)
    print(horizontal * depth)

    horizontal, depth = part_2(data)
    print(horizontal * depth)
