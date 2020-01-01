from lib.aoclib import AOCLib
from permutations import permutations
from intcode_computer import IntcodeComputer


puzzle = (2019, 7)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.to_list_int)

highest_signal = 0

for phase in permutations(range(5)):
    last_output = 0
    for amp in range(5):
        computer = IntcodeComputer(puzzle_input, phase[amp], last_output)
        last_output = next(computer.run_program())
    if last_output > highest_signal:
        highest_signal = last_output

aoc.print_solution(1, highest_signal)

max_thruster_signal = -1

for phase in permutations(range(5, 10)):
    computers = []
    generators = []
    for amp in range(5):
        computers.append(IntcodeComputer(puzzle_input))
        computers[amp].add_input(phase[amp])
        generators.append(computers[amp].run_program())
    data = 0
    amp = 0
    while True:
        computers[amp].add_input(data)
        try:
            data = next(generators[amp])
        except StopIteration:
            if amp == 4:
                last_output = computers[4].get_last_output()
                if last_output > max_thruster_signal:
                    max_thruster_signal = last_output
                break
        amp = (amp + 1) % 5

aoc.print_solution(2, max_thruster_signal)
