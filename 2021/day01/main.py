import collections
from itertools import islice


def part_1(numbers):
    result = 0
    for i, number in enumerate(numbers):
        if i < len(numbers) - 1 and numbers[i + 1] > number:
            result += 1
    return result


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def part_2(numbers):
    result = 0
    prev = None
    for x, y, z in sliding_window(numbers, 3):
        current_sum = x + y + z
        if prev is not None and current_sum > prev:
            result += 1
        prev = current_sum
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        numbers = f.readlines()
    numbers = [int(i) for i in numbers]

    print(part_1(numbers))
    print(part_2(numbers))
