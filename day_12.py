from lib.aoclib import AOCLib


def sign(x):
    return -1 if x < 0 else 1 if x > 0 else 0

puzzle = (2019, 12)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

moons = []

for line in puzzle_input:
    moon = ([0, 0, 0], [0, 0, 0])
    coords = line[1:-1].split(', ')
    for coord in coords:
        key, value = coord.split('=')
        axis = 'xyz'.index(key)
        moon[0][axis] = int(value)
    moons.append(moon)

for step in range(1000):
    for moon1 in moons:
        for moon2 in moons:
            if moon1 != moon2:
                for axis in (0, 1, 2):
                    moon1[1][axis] += sign(moon2[0][axis] - moon1[0][axis])
    for moon in moons:
        for axis in (0, 1, 2):
            moon[0][axis] += moon[1][axis]

total_energy = 0

for moon in moons:
    potential_energy = abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2])
    kinetic_energy = abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2])
    total_energy += potential_energy * kinetic_energy

aoc.print_solution(1, total_energy)
