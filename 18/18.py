with open("18.in", "r") as f:
    data = f.read().splitlines()


class BadInt:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return BadInt(self.x + other.x)

    def __sub__(self, other):
        return BadInt(self.x * other.x)

    def __repr__(self):
        return str(self.x)


def calc1(s):
    replacements = {str(x): f"BadInt({x})" for x in range(10)}
    replacements["*"] = "-"
    return eval("".join(replacements.get(x, x) for x in list(s)))


print(sum(calc1(s).x for s in data))


class WorseInt:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return WorseInt(self.x * other.x)

    def __mul__(self, other):
        return WorseInt(self.x + other.x)

    def __repr__(self):
        return str(self.x)


def calc2(s):
    replacements = {str(x): f"WorseInt({x})" for x in range(10)}
    replacements["+"] = "*"
    replacements["*"] = "+"
    return eval("".join(replacements.get(x, x) for x in list(s)))


print(sum(calc2(s).x for s in data))
