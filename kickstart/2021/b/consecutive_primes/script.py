import math

t = int(input())

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def find_next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def find_previous_prime(n):
    while True:
        n -= 1
        if is_prime(n):
            return n

for i in range(1, t+1):
    z = int(input())
    n = int(math.sqrt(z))
    next_prime = find_next_prime(n)
    if is_prime(n):
        prev_prime = n
    else:
        prev_prime = find_previous_prime(n)
    answer = next_prime * prev_prime
    if answer > z:
        second_prev_prime = find_previous_prime(prev_prime)
        answer = prev_prime * second_prev_prime
    print(f"Case #{i}: {answer}")