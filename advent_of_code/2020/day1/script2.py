import sys

numbers = []
remaining = []

with open("input", "r") as input:
    for line in input:
        numbers.append(int(line.strip("\n")))

for i in numbers:
    remaining.append(2020 - i)

for i in remaining:
    for j in numbers:
        if (i - j) in numbers:
            print (j * (i - j) * (2020 - i))
            sys.exit(0)

sys.exit(1)