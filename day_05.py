from lib.aoclib import AOCLib
from intcode_computer import IntcodeComputer

puzzle = (2019, 5)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.to_list_int)

diagnostic_code_1 = IntcodeComputer(puzzle_input, 1). run_to_end()

aoc.print_solution(1, diagnostic_code_1)

diagnostic_code_2 = IntcodeComputer(puzzle_input, 5).run_to_end()

aoc.print_solution(2, diagnostic_code_2)
