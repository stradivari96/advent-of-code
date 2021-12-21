from collections import defaultdict


def part_1(data):
    points = defaultdict(int)
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            y1, y2 = sorted([y1, y2])
            for y in range(y1, y2 + 1):
                points[x1, y] += 1
        elif y1 == y2:
            x1, x2 = sorted([x1, x2])
            for x in range(x1, x2 + 1):
                points[x, y1] += 1
    return sum(1 for v in points.values() if v > 1)


def part_2(data):
    points = defaultdict(int)
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            y1, y2 = sorted([y1, y2])
            for y in range(y1, y2 + 1):
                points[x1, y] += 1
        elif y1 == y2:
            x1, x2 = sorted([x1, x2])
            for x in range(x1, x2 + 1):
                points[x, y1] += 1
        else:
            x_sign = 1 if x1 < x2 else -1
            y_sign = 1 if y1 < y2 else -1
            for (x, y) in zip(
                range(x1, x2 + x_sign, x_sign), range(y1, y2 + y_sign, y_sign)
            ):
                points[x, y] += 1
    return sum(1 for v in points.values() if v > 1)


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()
    data = [i.strip() for i in data]
    clean_data = []
    for row in data:
        a, b = row.split(" -> ")
        x1, y1 = a.split(",")
        x2, y2 = b.split(",")
        clean_data.append([(int(x1), int(y1)), (int(x2), int(y2))])

    print(clean_data)
    print(part_1(clean_data))
    print(part_2(clean_data))
