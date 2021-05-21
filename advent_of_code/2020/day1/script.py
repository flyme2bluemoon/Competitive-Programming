import sys

numbers = []

with open("input", "r") as input:
    for line in input:
        numbers.append(int(line.strip("\n")))

for i in numbers:
    if (2020 - i) in numbers:
        print(i * (2020 - i))
        sys.exit(0)

sys.exit(1)