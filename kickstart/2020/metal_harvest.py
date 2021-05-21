T = int(input())

for i in range (1, T + 1):
    answer = 0
    n, k = [int(s) for s in input().split(" ")]

    harvest_interval = []
    for j in range(n):
        x, y = [int(s) for s in input().split(" ")]
        harvest_interval.append((x, y))

    harvest_interval.sort()

    harvest_interval_raw = []
    for j in harvest_interval:
        harvest_interval_raw += list(range(j[0], j[1] + 1))

    print(n, k)
    print(harvest_interval)
    print(harvest_interval_raw)

    print ("Case #" + str(i) + ": " + str(answer))