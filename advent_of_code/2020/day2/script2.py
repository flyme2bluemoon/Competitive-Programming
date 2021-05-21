valid_passwords = 0

with open("input", "r") as f:
    for line in f:
        the_input = line.strip("\n")
        rule, password = [s for s in the_input.split(": ")]
        indicies, letter = [s for s in rule.split(" ")]
        a, b = [int(s) for s in indicies.split("-")]
        if (password[a - 1] == letter and password[b - 1] != letter) or (password[a - 1] != letter and password[b - 1] == letter):
            valid_passwords += 1

print(valid_passwords)