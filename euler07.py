# Project Euler 07 - https://projecteuler.net/problem=7 - Lösung ...
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
    result = 0
    count = 0
    while not count == x:
        count +=1
        if is_prime(count):
            result = count

    
    return result 

print(x_prime(6))