from collections import Counter

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
        lines = [line.split("   ") for line in lines]
        lines = [(int(line[0]), int(line[1])) for line in lines]
    print(part_1(lines))
    print(part_2(lines))


def part_1(lines: list[tuple[int]]):
    left = sorted(line[0] for line in lines)
    right = sorted(line[1] for line in lines)
    result = 0
    for l, r in zip(right, left):
        result += abs(l - r)
    return result


def part_2(lines: list[tuple[int]]):
    right = Counter(line[1] for line in lines)
    result = 0
    for l, _ in lines:
        result += l * right.get(l, 0)
    return result


if __name__ == "__main__":
    main()
