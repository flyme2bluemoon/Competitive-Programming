valid_passwords = 0

with open("input", "r") as f:
    for line in f:
        the_input = line.strip("\n")
        rule, password = [s for s in the_input.split(": ")]
        min_max_range, letter = [s for s in rule.split(" ")]
        minimum, maximum = [int(s) for s in min_max_range.split("-")]
        if password.count(letter) in range(minimum, maximum + 1):
            valid_passwords += 1

print(valid_passwords)