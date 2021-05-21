trees = 0

map_array = []

with open("input", "r") as f:
    for lines in f:
        map_array.append([])
        for item in lines:
            if item == ".":
                map_array[-1].append(0)
            elif item == "#":
                map_array[-1].append(1)

for i in range(len(map_array)):
    if map_array[i][(i * 3) % len(map_array[i])] == 1:
        trees += 1

print(trees)