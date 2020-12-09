import re

with open("4.in", "r") as f:
    data = [x.replace("\n", " ").split(" ") for x in f.read().split("\n\n")]
    data = [[y for y in map(lambda att: att.split(":"), x)] for x in data]
    data = [{vals[0]: vals[1] for vals in x if len(vals) == 2} for x in data]

valid_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

print(sum(1 for i in data if valid_keys.issubset(set(i.keys()))))


def valid_height(s):
    if s[-2:] == "cm":
        return 150 <= int(s[:-2]) <= 193
    elif s[-2:] == "in":
        return 59 <= int(s[:-2]) <= 76
    else:
        return False


def valid_eyes(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


print(
    sum(
        1
        for i in data
        if valid_keys.issubset(set(i.keys()))
        and 1920 <= int(i["byr"]) <= 2002
        and 2010 <= int(i["iyr"]) <= 2020
        and 2020 <= int(i["eyr"]) <= 2030
        and valid_height(i["hgt"])
        and re.match(r"^#[a-fA-F0-9]{6}$", i["hcl"])
        and valid_eyes(i["ecl"])
        and re.match(r"^[0-9]{9}$", i["pid"])
    )
)
