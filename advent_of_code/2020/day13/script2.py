with open("input", "r") as f:
    first = int(f.readline().strip())
    bus = [_ for _ in f.readline().strip().split(",")]

timetable = {}
for i in bus:
    if i.isnumeric():
        timetable[bus.index(i)] = int(i)

answer = 100000000000000
increment = 1

for offset in timetable:
    while True:
        if ((answer + offset) % timetable[offset]) == 0:
            increment *= timetable[offset]
            break
        answer += increment

print(answer)