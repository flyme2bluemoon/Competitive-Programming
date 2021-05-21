T = int(input())

for i in range (T):
    rule_break = 0
    K = int(input()) # number of notes
    A = [int(s) for s in input().split() if s.isdigit()] # A[i] is the pitch of the i-th note

    variation = 0

    for j in range(1,K):
        if A[j] > A[j-1]:
            variation += 1
        elif A[j] < A[j-1]:
            variation -= 1

        if variation >= 4 or variation <= -4:
            rule_break += 1
            variation = 0

    print ("Case #" + str(i + 1) + ": " + str(rule_break))