from lib.aoclib import AOCLib

puzzle = (2019, 6)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

orbits = {}
orbited_by = {}

for pair in puzzle_input:
    body_1, body_2 = pair.split(')')
    orbits[body_2] = body_1
    if body_1 in orbited_by:
        orbited_by[body_1].append(body_2)
    else:
        orbited_by[body_1] = [body_2]

body_stack = ['COM']
orbit_count = {'COM': 0}

while body_stack:
    body = body_stack.pop()
    for orbiting_body in orbited_by.get(body, []):
        orbit_count[orbiting_body] = orbit_count[body] + 1
        body_stack.append(orbiting_body)

total_orbits = sum(orbit_count.values())

aoc.print_solution(1, total_orbits)

you_path = []
body = 'SAN'

while body != 'COM':
    you_path.append(orbits[body])
    body = orbits[body]

san_path = []
body = 'YOU'

while body not in you_path:
    san_path.append(orbits[body])
    body = orbits[body]

aoc.print_solution(2, orbit_count['YOU'] +
                   orbit_count['SAN'] -
                   2*orbit_count[body] - 2)
