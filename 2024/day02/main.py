from collections import Counter

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
        lines = [line.split(" ") for line in lines]
        lines = [[int(i) for i in line] for line in lines]
    print(part_1(lines))
    print(part_2(lines))


def part_1(lines: list[tuple[int]]):
    result = 0
    for line in lines:
        if is_ok(line):
            result += 1
    return result


def part_2(lines: list[tuple[int]]):
    result = 0
    for line in lines:
        if is_ok(line):
            result += 1
        else:
            if any(is_ok(line[:i] + line[i + 1 :]) for i in range(len(line))):
                result += 1
    return result


def is_ok(line) -> bool:
    increasing = line[0] <= line[1]
    decreasing = line[0] >= line[1]
    for i, j in zip(line, line[1:]):
        if increasing and i > j:
            return False
        if decreasing and i < j:
            return False
        if not (1 <= abs(i - j) <= 3):
            return False
    return True


if __name__ == "__main__":
    main()
