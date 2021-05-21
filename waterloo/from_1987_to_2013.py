d = int(input())

for i in range(d + 1, 10000):
    unique = True
    for j in str(i):
        if str(i).count(str(j)) > 1:
            unique = False
            break
    if unique:
        print(i)
        break