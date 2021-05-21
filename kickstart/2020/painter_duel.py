T = int(input())

for i in range (1, T + 1):
    answer = 0
    s, ra, pa, rb, pb, c = [int(s) for s in input().split(" ")]
    under_construction = []
    for i in range(c):
        ri, pi = [int(s) for s in input().split(" ")]
        under_construction.append((ri, pi))

    print(s, ra, pa, rb, pb, c)
    print(under_construction)

    print ("Case #" + str(i) + ": " + str(answer))