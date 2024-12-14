import re


def main():
    with open("data.txt") as f:
        text = f.read().splitlines()
    print(part_1(text))
    print(part_2(text))


def part_1(text: list[str]) -> int:
    result = 0
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] != "X":
                continue
            # horizontal xmas
            if j + 3 < len(text[i]) and text[i][j + 1] == "M" and text[i][j + 2] == "A" and text[i][j + 3] == "S":
                result += 1
            # horizontal backwards xmas
            if j - 3 >= 0 and text[i][j - 1] == "M" and text[i][j - 2] == "A" and text[i][j - 3] == "S":
                result += 1
            # vertical xmas
            if i + 3 < len(text) and text[i + 1][j] == "M" and text[i + 2][j] == "A" and text[i + 3][j] == "S":
                result += 1
            # vertical backwards xmas
            if i - 3 >= 0 and text[i - 1][j] == "M" and text[i - 2][j] == "A" and text[i - 3][j] == "S":
                result += 1
            # diagonal xmas
            if i + 3 < len(text) and j + 3 < len(text[i]) and text[i + 1][j + 1] == "M" and text[i + 2][j + 2] == "A" and text[i + 3][j + 3] == "S":
                result += 1
            # diagonal backwards xmas
            if i - 3 >= 0 and j - 3 >= 0 and text[i - 1][j - 1] == "M" and text[i - 2][j - 2] == "A" and text[i - 3][j - 3] == "S":
                result += 1
            # other diagonal xmas
            if i + 3 < len(text) and j - 3 >= 0 and text[i + 1][j - 1] == "M" and text[i + 2][j - 2] == "A" and text[i + 3][j - 3] == "S":
                result += 1
            # other diagonal backwards xmas
            if i - 3 >= 0 and j + 3 < len(text[i]) and text[i - 1][j + 1] == "M" and text[i - 2][j + 2] == "A" and text[i - 3][j + 3] == "S":
                result += 1
    return result


def part_2(lines: list[str]) -> int:
    result = 0
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            if lines[i][j] != "A":
                continue
            # diag1
            if (
                sorted((lines[i-1][j-1], lines[i+1][j+1])) == ["M", "S"]
                and sorted((lines[i-1][j+1], lines[i+1][j-1])) == ["M", "S"]
            ):
                result += 1
    return result

if __name__ == "__main__":
    main()
