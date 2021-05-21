T = int(input())

for i in range (1, T + 1):
    house = 0
    n = [int(s) for s in input().split(" ")]
    b = [int(s) for s in input().split(" ")]

    b.sort()

    for j in range (n[0]):
        n[1] -= b[j]
        if (n[1] >= 0):
            house += 1

    print ("Case #" + str(i) + ": " + str(house))