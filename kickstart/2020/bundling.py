T = int(input())

for i in range (1, T + 1):
    n, k = [int(s) for s in input().split(" ")]

    pip_strings = {}
    for j in range(n):
        pip_strings["string{0}".format(j)] = input()
    
    print(pip_strings)
    # print("Case #" + str(i) + ": " + str(answer))