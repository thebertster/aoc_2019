from lib.aoclib import AOCLib
from intcode_computer import IntcodeComputer

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def paint_ship(program, start_colour):
    location = (0, 0)
    direction = 0

    panels = {}

    panels[location] = start_colour

    computer = IntcodeComputer(program)

    program_output = computer.run_program()

    while True:
        current_panel = panels.setdefault(location)
        computer.add_input(0 if current_panel is None else current_panel)
        try:
            colour = next(program_output)
            turn = next(program_output)
        except StopIteration:
            break
        panels[location] = colour
        direction = (direction + turn*2 - 1) % 4
        location = (location[0] + DIRECTIONS[direction][0],
                    location[1] + DIRECTIONS[direction][1])

    return panels


puzzle = (2019, 11)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.to_list_int)

panels_painted = len(paint_ship(puzzle_input, 0))

aoc.print_solution(1, panels_painted)

registration_id = paint_ship(puzzle_input, 1)

min_x = min([location[0] for location in registration_id])
max_x = max([location[0] for location in registration_id])
min_y = min([location[1] for location in registration_id])
max_y = max([location[1] for location in registration_id])

registration_id_string = ''

for y in range(max_y, min_y - 1, -1):
    registration_id_string += '\r\n'
    for x in range(min_x, max_x + 1):
        registration_id_string += ('#' if registration_id.get((x, y), 0) == 1
                                   else ' ')

aoc.print_solution(2, registration_id_string)
