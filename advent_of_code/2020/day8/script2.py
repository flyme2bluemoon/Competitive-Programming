accumulator = 0

program = {}

with open("input", "r") as f:
    address = 0
    for i in f:
        instruction, argument = [_ for _ in i.strip("\n").split(" ")]
        program[address] = [instruction, argument]
        address += 1

def modify_program(n):
    if program[n][0] == "jmp":
        program[n][0] = "nop"
    elif program[n][0] == "nop":
        program[n][0] = "jmp"

def run_program():
    history = []
    accumulator = 0
    i = 0
    while i < 637:
        if i in history:
            return False
        else:
            history.append(i)
        if program[i][0] == "acc":
            accumulator += int(program[i][1])
            i += 1
        elif program[i][0] == "jmp":
            i += int(program[i][1])
        elif program[i][0] == "nop":
            i += 1
    print(accumulator)
    return True

for j in range(638):
    modify_program(j)
    if run_program():
        break
    modify_program(j)