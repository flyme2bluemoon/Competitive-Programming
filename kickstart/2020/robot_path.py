T = int(input())

for i in range (1, T + 1):
    w = 1
    h = 1

    program = input()

    functions = 1
    functions_stack = []
    
    for j in range(len(program)):
        if (program[j] == "N"):
            h -= functions
        elif (program[j] == "S"):
            h += functions
        elif (program[j] == "W"):
            w -= functions
        elif (program[j] == "E"):
            w += functions
        elif (program[j] in "23456789"):
            functions *= int(program[j])
            functions_stack.append(int(program[j]))
        elif (program[j] == ")"):
            functions //= functions_stack.pop()

    h = int(h % (10 ** 9))
    w = int(w % (10 ** 9))

    if (h == 0):
        h = (10 ** 9)
    if (w == 0):
        w = (10 ** 9)

    print ("Case #" + str(i) + ":", str(w), str(h))