answer = 0

def counter_upper(mass):
    return (mass // 3) - 2

with open("input", "r") as f:
    for line in f:
        answer += counter_upper(int(line.strip("\n")))
        
print(answer)