with open("input", "r") as f:
    intcode_program = [int(s) for s in f.readline().strip("\n").split(",")]

def run_program(arr):
    try:
        for i in range(0, len(arr), 4):
            if arr[i] == 1:
                arr[arr[i + 3]] = arr[arr[i + 1]] + arr[arr[i + 2]]
            elif arr[i] == 2:
                arr[arr[i + 3]] = arr[arr[i + 1]] * arr[arr[i + 2]]
            elif arr[i] == 99:
                break
        return arr[0]
    except IndexError:
        return 0

for a in range(0,100):
    for b in range(0,100):
        copy_of_intcode = intcode_program.copy()
        copy_of_intcode[1] = a
        copy_of_intcode[2] = b
        result = run_program(copy_of_intcode)
        if result == 19690720:
            print(f"a: {a}")
            print(f"b: {b}")
            print(100 * a + b)
            break