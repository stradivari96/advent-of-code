def part_1(lines):
    result = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (
                all(lines[ii][j] < lines[i][j] for ii in range(0, i))
                or all(lines[ii][j] < lines[i][j] for ii in range(i + 1, len(lines)))
                or all(lines[i][jj] < lines[i][j] for jj in range(0, j))
                or all(lines[i][jj] < lines[i][j] for jj in range(j + 1, len(lines[0])))
            ):
                result += 1
    return result


def part_2(lines):
    result = 0

    def dfs(i, j, d, limit):
        if i <= 0 or j <= 0 or i >= len(lines) - 1 or j >= len(lines[0]) - 1:
            return 1
        if lines[i][j] >= limit:
            return 1
        return 1 + dfs(i + d[0], j + d[1], d, limit)

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            result = max(
                result,
                dfs(i + 1, j, (1, 0), lines[i][j])
                *dfs(i, j + 1, (0, 1), lines[i][j])
                *dfs(i - 1, j, (-1, 0), lines[i][j])
                *dfs(i, j - 1, (0, -1), lines[i][j])
            )
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()
    lines = data.split("\n")
    lines = [[int(c) for c in line] for line in lines]
    print(part_1(lines))
    print(part_2(lines))
