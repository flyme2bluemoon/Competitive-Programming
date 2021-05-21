# 1 × S + 2 × M + 3 × L

s = int(input())
m = int(input())
l = int(input())

score = s + 2 * m + 3 * l

if score >= 10:
    print("happy")
else:
    print("sad")