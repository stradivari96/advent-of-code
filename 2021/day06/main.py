from collections import Counter, defaultdict


def part_1(data):
    data = data[:]
    for _ in range(80):
        new = []
        for i in range(len(data)):
            if data[i] == 0:
                new.append(8)
                data[i] = 6
            else:
                data[i] -= 1
        data += new
    return len(data)


def part_2(data):
    data = Counter(data)
    for _ in range(256):
        new_data = defaultdict(int)
        for i in range(8 + 1):
            if i == 0:
                new_data[8] = data.get(i, 0)
                new_data[6] = data.get(i, 0)
            else:
                new_data[i - 1] += data.get(i, 0)
        data = new_data
    return sum(data.values())


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split(",")
    data = [int(i) for i in data]
    print(part_1(data))
    print(part_2(data))
