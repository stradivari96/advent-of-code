from typing import List


def has_two_sum(arr, target):
    arr = set(arr)
    for n in arr:
        if target - n in arr:
            return True
    return False


def part_1(nums: List[int]):
    for i in range(25, len(nums)):
        prev = nums[:i]
        n = nums[i]
        if not has_two_sum(prev, n):
            return n
    return None


def part_2(nums: List[int], target: int):
    for i in range(len(nums)):
        for j in range(i, i + 25):
            if sum(nums[i:j]) == target:
                result = nums[i:j]
                return min(result) + max(result)
    return None


if __name__ == "__main__":
    with open("data.txt") as f:
        numbers = f.read()
    numbers = numbers.split("\n")
    numbers = [int(n) for n in numbers]

    n = part_1(numbers)
    print(n)
    print(part_2(numbers, n))
