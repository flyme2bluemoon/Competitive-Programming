import copy
import sys

seat_layout = []

with open("input", "r") as f:
    for i in f:
        seat_layout.append(list(i.strip()))

def simulate_round(seat_layout):
    output_layout = copy.deepcopy(seat_layout)
    if len(seat_layout) > len(seat_layout[0]):
        max_width = len(seat_layout)
    else:
        max_width = len(seat_layout[0])
    for i in range(len(seat_layout)):
        for j in range(len(seat_layout[0])):
            if seat_layout[i][j] == ".":
                continue
            elif seat_layout[i][j] == "L":
                will_be_occupied = True
                for x in range(-1,2):
                    for y in range(-1,2):
                        for m in range(1, max_width + 1):
                            dx = x * m
                            dy = y * m
                            if (dx == 0 and dy == 0) or i + dx < 0 or j + dy < 0:
                                continue
                            try:
                                if seat_layout[i + dx][j + dy] == "#":
                                    will_be_occupied = False
                                if seat_layout[i + dx][j + dy] != ".":
                                    break
                            except IndexError:
                                break
                if will_be_occupied:
                    output_layout[i][j] = "#"
            elif seat_layout[i][j] == "#":
                occupied_adjacent_seats = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        for m in range(1, max_width + 1):
                            dx = x * m
                            dy = y * m
                            if (dx == 0 and dy == 0) or i + dx < 0 or j + dy < 0:
                                continue
                            try:
                                if seat_layout[i + dx][j + dy] == "#":
                                    occupied_adjacent_seats += 1
                                if seat_layout[i + dx][j + dy] != ".":
                                    break
                            except IndexError:
                                break
                if occupied_adjacent_seats >= 5:
                    output_layout[i][j] = "L"
    if output_layout == seat_layout:
        occupied = 0
        for i in output_layout:
            occupied += i.count("#")
        print(occupied)
        sys.exit(0)
    else:
        return output_layout

while True:
    seat_layout = copy.deepcopy(simulate_round(seat_layout))