adapters = []

with open("input", "r") as f:
    for line in f:
        adapters.append(int(line.strip()))

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()
paths = [0] * len(adapters)
paths[0] = 1

for i in range(1, len(adapters)):
    for j in range(1,4):
        if adapters[i] - j in adapters:
            paths[i] += paths[adapters.index(adapters[i] - j)]

print(paths[-1])