import copy

"""
    cube = ["x_y_z", "x_y_z"]
    x is width
    y is height
    z is depth
"""

initial_state = []
active = []

def check_adjacent_status(x, y, z, previously_active):
    active_adjacencies = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == 0 and dy == 0 and dz == 0:
                    pass
                elif f"{x + dx}_{y + dy}_{z + dz}" in previously_active:
                    # print(f"{x + dx}_{y + dy}_{z + dz}")
                    active_adjacencies += 1
    return active_adjacencies

with open("test", "r") as f:
    for line in f:
        initial_state.append(line.strip())

width = len(initial_state[0])
height = len(initial_state)
depth = 1
layers_added = 0

for i in range(height):
    for j in range(width):
        if initial_state[i][j] == "#":
            active.append(f"{i}_{j}_0")

for i in range(6):
    previously_active = copy.deepcopy(active)
    for x in range(0 - layers_added, width + layers_added):
        for y in range(0 - layers_added, height + layers_added):
            for z in range(0 - layers_added, depth + layers_added):
                print(x, y, z)
                active_adjacentcies = check_adjacent_status(x, y, z, previously_active)
                if f"{x}_{y}_{z}" in previously_active:
                    if active_adjacentcies == 2 or active_adjacentcies == 3:
                        pass
                    else:
                        active.remove(f"{x}_{y}_{z}")
                else:
                    if active_adjacentcies == 3:
                        active.append(f"{x}_{y}_{z}")
    layers_added += 1

print(initial_state)
print(width)
print(height)
print(active)
print(len(active))
