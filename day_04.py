from lib.aoclib import AOCLib

puzzle = (2019, 4)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

puzzle_input = aoc.get_puzzle_input(puzzle[1])

code_min, code_max = (int(n) for n in puzzle_input.split('-'))

criteria_met_1 = 0
criteria_met_2 = 0

for code in range(code_min, code_max + 1):
    last_digit = code % 10
    double_digit = 0
    repeated_digit = 0
    repeated_digit_count = 1
    for n in range(6):
        code //= 10
        digit = code % 10
        if digit > last_digit:
            break
        if digit == last_digit:
            repeated_digit_count += 1
        else:
            if repeated_digit_count >= 2:
                repeated_digit = 1
                if repeated_digit_count == 2:
                    double_digit = 1
            repeated_digit_count = 1
        last_digit = digit
    else:
        criteria_met_1 += repeated_digit
        criteria_met_2 += double_digit

aoc.print_solution(1, criteria_met_1)
aoc.print_solution(2, criteria_met_2)
