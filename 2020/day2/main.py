from collections import Counter


def part_1(arr):
    result = 0
    for password in arr:
        minmax, letter, password = password.split(" ")
        min_times, max_times = [int(i) for i in minmax.split("-")]
        letter = letter[0]
        counter = Counter(password)
        if letter not in counter:
            continue
        if counter[letter] >= min_times and counter[letter] <= max_times:
            result += 1
    return result


def part_2(arr):
    result = 0
    for password in arr:
        minmax, letter, password = password.split(" ")
        min_times, max_times = [int(i) for i in minmax.split("-")]
        letter = letter[0]
        if min_times - 1 >= len(password):
            continue
        if max_times - 1 >= len(password):
            continue
        if (password[min_times - 1] == letter) ^ (password[max_times - 1] == letter):
            result += 1
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        passwords = f.read()
    passwords = passwords.split("\n")

    print(part_1(passwords))
    print(part_2(passwords))
