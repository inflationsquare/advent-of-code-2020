import re


pattern = re.compile(r"^(?P<n1>.*?)-(?P<n2>.*?)\s(?P<l>.*?)\:\s(?P<s>.*?)$")


def is_valid_1(s):
    parse = re.search(pattern, s)
    substrs = len(parse.group("s")) - len(parse.group("s").replace(parse.group("l"), ""))
    valid = int(parse.group("n1")) <= substrs <= int(parse.group("n2"))
    return valid


def is_valid_2(s):
    parse = re.search(pattern, s)
    try:
        valid = (parse.group("s")[int(parse.group("n1")) - 1] == parse.group("l")) ^ (
            parse.group("s")[int(parse.group("n2")) - 1] == parse.group("l")
        )
    except:
        valid = False
    return valid


with open("2.in", "r") as f:
    data = f.read().splitlines()

print(sum(map(is_valid_1, data)))
print(sum(map(is_valid_2, data)))
