import argparse

def read_program(filename):
    with open(filename, 'r') as f:
        program = f.read()
    return program
def parse(program):
    instructions = []
    stack = []
    for char in program:
        if char == '>':
            instructions.append(('ptr', 1))
        elif char == '<':
            instructions.append(('ptr', -1))
        elif char == '+':
            instructions.append(('inc', 1))
        elif char == '-':
            instructions.append(('inc', -1))
        elif char == '.':
            instructions.append(('out', None))
        elif char == ',':
            instructions.append(('in', None))
        elif char == '[':
            instructions.append(('start', None))
            stack.append(len(instructions) - 1)
        elif char == ']':
            start = stack.pop()
            instructions[start] = ('start', len(instructions))
            instructions.append(('end', start))
    return instructions
def execute(instructions):
    memory = [0] * 30000
    ptr = 0
    pc = 0
    while pc < len(instructions):
        inst, arg = instructions[pc]
        if inst == 'ptr':
            ptr += arg
        elif inst == 'inc':
            memory[ptr] += arg
        elif inst == 'out':
            print(chr(memory[ptr]), end='')
        elif inst == 'in':
            memory[ptr] = ord(input())
        elif inst == 'start' and memory[ptr] == 0:
            pc = arg
        elif inst == 'end' and memory[ptr] != 0:
            pc = arg
        pc += 1
def main(filename):
    program = read_program(filename)
    instructions = parse(program)
    execute(instructions)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Brainfuck Compiler')
    parser.add_argument('filename', help='Brainfuck program file')
    args = parser.parse_args()
    main(args.filename)
