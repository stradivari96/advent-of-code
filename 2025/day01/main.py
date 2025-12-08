import typing


class Instruction(typing.NamedTuple):
    direction: typing.Literal['L', 'R']
    steps: int


class Problem(typing.NamedTuple):
    instructions: list[Instruction]


def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(
        instructions=[
            Instruction(direction=line[0], steps=int(line[1:]))
            for line in lines
        ]
    )
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    times_is_zero = 0
    dial = 50
    for ins in problem.instructions:
        if ins.direction == 'L':
            dial -= ins.steps
        else:
            dial += ins.steps
        dial %= 100
        if dial == 0:
            times_is_zero += 1
    return times_is_zero


def part_2(problem: Problem):
    crossings = 0
    dial = 50

    for ins in problem.instructions:
        step = ins.steps if ins.direction == 'R' else -ins.steps
        new_dial = dial + step
        
        if step > 0:
            crossings += (new_dial // 100) - (dial // 100)
        else:
            # -1 to handle starting or ending at zero
            crossings += (dial - 1) // 100 - (new_dial - 1) // 100
        dial = new_dial

    return crossings


if __name__ == "__main__":
    main()
