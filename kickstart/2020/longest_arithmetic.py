T = int(input())

for i in range (1, T + 1):
    n = int(input())
    b = [int(s) for s in input().split(" ")]

    # print(n)
    # print(b)

    the_longest_arithmetic_subarray = 0
    the_current_arithmetic_subarray = 1

    the_old_difference = b[1] - b[0]
    
    for j in range(2, n):
        the_new_difference = b[j] - b[j-1]
        if the_new_difference == the_old_difference:
            the_current_arithmetic_subarray += 1
        else:
            the_old_difference = the_new_difference
            if the_current_arithmetic_subarray >= the_longest_arithmetic_subarray:
                the_longest_arithmetic_subarray = the_current_arithmetic_subarray + 1
            the_current_arithmetic_subarray = 1
    
    if the_current_arithmetic_subarray >= the_longest_arithmetic_subarray:
            the_longest_arithmetic_subarray = the_current_arithmetic_subarray + 1

    print ("Case #" + str(i) + ": " + str(the_longest_arithmetic_subarray))

# Case #1: 4
# Case #2: 4
# Case #3: 3
# Case #4: 6