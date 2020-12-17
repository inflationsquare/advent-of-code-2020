import re

with open("8.in", "r") as f:
    data = f.read().splitlines()

pattern = re.compile("^(nop|acc|jmp) ([\+-]\d+)$")

instructions = [[ix, op, int(off)] for (ix, [(op, off)]) in enumerate(map(lambda x: pattern.findall(x), data))]


class Interpreter:
    def __init__(self, instructions, swapop=None):
        self.instructions = instructions
        self.acc = 0
        self.ptr = 0
        self.visited_instructions = set()
        self.status = "initialised"
        self.ix, self.current_op, self.arg = self.instructions[self.ptr]
        self.swapop = swapop

    def __iter__(self):
        return self

    def __next__(self):
        if self.ptr == len(self.instructions):
            self.status = "finished"
            raise StopIteration

        elif self.instructions[self.ptr][0] in self.visited_instructions:
            self.status = "looped"
            raise StopIteration

        else:
            self.ix, self.current_op, self.arg = self.instructions[self.ptr]
            if self.swapop and self.ix == self.swapop:
                if self.current_op == "jmp":
                    self.current_op = "nop"
                elif self.current_op == "nop":
                    self.current_op = "jmp"

            self.status = "running"
            self.op(self.current_op, self.arg)
            self.visited_instructions.add(self.ix)
        return self

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
looped_nodes = machine.visited_instructions
machine.reset()

swappable = [i[0] for i in instructions if i[1] in ["jmp", "nop"] and i[0] in looped_nodes]
for swap in swappable:
    result = machine.run(swap)
    machine.reset()
    if result["code"] == 0:
        print(result["result"])
        break

# for s in swappable:
# new_machine = Interpreter(instructions)
# new_machine.swapop = s
# for i in new_machine:
# pass
# if new_machine.status == "finished":
# print(new_machine.acc)
# break
