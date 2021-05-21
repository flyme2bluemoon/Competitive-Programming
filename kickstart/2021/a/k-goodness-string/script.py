t = int(input())

for i in range(1, t+1):
    n, k = [int(_) for _ in input().split()]
    s = input()
    goodness = 0
    for j in range(n//2):
        if (s[j] == s[n-j-1]):
            goodness += 1
    answer = k - goodness
    if answer < 0:
        answer = 0
    print(f"Case #{i}: {answer}")