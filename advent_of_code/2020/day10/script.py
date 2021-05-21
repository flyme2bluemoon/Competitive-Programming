adapters = []
one_jolt = 1
three_jolt = 1

with open("input", "r") as f:
    for line in f:
        adapters.append(int(line.strip()))

adapters.sort()

for i in range(len(adapters) - 1):
    if adapters[i + 1] - adapters[i] == 1:
        one_jolt += 1
    elif adapters[i + 1] - adapters[i] == 3:
        three_jolt += 1

print(one_jolt * three_jolt)