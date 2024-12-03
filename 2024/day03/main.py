import re

ok_mul = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")

def main():
    with open("data.txt") as f:
        text = f.read()
    print(part_1(text))
    print(part_2(text))


def part_1(text: str):
    muls = ok_mul.findall(text)
    result = 0
    for m in muls:
        if m[2] or m[3]:
            continue
        result += int(m[0]) * int(m[1])
    return result
    


def part_2(text: str):
    muls = ok_mul.findall(text)
    result = 0
    do = True
    for m in muls:
        if m[2]:
            do = True
        elif m[3]:
            do = False
        elif do:
            result += int(m[0]) * int(m[1])
    return result


if __name__ == "__main__":
    main()
