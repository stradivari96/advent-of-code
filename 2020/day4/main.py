required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}


def validate_hcl(hcl):
    chars = [str(i) for i in range(10)] + [
        chr(c) for c in range(ord("a"), ord("f") + 1)
    ]
    assert hcl[0] == "#"
    assert all(c in chars for c in hcl[1:])


def part_1(arr):
    result = 0
    for passport in arr:
        passport = " ".join(passport.split("\n"))
        passport = passport.split(" ")
        passport = [f.split(":") for f in passport]
        passport = {k: v for k, v in passport}
        missing_keys = required_fields - passport.keys()
        if missing_keys:
            continue
        result += 1
    return result


def part_2(arr):
    result = 0
    for passport in arr:
        passport = " ".join(passport.split("\n"))
        passport = passport.split(" ")
        passport = [f.split(":") for f in passport]
        passport = {k: v for k, v in passport}
        missing_keys = required_fields - passport.keys()
        if missing_keys:
            continue
        hgt = passport["hgt"][:-2]
        hgt_unit = passport["hgt"][-2:]
        try:
            hgt = int(hgt)
            assert 1920 <= int(passport["byr"]) <= 2002
            assert 2010 <= int(passport["iyr"]) <= 2020
            assert 2020 <= int(passport["eyr"]) <= 2030
            assert hgt_unit in ("cm", "in")
            assert (hgt_unit == "cm" and 150 <= hgt <= 193) or (
                hgt_unit == "in" and 59 <= hgt <= 76
            )
            assert passport["ecl"] in "amb blu brn gry grn hzl oth".split(" ")
            validate_hcl(passport["hcl"])
            assert len(passport["pid"]) == 9 and all(
                c in [str(i) for i in range(10)] for c in passport["pid"]
            )
        except (ValueError, AssertionError):
            continue
        result += 1
    return result


if __name__ == "__main__":
    with open("data.txt") as f:
        passports = f.read()
    passports = passports.split("\n\n")

    print(part_1(passports))
    print(part_2(passports))
