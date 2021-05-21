actions = []

with open("input", "r") as f:
    actions = [_ for _ in f.read().strip().split("\n")]

waypoint_x = 10
waypoint_y = 1
ship_x = 0
ship_y = 0

for i in actions:
    action_type = i[0]
    action_value = int(i[1:])
    if action_type == "N":
        waypoint_y += action_value
    elif action_type == "S":
        waypoint_y -= action_value
    elif action_type == "E":
        waypoint_x += action_value
    elif action_type == "W":
        waypoint_x -= action_value
    elif action_type == "L":
        # CCW
        if action_value == 90:
            waypoint_y *= -1
            waypoint_x, waypoint_y = waypoint_y, waypoint_x
        elif action_value == 180:
            waypoint_x *= -1
            waypoint_y *= -1
            # waypoint_x, waypoint_y = waypoint_y, waypoint_x
        elif action_value == 270:
            waypoint_x *= -1
            waypoint_x, waypoint_y = waypoint_y, waypoint_x
    elif action_type == "R":
        if action_value == 90:
            waypoint_x *= -1
            waypoint_x, waypoint_y = waypoint_y, waypoint_x
        elif action_value == 180:
            waypoint_x *= -1
            waypoint_y *= -1
            # waypoint_x, waypoint_y = waypoint_y, waypoint_x
        elif action_value == 270:
            waypoint_y *= -1
            waypoint_x, waypoint_y = waypoint_y, waypoint_x
    elif action_type == "F":
        ship_x += waypoint_x * action_value
        ship_y += waypoint_y * action_value

print(abs(ship_x) + abs(ship_y))