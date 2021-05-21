map_array = []

with open("input", "r") as f:
    for lines in f:
        map_array.append([])
        for item in lines:
            if item == ".":
                map_array[-1].append(0)
            elif item == "#":
                map_array[-1].append(1)

line_len = len(map_array[1])

def solve(n, d):
    trees = 0
    for i in range(0, len(map_array) // d):
        if map_array[i * d][(i * n) % len(map_array[i])] == 1:
            trees += 1
    return trees

print(solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))