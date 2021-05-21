highest_seat_id = 0

def calculate_seat_id(boarding_pass):
    front = 0
    back = 127
    for i in range(0, 7):
        if boarding_pass[i] == "F":
            back = front + ((back - front) / 2 - 0.5)
        else:
            front = front + ((back - front) / 2 + 0.5)
    left = 0
    right = 7
    for i in range(7,10):
        if boarding_pass[i] == "L":
            right = left + ((right - left) / 2 - 0.5)
        else:
            left = left + ((right - left) / 2 + 0.5)
    return int(front * 8 + left)

with open("input", "r") as f:
    for line in f:
        line = line.strip("\n")
        seat_id = calculate_seat_id(line)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

print(highest_seat_id)