import copy
import sys

seat_layout = []

with open("input", "r") as f:
    for i in f:
        seat_layout.append(list(i.strip()))

def simulate_round(seat_layout):
    output_layout = copy.deepcopy(seat_layout)
    for i in range(len(seat_layout)):
        for j in range(len(seat_layout[0])):
            if seat_layout[i][j] == ".":
                continue
            elif seat_layout[i][j] == "L":
                will_be_occupied = True
                for x in range(-1,2):
                    for y in range(-1,2):
                        if (x == 0 and y == 0) or i + x < 0 or j + y < 0:
                            continue
                        try:
                            if seat_layout[i + x][j + y] == "#":
                                will_be_occupied = False
                        except IndexError:
                            pass
                if will_be_occupied:
                    output_layout[i][j] = "#"
            elif seat_layout[i][j] == "#":
                occupied_adjacent_seats = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if (x == 0 and y == 0) or i + x < 0 or j + y < 0:
                            continue
                        try:
                            if seat_layout[i + x][j + y] == "#":
                                occupied_adjacent_seats += 1
                        except IndexError:
                            pass
                if occupied_adjacent_seats >= 4:
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