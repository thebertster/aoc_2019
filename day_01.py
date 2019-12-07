from lib.aoclib import AOCLib

puzzle = (2019, 1)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list_int)

module_fuel_count = 0
actual_fuel_count = 0

for module_mass in puzzle_input:
    additional_fuel = (module_mass // 3) - 2
    module_fuel_count += additional_fuel
    while additional_fuel > 0:
        actual_fuel_count += additional_fuel
        additional_fuel = (additional_fuel // 3) - 2

aoc.print_solution(1, module_fuel_count)
aoc.print_solution(2, actual_fuel_count)
