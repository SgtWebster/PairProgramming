# Project Euler 22 - https://projecteuler.net/problem=22 - Lösung 871198282
# non-abundant sums


def proper_divisor(x):   #Summe der echten Teiler einer Zeil 
    result = 0
    for i in range(1, int(x*0.5)+1):
        if x % i == 0:
            result += i
    return result

#print(proper_divisor(12))   #debug-print


def find_abundants(x):   # x = max Range 
    result = []
    for number in range(1,x+1):
        if number < proper_divisor(number):
            result.append(number)
    return result

abundants = find_abundants(28123)
#print(abundants)    #debug-print


def abundant_sum(x):    # prüft ob x aus zwei abundants summiert werden kann.
    for first_number in abundants:
        for second_number in abundants:
            if first_number + second_number == x:
                return True
            if second_number > x:
                break
        if first_number > x:
            break
    return False

def abundant_sum_range(x):   # prüft von Range 0 bis x welche Zahlen aus zwei abundants summieren lässt
    result = 0
    for i in range(1,x+1):
        if abundant_sum(i):
            result += i
    return result

print(abundant_sum_range(28123))
