from typing import NamedTuple
from functools import cache


class Problem(NamedTuple):
    lines: list[list[str]]
    contiguous: list[list[int]]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    p_lines = []
    p_contiguous = []
    for l in lines:
        a, b = l.split(" ")
        p_lines.append(list(a))
        p_contiguous.append([int(n) for n in b.split(",")])
    problem = Problem(lines=p_lines, contiguous=p_contiguous)
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    result = 0
    for line, arr in zip(problem.lines, problem.contiguous):
        total_line = 0
        for possible in possible_arr(line, 0):
            if is_valid(possible, arr):
                total_line += 1
        result += total_line
    return result


def possible_arr(line, i):
    if i == len(line):
        yield line
    elif line[i] == "?":
        line[i] = "."
        yield from possible_arr(line, i+1)
        line[i] = "#"
        yield from possible_arr(line, i+1)
        line[i] = "?"
    else:
        yield from possible_arr(line, i+1)


def is_valid(line, arr):
    count = 0
    i = 0
    result = []
    while i < len(line):
        if count and line[i] == ".":
            result.append(count)
            count = 0
        elif line[i] == "#":
            count += 1
        i += 1
    if count:
        result.append(count)
    return result == arr


def part_2(problem: Problem):
    result = 0
    for line, arr in zip(problem.lines, problem.contiguous):
        original_line = line[:]
        original_arr = arr[:]
        for _ in range(4):
            line.append("?")
            line.extend(original_line)
            arr.extend(original_arr)

        @cache
        def recurse(l, a, result=0):
            if not a:
                return '#' not in l
            current, a = a[0], a[1:]
            for i in range(len(l) - sum(a) - len(a) - current + 1):
                if "#" in l[:i]:
                    break
                nxt = i + current
                if nxt <= len(l) and '.' not in l[i: nxt] and l[nxt: nxt + 1] != ("#",):
                    result += recurse(l[nxt + 1:], a)
            return result

        result += recurse(tuple(line), tuple(arr))
    return result


if __name__ == "__main__":
    main()
