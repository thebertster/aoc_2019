from math import atan2, cos, sin, sqrt
from lib.aoclib import AOCLib


puzzle = (2019, 10)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

asteroids = []

for y, row in enumerate(puzzle_input):
    for x, obj in enumerate(row):
        if obj == '#':
            asteroids.append((x, y))

most_visible = (-1, None)

rounding_factor = -100000
best_asteroid = None

for asteroid in asteroids:
    rays = {}
    for other_asteroid in asteroids:
        if asteroid != other_asteroid:
            x, y = ((other_asteroid[0] - asteroid[0]),
                    (other_asteroid[1] - asteroid[1]))
            direction = round(rounding_factor * atan2(x, y))
            magnitude = sqrt(x*x + y*y)
            rays.setdefault(direction, []).append(magnitude)
    visible_asteroids = len(rays)
    if visible_asteroids > most_visible[0]:
        most_visible = (visible_asteroids, rays, asteroid)

aoc.print_solution(1, most_visible[0])

visible_asteroids = most_visible[1]
directions = sorted(visible_asteroids.keys())

asteroids_to_vaporise = 200
while True:
    for direction in directions:
        asteroids_in_direction = visible_asteroids[direction]
        if asteroids_in_direction:
            closest_asteroid_distance = min(asteroids_in_direction)
            asteroids_in_direction.remove(closest_asteroid_distance)
            asteroids_to_vaporise -= 1
            if asteroids_to_vaporise == 0:
                break
    else:
        continue
    break

angle = direction/rounding_factor
x = most_visible[2][0] + round(closest_asteroid_distance * sin(angle))
y = most_visible[2][1] + round(closest_asteroid_distance * cos(angle))

aoc.print_solution(2, 100*x + y)
