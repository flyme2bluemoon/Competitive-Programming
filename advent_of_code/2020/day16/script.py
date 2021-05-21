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
# my_ticket = [_ for _ in sections[1].split("\n")][1]
# my_ticket = [int(_) for _ in my_ticket.split(",")]

# organize nearby tickets
nearby_tickets = [_ for _ in sections[2].split("\n")][1:]
for i in range(len(nearby_tickets)):
    nearby_tickets[i] = [int(_) for _ in nearby_tickets[i].split(",")]

ticket_scanning_error_rate = 0
for i in nearby_tickets:
    for j in i:
        if not check_rules(j):
            ticket_scanning_error_rate += j

print(ticket_scanning_error_rate)