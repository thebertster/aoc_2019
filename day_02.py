from lib.aoclib import AOCLib

def run_program(program):
    pc = 0

    while True:
        opcode = program[pc]
        if opcode == 1:
            a, b, c = program[pc + 1:pc + 4]
            program[c] = program[a] + program[b]
            pc += 4
        elif opcode == 2:
            a, b, c = program[pc + 1:pc + 4]
            program[c] = program[a] * program[b]
            pc += 4
        elif opcode == 99:
            break

    return program[0]

puzzle = (2019, 2)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.to_list_int)
magic_number = 19690720

part_one = puzzle_input[:]

part_one[1:3] = [12, 2]

part_one_solution = run_program(part_one)

aoc.print_solution(1, part_one_solution)

for noun in range(100):
    for verb in range(100):
        part_two = puzzle_input[:]
        part_two[1:3] = [noun, verb]
        part_two_solution = run_program(part_two)
        if part_two_solution == magic_number:
            break
    else:
        continue
    break

aoc.print_solution(2, 100 * noun + verb)
