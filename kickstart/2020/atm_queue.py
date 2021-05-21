import math

T = int(input())

for i in range (1, T + 1):
    answer = ""
    n, x = [int(s) for s in input().split(" ")]
    a = [int(s) for s in input().split(" ")]

    # print("Answer:", answer)
    # print("N:", n)
    # print("X:", x)
    # print("A:", a)

    attempts = {}
    for j in range(n):
        attempts[j + 1] = (math.ceil(a[j]/x))

    attempts = sorted(attempts.items(), key=lambda x: x[1])

    # print("Attempts:", attempts)

    for j in attempts:
        answer += str(j[0])
        answer += " "

    print ("Case #" + str(i) + ": " + answer)