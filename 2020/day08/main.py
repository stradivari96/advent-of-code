from typing import List


def part_1(instructions: List[str]) -> int:
    acc, infinite = execute(instructions)
    return acc


def part_2(instructions: List[str]) -> int:
    acc, infinite = execute(instructions)
    idx = 0
    while infinite:
        idx, new_inst = swap(instructions, idx)
        acc, infinite = execute(new_inst)
    return acc


def swap(instructions, idx):
    copy = instructions[:]
    while idx < len(copy):
        if copy[idx].startswith("nop"):
            copy[idx] = copy[idx].replace("nop", "jmp")
            return idx + 1, copy
        if copy[idx].startswith("jmp"):
            copy[idx] = copy[idx].replace("jmp", "nop")
            return idx + 1, copy
        idx += 1


def execute(instructions):
    idx = 0
    acc = 0
    executed = set()
    while idx not in executed and idx < len(instructions):
        executed.add(idx)
        op, n = instructions[idx].split(" ")
        if op == "nop":
            idx += 1
        elif op == "acc":
            acc += int(n)
            idx += 1
        elif op == "jmp":
            idx += int(n)
    if idx in executed:
        return acc, True
    return acc, False


if __name__ == "__main__":
    with open("data.txt") as f:
        instructions = f.read()
    instructions = instructions.split("\n")

    print(part_1(instructions))
    print(part_2(instructions))
