with open("input", "r") as f:
    sections = [_ for _ in f.read().strip("\n").split("\n\n")]

def check_rules(number):
    for i in rules:
        if number in rules[i]:
            return True
    return False

# organize the rules
rules = {}
for i in [_ for _ in sections[0].split("\n")]:
    field, valid_ranges = [_ for _ in i.split(": ")]
    rules[field] = []
    valid_ranges = [_ for _ in valid_ranges.split(" or ")]
    for j in valid_ranges:
        bounds = [int(_) for _ in j.split("-")]
        rules[field] += list(range(bounds[0], bounds[1] + 1))

# organize my ticket
my_ticket = [_ for _ in sections[1].split("\n")][1]
my_ticket = [int(_) for _ in my_ticket.split(",")]

# organize nearby tickets
nearby_tickets = [_ for _ in sections[2].split("\n")][1:]
for i in range(len(nearby_tickets)):
    nearby_tickets[i] = [int(_) for _ in nearby_tickets[i].split(",")]

# remove invalid tickets
for i in nearby_tickets:
    for j in i:
        if not check_rules(j):
            nearby_tickets.remove(i)

# initialize possibilities
possibilities = {}
for i in rules:
    possibilities[i] = list(range(0,len(my_ticket)))

for i in nearby_tickets:
    for j in i:
        for k in rules:
            if j not in rules[k]:
                try:
                    possibilities[k].remove(i.index(j))
                except ValueError:
                    pass

working = True
while working:
    working = False
    for i in possibilities:
        if str(type(possibilities[i])) == "<class 'list'>":
            if len(possibilities[i]) == 1:
                possibilities[i] = possibilities[i][0]
                for j in possibilities:
                    if str(type(possibilities[j])) == "<class 'list'>":
                        if possibilities[i] in possibilities[j]:
                            possibilities[j].remove(possibilities[i])
                working = True

answer = 1
for i in possibilities:
    if [_ for _ in i.split(" ")][0] == "departure" and str(type(possibilities[i])) == "<class 'int'>":
        answer *= possibilities[i]

print(answer)