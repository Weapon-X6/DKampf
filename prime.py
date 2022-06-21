import math


def is_prime(n):
    # Define the initial check
    if n < 2:
        return False
    # Define the loop checking if a number is not prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


cands = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49]
# Filter prime numbers into the new list
primes = [num for num in cands if is_prime(num)]
print("primes = " + str(primes))
