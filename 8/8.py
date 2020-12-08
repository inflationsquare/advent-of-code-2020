import re
import copy

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
                return self.acc
        return None

    def reset(self):
        self.acc = 0
        self.ptr = 0
        self.visited_instructions = set()

    def find_loop(self):
        while self.instructions[self.ptr][0] not in self.visited_instructions:
            ix, op, arg = self.instructions[self.ptr]
            self.op(op, arg)
            self.visited_instructions.add(ix)
        return self.acc

    def find_unreachable(self):
        target = len(self.instructions)
        instruction_targets = [(i[0], i[0] + i[2] if i[1] == "jmp" else i[0] + 1) for i in self.instructions]

        def recur(target):
            if target not in [x[1] for x in instruction_targets]:
                return target
            else:
                new_target = next(filter(lambda x: x[1] == target, instruction_targets))[0]
                return recur(new_target)

        return recur(target)


machine = Interpreter(instructions)
print(machine.find_loop())

swappable = [i[0] for i in filter(lambda x: x[1] in ["jmp", "nop"], instructions)]
for swap in swappable:
    fixed_machine = Interpreter(instructions)
    result = fixed_machine.run(swap)
    if result:
        print(result)
