rules = {}
bag_count = 0
layers = []

def product():
    answer = 1
    for i in layers:
        answer *= i
    return answer

def count_nested_bags(bag):
    global bag_count
    for i in rules[bag]:
        if i == "no other bags":
            continue
        layers.append(int(i[0]))
        count_nested_bags(i[2:])
        bag_count += product()
        layers.pop()

with open("input", "r") as f:
    for i in f:
        outer, inner = [_ for _ in i.strip("\n").strip(".").split(" contain ")]
        inner = [_ for _ in inner.split(",")]
        for j in range(len(inner)):
            inner[j] = inner[j].strip()
            if inner[j][0] == "1":
                inner[j] += "s"
        rules[outer] = inner

# print(rules)

count_nested_bags("shiny gold bags")

print(bag_count)