answer = 0

def counter_upper(n):
    mass_of_fuel = (n // 3) - 2
    if mass_of_fuel > 0:
        mass_of_fuel += counter_upper(mass_of_fuel)
        return mass_of_fuel
    else:
        return 0

with open("input", "r") as f:
    for line in f:
        answer += counter_upper(int(line.strip("\n")))

print(answer)