def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print(part_1(lines))
    print(part_2(lines))


def part_1(lines: list[str]):
    total = 0
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        if not digits:
            continue
        num = int(digits[0] + digits[-1])
        total += num
    return total


def part_2(lines: list[str]):
    names_to_digit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    total = 0
    for line in lines:
        digits = []
        for i in range(len(line)):
            if line[i].isdigit():
                digits.append(line[i])
                continue
            text = str(line[i:i+6])
            for k, v in names_to_digit.items():
                if text.startswith(k):
                    digits.append(v)
                    break
        num = int(digits[0] + digits[-1])
        total += num
    return total


if __name__ == "__main__":
    main()
