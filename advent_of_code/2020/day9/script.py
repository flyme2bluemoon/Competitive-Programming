data = []

with open("input", "r") as f:
    for line in f:
        data.append(int(line.strip()))

def check_rule(index):
    twenty_five = data[index - 25:index]
    goal = data[index]
    for j in twenty_five:
        if (goal - j) in twenty_five:
            return True

for i in range(25, len(data)):
    if not check_rule(i):
        print(data[i])
        break
