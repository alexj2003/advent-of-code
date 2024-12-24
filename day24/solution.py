# Run instructions
def run_instructions(inputs, instructions, outputs):
    wires = inputs.copy()
    z_outputs = outputs.copy()
    to_solve = instructions.copy()

    # Run instructions until we have a value for each z output
    while z_outputs:
        for inp1, inp2, operator, out in to_solve:
            # Skip if we can't solve this instruction yet
            if inp1 not in wires or inp2 not in wires:
                continue

            if out not in wires:
                wires[out] = 0

            # Solve instruction
            if operator == "AND":
                wires[out] = wires[inp1] & wires[inp2]
            elif operator == "OR":
                wires[out] = wires[inp1] | wires[inp2]
            elif operator == "XOR":
                wires[out] = wires[inp1] ^ wires[inp2]
            
            # Remove instruction from list
            to_solve.remove((inp1, inp2, operator, out))

            if out in z_outputs:
                z_outputs.remove(out)
    
    return wires

# Part 1, get output of z values
def get_z_output_val(wires):
    result = 0
    for wire, val in wires.items():
        if val and wire.startswith("z"):
            result += 1 << int(wire[1:])
    
    return result

# Parse data
def parse_data(data):
    initial, instructions = data.strip().split("\n\n")
    
    inputs = {k: int(v) for k, v in [line.split(": ") for line in initial.split("\n")]}

    # (input 1, input 2, operator, output)
    operations = []
    outputs = []
    for line in instructions.split("\n"):
        inp, out = line.strip().split(" -> ")
        inp1, operator, inp2 = inp.split(" ")
        operations.append((inp1, inp2, operator, out))

        if out.startswith("z"):
            outputs.append(out)
    
    return inputs, operations, outputs

# Test data
data = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

# Read data
with open("input.txt", "r") as f:
    data = f.read()

inputs, operations, outputs = parse_data(data)

# Part 1
wires = run_instructions(inputs, operations, outputs)
result = get_z_output_val(wires)
print(f"Part 1: {result}")
