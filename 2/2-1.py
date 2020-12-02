import re


def is_valid(s):
    pattern = re.compile(r'^(?P<n1>.*?)-(?P<n2>.*?)\s(?P<l>.*?)\:\s(?P<s>.*?)$')
    parse = re.search(pattern, s)
    substrs = len(parse.group('s')) - len(parse.group('s').replace(parse.group('l'), '')) 
    valid = int(parse.group('n1')) <= substrs <= int(parse.group('n2'))
    return valid


with open('2.in', 'r') as f:
    data = f.read().splitlines()

print(sum(map(is_valid, data)))
