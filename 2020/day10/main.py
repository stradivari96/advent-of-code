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
    n = max(arr)
    res = [0 for _ in range(n + 1)]
    res[0] = 1

    for i in range(n + 1):
        if i not in arr:
            continue
        for j in range(i - 3, i):
            if j >= 0:
                res[i] += res[j]
    return res[n]


if __name__ == "__main__":
    with open("data.txt") as f:
        adapters = f.read()
    adapters = adapters.split("\n")
    adapters = [int(n) for n in adapters]

    print(part_1(adapters))
    print(part_2(adapters))
