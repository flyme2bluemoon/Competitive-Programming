T = int(input())

for j in range (T):
    breakers = 0
    record = -1
    N = int(input())
    v = [int(s) for s in input().split() if s.isdigit()]

    for i in range((N - 1)):
        if v[i] > record:
            record = v[i]
            if v[i] > v[i + 1]:
                breakers += 1

    if v[(N - 1)] > record:
        breakers += 1

    print ("Case #" + str(j + 1) + ": " + str(breakers))