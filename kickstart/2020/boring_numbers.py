from time import sleep

T = int(input())

def get_int_length(n):
    return len(str(n))

def get_nth_digit(number, n, length):
    n = length - n
    return number // 10**n % 10
    # return int(str(number)[n-1]) # worry abt this if i get a TLE

def get_until_digit(number, n):
    return int(str(number)[:n]) # worry abt this if i get a TLE

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for j in range (1, T + 1):
    answer = 0
    l, r = [int(s) for s in input().split(" ")]

    x = l
    while x <= r:
        print(f"checking if {x} is boring")
        # print(f"Hello {x} has length {get_int_length(x)}")
        the_int_length_of_x = get_int_length(x)
        for p in range(1, the_int_length_of_x + 1):
            # print(p)
            sleep(0.25)
            the_flag1 = is_even(get_nth_digit(x, p, the_int_length_of_x))
            the_flag2 = is_even(p)
            if the_flag1 == the_flag2:
                # print("true")
                the_potential_flag = True        # potentially boring
            else:
                # print("false")
                the_potential_flag = False        # not boring so jump
                break
        if the_potential_flag == False:
            # print(f"get until {get_until_digit(x, p)} and get length {get_int_length(x)}")
            x = (get_until_digit(x, p) + 1) * 10**(the_int_length_of_x-p)
            # print(f"Yoo hoo im here and tmp is {tmp}")
        elif the_potential_flag == True:
            # print(f"{x} is a boring number")
            answer += 1
            if x % 10 == 9:
                x += 1
            else:
                x += 2

    print ("Case #" + str(j) + ": " + str(answer))