def part_1(arr):
    result = 0
    slope = 1
    right = 3
    for i in range(slope, len(arr), slope):
        if arr[i][(i * right) % len(arr[i])] == "#":
            result += 1
    return result


def part_2(arr):
    results = []
    for right, slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result = 0
        for i in range(slope, len(arr), slope):
            j = (i // slope * right) % len(arr[i])
            if arr[i][j] == "#":
                result += 1
        results.append(result)
    result = 1
    print(results)
    for n in results:
        result *= n
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        rows = f.read()
    rows = rows.split("\n")

    print(part_1(rows))
    # 2993292000 low
    print(part_2(rows))
