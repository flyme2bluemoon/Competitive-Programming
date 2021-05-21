class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def move_left(path, distance, x, y):
    for i in range(int(distance)):
        path.append(Coordinate(x - i, y))

def move_right(path, distance, x, y):
    for i in range(int(distance)):
        path.append(Coordinate(x + i, y))

def move_up(path, distance, x, y):
    for i in range(int(distance)):
        path.append(Coordinate(x, y + i))

def move_down(path, distance, x, y):
    for i in range(int(distance)):
        path.append(Coordinate(x, y - i))

def move(path, instructions):
    for i in instructions:
        current_position_x = path[-1].x
        current_position_y = path[-1].y
        if i[0] == "L":
            move_left(path, i[1:], current_position_x, current_position_y)
        elif i[0] == "R":
            move_right(path, i[1:], current_position_x, current_position_y)
        elif i[0] == "U":
            move_up(path, i[1:], current_position_x, current_position_y)
        elif i[0] == "D":
            move_down(path, i[1:], current_position_x, current_position_y)

def converter(path):
    for i in range(len(path)):
        path[i] = [path[i].x, path[i].y]

with open("input", "r") as f:
    instructions_one, instructions_two = [_ for _ in f.read().split("\n")]

instructions_one = [_ for _ in instructions_one.split(",")]
instructions_two = [_ for _ in instructions_two.split(",")]

path_one = []
path_two = []

central_port = Coordinate(0, 0)

path_one.append(central_port)
path_two.append(central_port)

move(path_one, instructions_one)
move(path_two, instructions_two)

converter(path_one)
converter(path_two)

intersections = []

for i in path_one:
    if i in path_two:
        print(i)
        intersections.append(i)