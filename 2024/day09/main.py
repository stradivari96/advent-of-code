import re

ok_mul = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")

def main():
    with open("data.txt") as f:
        text = f.read()
    print(part_1(text))
    print(part_2(text))


def part_1(text: str):
    arr = create_arr(text)
    i = 0
    j = len(arr) - 1
    while i < j:
        while arr[i] != '.':
            i += 1
        while arr[j] == ".":
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    result = 0
    for i, n in enumerate(arr):
        if n == ".":
            continue
        result += int(n) * i
    return result

def part_2(text: str):
    arr = create_arr(text)
    j = len(arr) - 1
    while j >= 0:
        while arr[j] == ".":
            j -= 1
        n = arr[j]
        length = 0
        while arr[j] == n:
            j -= 1
            length += 1
        start = j + 1        
        
        i = 0
        while i < start:
            while arr[i] != ".":
                i += 1
            if all(arr[i + k] == "." for k in range(length)):
                break
            else:
                i += 1
        else:
            continue
        if i < start:
            for k in range(length):
                arr[start + k] = "."
                arr[i + k] = n
    result = 0
    for i, n in enumerate(arr):
        if n == ".":
            continue
        result += int(n) * i
    return result


def create_arr(text: str):
    current_id = 0
    arr = []
    for i, n in enumerate(text):
        n = int(n)
        if i % 2 == 0:
            for _ in range(n):
                arr.append(current_id)
            current_id += 1
        else:
            arr.extend('.' * n)
    return arr

if __name__ == "__main__":
    main()
