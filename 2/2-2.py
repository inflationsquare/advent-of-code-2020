import re


def is_valid(s):
    pattern = re.compile(r'^(?P<n1>.*?)-(?P<n2>.*?)\s(?P<l>.*?)\:\s(?P<s>.*?)$')
    parse = re.search(pattern, s)
    try:
        valid = (parse.group('s')[int(parse.group('n1'))-1] == parse.group('l')) ^ (parse.group('s')[int(parse.group('n2'))-1] == parse.group('l'))
    except:
        valid = False
    return valid


with open('2.in', 'r') as f:
    data = f.read().splitlines()

print(sum(map(is_valid, data)))
