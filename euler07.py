# Project Euler 07 - https://projecteuler.net/problem=7 - Lösung 104.743
# Was ist die 10.001. Primzahl?

def is_prime(x):   #Von euler03 übernommen 
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
#print(is_prime(13))   #test

def x_prime(x): # Xte Nummer ist welche Primzahl? Also zB x_prime(6) == 13
    result, count = 0, 0

    while result < x:
        count +=1
        if is_prime(count):
            result += 1
    return count 

print(x_prime(10001))