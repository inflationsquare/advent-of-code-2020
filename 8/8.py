import re

with open("8.in", "r") as f:
    data = f.read().splitlines()

pattern = re.compile("^(nop|acc|jmp) ([\+-]\d+)$")

instructions = [[ix, op, int(off)] for (ix, [(op, off)]) in enumerate(map(lambda x: pattern.findall(x), data))]


class Interpreter:
    def __init__(self, instructions):
        self.instructions = instructions
        self.acc = 0
        self.ptr = 0
        self.visited_instructions = set()

    def op(self, opcode, argument):
        if opcode == "nop":
            self.ptr += 1
        elif opcode == "acc":
            self.acc += argument
            self.ptr += 1
        elif opcode == "jmp":
            self.ptr += argument
        else:
            pass

    def run(self, swapop=None):
        while self.instructions[self.ptr][0] not in self.visited_instructions:
            ix, op, arg = self.instructions[self.ptr]

            if swapop and ix == swapop:
                if op == "jmp":
                    op = "nop"
                elif op == "nop":
                    op = "jmp"

            self.op(op, arg)
            self.visited_instructions.add(ix)
            if self.ptr == len(self.instructions):
                return {"code": 0, "result": self.acc}
        return {"code": 1, "result": self.acc}

    def reset(self):
        self.acc = 0
        self.ptr = 0
        self.visited_instructions = set()


machine = Interpreter(instructions)
print(machine.run()["result"])
machine.reset()

swappable = [i[0] for i in instructions if i[1] in ["jmp", "nop"]]
for swap in swappable:
    result = machine.run(swap)
    machine.reset()
    if result["code"] == 0:
        print(result["result"])
        break
