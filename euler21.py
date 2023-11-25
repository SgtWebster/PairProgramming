# Project Euler 21 - https://projecteuler.net/problem=21 - Lösung 31626
# Amicable Numbers


def proper_divisor(x):
    result = 0
    for i in range(1, int(x*0.5)+1):
        if x % i == 0:
            result += i
    return result

def amicable_numbers(x):
    result = 0
    amicable = []
    for i in range (1, x):
        if proper_divisor(proper_divisor(i)) == i and proper_divisor(i) != i:
            result += i
            amicable.append(i)
    print(amicable)
    return result


#print(proper_divisor(284))   #debug
#print(proper_divisor(proper_divisor(220)))   #debug

print(amicable_numbers(10000))
