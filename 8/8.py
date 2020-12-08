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

    def run(self):
        while self.instructions[self.ptr][0] not in self.visited_instructions:
            print(self.instructions[self.ptr])
            ix, op, arg = self.instructions[self.ptr]
            self.op(op, arg)
            self.visited_instructions.add(ix)
            if self.ptr == len(instructions):
                return self.acc
        print("Loop detected, terminating")
        return self.acc

    def reset(self):
        self.acc = 0
        self.ptr = 0
        self.visited_instructions = set()

    def find_loop(self):
        while (self.instructions[self.ptr][0]) not in self.visited_instructions:
            ix, op, arg = self.instructions[self.ptr]
            self.op(op, arg)
            self.visited_instructions.add(ix)
        return self.acc

    def find_unreachable(self):
        target = len(self.instructions)
        instruction_targets = [(i[0], i[0] + i[2] if i[1] == "jmp" else i[0] + 1) for i in self.instructions]
        # print(f"targets: {instruction_targets}")

        def recur(target):
            # print(f"checking {target}")
            if target not in [x[1] for x in instruction_targets]:
                # print("not found")
                return target
            else:
                new_target = next(filter(lambda x: x[1] == target, instruction_targets))[0]
                # print(f"found. Checking source: {new_target}")
                return recur(new_target)

        return recur(target)


machine = Interpreter(instructions)
print(machine.find_loop())

unreachable = machine.find_unreachable()
print(f"unreachable target: {unreachable}")

swapped_targets = [
    (i[0], i[0] + 1 if i[1] == "jmp" else i[0] + i[2]) for i in filter(lambda x: x[1] in ["jmp", "nop"], instructions)
]

corrupt_op = next(filter(lambda x: x[1] == unreachable, swapped_targets))[0]
print(instructions[corrupt_op])

if instructions[corrupt_op][1] == "jmp":
    print("swapping jmp to nop")
    instructions[corrupt_op][1] = "nop"
else:
    print("swapping nop to jmp")
    instructions[corrupt_op][1] = "jmp"

fixed_machine = Interpreter(instructions)
print(fixed_machine.run())
