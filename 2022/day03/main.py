

def part_1(arr):
    result = 0
    for sack in arr:
        mid = len(sack) // 2
        a = set(sack[:mid])
        b = set(sack[mid:])
        for item in a.intersection(b):
            if item == item.lower():
                result += ord(item)-ord("a")+1
            else:
                result += ord(item)-ord("A")+27
    return result


def part_2(arr):
    result = 0
    for group in range(0, len(arr), 3):
        a, b, c = set(arr[group]), set(arr[group+1]), set(arr[group+2])
        item = next(iter(a.intersection(b).intersection(c)))
        if item == item.lower():
            result += ord(item) - ord("a") + 1
        else:
            result += ord(item) - ord("A") + 27
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        numbers = f.read()
    lines = numbers.split("\n")

    print(part_1(lines))
    print(part_2(lines))
