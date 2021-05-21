rules = {}
number_of_bags = 0
shiny_gold_bag = "shiny gold bags"
failed = "no other bags"

def check_for_gold(bag):
    if failed in rules[bag]:
        return False
    elif shiny_gold_bag in rules[bag]:
        return True
    else:
        for i in rules[bag]:
            if check_for_gold(i):
                return True
        return False

with open("input", "r") as f:
    for i in f:
        outer, inner = [_ for _ in i.strip("\n").split("contain")]
        inner = [_ for _ in inner.split(",")]
        outer = outer.strip()
        for j in range(len(inner)):
            inner[j] = inner[j].strip(".").strip()
            if inner[j][0] in list("23456789"):
                inner[j] = inner[j][2:]
            elif inner[j][0] == '1':
                inner[j] = inner[j][2:] + 's'
        rules[outer] = inner

for i in rules:
    if check_for_gold(i):
        number_of_bags += 1

print(number_of_bags)