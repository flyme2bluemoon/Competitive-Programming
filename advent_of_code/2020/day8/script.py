accumulator = 0

program = {}
history = []

with open("input", "r") as f:
    address = 0
    for i in f:
        instruction, argument = [_ for _ in i.strip("\n").split(" ")]
        program[address] = [instruction, argument]
        address += 1

i = 0
while True:
    if i in history:
        break
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