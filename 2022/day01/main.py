def part_1(arr):
    return max(arr)


def part_2(arr):
    return sum(sorted(arr, reverse=True)[:3])


if __name__ == "__main__":
    with open("data.txt") as f:
        numbers = f.read()
    numbers = numbers.split("\n")
    elves = []
    current = 0
    for n in numbers:
        if n == "":
            elves.append(current)
            current = 0
        else:
            current += int(n)
    elves.append(current)
    print(part_1(elves))
    print(part_2(elves))
