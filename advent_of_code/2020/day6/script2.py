import string as s

total = 0

with open("input", "r") as f:
    groups = [g for g in f.read().split("\n\n")]

for i in groups:
    people = [person for person in i.split("\n")]
    for j in people[0]:
        is_in_all = True
        for k in people:
            if j not in k:
                is_in_all = False
        if is_in_all:
            total += 1

print(total)