from helper import load_input
import itertools

class Program:
    def __init__(self, register_a, register_b, register_c, program):
        self.register_a = register_a
        self.register_b = register_b
        self.register_c = register_c
        self.program = program
        self.instruction_pointer = 0
        self.output = []

    def reset(self):
        self.register_a = 0
        self.register_b = 0
        self.register_c = 0
        self.instruction_pointer = 0
        self.output = []

    def get_operand_value(self, operand):
        if operand == 4:
            return self.register_a
        elif operand == 5:
            return self.register_b
        elif operand == 6:
            return self.register_c
        elif operand in [0, 1, 2, 3]:
            return operand
        else:
            raise ValueError("Invalid operand")

    def adv(self, operand):
        value = self.get_operand_value(operand)
        self.register_a //= 2 ** value

    def bxl(self, operand):
        value = operand
        self.register_b ^= value

    def bst(self, operand):
        value = self.get_operand_value(operand)
        self.register_b = value % 8

    def jnz(self, operand):
        value = operand
        if self.register_a != 0:
            self.instruction_pointer = value
            return True
        return False

    def bxc(self, operand):
        self.register_b ^= self.register_c

    def out(self, operand):
        value = self.get_operand_value(operand)
        self.output.append(str(value % 8))

    def bdv(self, operand):
        value = self.get_operand_value(operand)
        self.register_b = self.register_a // (2 ** value)

    def cdv(self, operand):
        value = self.get_operand_value(operand)
        self.register_c = self.register_a // (2 ** value)

    def execute_instruction(self):
        opcode = self.program[self.instruction_pointer]
        operand = self.program[self.instruction_pointer + 1]
        self.instruction_pointer += 2

        if opcode == 0:
            self.adv(operand)
        elif opcode == 1:
            self.bxl(operand)
        elif opcode == 2:
            self.bst(operand)
        elif opcode == 3:
            if self.jnz(operand):
                return
        elif opcode == 4:
            self.bxc(operand)
        elif opcode == 5:
            self.out(operand)
        elif opcode == 6:
            self.bdv(operand)
        elif opcode == 7:
            self.cdv(operand)

    def run(self):
        while self.instruction_pointer < len(self.program):
            self.execute_instruction()
        return ','.join(self.output)

def parse_input(input_str):
    lines = input_str.strip().split('\n')
    register_a = int(lines[0].split(': ')[1])
    register_b = int(lines[1].split(': ')[1])
    register_c = int(lines[2].split(': ')[1])
    program = list(map(int, lines[4].split(': ')[1].split(',')))
    return Program(register_a, register_b, register_c, program)

def part1(contents):
    program = parse_input(contents)
    return program.run()

def part2(contents):
    program = parse_input(contents)
    original_program = ','.join([str(x) for x in program.program])
    for i in itertools.count(start=175900000000000, step=1):
    # i = int(input("register_a: "))
    # while True:
        program.reset()
        program.register_a = i
        output = program.run()
        # print(output)
        if output == original_program:
            return i
        # print(output, "output")
        # print(original_program, "original")
        # i = int(input("Try again. register_a: "))
    

if __name__ == "__main__":
    test_input = load_input("day17_test").read()
    test_solution = part1(test_input)
    assert test_solution == "4,6,3,5,6,3,5,2,1,0", test_solution

    puzzle_input = load_input("day17").read()
    puzzle_solution = part1(puzzle_input)
    print(f"Part1: {puzzle_solution}")

    # test_input = load_input("day17_test2").read()
    # test_solution = part2(test_input)
    # assert test_solution == 117440, test_solution

    puzzle_solution = part2(puzzle_input)
    print(f"Part2: {puzzle_solution}")
