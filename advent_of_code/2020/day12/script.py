actions = []

with open("input", "r") as f:
    actions = [_ for _ in f.read().strip().split("\n")]

facing = 90
x_position = 0
y_position = 0

def north(magnitude):
    global y_position
    y_position += magnitude

def south(magnitude):
    global y_position
    y_position -= magnitude

def east(magnitude):
    global x_position
    x_position += magnitude

def west(magnitude):
    global x_position
    x_position -= magnitude

for i in actions:
    action_type = i[0]
    action_value = int(i[1:])
    if action_type == "N":
        north(action_value)
    elif action_type == "S":
        south(action_value)
    elif action_type == "E":
        east(action_value)
    elif action_type == "W":
        west(action_value)
    elif action_type == "L":
        facing = (facing - action_value) % 360
    elif action_type == "R":
        facing = (facing + action_value) % 360
    elif action_type == "F":
        if facing == 0:
            north(action_value)
        elif facing == 90:
            east(action_value)
        elif facing == 180:
            south(action_value)
        elif facing == 270:
            west(action_value)

print(abs(x_position) + abs(y_position))