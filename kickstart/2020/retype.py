T = int(input())

for i in range (1, T + 1):
    time = 0
    n, k, s = [int(s) for s in input().split(" ")]
    
    time = k - 1
    time_to_restart = n + 1
    time_to_return = (k - s) + (n - s) + 1

    # print(time)
    # print(time_to_restart)
    # print(time_to_return)

    if time_to_restart < time_to_return:
        time += time_to_restart
    else:
        time += time_to_return

    print ("Case #" + str(i) + ": " + str(time))