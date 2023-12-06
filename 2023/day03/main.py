from collections import defaultdict


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    numbers = []
    for row, line in enumerate(lines):
        col_start = None
        for c, char in enumerate(line):
            if char.isdigit():
                if col_start is None:
                    col_start = c
            elif col_start is not None:
                numbers.append((row, col_start, c - 1))
                col_start = None
        if col_start is not None:
            numbers.append((row, col_start, c))
    print(part_1(lines, numbers))
    print(part_2(lines, numbers))


def part_1(lines: list[str], numbers):
    result = 0
    for row, col_start, col_end in numbers:
        number = int(lines[row][col_start:col_end + 1])
        if row > 0:
            prev_row = lines[row - 1]
            i = max(col_start - 1, 0)
            j = min(col_end + 1, len(prev_row) - 1)
            if any(not c.isdigit() and not c == "." for c in prev_row[i:j + 1]):
                result += number
                continue
        if col_start > 0:
            if lines[row][col_start - 1] != ".":
                result += number
                continue
        if col_end < len(lines[row]) - 1:
            if lines[row][col_end + 1] != ".":
                result += number
                continue
        if row < len(lines) - 1:
            next_row = lines[row + 1]
            i = max(col_start - 1, 0)
            j = min(col_end + 1, len(next_row) - 1)
            if any(not c.isdigit() and not c == "." for c in next_row[i:j + 1]):
                result += number
    return result


def part_2(lines, numbers):
    result = 0
    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            if c != "*":
                continue
            adjacent = []
            for n_row, col_start, col_end in numbers:
                number = int(lines[n_row][col_start:col_end + 1])
                if n_row == i-1:
                    if col_start-1 <= j <= col_end+1:
                        adjacent.append(number)
                elif n_row == i:
                    if col_end == j-1 or col_start == j+1:
                        adjacent.append(number)
                elif n_row == i+1:
                    if col_start-1 <= j <= col_end+1:
                        adjacent.append(number)
            if len(adjacent) == 2:
                result += adjacent[0]*adjacent[1]
    return result


if __name__ == "__main__":
    main()
