import sys

data = []
invalid_number = 22406676

with open("input", "r") as f:
    for line in f:
        data.append(int(line.strip()))

for i in range(len(data)):
    total = 0
    counter = 2
    while total < invalid_number:
        total = sum(data[i:i+counter])
        if total == invalid_number:
            subset = data[i:i+counter]
            print(min(subset) + max(subset))
            sys.exit(0)
        counter += 1