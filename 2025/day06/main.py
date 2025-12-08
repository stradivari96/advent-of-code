import typing


class Problem(typing.NamedTuple):
    rows: list[list[int]]
    operations: list[str]
    raw_lines: list[str]

def main():
    with open("data.txt") as f:
        raw_lines = f.read().splitlines()
    lines = [list(filter(lambda x: x,  l.split(' '))) for l in raw_lines]
    problem = Problem(
        rows=lines[:-1],
        operations=[x for x in lines[-1]],
        raw_lines=raw_lines,
    )
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    total = 0
    for col, op in enumerate(problem.operations):
        result = 0
        if op == '*':
            result = 1
            for row in problem.rows:
                result *= int(row[col])
        elif op == '+':
            for row in problem.rows:
                result += int(row[col])
        total += result
    return total


def part_2(problem: Problem):
    op_row = problem.raw_lines[-1]
    op_indexes = []
    for i in range(len(op_row)):
        if op_row[i] in ('*', '+'):
            op_indexes.append([i])
        else:
            op_indexes[-1].append(i)

    total = 0 
    for indexes in op_indexes:
        op = op_row[indexes[0]]
        result = 0 if op == '+' else 1
        for col in indexes:
            if op == '*':
                n = ''
                for row in problem.raw_lines[:-1]:
                    if row[col] != ' ':
                        n += row[col]
                if n:
                    result *= int(n)
            elif op == '+':
                n = ''
                for row in problem.raw_lines[:-1]:
                    if row[col] != ' ':
                        n += row[col]
                if n:
                    result += int(n)
        total += result
    return total


if __name__ == "__main__":
    main()
