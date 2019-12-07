from lib.aoclib import AOCLib

puzzle = (2019, 3)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

wire_path_1 = AOCLib.to_list(puzzle_input[0])
wire_path_2 = AOCLib.to_list(puzzle_input[1])

grid = {}
directions = {'U': lambda p: (p[0], p[1] + 1),
              'R': lambda p: (p[0] + 1, p[1]),
              'D': lambda p: (p[0], p[1] - 1),
              'L': lambda p: (p[0] - 1, p[1])}

origin = (0, 0)

current = origin

step = 0

for part in wire_path_1:
    move = directions[part[0]]
    count = int(part[1:])
    for n in range(count):
        if current not in grid:
            grid[current] = step
        current = move(current)
        step += 1

current = origin
shortest_crossing = 0
shortest_steps = 0

step = 0

for part in wire_path_2:
    move = directions[part[0]]
    count = int(part[1:])
    for n in range(count):
        if current in grid and current != origin:
            manhattan = abs(current[0]) + abs(current[1])
            if shortest_crossing == 0 or manhattan < shortest_crossing:
                shortest_crossing = manhattan
            steps = grid[current] + step
            if shortest_steps == 0 or steps < shortest_steps:
                shortest_steps = steps
        current = move(current)
        step += 1

aoc.print_solution(1, shortest_crossing)
aoc.print_solution(1, shortest_steps)
