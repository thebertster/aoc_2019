from lib.aoclib import AOCLib

puzzle = (2019, 8)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.sequence_to_int)

width = 25
height = 6
layer_size = width * height
layers = len(puzzle_input) // layer_size

min_number_of_zeroes = width + 1
ones_times_twos = None

image = [0] * layer_size

for layer in range(layers-1, -1, -1):
    digit_count = [0, 0, 0]
    for pixel_pos in range(layer_size):
        pixel = puzzle_input[layer * layer_size + pixel_pos]
        digit_count[pixel] += 1
        if pixel != 2:
            image[pixel_pos] = pixel
    if digit_count[0] < min_number_of_zeroes:
        min_number_of_zeroes = digit_count[0]
        ones_times_twos = digit_count[1] * digit_count[2]

aoc.print_solution(1, ones_times_twos)

raster = '\r\n'

for row in range(height):
    for col in range(width):
        pixel = image[row * width + col]
        raster += ' ' if pixel == 0 else '#' if pixel == 1 else '?'
        raster += ' ' if pixel == 0 else '#' if pixel == 1 else '?'
    raster += '\r\n'

aoc.print_solution(2, raster)
