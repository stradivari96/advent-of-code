from functools import cmp_to_key, cache
from typing import NamedTuple
from collections import Counter
from enum import IntEnum


class Problem(NamedTuple):
    hands: list[tuple]


class HandType(IntEnum):
    FIVE = 0
    FOUR = 1
    FULL_HOUSE = 2
    THREE = 3
    TWO_PAIR = 4
    ONE_PAIR = 5
    HIGH = 6


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    problem = Problem(hands=[])
    for line in lines:
        hand, bid = line.split(" ")
        problem.hands.append((hand, int(bid)))
    print(part_1(problem))
    print(part_2(problem))


def part_1(problem: Problem):
    def cmp(a, b):
        a, b = a[0], b[0]
        if hand_type(a) > hand_type(b):
            return -1
        if hand_type(a) < hand_type(b):
            return 1
        for i, j in zip(a, b):
            if i == j:
                continue
            i, j = to_value(i), to_value(j)
            return 1 if i < j else -1
        return 0
    hands = sorted(problem.hands, key=cmp_to_key(cmp))
    return sum((i+1)*bid for i, (h, bid) in enumerate(hands))


@cache
def hand_type(hand):
    counter = Counter(hand)
    values = sorted(counter.values())
    if values == [5]:
        return HandType.FIVE
    if values == [1, 4]:
        return HandType.FOUR
    if values == [2, 3]:
        return HandType.FULL_HOUSE
    if values == [1, 1, 3]:
        return HandType.THREE
    if values == [1, 2, 2]:
        return HandType.TWO_PAIR
    if values == [1, 1, 1, 2]:
        return HandType.ONE_PAIR
    return HandType.HIGH


def to_value(char, j_val=-11):
    if char == "A":
        return -14
    if char == "K":
        return -13
    if char == "Q":
        return -12
    if char == "J":
        return j_val
    if char == "T":
        return -10
    return -int(char)


def part_2(problem: Problem):
    def cmp(a, b):
        a, b = a[0], b[0]
        if hand_type_joker(a) > hand_type_joker(b):
            return -1
        if hand_type_joker(a) < hand_type_joker(b):
            return 1
        for i, j in zip(a, b):
            if i == j:
                continue
            i, j = to_value(i, j_val=0), to_value(j, j_val=0)
            return 1 if i < j else -1
        return 0
    # 248948468 low
    hands = sorted(problem.hands, key=cmp_to_key(cmp))
    return sum((i + 1) * bid for i, (h, bid) in enumerate(hands))


@cache
def hand_type_joker(hand):
    if "J" not in hand:
        return hand_type(hand)
    counter = Counter(hand)
    j = counter.pop("J")
    values = sorted(counter.values())
    # j == 1
    if values == [4]:
        return HandType.FIVE
    if values == [1, 3]:
        return HandType.FOUR
    if values == [2, 2]:
        return HandType.FULL_HOUSE
    if values == [1, 1, 2]:
        return HandType.THREE
    if values == [1, 1, 1, 1]:
        return HandType.ONE_PAIR
    # j == 2
    if values == [3]:
        return HandType.FIVE
    if values == [1, 2]:
        return HandType.FOUR
    if values == [1, 1, 1]:
        return HandType.THREE
    # j == 3
    if values == [2]:
        return HandType.FIVE
    if values == [1, 1]:
        return HandType.FOUR
    # j == 4
    if values == [1]:
        return HandType.FIVE
    # j == 5
    return HandType.FIVE


if __name__ == "__main__":
    main()
