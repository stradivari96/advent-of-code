from typing import NamedTuple


class Problem(NamedTuple):
    patterns: list[list[str]]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    problem = Problem(patterns=[])
    pattern = []
    for line in lines + [""]:
        if line == "":
            problem.patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    result = 0
    for pattern in problem.patterns:
        found = False
        # rows
        for i in range(len(pattern)-1):
            if is_mirror_row(i, i+1, pattern):
                result += 100*(i+1)
                found = True
                break
        if found:
            continue
        # cols
        for i in range(len(pattern[0])-1):
            if is_mirror_col(i, i+1, pattern):
                result += i+1
                break
    return result


def is_mirror_row(i, j, pattern):
    while i >= 0 and j < len(pattern):
        if any(a != b for a, b in zip(pattern[i], pattern[j])):
            return False
        i -= 1
        j += 1
    return True


def is_mirror_col(i, j, pattern):
    while i >= 0 and j < len(pattern[0]):
        col_i = [row[i] for row in pattern]
        col_j = [row[j] for row in pattern]
        if any(a != b for a, b in zip(col_i, col_j)):
            return False
        i -= 1
        j += 1
    return True



def part_2(problem: Problem):
    ...


if __name__ == "__main__":
    main()
