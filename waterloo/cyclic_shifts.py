answer = "no"

text = input()
string = input()

cyclic_shifts = []

for i in range(len(string)):
    cyclic_shifts.append(string[i:] + string[:i])

for i in cyclic_shifts:
    if i in text:
        answer = "yes"
        break

print(answer)