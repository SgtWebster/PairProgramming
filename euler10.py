# Project Euler 10 - https://projecteuler.net/problem=10 - Lösung 142913828922
# Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million.

def is_prime(x):   #von euler03 übernommen
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def summation_primes(x):
    result = 0
    for i in range(1, x):
        if is_prime(i):
            result += i
    return result

print(summation_primes(2000000))