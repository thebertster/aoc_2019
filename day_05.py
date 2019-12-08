from lib.aoclib import AOCLib

def run_program(program, program_input):
    pc = 0
    program_output = None

    while True:
        opcode = program[pc] % 100
        parameter_modes = program[pc] // 100
        if opcode == 1:
            a, b, c = program[pc + 1:pc + 4]
            a_value = a if parameter_modes  % 10 else program[a]
            b_value = b if (parameter_modes // 10) % 10 else program[b]
            program[c] = a_value + b_value
            pc += 4
        elif opcode == 2:
            a, b, c = program[pc + 1:pc + 4]
            a_value = a if parameter_modes % 10 else program[a]
            b_value = b if (parameter_modes // 10) % 10 else program[b]
            program[c] = a_value * b_value
            pc += 4
        elif opcode == 3:
            a = program[pc + 1]
            program[a] = program_input
            pc += 2
        elif opcode == 4:
            a = program[pc + 1]
            a_value = a if parameter_modes % 10 else program[a]
            program_output = a_value
            pc += 2
        elif opcode == 5:
            a, b = program[pc + 1: pc + 3]
            a_value = a if parameter_modes % 10 else program[a]
            b_value = b if (parameter_modes // 10) % 10 else program[b]
            if a_value != 0:
                pc = b_value
            else:
                pc += 3
        elif opcode == 6:
            a, b = program[pc + 1: pc + 3]
            a_value = a if parameter_modes % 10 else program[a]
            b_value = b if (parameter_modes // 10) % 10 else program[b]
            if a_value == 0:
                pc = b_value
            else:
                pc += 3
        elif opcode == 7:
            a, b, c = program[pc + 1:pc + 4]
            a_value = a if parameter_modes % 10 else program[a]
            b_value = b if (parameter_modes // 10) % 10 else program[b]
            program[c] = 1 if a_value < b_value else 0
            pc += 4
        elif opcode == 8:
            a, b, c = program[pc + 1:pc + 4]
            a_value = a if parameter_modes % 10 else program[a]
            b_value = b if (parameter_modes // 10) % 10 else program[b]
            program[c] = 1 if a_value == b_value else 0
            pc += 4
        elif opcode == 99:
            break

    return program_output

puzzle = (2019, 5)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.to_list_int)

diagnostic_code_1 = run_program(puzzle_input[:], 1)

aoc.print_solution(1, diagnostic_code_1)

diagnostic_code_2 = run_program(puzzle_input[:], 5)

aoc.print_solution(2, diagnostic_code_2)
