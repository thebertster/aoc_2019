from lib.aoclib import AOCLib
from intcode_computer import IntcodeComputer


puzzle = (2019, 9)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.to_list_int)

test_mode = IntcodeComputer(puzzle_input, 1).run_to_end()

aoc.print_solution(1, test_mode)

coordinates = IntcodeComputer(puzzle_input, 2).run_to_end()

aoc.print_solution(1, coordinates)
