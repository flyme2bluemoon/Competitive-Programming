import re

mem = {}
total = 0

def use_mask(decimal, mask):
    binary_representation = list(bin(int(decimal))[2:].zfill(36))
    for i in range(len(mask)):
        if mask[i] == "1":
            binary_representation[i] = "1"
        elif mask[i] == "0":
            binary_representation[i] = "0"
    binary_representation = int("".join(binary_representation), 2)
    return binary_representation

with open("input", "r") as f:
    for i in f:
        i = i.strip()
        if i[:4] == "mask":
            mask = i[-36:]
        elif i[:3] == "mem":
            index = re.search(r"\[([A-Za-z0-9_]+)\]", i).group(1)
            index = int(index)
            value = i.split(" = ")[1]
            value = use_mask(value, mask)
            mem[index] = value

for i in mem:
    total += mem[i]

print(total)