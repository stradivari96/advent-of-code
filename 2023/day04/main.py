from collections import defaultdict


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    cards = []
    for i, line in enumerate(lines):
        line = line.split(": ")[1]
        winning, have = line.split(" | ")
        winning = [n for n in winning.split(" ") if n]
        have = [n for n in have.split(" ") if n]
        cards.append((i, winning, have))
    print(part_1(cards))
    print(part_2(cards))


def part_1(cards):
    total = 0
    for _, winning, have in cards:
        winning = set(winning)
        count = 0
        for n in have:
            if n in winning:
                count += 1
        if count:
            total += 2**(count-1)
    return total


def part_2(cards):
    card_count = {i: 1 for i in range(len(cards))}
    for i, winning, have in cards:
        winning = set(winning)
        count = 0
        for n in have:
            if n in winning:
                count += 1
        for j in range(count):
            card_count[i+j+1] += 1*card_count[i]
    return sum(card_count.values())


if __name__ == "__main__":
    main()
