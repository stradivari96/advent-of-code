

def part_1(arr):
    result = 0
    for a, b in arr:
        if a[0] <= b[0] and a[1] >= b[1]:
            result += 1
        elif b[0] <= a[0] and b[1] >= a[1]:
            result += 1
    return result


def part_2(arr):
    result = 0
    for a, b in arr:
        a, b = sorted([a, b])
        if b[0] > a[1]:
            continue
        else:
            result += 1
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        numbers = f.read()
    lines = numbers.split("\n")
    pairs = []
    for line in lines:
        a, b = line.split(",")
        a = [int(n) for n in a.split("-")]
        b = [int(n) for n in b.split("-")]
        pairs.append((a,b))

    print(part_1(pairs))
    print(part_2(pairs))
