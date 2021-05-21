T = int(input())

for t in range (T):
    number_of_checkpoints = int(input())
    height_of_checkpoints = [int(s) for s in input().split() if s.isdigit()]
    peaks = 0
    for c in range (1,(number_of_checkpoints - 1)):
        if (height_of_checkpoints[c] > height_of_checkpoints[c - 1] and height_of_checkpoints[c] > height_of_checkpoints[c + 1]):
            peaks += 1

    print ("Case #" + str(t + 1) + ": " + str(peaks))