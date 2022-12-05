import re


def part_1(stacks, procedures):
    stacks = [s[:] for s in stacks]
    for count, src, dst in procedures:
        for _ in range(int(count)):
            crate = stacks[int(src)-1].pop()
            stacks[int(dst)-1].append(crate)
    return "".join([s[-1] for s in stacks])


def part_2(stacks, procedures):
    stacks = [s[:] for s in stacks]
    for count, src, dst in procedures:
        crates = []
        for _ in range(int(count)):
            crate = stacks[int(src) - 1].pop()
            crates.insert(0, crate)
        stacks[int(dst) - 1].extend(crates)
    return "".join([s[-1] for s in stacks])


if __name__ == "__main__":
    with open("data.txt") as f:
        numbers = f.read()
    lines = numbers.split("\n")
    moves_start = lines.index("")
    crates = lines[:moves_start]
    procedures = lines[moves_start+1:]
    stacks = []
    for line in crates[:-1]:
        stack = 0
        for i in range(1, len(line), 4):
            while stack > len(stacks)-1:
                stacks.append([])
            if line[i] != " ":
                stacks[stack].insert(0, line[i])
            stack += 1
    procedures = [re.match(r"move (\d+) from (\d+) to (\d+)", l).groups() for l in procedures]
    print(part_1(stacks, procedures))
    print(part_2(stacks, procedures))
