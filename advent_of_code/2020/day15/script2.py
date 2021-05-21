from sys import exit

turns = {}

with open("input", "r") as f:
    tmp = [int(_) for _ in f.read().strip().split(",")]

# Initializing the dictionary with the input
for i in range(len(tmp)):
    if tmp[i] in turns:
        turns[tmp[i]][0] = i
        turns[tmp[i]][1] += 1
    else:
        turns[tmp[i]] = [i, 1]

print(turns)

# TODO Fix this line of code as it makes a dangerous assumption
last_element = list(turns)[-1]

for i in range(len(tmp), 2020):
    if turns[last_element][1] == 1:
        turns[0][0] = i
        turns[0][1] += 1
    else:
        last_index = turns[last_element][0]
        next_number = len(turns) - last_index - 1
        if next_number in turns:
            turns[next_number][0] = i
            turns[next_number][1] += 1
        else:
            turns[next_number] = [i, 1]

print(turns)