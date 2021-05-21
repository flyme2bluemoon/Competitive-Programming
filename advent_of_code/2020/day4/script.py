# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

def validate_passport(input):
    for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if i not in input:
            return False
    return True

with open("input", "r") as f:
    valid_passport_count = 0
    current_passport = {}
    for line in f:
        if line == "\n":
            if validate_passport(current_passport):
                valid_passport_count += 1
            current_passport = {}
        else:
            fields = [s for s in line.strip("\n").split(" ")]
            for field in fields:
                key, value = [s for s in field.split(":")]
                current_passport[key] = value

print(valid_passport_count)