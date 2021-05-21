number_of_measurements = int(input())

measurements = [int(_) for _ in input().split(" ")]

measurements.sort()

if number_of_measurements % 2 == 0:
    low_tide = measurements[:number_of_measurements // 2]
    low_tide.reverse()
    high_tide = measurements[number_of_measurements // 2:]

    for i in range(0, number_of_measurements // 2):
        print(low_tide[i], high_tide[i], end=" ")

    print()
else:
    low_tide = measurements[:(number_of_measurements // 2) + 1]
    low_tide.reverse()
    high_tide = measurements[(number_of_measurements // 2) + 1:]

    for i in range(0, number_of_measurements // 2):
        print(low_tide[i], high_tide[i], end=" ")

    print(low_tide[-1])