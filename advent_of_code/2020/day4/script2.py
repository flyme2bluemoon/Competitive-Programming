# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

import re

def validate_passport(input):
    for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if i not in input:
            return False
    if int(input["byr"]) < 1920 or int(input["byr"]) > 2002:
        # print(f"Invalid birthyear {input['byr']}")
        return False
    if int(input["iyr"]) < 2010 or int(input["iyr"]) > 2020:
        # print(f"Invalid issueyear {input['iyr']}")
        return False
    if int(input["eyr"]) < 2020 or int(input["eyr"]) > 2030:
        # print(f"Invalid expirationyear {input['eyr']}")
        return False
    if input["hgt"][-2:] == "in":
        if int(input["hgt"][:-2]) < 59 or int(input["hgt"][:-2]) > 76:
            # print(f"Invalid height {input['hgt']}")
            return False
    elif input["hgt"][-2:] == "cm":
        if int(input["hgt"][:-2]) < 150 or int(input["hgt"][:-2]) > 193:
            # print(f"Invalid height {input['hgt']}")
            return False
    else:
        # print(f"Invalid height {input['hgt']}")
        return False
    if input["hcl"][0] != "#" or bool(re.match("^[0-9a-f]$", input["hcl"][1:])) or len(input["hcl"]) != 7:
        # print(f"Invalid haircolor {input['hcl']}")
        return False
    if input["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        # print(f"Invalid eyecolor {input['ecl']}")
        return False
    if len(input["pid"]) != 9:
        # print(f"Invalid passportid {input['pid']}")
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