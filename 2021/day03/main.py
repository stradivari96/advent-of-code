def part_1(data):
    gamma = ""
    epsilon = ""
    for j in range(len(data[0])):
        count = {"1": 0, "0": 0}
        for row in data:
            count[row[j]] += 1
        gamma += max(count, key=lambda x: count[x])
        epsilon += min(count, key=lambda x: count[x])
    return int(gamma, 2) * int(epsilon, 2)


def part_2(data):
    oxygen_generator_rating = get_oxygen_rating(data)
    co2_rating = get_co2_rating(data)
    return int(oxygen_generator_rating, 2) * int(co2_rating, 2)


def get_oxygen_rating(data):
    remaining = data[:]
    for j in range(len(data[0])):
        count = {"1": 0, "0": 0}
        for row in remaining:
            count[row[j]] += 1
        common = "1" if count["1"] >= count["0"] else "0"
        remaining = [row for row in remaining if row[j] == common]
        if len(remaining) == 1:
            return remaining[0]


def get_co2_rating(data):
    remaining = data[:]
    for j in range(len(data[0])):
        count = {"1": 0, "0": 0}
        for row in remaining:
            count[row[j]] += 1
        common = "1" if count["1"] < count["0"] else "0"
        remaining = [row for row in remaining if row[j] == common]
        if len(remaining) == 1:
            return remaining[0]


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.readlines()
    data = [i.strip() for i in data]
    print(part_1(data))
    print(part_2(data))
