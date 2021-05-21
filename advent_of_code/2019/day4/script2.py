def check_for_adjacent_digits(pw):
    for i in range(len(pw) - 1):
        try:
            if pw[i] == pw[i + 1] and pw[i] != pw[i + 2] and pw[i] != pw[i - 1]:
                return True
        except IndexError:
            try:
                if pw[i] == pw[i + 1] and pw[i] != pw[i + 2]:
                    return True
            except IndexError:
                if pw[i] == pw[i + 1] and pw[i] != pw[i - 1]:
                    return True
    return False

def check_for_increasing_order(pw):
    for i in range(len(pw) - 1):
        if int(pw[i]) > int(pw[i + 1]):
            return False
    return True

def password_checker(pw):
    if not check_for_adjacent_digits(pw):
        return False
    if not check_for_increasing_order(pw):
        return False
    return True

valid_passwords_count = 0

with open("input", "r") as f:
    lower, upper = [int(_) for _ in f.readline().strip("\n").split("-")]

for i in range(lower, upper):
    if password_checker(str(i)):
        print(i)
        valid_passwords_count += 1

print(valid_passwords_count)