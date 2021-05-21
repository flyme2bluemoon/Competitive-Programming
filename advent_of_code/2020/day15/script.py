turns = []

with open("input", "r") as f:
    turns = [int(_) for _ in f.read().strip().split(",")]

while len(turns) < 2020:
    if turns.count(turns[-1]) == 1:
        turns.append(0)
    else:
        for i in range(len(turns) - 2, -1, -1):
            if turns[i] == turns[-1]:
                last_index = i
                break
        turns.append(len(turns) - last_index - 1)

print(turns[-1])