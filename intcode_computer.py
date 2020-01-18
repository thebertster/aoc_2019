class IntcodeMemory:
    def __init__(self, initial_data):
        self._data = dict(enumerate(initial_data))

    def __getitem__(self, given):
        if isinstance(given, slice):
            return [self._data.get(index, 0)
                    for index in range(given.start, given.stop)]
        return self._data.get(given, 0)

    def __setitem__(self, index, value):
        self._data[index] = value


class IntcodeComputer:
    def __init__(self, starting_program, *args):
        self._program = IntcodeMemory(starting_program)
        self._input = list(args)
        self._last_output = None

    def add_input(self, *args):
        self._input.extend(args)

    def get_last_output(self):
        return self._last_output

    def run_to_end(self):
        for dummy in self.run_program():
            pass
        return self._last_output

    def _get_data(self, data, parameter_mode, rb):
        return (self._program[data] if parameter_mode == 0
                else data if parameter_mode == 1
                else self._program[rb + data])

    def run_program(self):
        pc = 0
        rb = 0
        while True:
            opcode = self._program[pc] % 100
            parameter_mode_a = (self._program[pc] // 100) % 10
            parameter_mode_b = (self._program[pc] // 1000) % 10
            parameter_mode_c = (self._program[pc] // 10000) % 10
            if opcode == 1:
                a, b, c = self._program[pc + 1:pc + 4]
                a_value = self._get_data(a, parameter_mode_a, rb)
                b_value = self._get_data(b, parameter_mode_b, rb)
                c_value = rb + c if parameter_mode_c == 2 else c
                self._program[c_value] = a_value + b_value
                pc += 4
            elif opcode == 2:
                a, b, c = self._program[pc + 1:pc + 4]
                a_value = self._get_data(a, parameter_mode_a, rb)
                b_value = self._get_data(b, parameter_mode_b, rb)
                c_value = rb + c if parameter_mode_c == 2 else c
                self._program[c_value] = a_value * b_value
                pc += 4
            elif opcode == 3:
                a = self._program[pc + 1]
                a_value = rb + a if parameter_mode_a == 2 else a
                self._program[a_value] = self._input.pop(0)
                pc += 2
            elif opcode == 4:
                a = self._program[pc + 1]
                a_value = self._get_data(a, parameter_mode_a, rb)
                self._last_output = a_value
                pc += 2
                yield a_value
            elif opcode == 5:
                a, b = self._program[pc + 1:pc + 3]
                a_value = self._get_data(a, parameter_mode_a, rb)
                b_value = self._get_data(b, parameter_mode_b, rb)
                if a_value != 0:
                    pc = b_value
                else:
                    pc += 3
            elif opcode == 6:
                a, b = self._program[pc + 1:pc + 3]
                a_value = self._get_data(a, parameter_mode_a, rb)
                b_value = self._get_data(b, parameter_mode_b, rb)
                if a_value == 0:
                    pc = b_value
                else:
                    pc += 3
            elif opcode == 7:
                a, b, c = self._program[pc + 1:pc + 4]
                a_value = self._get_data(a, parameter_mode_a, rb)
                b_value = self._get_data(b, parameter_mode_b, rb)
                c_value = rb + c if parameter_mode_c == 2 else c
                self._program[c_value] = 1 if a_value < b_value else 0
                pc += 4
            elif opcode == 8:
                a, b, c = self._program[pc + 1:pc + 4]
                a_value = self._get_data(a, parameter_mode_a, rb)
                b_value = self._get_data(b, parameter_mode_b, rb)
                c_value = rb + c if parameter_mode_c == 2 else c
                self._program[c_value] = 1 if a_value == b_value else 0
                pc += 4
            elif opcode == 9:
                a = self._program[pc + 1]
                a_value = self._get_data(a, parameter_mode_a, rb)
                rb += a_value
                pc += 2
            elif opcode == 99:
                return
