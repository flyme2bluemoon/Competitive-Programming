T = int(input())

def works (k):
    for j in range(n):
        if (k % bus_routes[j] != 0):
            k += (bus_routes[j] - k % bus_routes[j])

    return (k <= d)

for i in range(1, T + 1):
    last_day = 0
    n, d = [int(s) for s in input().split(" ")]
    bus_routes = [int(s) for s in input().split(" ")]

    low, high = 0, d

    while (high > low):
        mid = int((low + high + 1) / 2)
        if (works(mid)):
            low = mid
        else:
            high = mid - 1
    
    print("Case #" + str(i) + ": " + str(low))



# 3
# 3 10
# 3 7 2
# 4 100
# 11 10 5 50
# 1 1
# 1