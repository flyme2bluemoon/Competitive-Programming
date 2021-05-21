number_of_points = int(input())

x_coordinates = []
y_coordinates = []

for i in range(0, number_of_points):
    x, y = [int(_) for _ in input().split(",")]
    x_coordinates.append(x)
    y_coordinates.append(y)

bottom_left_x = min(x_coordinates) - 1
bottom_left_y = min(y_coordinates) - 1
top_right_x = max(x_coordinates) + 1
top_right_y = max(y_coordinates) + 1

print(f"{bottom_left_x},{bottom_left_y}")
print(f"{top_right_x},{top_right_y}")