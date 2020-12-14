from typing import List


def parse_data(data):
    data = data.split("\n")
    data = [i.split(" = ") for i in data]
    result = []
    for left, right in data:
        if left == "mask":
            pass
        else:
            left = int(left[4:-1])
            right = int(right)
        result.append((left, right))
    return result


def part_1(data):
    mask = None
    mem = {}
    for left, right in data:
        if left == "mask":
            mask = right
        else:
            b = bin(right)[2:].zfill(len(mask))
            for i, m in enumerate(mask):
                if m != "X":
                    b = b[:i] + m + b[i + 1 :]
            mem[left] = int(b, 2)
    return sum(mem.values())


def part_2(data):
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()
    data = parse_data(data)

    print(part_1(data))
    print(part_2(data))
