import  sys

def handle_hexadecimal_value(value):
    value = value.replace(',', '')
    value_size = len(value)

    if value_size > 4:
        first_hex = int(value[:4], 16)
        second_hex = int('0x' + value[4:], 16)

        return bytes([second_hex,first_hex])

    hex_value = int(value.replace(',', ''), 16)
    return bytes([hex_value])

def handle_char_value(value: str):
    value = value.replace(',', '').replace('\'', '')
    return value.encode('utf-8')

def get_register_mov_opcode(register):
    if register == 'al':
        return bytes([176])
    elif register == 'ah':
        return bytes([180])

def mov_instruction(instructions, index):
    value = instructions[index+1].replace('$', '')
    register = instructions[index+2].replace('%', '')

    if register[0] == '\'':
        value = '\' \','
        register = instructions[index+3].replace('%', '')

    prefix = value[0]
    if prefix == '0':
        value = handle_hexadecimal_value(value)
    if prefix == '\'':
        value = handle_char_value(value)

    register = get_register_mov_opcode(register)

    return register+value

def int_instruction(instructions, index):
    value = instructions[index+1].replace('$', '')
    value = handle_hexadecimal_value(value)

    opcode = bytes([205])
    
    return opcode+value

def jmp_instruction():
    return bytes([235, 253])

def hlt_instruction():
    return bytes([244])

def word_instruction(instructions, index):
    return handle_hexadecimal_value(instructions[index+1].replace('$', ''))

## Main

argv = sys.argv

if (len(argv)) < 3:
    print("Invalid usage. Try hwasm.py inputfile.as outputfile.bin")

try:
    input_filename = argv[1]
    input_file = open(input_filename, "r")
except:
    print("Failure opening input file " + input_filename)

try:
    output_filename = argv[2]
    output_file = open(output_filename, "wb")
except:
    print("Failure opening output file " + output_file)

line = input_file.readline()
while(line):
    instructions = line.rstrip().split()
    for index in range(len(instructions)):
        instruction = instructions[index]

        if instruction == '#':
            break
        elif instruction == 'mov':
            binary = mov_instruction(instructions, index)
            output_file.write(binary)
        elif instruction == 'int':
            binary = int_instruction(instructions, index)
            output_file.write(binary)
        elif instruction == 'hlt':
            binary = hlt_instruction()
            output_file.write(binary)
        elif instruction == 'jmp':
            binary = jmp_instruction()
            output_file.write(binary)
        elif instruction == '.fill':
            # auto-filling with zeros
            output_file.write(bytes(461))
        elif instruction == '.word':
            binary = word_instruction(instructions, index)
            output_file.write(binary)

    line = input_file.readline()

input_file.close()
output_file.close()