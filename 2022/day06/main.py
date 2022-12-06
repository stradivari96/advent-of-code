def distinct_window(data, k):
    freq = {}
    for r in range(len(data)):
        freq[data[r]] = freq.get(data[r], 0) + 1
        if r < k:
            continue
        freq[data[r - k]] -= 1
        if all(v == 1 for v in freq.values() if v != 0):
            return r + 1


def part_1(data):
    return distinct_window(data, 4)


def part_2(data):
    return distinct_window(data, 14)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()
    print(part_1(data))
    print(part_2(data))
