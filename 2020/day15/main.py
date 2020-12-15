def solve(numbers, end):
    last_spoken = {n: i + 1 for i, n in enumerate(numbers)}
    n = 0
    for i in range(len(numbers) + 1, end):
        if n in last_spoken:
            new_n = i - last_spoken[n]
            last_spoken[n] = i
            n = new_n
        else:
            last_spoken[n] = i
            n = 0
    return n


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split(",")
    data = [int(i) for i in data]

    print(solve(data, 2020))
    print(solve(data, 30000000))
