from typing import List


def get_first_bus(min_time, bus):
    result = bus
    while result < min_time:
        result += bus
    return result


def part_1(min_time: int, busses: List[str]):
    busses = [int(b) for b in busses if b != "x"]
    result = busses[0]
    for b in busses:
        time = get_first_bus(min_time, b)
        if time < get_first_bus(min_time, result):
            result = b
    return result * (get_first_bus(min_time, result) - min_time)


def part_2(busses: List[str]):
    busses = [int(b) if b != "x" else "x" for b in busses]
    return "https://www.wolframalpha.com/input/?i=0+%3D+" + "+%3D+".join(
        [f"((n+%2B+{i})+mod+{n})" for i, n in enumerate(busses) if n != "x"]
    )


if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read()
    data = data.split("\n")
    earliest = int(data[0])
    all_busses = data[1].split(",")

    print(part_1(earliest, all_busses))
    print(part_2(all_busses))
