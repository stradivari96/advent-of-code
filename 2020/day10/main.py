from typing import List


def part_1(arr: List[int]):
    arr = sorted(arr + [0] + [max(arr) + 3])
    one_jolt = 0
    three_jolt = 0
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff == 1:
            one_jolt += 1
        elif diff == 3:
            three_jolt += 1
    return one_jolt * three_jolt


def part_2(arr: List[int]):
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        adapters = f.read()
    adapters = adapters.split("\n")
    adapters = [int(n) for n in adapters]

    print(part_1(adapters))
