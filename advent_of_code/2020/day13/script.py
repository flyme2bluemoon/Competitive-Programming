time_until_bus = {}

with open("input", "r") as f:
    timestamp = int(f.readline().strip())
    buses = [_ for _ in f.readline().strip().split(",")]

while True:
    try:
        buses.remove("x")
    except ValueError:
        break

for i in range(len(buses)):
    buses[i] = int(buses[i])

for i in buses:
    time_until_bus[i] = timestamp - (timestamp % i) + i

first_bus = min(time_until_bus.keys(), key=(lambda k: time_until_bus[k]))

print((time_until_bus[first_bus] - timestamp) * first_bus)