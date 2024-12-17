# Get combo value of operand
def combo(operand, registers):
    if operand == 0: 
        return 0
    elif operand == 1: 
        return 1
    elif operand == 2: 
        return 2
    elif operand == 3: 
        return 3
    elif operand == 4: 
        return registers["A"]
    elif operand == 5: 
        return registers["B"]
    elif operand == 6: 
        return registers["C"]
    else: 
        return None

# Read instructions
def read_instructions(registers, program):
    ip = 0 # Instruction pointer
    output = []

    while ip < len(program):
        instruction = program[ip]
        opcode = program[ip + 1]
        ip += 2

        if instruction == 0: # adv
            registers["A"] = registers["A"] // (2 ** combo(opcode, registers))
        elif instruction == 1: # bxl
            registers["B"] = registers["B"] ^ opcode
        elif instruction == 2: # bst
            registers["B"] = combo(opcode, registers) % 8
        elif instruction == 3: # jnz
            if registers["A"] != 0:
                ip = opcode
        elif instruction == 4: # bxc
            registers["B"] = registers["B"] ^ registers["C"]
        elif instruction == 5: # out
            output.append(combo(opcode, registers) % 8)
        elif instruction == 6: # bdv
            registers["B"] = registers["A"] // (2 ** combo(opcode, registers))
        elif instruction == 7: # cdv
            registers["C"] = registers["A"] // (2 ** combo(opcode, registers))
    
    return output

# Parse input
def parse_input(data):
    registers, program = data.strip().split("\n\n")
    
    reg_dict = {}
    for register in registers.split("\n"):
        reg, val = register.split("Register ")[1].split(": ")
        reg_dict[reg] = int(val)
    
    program = [int(x) for x in program.split("Program: ")[1].split(",")]

    return reg_dict, program

# Read input
with open("input.txt", "r") as f:
    data = f.read()

# Test data
# data = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

# data = """Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0"""

# Part 1
registers, program = parse_input(data)
output = read_instructions(registers, program)
print(f"Part 1: {",".join(map(str, output))}")

# Part 2
a = 0
for i in range(len(program)):
    # Construct the program in reverse
    search_for = program[len(program) - i - 1:]
    offset = 0

    while True:
        # Shift a by 3 bits - program does the reverse when looping
        a_val = (a << 3) + offset
        new_regs = {
            "A": a_val,
            "B": 0,
            "C": 0
        }

        output = read_instructions(new_regs, program)
        if output == search_for:
            a = a_val
            break
        offset += 1

print(f"Part 2: {a}")
