

def get_size(d, total_size):
    if isinstance(total_size[d], int):
        return total_size[d]
    result = 0
    for n in total_size[d]:
        if isinstance(n, int):
            result += n
        else:
            result += get_size(n, total_size)
    total_size[d] = result
    return total_size[d]


def part_1(lines):
    total_size = {}
    dir_stack = []
    for line in lines:
        if line.startswith("$ cd "):
            d = line.split("$ cd ")[-1]
            if d == "..":
                dir_stack.pop()
            else:
                prev = tuple(dir_stack)
                dir_stack.append((d, prev))
                if d not in total_size:
                    total_size[(d, prev)] = []
        elif line.startswith("dir"):
            d = line.split("dir ")[-1]
            total_size[dir_stack[-1]].append((d, tuple(dir_stack)))
        elif line[0].isdigit():
            total_size[dir_stack[-1]].append(int(line.split(" ")[0]))
    result = 0
    for n in total_size:
        if get_size(n, total_size) <= 100000:
            result += get_size(n, total_size)
    return result

def part_2(lines):
    total_size = {}
    dir_stack = []
    for line in lines:
        if line.startswith("$ cd "):
            d = line.split("$ cd ")[-1]
            if d == "..":
                dir_stack.pop()
            else:
                prev = tuple(dir_stack)
                dir_stack.append((d, prev))
                if d not in total_size:
                    total_size[(d, prev)] = []
        elif line.startswith("dir"):
            d = line.split("dir ")[-1]
            total_size[dir_stack[-1]].append((d, tuple(dir_stack)))
        elif line[0].isdigit():
            total_size[dir_stack[-1]].append(int(line.split(" ")[0]))

    available = 70000000 - get_size(('/', ()), total_size)
    needed = 30000000 - available
    result = float("inf")
    for n in total_size:
        if get_size(n, total_size) >= needed:
            result = min(result, get_size(n, total_size))
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()
    lines = data.split("\n")
    print(part_1(lines))
    print(part_2(lines))
