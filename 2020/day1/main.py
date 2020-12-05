def part_1(arr):
    for n in arr:
        inverse = 2020 - n
        if inverse in arr:
            return inverse * n


def part_2(arr):
    for i, n in enumerate(arr):
        if n > 2020:
            continue
        l, r = i + 1, len(arr) - 1
        while l < r:
            three_sum = n + arr[l] + arr[r]
            if three_sum > 2020:
                r -= 1
            elif three_sum < 2020:
                l += 1
            else:
                return n * arr[l] * arr[r]


if __name__ == "__main__":
    with open("data.txt") as f:
        numbers = f.read()
    numbers = numbers.split("\n")
    numbers = [int(i) for i in numbers]

    print(part_1(set(numbers)))
    print(part_2(sorted(numbers)))
