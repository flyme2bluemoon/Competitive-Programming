T = int(input())

for i in range (1, T + 1):
    beauty_value = 0
    plates = 0
    n, k, p = [int(s) for s in input().split(" ")]

    stacks = {}
    for j in range(n):
        stacks["stack{0}".format(j)] = [int(s) for s in input().split(" ")]

    while (plates < p):
        scores = {}
        for j in range(n):
            stack_sum = 0
            if (len(stacks["stack{0}".format(j)]) > (p - plates)):
                x = (p - plates)
            else:
                x = len(stacks["stack{0}".format(j)])
            for l in range(x):
                stack_sum += stacks["stack{0}".format(j)][l]
                scores["{0},{1}".format(j,l)] = (stack_sum / (l + 1))

        record = 0
        for j in range(n):
            if (len(stacks["stack{0}".format(j)]) > (p - plates)):
                x = (p - plates)
            else:
                x = len(stacks["stack{0}".format(j)])
            current_value = 0
            for l in range(x):
                current_value += stacks["stack{0}".format(j)][l]
                if (scores["{0},{1}".format(j,l)] > record):
                    record = scores["{0},{1}".format(j,l)]
                    record_breaker = stacks["stack{0}".format(j)][l]
                    stack = j
                    index = l
                    added_value = current_value

        plates += (index + 1)
        beauty_value += added_value

        stacks["stack{0}".format(stack)].remove(record_breaker)

    print("Case #" + str(i) + ": " + str(beauty_value))