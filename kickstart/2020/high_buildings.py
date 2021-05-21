T = int(input())

for i in range (1, T + 1):
    the_answer = 0
    n, a, b, c = [int(s) for s in input().split(" ")]

    if ((a + b - c > n) or (n > 1 and a == 1 and b == 1)):
        print ("Case #" + str(i) + ": " + "IMPOSSIBLE")
    elif (n == 1):
        print ("Case #" + str(i) + ": " + str(n))
    else:
        buildings = [0] * n

        buildings_left = a - c
        buildings_right = b - c

        if (buildings_left == 0):
            buildings[0] = n
            c -= 1
        else:
            for j in range(buildings_left):
                buildings[j] = n - 1

        if (buildings_right == 0):
            buildings[n-1] = n
            c -= 1
        else:
            for j in range(1, buildings_right + 1):
                buildings[n - j] = n - 1
        
        for j in range(c):
            buildings[buildings.index(0)] = n

        while 0 in buildings:
            buildings[buildings.index(0)] = 1

        print ("Case #" + str(i) + ":", *buildings)