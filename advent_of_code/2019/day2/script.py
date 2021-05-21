with open("input", "r") as f:
    intcode_program = [int(s) for s in f.readline().strip("\n").split(",")]
    intcode_program[1] = 12
    intcode_program[2] = 2

for i in range(0, len(intcode_program), 4):
    if intcode_program[i] == 1:
        intcode_program[intcode_program[i + 3]] = intcode_program[intcode_program[i + 1]] + intcode_program[intcode_program[i + 2]]
    elif intcode_program[i] == 2:
        intcode_program[intcode_program[i + 3]] = intcode_program[intcode_program[i + 1]] * intcode_program[intcode_program[i + 2]]
    elif intcode_program[i] == 99:
        break

print(intcode_program)