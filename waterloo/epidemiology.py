p = int(input())
n = int(input())
r = int(input())

day = 0
total = n
while True:
    day += 1
    n *= r
    total += n
    if total > p:
        print(day)
        break
