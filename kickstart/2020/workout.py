T = int(input())

for i in range (1, T + 1):
    difficulty = []
    n, k = [int(s) for s in input().split(" ")]

    program = [int(s) for s in input().split(" ")]

    for j in range(n - 1):
        difficulty.append(program[j + 1] - program[j])

    difficulty.sort(reverse = True)

    # print(difficulty)

    while (k > 0):
        for small in range(2, k + 2):
            if ((difficulty[0] / small) < (difficulty[1])):
                break

        for x in range(small):
            difficulty.insert(1, (difficulty[0] / small))

        difficulty.pop(0)
        difficulty.sort(reverse = True)

        k -= (small - 1)
        # print(k)
        # print(difficulty)

    print("Case #" + str(i) + ": " + str(int(difficulty[0])))