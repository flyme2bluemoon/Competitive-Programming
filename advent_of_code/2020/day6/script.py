total = 0

with open("input", "r") as f:
    groups = [g for g in f.read().split("\n\n")]
    
for group in groups:
    answers = []
    for i in group:
        if i != "\n":
            answers.append(i)
    answers = set(answers)
    total += len(answers)

print(total)