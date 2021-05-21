n = int(input())

friends = []
positions = []

for i in range(n):
    friends.append([int(_) for _ in input().split(" ")])
    positions.append(friends[-1][0])

average = sum(positions) // n
minimum = min(positions)
maximum = max(positions)

# average = 9

c_history = [average]
time_record = []

while True:
    left_seconds = 0
    right_seconds = 0
    seconds = 0
    for i in friends:
        time_needed = (abs(i[0] - average) - i[2]) * i[1]
        if time_needed > 0:
            if i[0] > average:
                right_seconds += time_needed
            elif i[0] < average:
                left_seconds += time_needed
            else:
                seconds += time_needed
    seconds += (left_seconds + right_seconds)
    time_record.append(seconds)
    print(minimum, average, maximum)
    print(left_seconds, right_seconds)
    if left_seconds > right_seconds:
        maximum = average
        average = (minimum + maximum) // 2
    elif left_seconds < right_seconds:
        minimum = average
        average = (minimum + maximum) // 2
    else:
        break
    if average in c_history:
        print(f"breaker: {average}")
        break
    else:
        c_history.append(average)

print(min(time_record))