# I, O, S, H, Z, X, and N.

word = input()
valid = True

for i in word:
    if i not in ["I", "O", "S", "H", "Z", "X", "N"]:
        valid = False
        break

if valid:
    print("YES")
else:
    print("NO")
